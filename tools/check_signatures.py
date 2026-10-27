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
    # GetUnitSelectState (0x800284B4): context for the EXP-06 hook
    (0x80028504, 0x3BE30708, "addi r31,r3,0x708         r31 = state"),
    (0x80028508, 0x8BC40008, "lbz r30,8(r4)             r30 = unit force id"),
    (0x8002858C, 0x801D01A0, "lwz r0,0x1A0(r29)         EXP-06 hook site (original insn)"),
    (0x800285A4, 0x80010024, "lwz r0,0x24(r1)           epilogue, returns r3"),
    # phase advance: context for the EXP-08 hook (r3 = state, single caller)
    (0x8002E658, 0x38630708, "addi r3,r3,0x708          caller passes state"),
    (0x8002E65C, 0x4811ED59, "bl 0x8014D3B4             only call to phase advance"),
    (0x8014D3B4, 0x88030011, "lbz r0,0x11(r3)           EXP-08 hook site"),
    # CanGainExp (0x8003D13C): force id must be 0 or 5; EXP-10 hook site
    (0x8003D174, 0x88030008, "lbz r0,8(r3)              force id"),
    (0x8003D178, 0x28000000, "cmplwi r0,0               player force may gain EXP"),
    (0x8003D180, 0x28000005, "cmplwi r0,5               EXP-10 hook site (force 5 allowed)"),
    (0x8003D188, 0x38600000, "li r3,0                   otherwise no EXP"),
    (0x8003D1A8, 0x4BFFB509, "bl 0x800386B0             CanGainExp: GetExp == 0xFF -> no EXP"),
    # battle write-back 0x80034F40: level/EXP copied only for force 0 or 5; EXP-12 hook site
    (0x80034F54, 0x80830280, "lwz r4,0x280(r3)          real unit of battle copy"),
    (0x80034F60, 0x28000000, "cmplwi r0,0               player force: write back"),
    (0x80034F68, 0x28000005, "cmplwi r0,5               EXP-12 hook site (force 5 written back)"),
    (0x80034F78, 0x9804019A, "stb r0,0x19A(r4)          level written back"),
    (0x80034F88, 0x48003705, "bl 0x8003868C             SetExp (EXP written back)"),
    # battle-result unit pickers (EXP-13): lbz r0,8(force) ... cmplwi r0,5 at each hook site
    (0x801B60F0, 0x80630280, "lwz r3,0x280(r3)          picker: copy A real unit"),
    (0x801B6120, 0x80630560, "lwz r3,0x560(r3)          picker: copy B real unit"),
    (0x801B6148, 0x38600000, "li r3,0                   picker: no player unit -> NULL"),
    (0x801B614C, 0x4BFFD17D, "bl 0x801B32C8             level-up screen setup"),
    *[(a, 0x28000005, "cmplwi r0,5               EXP-13 hook site") for a in (
        0x801B610C, 0x801B613C, 0x801B62D4, 0x801B6304, 0x801B63BC,
        0x801B63EC, 0x801B6814, 0x801B6844, 0x801B6C28, 0x801B6C58)],
    (0x801B5E6C, 0x801E018C, "lwz r0,0x18C(r30)         level-up screen reads unit class (NULL crash site)"),
    # pad input (EXP-14): PADStatus[4] @0x802EF408, pad objects @0x802EF438 (stride 0x24), current pad @r13-0x7B60
    (0x80003334, 0x3DA08036, "lis r13,0x8036             SDA base (r13 = 0x8036EDA0)"),
    (0x80003338, 0x61ADEDA0, "ori r13,r13,0xEDA0"),
    (0x80025A48, 0x481EC279, "bl 0x80211CC0             PADRead(0x802EF408)"),
    (0x80025A98, 0x4BFFFC35, "bl 0x800256CC             pad object update from PADStatus"),
    (0x80025B8C, 0xBB61000C, "lmw r27,0xC(r1)           EXP-14 hook site (pad update epilogue)"),
    (0x80025C3C, 0x3803F438, "addi r0,r3,-0xBC8         pad object 0 (0x802EF438)"),
    (0x80025C48, 0x900D84A0, "stw r0,-0x7B60(r13)       current pad = pad object 0 (only store)"),
    (0x8002595C, 0x1C830024, "mulli r4,r3,0x24          GetPad(n)"),
    # GetExp (0x800386B0): 0xFF for force 1/2/3, else unit+0x19B; EXP-11 hook site
    (0x800386B4, 0x88040008, "lbz r0,8(r4)              force id"),
    (0x800386C8, 0x28000003, "cmplwi r0,3               EXP-11 hook site (yellow -> 0xFF)"),
    (0x800386CC, 0x4082000C, "bne 0x800386D8            not 1/2/3: read EXP"),
    (0x800386D0, 0x386000FF, "li r3,0xFF                EXP shown as --"),
    (0x800386D8, 0x8863019B, "lbz r3,0x19B(r3)          unit EXP byte"),
    # phase-end handler 0x8002E670: context for the EXP-07 hook
    (0x8002E684, 0x3BE40708, "addi r31,r4,0x708         r31 = state"),
    (0x8002E6DC, 0x28030000, "cmplwi r3,0               EXP-07 hook site (phase-3 branch)"),
    (0x8002E6F4, 0x480CDF49, "bl 0x800FC63C             launch E_CP_PhaseMain (mode 1)"),
    (0x8002E70C, 0x28000002, "cmplwi r0,2               phases 1/2: CP only if control==2"),
    (0x8002E71C, 0x80010024, "lwz r0,0x24(r1)           handler epilogue"),
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
