"""Generate the preparation-screen codes (PREP-01): EXP-25 = ownership colours in the native unit lists.

The unit-list module (Pick Units = E_SallyList in preparations, Base Data in battle) draws every cell through
0x8012EF5C. Before each cell draw (0x8012F0D4), r5 holds the cell's colour index into the native text palette
0x80296088 (F-58). EXP-25 changes it for the **Name column only** from the row's unit ownership (F-52):

  Player 1 (OWNED, not P2) and Ike (unit id 1)  -> 0x21  light blue #6DCFF6
  Player 2 (OWNED | P2)                        -> 0x06  yellow     #FFFF64
  unassigned                                   -> unchanged (white 0x01, or forced green 0x13)
  unavailable (index 0 = grey)                 -> unchanged

Display only: no calls, no writes. Registers at the hook: r24 = column object, r25 = list object,
r29 = row offset (0x24 per row), r5 = colour index; r0/r11/r12 are free (r0 is reloaded right after).
Row record = *(list+0x3C) + r29, unit pointer at +0; the Name column is the first entry of list+0x38.

Usage: python -m tools.prep_code [--write]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from tools.draft_code import OWNED, P2, Asm, andis_
from tools.owner_code import _d, c2_lines, cmpw, cmpwi, li, lbz, lis, lwz, ori, NOP

ROOT = Path(__file__).resolve().parents[1]
NAME = "EXP-25 Unit lists show ownership: Player 1 light blue, Player 2 yellow (Pick Units, Base Data)"
DRAW_HOOK = (0x8012F0D4, 0x8198004C)     # lwz r12,0x4c(r24)
UNIT_TABLE = 0x802B14E4
COLOUR_P1, COLOUR_P2 = 0x21, 0x06


def lwzx(d, a, b): return (31 << 26) | (d << 21) | (a << 16) | (b << 11) | (23 << 1)
def subf(d, a, b): return (31 << 26) | (d << 21) | (a << 16) | (b << 11) | (40 << 1)
def cmplw(a, b): return (31 << 26) | (a << 16) | (b << 11) | (32 << 1)


def colour_cave() -> list[int]:
    a = Asm()
    a(lwz(12, 0x38, 25), lwz(12, 0, 12), cmpw(12, 24)); a.br("bne", "done")           # Name column only
    a(lwz(12, 0x3C, 25), lwzx(12, 12, 29))                                              # row's unit
    a(lis(11, UNIT_TABLE >> 16), ori(11, 11, UNIT_TABLE & 0xFFFF), subf(11, 11, 12),
      lis(0, 2), cmplw(11, 0)); a.br("bge", "done")                                     # a unit-table pointer
    a(cmpwi(5, 0)); a.br("beq", "done")                                                 # unavailable stays grey
    a(lbz(0, 0x198, 12), cmpwi(0, 1)); a.br("beq", "p1")                                # Ike = Player 1
    a(lwz(11, 0x1A0, 12), andis_(0, 11, OWNED >> 16)); a.br("beq", "done")             # unassigned unchanged
    a(andis_(0, 11, P2 >> 16)); a.br("bne", "p2")
    a.label("p1")
    a(li(5, COLOUR_P1)); a.br("b", "done")
    a.label("p2")
    a(li(5, COLOUR_P2))
    a.label("done")
    a(DRAW_HOOK[1])
    w = a.words()
    return w + ([NOP, 0] if len(w) % 2 == 0 else [0])


def blocks() -> list[tuple[int, list[int]]]:
    return [(DRAW_HOOK[0], colour_cave())]


def code_lines() -> list[str]:
    lines = [f"${NAME}"]
    for addr, words in blocks():
        lines += c2_lines(addr, words)
    return lines


def write_ini(path: Path) -> None:
    lines = path.read_text().split("\n")
    head = next((i for i, l in enumerate(lines) if l.startswith("$EXP-25 ")), None)
    if head is None:
        anchor = next(i for i, l in enumerate(lines) if l.startswith("# DBG-01"))
        lines[anchor:anchor] = code_lines() + [""]
    else:
        end = head + 1
        while end < len(lines) and len(lines[end].split()) == 2 and all(
                len(t) == 8 and all(c in "0123456789ABCDEF" for c in t) for t in lines[end].split()):
            end += 1
        lines[head:end] = code_lines()
    path.write_text("\n".join(lines), newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if args.write:
        write_ini(ROOT / "codes/GFEE01.ini")
        print("updated $EXP-25 in codes/GFEE01.ini")
    else:
        print("\n".join(code_lines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
