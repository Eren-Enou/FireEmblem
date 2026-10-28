"""Generate the preparation-screen codes (PREP-01): EXP-25 = ownership colours in the native unit lists.

The unit-list module (Pick Units = E_SallyList in preparations, Base Data in battle) draws every cell through
0x8012EF5C. Before each cell draw (0x8012F0D4), r5 holds the cell's colour index into the native text palette
0x80296088 (F-58). EXP-25 changes it for every **data-page cell** (columns drawn by 0x8012F154: Class/Lv/
Exp/HP, Equipment, ... on every page) from the row's unit ownership (F-52). The Name column has its own draw
(0x80130D34) and keeps its native colour, so forced/picked states stay readable (PREP-02 run 1):

  Player 1 (OWNED, not P2) and Ike (unit id 1)  -> 0x21  light blue #6DCFF6
  Player 2 (OWNED | P2)                        -> 0x06  yellow     #FFFF64
  unassigned                                   -> unchanged (white 0x01, or forced green 0x13)
  unavailable (index 0 = grey)                 -> unchanged

Display only: no calls, no writes. Registers at the hook: r24 = column object, r25 = list object,
r29 = row offset (0x24 per row), r5 = colour index; r0/r11/r12 are free (r0 is reloaded right after).
Row record = *(list+0x3C) + r29, unit pointer at +0; the column's draw method = *(*(r24+0x4C)+0x1C).

EXP-26 (PREP-01 Step 3): the draft and transfers in Choose Units. Each player presses Z on their own
controller (raw PADStatus) on the highlighted row (unit = *(list+0x3C + list[+0x62]*0x24), as the game does at
0x8012DBE4). Only in the E_SallyList proc (name pointer list+0x14 = 0x80275B0E); no force changes (EXP-21 makes
Player 2's characters yellow at the first blue phase).
  unassigned          -> claimed on your pick (alternating, Player 1 first, as EXP-22)
  yours               -> released; or, if the other player requested it, accepted: ownership flips
  the other player's  -> transfer request (OFFER 0x08000000, row orange via EXP-25); again = cancel
  Ike, away/unavailable (force not 0/5), no unit -> refusal buzz
A requested transfer needs both players: the request on one controller, the acceptance on the owner's.

Usage: python -m tools.prep_code [--write]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from tools.draft_code import (HAS_ATTR, OWNED, P2, PADSTATUS, PLAY_SE, Asm, andi_, andis_, lbzx, lhzx, mulli,
                              oris, rlwinm, stbx)
from tools.owner_code import (_d, addi, c2_lines, cmpw, cmpwi, li, lbz, lis, lwz, mr, ori, stw, stwu,
                              MFLR0, MTLR0, NOP)

ROOT = Path(__file__).resolve().parents[1]
NAME = "EXP-25 Unit lists show ownership: Player 1 light blue, Player 2 yellow (Pick Units, Base Data)"
DRAW_HOOK = (0x8012F0D4, 0x8198004C)     # lwz r12,0x4c(r24)
UNIT_TABLE = 0x802B14E4
COLOUR_P1, COLOUR_P2 = 0x21, 0x06
DATA_CELL_DRAW = 0x8012F154                # draw method of the data-page columns (not the Name column)


MFLR30 = 0x7FC802A6
def extsb(a, s): return (31 << 26) | (s << 21) | (a << 16) | (954 << 1)
def xoris(a, s, imm): return _d(27, s, a, imm)
def lwzx(d, a, b): return (31 << 26) | (d << 21) | (a << 16) | (b << 11) | (23 << 1)
def subf(d, a, b): return (31 << 26) | (d << 21) | (a << 16) | (b << 11) | (40 << 1)
def cmplw(a, b): return (31 << 26) | (a << 16) | (b << 11) | (32 << 1)


def colour_cave() -> list[int]:
    a = Asm()
    a(lwz(12, 0x4C, 24), lwz(12, 0x1C, 12), lis(11, DATA_CELL_DRAW >> 16),
      ori(11, 11, DATA_CELL_DRAW & 0xFFFF), cmpw(12, 11)); a.br("bne", "done")        # data-page cells only
    a(lwz(12, 0x3C, 25), lwzx(12, 12, 29))                                              # row's unit
    a(lis(11, UNIT_TABLE >> 16), ori(11, 11, UNIT_TABLE & 0xFFFF), subf(11, 11, 12),
      lis(0, 2), cmplw(11, 0)); a.br("bge", "done")                                     # a unit-table pointer
    a(cmpwi(5, 0)); a.br("beq", "done")                                                 # unavailable stays grey
    a(lbz(0, 0x198, 12), cmpwi(0, 1)); a.br("beq", "p1")                                # Ike = Player 1
    a(lwz(11, 0x1A0, 12), andis_(0, 11, 0x0800)); a.br("bne", "offer")                 # transfer requested
    a(andis_(0, 11, OWNED >> 16)); a.br("beq", "done")                                   # unassigned unchanged
    a(andis_(0, 11, P2 >> 16)); a.br("bne", "p2")
    a.label("p1")
    a(li(5, COLOUR_P1)); a.br("b", "done")
    a.label("p2")
    a(li(5, COLOUR_P2)); a.br("b", "done")
    a.label("offer")
    a(li(5, 0x10))                                                                      # orange #FFC010
    a.label("done")
    a(DRAW_HOOK[1])
    w = a.words()
    return w + ([NOP, 0] if len(w) % 2 == 0 else [0])



# ---- EXP-26: the draft and transfers in Choose Units (E_SallyList) ----
OFFER = 0x08000000                         # transfer requested by the non-owner (another unused flag bit, F-52)
LIST_STEP = (0x8012D6A4, 0x9421FFD0)       # list input step entry: stwu r1,-0x30(r1); r3 = list object
SALLY_LIST_NAME = 0x80275B0E               # "E_SallyList" (proc name pointer at list+0x14)
Z_BIT = 0x0010                             # PAD_TRIGGER_Z (free in the list: it tests only A/B/X/Y/Start)
SE26 = {"p1": 0x802691DF, "p2": 0x802747B5, "release": 0x80269193, "miss": 0x80269175,
        "request": 0x80269183, "transfer": 0x802747B5}
NAME26 = "EXP-26 Draft and transfers in Choose Units: Z on your own controller claims, releases or requests"
COLOUR_OFFER = 0x10                         # palette orange #FFC010 (transfer requested)


def _se(a, name):
    a(lis(3, SE26[name] >> 16), ori(3, 3, SE26[name] & 0xFFFF), li(4, 0x64)); a.call(PLAY_SE)


def _head(a, reg, force):
    a(lis(12, 0x802D), lwz(reg, {0: -0x5D9C, 3: -0x5D78, 5: -0x5D60, 7: -0x5D48}[force], 12))


def prep_draft_cave() -> list[int]:
    a = Asm()
    a(stwu(1, -0x30, 1), MFLR0, stw(0, 0x34, 1), stw(3, 8, 1), stw(4, 0xC, 1), stw(31, 0x10, 1),
      stw(30, 0x14, 1), stw(29, 0x18, 1), stw(28, 0x1C, 1))
    a(mr(31, 3), lwz(0, 0x14, 31), lis(12, SALLY_LIST_NAME >> 16), ori(12, 12, SALLY_LIST_NAME & 0xFFFF),
      cmpw(0, 12)); a.br("bne", "done")                                                  # Choose Units only
    a.br("bl", "past"); a.w.append(0); a.label("past")
    a(MFLR30, li(29, 0))                                                                 # r30 prev, r29 port
    a.label("port")
    a(lis(12, PADSTATUS >> 16), ori(12, 12, PADSTATUS & 0xFFFF), mulli(0, 29, 12), lhzx(0, 12, 0))
    a(andi_(0, 0, Z_BIT), cmpwi(0, 0), li(0, 0)); a.br("beq", "held"); a(li(0, 1))
    a.label("held")
    a(lbzx(28, 30, 29), stbx(0, 30, 29), cmpwi(0, 1)); a.br("bne", "nextport")
    a(cmpwi(28, 0)); a.br("bne", "nextport")                                            # press edge only
    # highlighted unit = *(list+0x3C + list[+0x62] * 0x24)   (0x8012DBE4..0x8012DBFC)
    a(lbz(0, 0x62, 31), extsb(0, 0), lwz(3, 0x3C, 31), mulli(0, 0, 0x24), lwzx(28, 3, 0))
    a(lis(11, 0x802B), ori(11, 11, 0x14E4), subf(11, 11, 28), lis(0, 2), cmplw(11, 0)); a.br("bge", "reject")
    a(addi(3, 28, 0x1BC), li(4, 0)); a.call(HAS_ATTR)
    a(cmpwi(3, 0)); a.br("bne", "reject")                                                # Ike stays Player 1
    a(lwz(12, 0x190, 28), lbz(0, 8, 12), cmpwi(0, 0)); a.br("beq", "avail")
    a(cmpwi(0, 5)); a.br("bne", "reject")                                                # away/unavailable
    a.label("avail")
    a(lwz(11, 0x1A0, 28), andis_(12, 11, OWNED >> 16)); a.br("bne", "owned")
    # unassigned: whose pick? r3 = #P1 - #P2 over forces 0, 3, 5, 7 (as EXP-22)
    a(li(3, 0))
    for n, force in enumerate((0, 3, 5, 7)):
        _head(a, 12, force)
        a.label(f"c{n}")
        a(cmpwi(12, 0)); a.br("beq", f"c{n}end")
        a(lwz(0, 0x1A0, 12), andis_(4, 0, OWNED >> 16)); a.br("beq", f"c{n}nx")
        a(andis_(4, 0, P2 >> 16), addi(3, 3, 1)); a.br("beq", f"c{n}nx")
        a(addi(3, 3, -2))
        a.label(f"c{n}nx")
        a(lwz(12, 0x184, 12)); a.br("b", f"c{n}")
        a.label(f"c{n}end")
    a(lwz(11, 0x1A0, 28), rlwinm(11, 11, 0, 5, 3))                                       # clear OFFER
    a(cmpwi(29, 0)); a.br("bne", "p2pick")
    a(cmpwi(3, 0)); a.br("bgt", "reject")
    a(oris(11, 11, OWNED >> 16), stw(11, 0x1A0, 28)); _se(a, "p1"); a.br("b", "nextport")
    a.label("p2pick")
    a(cmpwi(3, 0)); a.br("ble", "reject")
    a(oris(11, 11, (OWNED | P2) >> 16), stw(11, 0x1A0, 28)); _se(a, "p2"); a.br("b", "nextport")
    a.label("owned")
    a(andis_(12, 11, P2 >> 16), li(0, 0)); a.br("beq", "ownerok"); a(li(0, 1))
    a.label("ownerok")
    a(cmpw(0, 29)); a.br("bne", "other")
    # the owner pressed Z
    a(andis_(12, 11, OFFER >> 16)); a.br("beq", "release")
    a(xoris(11, 11, P2 >> 16), rlwinm(11, 11, 0, 5, 3), stw(11, 0x1A0, 28))             # accept: owner flips
    _se(a, "transfer"); a.br("b", "nextport")
    a.label("release")
    a(rlwinm(11, 11, 0, 3, 0), stw(11, 0x1A0, 28)); _se(a, "release"); a.br("b", "nextport")
    a.label("other")                                                                      # the other player
    a(andis_(12, 11, OFFER >> 16)); a.br("beq", "request")
    a(rlwinm(11, 11, 0, 5, 3), stw(11, 0x1A0, 28)); _se(a, "release"); a.br("b", "nextport")   # cancel request
    a.label("request")
    for n, force in enumerate((0, 5, 7)):                                                 # one request at a time
        _head(a, 12, force)
        a.label(f"o{n}")
        a(cmpwi(12, 0)); a.br("beq", f"o{n}end")
        a(lwz(0, 0x1A0, 12), rlwinm(0, 0, 0, 5, 3), stw(0, 0x1A0, 12), lwz(12, 0x184, 12)); a.br("b", f"o{n}")
        a.label(f"o{n}end")
    a(lwz(11, 0x1A0, 28), oris(11, 11, OFFER >> 16), stw(11, 0x1A0, 28)); _se(a, "request"); a.br("b", "nextport")
    a.label("reject")
    _se(a, "miss")
    a.label("nextport")
    a(addi(29, 29, 1), cmpwi(29, 2)); a.br("blt", "port")
    a.label("done")
    a(lwz(0, 0x34, 1), MTLR0, lwz(3, 8, 1), lwz(4, 0xC, 1), lwz(31, 0x10, 1), lwz(30, 0x14, 1),
      lwz(29, 0x18, 1), lwz(28, 0x1C, 1), addi(1, 1, 0x30))
    a(LIST_STEP[1])
    w = a.words()
    return w + ([NOP, 0] if len(w) % 2 == 0 else [0])


def blocks26() -> list[tuple[int, list[int]]]:
    return [(LIST_STEP[0], prep_draft_cave())]


def blocks() -> list[tuple[int, list[int]]]:
    return [(DRAW_HOOK[0], colour_cave())]


def code_lines(n: int = 25) -> list[str]:
    lines = [f"${NAME if n == 25 else NAME26}"]
    for addr, words in (blocks() if n == 25 else blocks26()):
        lines += c2_lines(addr, words)
    return lines


def write_ini(path: Path) -> None:
    lines = path.read_text().split("\n")
    for n in (25, 26):
        head = next((i for i, l in enumerate(lines) if l.startswith(f"$EXP-{n} ")), None)
        if head is None:
            anchor = next(i for i, l in enumerate(lines) if l.startswith("# DBG-01"))
            lines[anchor:anchor] = code_lines(n) + [""]
            continue
        end = head + 1
        while end < len(lines) and len(lines[end].split()) == 2 and all(
                len(t) == 8 and all(c in "0123456789ABCDEF" for c in t) for t in lines[end].split()):
            end += 1
        lines[head:end] = code_lines(n)
    path.write_text("\n".join(lines), newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if args.write:
        write_ini(ROOT / "codes/GFEE01.ini")
        print("updated $EXP-25 and $EXP-26 in codes/GFEE01.ini")
    else:
        print("\n".join(code_lines(25) + [""] + code_lines(26)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
