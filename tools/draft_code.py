"""Generate the in-game ownership codes (Milestones A/B of the drafting goal): EXP-21 and EXP-22.

Ownership is stored in the unit itself, in two bits of the flag word unit+0x1A0 that the game never sets,
tests or clears (F-52), and that the card save writes and reads as 4 raw bytes (0x8003CBBC / 0x8003C994):

  OWNED = 0x20000000   assigned to a player (clear = unassigned; new recruits start clear)
  P2    = 0x40000000   owner is Player 2 (only meaningful with OWNED)

So ownership survives chapter transitions, saves and reloads, is identical on both Netplay machines (it is
game memory), and changing it never touches the character's progression.

EXP-21 (replaces EXP-16's PID table; same hook sites, so never enable both):
  apply   0x8002E738, phase 0: every force 0 unit with P2 -> force 3; then control[3] = 1 if force 3 has units
  return  0x800BA784 / 0x8002E0D0 / 0x80005F04 (chapter-end paths, F-38/F-39): force 3 units with P2 -> force 0
  escape  0x800BA8F8 (UnitEscape(id)): that unit only, if it is in force 3 with P2
  Native partners (Lethe, Mordecai, Ch10's Kieran...) never carry P2, so they are never moved.

EXP-22 (the draft; turn 1, blue phase only, i.e. the start of every chapter):
  hook 0x800291D8 = the human-phase input step (runs every frame of the blue phase). For each port 1/2,
  on the press of L+R together (raw PADStatus at 0x802EF408, so each player uses their own controller):
    unit = unit under the cursor (0x800AA794); refused if none, the lord (attribute bit 0, Ike), or a
    force 3 unit without OWNED (a native partner); only force 0 and owned force 3 units qualify
    unassigned  -> claimed by this player if it is their pick: Player 1 when #P1 <= #P2, else Player 2
                   (alternating draft, Player 1 first; counted over forces 0, 3, 5, 7, so nothing extra is
                   stored). Player 2's pick moves the unit to force 3 at once.
    own unit    -> released (unassigned again; back to force 0), which also hands the pick back
    other's unit-> nothing (transfers come later)
  A cursor sound confirms a change (0x801475FC with Next Unit's arguments).

Usage: python -m tools.draft_code            print both codes
       python -m tools.draft_code --write    insert/replace $EXP-21 and $EXP-22 in codes/GFEE01.ini
"""

from __future__ import annotations

import argparse
from pathlib import Path

from tools.owner_code import (_Asm, _d, addi, c2_lines, cmpw, cmpwi, li, lbz, lis, lwz, mr, ori, stb, stw, stwu,
                              BCTRL, MFLR0, MFLR31, MTCTR12, MTLR0, NOP, TRANSFER)

ROOT = Path(__file__).resolve().parents[1]
OWNED, P2 = 0x20000000, 0x40000000
FORCE_HEAD = {0: (0x802D, -0x5D9C), 3: (0x802D, -0x5D78), 5: (0x802D, -0x5D60), 7: (0x802D, -0x5D48)}
APPLY_HOOK = (0x8002E738, 0x9421FFF0)
RETURN_HOOKS = [(0x800BA784, 0x9421FFD0), (0x8002E0D0, 0x9421FFD0), (0x80005F04, 0x9421FFE0)]
ESCAPE_HOOK = (0x800BA8F8, 0x9421FFF0)
INPUT_HOOK = (0x800291D8, 0x9421FFD0)       # human-phase input step: stwu r1,-0x30(r1)
CURSOR_UNIT = 0x800AA794
HAS_ATTR = 0x80105BC0                       # (unit+0x1BC, attribute index) -> bool
PLAY_SE = 0x801475FC                        # (0x80269070+0x138, 0x64), as Next Unit does (0x800292BC)
PADSTATUS = 0x802EF408
LR_BITS = 0x0060                            # PAD_TRIGGER_R | PAD_TRIGGER_L
NAMES = {
    21: "EXP-21 Ownership stored in each unit (flag bits): Player 2 units fight as the yellow army",
    22: "EXP-22 Draft at chapter start: L+R on a unit claims or releases it (alternating picks)",
}


def andi_(a, s, imm): return _d(28, s, a, imm)
def andis_(a, s, imm): return _d(29, s, a, imm)
def oris(a, s, imm): return _d(25, s, a, imm)
def lha(d, off, a): return _d(42, d, a, off)
def mulli(d, a, imm): return _d(7, d, a, imm)
def subf(d, a, b): return (31 << 26) | (d << 21) | (a << 16) | (b << 11) | (40 << 1)
def lhzx(d, a, b): return (31 << 26) | (d << 21) | (a << 16) | (b << 11) | (279 << 1)
def lbzx(d, a, b): return (31 << 26) | (d << 21) | (a << 16) | (b << 11) | (87 << 1)
def stbx(s, a, b): return (31 << 26) | (s << 21) | (a << 16) | (b << 11) | (215 << 1)
def rlwinm(a, s, sh, mb, me): return (21 << 26) | (s << 21) | (a << 16) | (sh << 11) | (mb << 6) | (me << 1)


class Asm(_Asm):
    """_Asm with the extra branch kinds the draft code needs."""

    def words(self) -> list[int]:
        for i, kind, n in self.fix:
            off = (self.labels[n] - i) * 4
            cond = {"blt": (12, 0), "bgt": (12, 1), "ble": (4, 1), "bge": (4, 0),
                    "beq": (12, 2), "bne": (4, 2)}
            if kind == "b":
                self.w[i] = (18 << 26) | (off & 0x3FFFFFC)
            elif kind == "bl":
                self.w[i] = (18 << 26) | (off & 0x3FFFFFC) | 1
            else:
                bo, bi = cond[kind]
                self.w[i] = (16 << 26) | (bo << 21) | (bi << 16) | (off & 0xFFFC)
        return self.w


def _head(a: Asm, reg: int, force: int) -> None:
    hi, lo = FORCE_HEAD[force]
    a(lis(12, hi), lwz(reg, lo, 12))


def _prologue(a: Asm) -> None:
    a(stwu(1, -0x20, 1), MFLR0, stw(0, 0x24, 1), stw(3, 8, 1), stw(4, 0xC, 1), stw(31, 0x10, 1),
      stw(30, 0x14, 1), stw(29, 0x18, 1))


def _epilogue(a: Asm, original: int) -> list[int]:
    a.label("done")
    a(lwz(0, 0x24, 1), MTLR0, lwz(3, 8, 1), lwz(4, 0xC, 1), lwz(31, 0x10, 1), lwz(30, 0x14, 1),
      lwz(29, 0x18, 1), addi(1, 1, 0x20))
    a(original)
    w = a.words()
    return w + ([NOP, 0] if len(w) % 2 == 0 else [0])


def move_cave(src: int, dst: int, original: int, phase: int | None = None, only_r3_id: bool = False,
              set_control: bool = False) -> list[int]:
    """Walk force `src`; every unit with the P2 bit -> UnitTransferToForce(id, dst)."""
    a = Asm()
    _prologue(a)
    if phase is not None:
        a(lis(12, 0x8033), lbz(0, 0x719, 12), cmpwi(0, phase)); a.br("bne", "done")
    _head(a, 31, src)
    a.label("loop")
    a(cmpwi(31, 0)); a.br("beq", "after")
    a(lwz(30, 0x184, 31))                                   # next, read before the unit is unlinked
    a(lwz(0, 0x1A0, 31), andis_(0, 0, P2 >> 16)); a.br("beq", "next")
    a(lbz(3, 0x198, 31))
    if only_r3_id:
        a(lbz(0, 0xB, 1), cmpw(3, 0)); a.br("bne", "next")      # saved r3 low byte = this unit's id
    a(li(4, dst)); a.call(TRANSFER)
    a.label("next")
    a(mr(31, 30)); a.br("b", "loop")
    a.label("after")
    if set_control:
        _head(a, 12, 3)
        a(cmpwi(12, 0)); a.br("beq", "done")
        a(li(0, 1), lis(12, 0x8033), stb(0, 0x71F, 12))     # control[3] = 1 (EXP-08's rule, from turn 1)
    return _epilogue(a, original)


def draft_cave() -> list[int]:
    a = Asm()
    _prologue(a)
    a(lis(12, 0x8033), lbz(0, 0x719, 12), cmpwi(0, 0)); a.br("bne", "done")           # blue phase
    a(lha(0, 0x71A, 12), cmpwi(0, 1)); a.br("bne", "done")                             # turn 1
    a.br("bl", "past"); a.w.append(0); a.label("past")                                  # prev[2] bytes
    a(MFLR31, li(30, 0))                                                                # r31 = prev, r30 = port
    a.label("port")
    a(lis(12, PADSTATUS >> 16), ori(12, 12, PADSTATUS & 0xFFFF), mulli(0, 30, 12), lhzx(0, 12, 0))
    a(andi_(0, 0, LR_BITS), cmpwi(0, LR_BITS), li(0, 1)); a.br("beq", "held"); a(li(0, 0))
    a.label("held")
    a(lbzx(29, 31, 30), stbx(0, 31, 30), cmpwi(0, 1)); a.br("bne", "nextport")
    a(cmpwi(29, 0)); a.br("bne", "nextport")                                          # rising edge only
    # --- act for port r30 ---
    a.call(CURSOR_UNIT)
    a(cmpwi(3, 0)); a.br("beq", "nextport")
    a(mr(29, 3), addi(3, 29, 0x1BC), li(4, 0)); a.call(HAS_ATTR)
    a(cmpwi(3, 0)); a.br("bne", "nextport")                                           # never the lord
    a(lwz(12, 0x190, 29), lbz(0, 8, 12), lwz(11, 0x1A0, 29))
    a(cmpwi(0, 0)); a.br("beq", "eligible")
    a(cmpwi(0, 3)); a.br("bne", "nextport")
    a(andis_(12, 11, OWNED >> 16)); a.br("beq", "nextport")                           # native partner
    a.label("eligible")
    a(andis_(12, 11, OWNED >> 16)); a.br("bne", "owned")
    # unassigned: whose pick? count owned units per player in forces 0, 3, 5, 7 (r3 = #P1 - #P2)
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
    a(cmpwi(30, 0)); a.br("bne", "p2pick")
    a(cmpwi(3, 0)); a.br("bgt", "nextport")                                           # P1 picks if #P1 <= #P2
    a(lwz(11, 0x1A0, 29), oris(11, 11, OWNED >> 16), stw(11, 0x1A0, 29)); a.br("b", "sound")
    a.label("p2pick")
    a(cmpwi(3, 0)); a.br("ble", "nextport")                                           # P2 picks if #P1 > #P2
    a(lwz(11, 0x1A0, 29), oris(11, 11, (OWNED | P2) >> 16), stw(11, 0x1A0, 29))
    a(lbz(3, 0x198, 29), li(4, 3)); a.call(TRANSFER)
    a(li(0, 1), lis(12, 0x8033), stb(0, 0x71F, 12))                                    # control[3] = 1
    a.br("b", "sound")
    a.label("owned")
    a(andis_(12, 11, P2 >> 16), li(0, 0)); a.br("beq", "ownerok"); a(li(0, 1))
    a.label("ownerok")
    a(cmpw(0, 30)); a.br("bne", "nextport")                                          # only the owner releases
    a(rlwinm(11, 11, 0, 3, 0), stw(11, 0x1A0, 29))                                      # clear OWNED and P2
    a(cmpwi(30, 0)); a.br("beq", "sound")
    a(lbz(3, 0x198, 29), li(4, 0)); a.call(TRANSFER)                                    # Player 2's unit back to blue
    a.label("sound")
    a(lis(3, 0x8027), addi(3, 3, -0x6F90), addi(3, 3, 0x138), li(4, 0x64)); a.call(PLAY_SE)
    a.label("nextport")
    a(addi(30, 30, 1), cmpwi(30, 2)); a.br("blt", "port")
    return _epilogue(a, INPUT_HOOK[1])


def _rl_mask(mb: int, me: int) -> int:
    m, i = 0, mb
    while True:
        m |= 1 << (31 - i)
        if i == me:
            return m
        i = (i + 1) % 32


def flag_bit_usage(dol) -> dict[int, int]:
    """F-52 evidence: how often each bit of unit+0x1A0 appears in a narrow (<= 4-bit) mask within 8
    instructions before / 10 after any lwz/stw of +0x1A0 (andi./andis./ori/oris/rlwinm, shifted masks mapped
    back to source bits). Bits 25-30 count 0 in GFEE01 rev 0."""
    words = list(dol.text_words())
    bits = {b: 0 for b in range(32)}
    for i, (_a, w) in enumerate(words):
        if (w >> 26) not in (32, 36) or (w & 0xFFFF) != 0x1A0:
            continue
        for _b, x in words[max(0, i - 8):i + 10]:
            op = x >> 26
            m = {28: x & 0xFFFF, 29: (x & 0xFFFF) << 16, 24: x & 0xFFFF, 25: (x & 0xFFFF) << 16}.get(op)
            if op == 21:
                sh, m = (x >> 11) & 31, _rl_mask((x >> 6) & 31, (x >> 1) & 31)
                m = ((m >> sh) | (m << (32 - sh))) & 0xFFFFFFFF if sh else m
            if m is not None and bin(m).count("1") <= 4:
                for b in range(32):
                    bits[b] += (m >> b) & 1
    return bits


def blocks21() -> list[tuple[int, list[int]]]:
    out = [(APPLY_HOOK[0], move_cave(0, 3, APPLY_HOOK[1], phase=0, set_control=True))]
    out += [(addr, move_cave(3, 0, orig)) for addr, orig in RETURN_HOOKS]
    out.append((ESCAPE_HOOK[0], move_cave(3, 0, ESCAPE_HOOK[1], only_r3_id=True)))
    return out


def code_lines(n: int) -> list[str]:
    lines = [f"${NAMES[n]}"]
    for addr, words in (blocks21() if n == 21 else [(INPUT_HOOK[0], draft_cave())]):
        lines += c2_lines(addr, words)
    return lines


def write_ini(path: Path) -> None:
    """Replace the $EXP-21 / $EXP-22 code lines (their comment blocks stay); insert both if missing."""
    lines = path.read_text().split("\n")
    for n in (21, 22):
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
        print("updated $EXP-21 and $EXP-22 in codes/GFEE01.ini")
    else:
        print("\n".join(code_lines(21) + [""] + code_lines(22)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
