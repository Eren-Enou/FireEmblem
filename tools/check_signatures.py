"""Re-verify the static main.dol findings recorded in docs/RESEARCH.md (read-only).

Every entry pins an instruction word at an address in GFEE01 rev 0 main.dol.
If any check fails, the addresses in the docs do not apply to this build.

Usage: python -m tools.check_signatures [image] [--disasm]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tools.fe9.disc import DiscReader
from tools.fe9.ppc import Dol
from tools.verify_game import DEFAULT_IMAGE

# (address, expected word, meaning) -- see docs/RESEARCH.md section "Faction model"
SIGNATURES: list[tuple[int, int, str]] = [
    # map init (0x8014D920): phase=0, turn=1, control[0]=1 (human), control[1..3]=2 (CPU)
    (0x8014D950, 0x9BDF0011, "stb r30(=0),0x11(state)   phase = 0"),
    (0x8014D954, 0xB07F0012, "sth r3(=1),0x12(state)    turn = 1"),
    (0x8014D960, 0x987F0014, "stb r3(=1),0x14(state)    control[0] = human"),
    (0x8014D964, 0x981F0015, "stb r0(=2),0x15(state)    control[1] = CPU"),
    (0x8014D968, 0x981F0016, "stb r0(=2),0x16(state)    control[2] = CPU"),
    (0x8014D96C, 0x981F0017, "stb r0(=2),0x17(state)    control[3] = CPU"),
    # unit selectability: forces 2/3 selectable when phase==force and control==1
    (0x80028548, 0x88030016, "lbz r0,0x16(state)        control[2] check"),
    (0x80028578, 0x88030017, "lbz r0,0x17(state)        control[3] check"),
    # phase step: control[phase]==1 starts the human-input process
    (0x8002E754, 0x88040014, "lbz r0,0x14(state+phase)  control[phase]"),
    (0x8002E758, 0x28000001, "cmplwi r0,1"),
    # force table base 0x802CA264, 0xC per force, indexed by dispos byte
    (0x8003C898, 0x1CA0000C, "mulli r5,r0,0xC           force stride"),
    (0x8003C8A0, 0x3804A264, "addi r0,r4,-0x5D9C        0x802CA264"),
    (0x8003B6D0, 0x90830190, "stw r4,0x190(r3)          unit->force = r4"),
    # phase advance (0x8014D3B4): 0 -> 3 -> 1 -> 2 -> 0 (turn+1)
    (0x8014D3E0, 0x38000003, "li r0,3                   after phase 0 comes 3"),
    (0x8014D3EC, 0x38000001, "li r0,1                   after phase 3 comes 1"),
    (0x8014D3F8, 0x38000002, "li r0,2                   after phase 1 comes 2"),
    (0x8014D404, 0x38000000, "li r0,0                   after phase 2 comes 0, turn++"),
    # SetChapter(state, id): prev id -> state+0x51E, id -> state+0x10
    (0x8014D2C4, 0x98830010, "stb r4,0x10(r3)           chapter id"),
    # turn-loop proc step: control[phase]==1 -> start human input proc 0x80284AC8
    (0x8002E768, 0x38654AC8, "addi r3,r5,0x4AC8         human phase proc"),
    # US equivalent of Ralf's PAL hook 0x80029824 (unit->force load)
    (0x80029684, 0x80630190, "lwz r3,0x190(r3)"),
    (0x80029688, 0x88030008, "lbz r0,8(r3)              force->id"),
    # unit table 0x802B14E4, stride 0x280, ids 1..0x9F
    (0x800295D4, 0x38A314E4, "addi r5,r3,0x14E4         unit table"),
    (0x800295E8, 0x1C000280, "mulli r0,r0,0x280         unit stride"),
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("image", nargs="?", type=Path, default=DEFAULT_IMAGE)
    ap.add_argument("--disasm", action="store_true")
    args = ap.parse_args()
    with DiscReader(args.image) as disc:
        dol = Dol(disc.read_dol())
    failures = 0
    for addr, expected, meaning in SIGNATURES:
        actual = dol.u32(addr)
        ok = actual == expected
        failures += not ok
        print(f"{'OK ' if ok else 'BAD'} {addr:08X} {actual:08X} (expect {expected:08X})  {meaning}")
        if args.disasm:
            print("        " + dol.disasm(addr, 1)[0])
    print(f"{len(SIGNATURES) - failures}/{len(SIGNATURES)} signatures match")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
