"""EXPERIMENT (branch experiment/alternating-actions only): unit-by-unit alternating turns, EXP-24.

Never part of a COOP package; the sequential Blue -> Yellow -> Enemy co-op stays the stable mode.

Idea: keep the blue phase's human proc running for the whole shared round and switch the phase byte
(state+0x11, 0x80330719) between 0 (blue) and 3 (yellow) whenever a unit's activation completes. Everything
that decides who is in control already keys on that byte: selection (EXP-06), controller port (EXP-14),
Next Unit and auto-end (EXP-17), the cursor cue (EXP-20). No phase transition runs, so acted flags, phase-start
events, music and banners are untouched (F-55).

  handoff   hook 0x80028CC4 = the unit-finished step 0x80028C90 right after it sets the acted bit and before
            its auto-end check (it runs once per completed activation, after the post-action event checks of the
            human proc 0x80284BE4..0x80284C18: attack, staff, talk, items, Wait ...). Only when phase is 0 or 3
            and control[0] == control[3] == 1 (both armies human):
              phase := other; if 0x800AA5F0(0) finds a unit of the other army that can act -> stay switched and
              move the cursor to it (the vanilla cursor move 0x8014CBD8, as in 0x8002E4B0)
              else phase := current; if the current army still has a unit that can act -> keep playing
              else (both done) phase := 3, so the vanilla auto-end (or a manual End) advances 3 -> 1: exactly one
              enemy phase, and the yellow phase's start (which resets every acted bit, F-16) never runs
  end       hook the phase-advance call 0x8002E65C (was bl 0x8014D3B4): if phase is 0 and both armies are human
            and force 3 has units, phase := 3 first, so End during the shared round also goes to the enemy phase.
            Then call 0x8014D3B4 via ctr.

Usage: python -m tools.alt_code [--write]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from tools.draft_code import Asm, _head
from tools.owner_code import (addi, c2_lines, cmpwi, li, lbz, lis, lwz, mr, stb, stw, stwu,
                              MFLR0, MTLR0, NOP)

ROOT = Path(__file__).resolve().parents[1]
NAME = "EXP-24 EXPERIMENT alternating unit actions: Blue and Yellow take turns one unit at a time"
ACTED_HOOK = (0x80028CC4, 0x8803009E)       # lbz r0,0x9e(r3)
ADVANCE_CALL = (0x8002E65C, 0x4811ED59)     # bl 0x8014D3B4
NEXT_ACTOR = 0x800AA5F0                     # first unit of the phase's army that can act (EXP-17: force 3 in phase 3)
CURSOR_MOVE = 0x8014CBD8                    # (state, f1 = x, f2 = y)
PHASE_ADVANCE = 0x8014D3B4


def _d(op, s, a, d): return (op << 26) | (s << 21) | (a << 16) | (d & 0xFFFF)
def subfic(d, a, imm): return _d(8, d, a, imm)
def extsb(a, s): return (31 << 26) | (s << 21) | (a << 16) | (954 << 1)
def xoris(a, s, imm): return _d(27, s, a, imm)
def lfd(f, off, a): return _d(50, f, a, off)
def fsubs(d, a, b): return (59 << 26) | (d << 21) | (a << 16) | (b << 11) | (20 << 1)


def _prologue(a: Asm) -> None:
    a(stwu(1, -0x40, 1), MFLR0, stw(0, 0x44, 1), stw(3, 0x20, 1), stw(4, 0x24, 1), stw(31, 0x28, 1),
      stw(30, 0x2C, 1), stw(29, 0x30, 1))


def _restore(a: Asm) -> None:
    a(lwz(0, 0x44, 1), MTLR0, lwz(3, 0x20, 1), lwz(4, 0x24, 1), lwz(31, 0x28, 1), lwz(30, 0x2C, 1),
      lwz(29, 0x30, 1), addi(1, 1, 0x40))


def _finish(a: Asm) -> list[int]:
    w = a.words()
    return w + ([NOP, 0] if len(w) % 2 == 0 else [0])


def _both_human(a: Asm, fail: str) -> None:
    a(lis(12, 0x8033), lbz(0, 0x71C, 12), cmpwi(0, 1)); a.br("bne", fail)              # control[0] human
    a(lbz(0, 0x71F, 12), cmpwi(0, 1)); a.br("bne", fail)                               # control[3] human


def handoff_cave() -> list[int]:
    a = Asm()
    _prologue(a)
    a(lis(12, 0x8033), lbz(31, 0x719, 12), cmpwi(31, 0)); a.br("beq", "ok")
    a(cmpwi(31, 3)); a.br("bne", "done")
    a.label("ok")
    _both_human(a, "done")
    a(subfic(30, 31, 3), stb(30, 0x719, 12))                                            # try the other army
    a(li(3, 0)); a.call(NEXT_ACTOR)
    a(mr(29, 3), cmpwi(29, 0)); a.br("bne", "handoff")
    a(lis(12, 0x8033), stb(31, 0x719, 12))                                              # back to this army
    a(li(3, 0)); a.call(NEXT_ACTOR)
    a(cmpwi(3, 0)); a.br("bne", "done")                                                 # it continues
    a(li(0, 3), lis(12, 0x8033), stb(0, 0x719, 12)); a.br("b", "done")                 # both done -> end as 3
    a.label("handoff")
    # cursor to unit r29: the vanilla int -> float conversion (0x8002E4B0..0x8002E4F4), then 0x8014CBD8
    a(lbz(5, 0x19E, 29), lis(4, 0x4330), lbz(0, 0x19F, 29), extsb(5, 5), stw(4, 8, 1), extsb(0, 0),
      lfd(2, -0x7D80, 2), xoris(5, 5, 0x8000), stw(4, 0x10, 1), xoris(0, 0, 0x8000), stw(5, 0xC, 1),
      stw(0, 0x14, 1), lfd(1, 8, 1), lfd(0, 0x10, 1), fsubs(1, 1, 2), fsubs(2, 0, 2))
    a(lis(3, 0x8033), addi(3, 3, 0x708)); a.call(CURSOR_MOVE)
    a.label("done")
    _restore(a)
    a(ACTED_HOOK[1])
    return _finish(a)


def end_cave() -> list[int]:
    a = Asm()
    _prologue(a)
    a(lis(12, 0x8033), lbz(0, 0x719, 12), cmpwi(0, 0)); a.br("bne", "go")
    _both_human(a, "go")
    _head(a, 12, 3)
    a(cmpwi(12, 0)); a.br("beq", "go")                                                  # a yellow army exists
    a(li(0, 3), lis(12, 0x8033), stb(0, 0x719, 12))
    a.label("go")
    _restore(a)
    a.call(PHASE_ADVANCE)
    return _finish(a)


def blocks() -> list[tuple[int, list[int]]]:
    return [(ACTED_HOOK[0], handoff_cave()), (ADVANCE_CALL[0], end_cave())]


def code_lines() -> list[str]:
    lines = [f"${NAME}"]
    for addr, words in blocks():
        lines += c2_lines(addr, words)
    return lines


def write_ini(path: Path) -> None:
    lines = path.read_text().split("\n")
    head = next((i for i, l in enumerate(lines) if l.startswith("$EXP-24 ")), None)
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
        print("updated $EXP-24 in codes/GFEE01.ini")
    else:
        print("\n".join(code_lines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
