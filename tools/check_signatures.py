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
    # CAMP-005: original UnitSetPos fixture setup, GFEE01 rev0.
    (0x801A0E84, 0x9421FFE0, "UnitSetPos native entry"),
    (0x801A0E8C, 0x5463063F, "UnitSetPos takes byte-sized unit ID"),
    (0x801A0ED4, 0x98810009, "UnitSetPos stages x argument"),
    (0x801A0EE4, 0x98A10008, "UnitSetPos stages y argument"),
    (0x801A0EF4, 0x4BF66E71, "UnitSetPos calls original position helper"),
    (0x801A0F04, 0x4BE97269, "UnitSetPos calls original position worker"),
    (0x801A0F10, 0x4BE81A6D, "UnitSetPos refreshes original map state"),
    (0x801A0F18, 0x4BEAFD79, "UnitSetPos refreshes original unit display"),
    (0x800BD4C0, 0x9421FFE0, "UnitGetByPos native entry"),
    (0x800BD4E8, 0x38600003, "UnitGetByPos selects active tactical force mask"),
    (0x800BD550, 0x8805019E, "UnitGetByPos compares unit x"),
    (0x800BD560, 0x8805019F, "UnitGetByPos compares unit y"),
    (0x800BD584, 0x38600000, "UnitGetByPos returns zero when empty"),
    (0x800BD58C, 0x887F0198, "UnitGetByPos returns found unit ID"),
    (0x80037BD0, 0x2C040000, "unit indexed inventory accessor begins"),
    (0x80037BE4, 0x54831838, "unit inventory slot stride is eight bytes"),
    (0x80037BE8, 0x386301CC, "unit inventory slots 0..3 begin at +1CC"),
    (0x80037C0C, 0x386301EC, "unit inventory slots 4..7 begin at +1EC"),
    # CAMP-004: kind-8 original conversation identity/direction matching.
    (0x800BF1E8, 0x9421FFE0, "conversation matching query entry"),
    (0x800BF22C, 0x2C000008, "conversation matcher selects kind 8"),
    (0x800BF234, 0xA81E001A, "conversation key pool offset parameter 3"),
    (0x800BF260, 0xA81E0014, "conversation first identity pool offset"),
    (0x800BF274, 0xA81E0016, "conversation second identity pool offset"),
    (0x800BF29C, 0x80C40188, "conversation target character record"),
    (0x800BF2A0, 0x80850188, "conversation actor character record"),
    (0x800BF2A4, 0x7C04E040, "conversation compares first identity"),
    (0x800BF2AC, 0x7C061840, "conversation compares second identity"),
    (0x800BF2BC, 0xA81E0018, "conversation direction parameter"),
    (0x800BF2C4, 0x4182001C, "zero direction parameter skips reverse comparison"),
    (0x800BF2C8, 0x7C041840, "reverse actor identity comparison"),
    (0x800BF2D0, 0x7C06E040, "reverse target identity comparison"),
    # CAMP-003: original Escape menu availability and kind-5 tile-event query.
    (0x80077438, 0x9421FFF0, "Escape availability entry"),
    (0x8028841C, 0x80077438, "Escape menu availability callback"),
    (0x80288428, 0x8007749C, "Escape menu action callback"),
    (0x8026C444, 0x4D4D4D5F, "Escape label MMM_ESC prefix"),
    (0x80077464, 0x3860000E, "Escape uses tile action code 14"),
    (0x80077468, 0x8885019E, "Escape reads unit x"),
    (0x8007746C, 0x88A5019F, "Escape reads unit y"),
    (0x80077470, 0x480474F9, "Escape queries kind-5 tile event"),
    (0x800BE968, 0x9421FFE0, "kind-5 event query entry"),
    (0x800BE9C0, 0x2C000005, "query accepts scene kind 5"),
    (0x800BE9DC, 0xA81E0014, "query compares parameter 0 to x"),
    (0x800BE9FC, 0xA81E0016, "query compares parameter 1 to y"),
    (0x800BEA1C, 0xA81E0018, "query compares parameter 2 to action"),
    (0x800BEA30, 0xA81E001A, "query resolves parameter 3 as pool offset"),
    (0x800C273C, 0x80630008, "scene string resolver loads parent ScriptInfo"),
    (0x800C2744, 0x80630024, "scene string resolver loads parent pool"),
    # CAMP-002: FE9 VM decoding and escape passenger selector.
    (0x80011F18, 0x28000041, "VM dispatch highest FE9 opcode is 0x41"),
    (0x80011F28, 0x38633F90, "VM dispatch table at 0x80283F90"),
    (0x800127F4, 0x7C050774, "number.8 sign-extends operand"),
    (0x800128F8, 0x7C050774, "string.8 sign-extends pool offset"),
    (0x8028D41C, 0x800BD7C0, "UnitGet selector 4 dispatch"),
    (0x800BD7C0, 0x807F0194, "UnitGet selector 4 loads rescue-linked unit"),
    (0x800BD5B8, 0x4BF59625, "UnitGetByPID wrapper calls faction-independent PID lookup"),
    (0x80016C10, 0x80040188, "PID lookup scans character identity, not tactical faction"),
    (0x800B7174, 0x38800005, "Join creates group in roster force 5"),
    # Campaign audit CAMP-001: escape objective mask excludes tactical yellow.
    (0x801B71B4, 0x38600001, "PlayerEscapeCount: mask force 0 enabled"),
    (0x801B71C4, 0x38C00000, "PlayerEscapeCount: mask force 3 disabled"),
    (0x801B71CC, 0x39000001, "PlayerEscapeCount: mask force 5 enabled"),
    (0x801B7224, 0x7C0300AE, "PlayerEscapeCount: force-indexed mask lookup"),
    (0x801B7284, 0x38600001, "PlayerEscapeCheck: mask force 0 enabled"),
    (0x801B7294, 0x38C00000, "PlayerEscapeCheck: mask force 3 disabled"),
    (0x801B729C, 0x39000001, "PlayerEscapeCheck: mask force 5 enabled"),
    (0x801B72F4, 0x7C0300AE, "PlayerEscapeCheck: force-indexed mask lookup"),
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
    # Force change (F-34). UnitTransferToForce 0x800BCA38(unit id, force), registered as a script command
    (0x800BB3DC, 0x3883CA38, "addi r4,r3,-0x35C8        register UnitTransferToForce"),
    (0x800BCA38, 0x9421FFF0, "stwu r1,-0x10(r1)         UnitTransferToForce entry"),
    (0x800BCAB4, 0x4BF80B59, "bl SetUnitForce           0x8003D60C(unit, force)"),
    (0x8003D658, 0x4BFD8049, "bl 0x800156A0             unlink from old force list"),
    (0x8003D670, 0x4BFD80A9, "bl 0x80015718             append to new force list"),
    (0x80016BDC, 0x9421FFF0, "stwu r1,-0x10(r1)         unit by PID string (EXP-15)"),
    (0x80016C1C, 0x7C001840, "cmplw r0,r3               unit+0x188 == character record"),
    (0x800BD5CC, 0x88630198, "lbz r3,0x198(r3)          unit id byte (UnitGetByPID)"),
    # EXP-15 hook sites: human-phase start step, and the entries of both chapter-end steps (F-35)
    (0x8002E738, 0x9421FFF0, "stwu r1,-0x10(r1)         phase-start step entry (EXP-15 block 1)"),
    (0x8002E0D0, 0x9421FFD0, "stwu r1,-0x30(r1)         chapter transition step entry (EXP-15 block 3)"),
    (0x8002E0F8, 0x5400EFFF, "rlwinm. r0,r0,29,31,31    state+0x9F bit 0x08 -> early exit"),
    (0x80284FA4, 0x0000200F, "proc op call              turn loop: ... -> 0x8002E0D0"),
    (0x80284FA8, 0x8002E0D0, "proc step pointer         chapter transition"),
    (0x80005F04, 0x9421FFE0, "stwu r1,-0x20(r1)         chapter-sequence step entry (EXP-15 block 4)"),
    (0x80005F28, 0x481DD875, "bl 0x801E379C             rebuild units from save data"),
    (0x80005FF0, 0x48010C69, "bl 0x80016C58             roster move, after the rebuild"),
    (0x80016C58, 0x9421FFE0, "stwu r1,-0x20(r1)         army->roster (force 0 -> 5)"),
    # AllUnitEscape 0x800BA784 (script command, F-39): escapes the force 0 list, then forces 0-3 (mask 3)
    (0x800BA784, 0x9421FFD0, "stwu r1,-0x30(r1)         AllUnitEscape entry (EXP-15 block 2)"),
    (0x800BA840, 0x80630004, "lwz r3,4(r3)              force 0 tail"),
    (0x800BA84C, 0x4BF8376D, "bl 0x8003DFB8             escape unit (force 0 list)"),
    (0x800BA860, 0x38600003, "li r3,3                   mask query 3 = forces 0-3"),
    (0x800BA8B4, 0x4BF83705, "bl 0x8003DFB8             escape/free the rest of forces 0-3"),
    # Auto-end (F-42): unit done -> if Auto End on (state+0x9E bit 0x20 clear) and no next unit -> end phase
    (0x80028CBC, 0x60000001, "ori r0,r0,1               mark the unit as acted"),
    (0x80028CC4, 0x8803009E, "lbz r0,0x9E(state)        option flags"),
    (0x80028CC8, 0x5400DFFE, "rlwinm r0,r0,27,31,31     bit 0x20 = Auto End off"),
    (0x80028CD8, 0x48081919, "bl 0x800AA5F0             next unit that can act"),
    (0x80028CEC, 0x4BFE3921, "bl 0x8000C60C             end the human-phase proc"),
    (0x80029258, 0x48081399, "bl 0x800AA5F0             Next Unit button"),
    (0x800AA5F8, 0x80840000, "lwz r4,0(r4)              force 0 head (EXP-17 block 1)"),
    (0x800AA61C, 0x28000000, "cmplwi r0,0               start unit in force 0? (EXP-17 block 2)"),
    # Unit list (F-43): map menu Unit -> 0x8012C9FC(force 0) -> builder 0x8012DFA8 single-force path
    (0x8007384C, 0x38600000, "li r3,0                   Base Data for force 0"),
    (0x80073854, 0x480B91A9, "bl 0x8012C9FC             open E_UnitList(force)"),
    (0x8012E120, 0x7C83002E, "lwzx r4,r3,r0             head of force +0x60 (count)"),
    (0x8012E12C, 0x80840184, "lwz r4,0x184(r4)          count walk next (EXP-18 block 1)"),
    (0x8012E46C, 0x837A0184, "lwz r27,0x184(r26)        fill walk next (EXP-18 block 2)"),
    (0x8002EA48, 0x60000400, "ori r0,r0,0x400           map start: force 0 units = deployed players"),
    # Death routine 0x8003E8DC (F-45): force 0 -> force 6 died list + flag 0x8000; others freed
    (0x8003E8F0, 0x880301A8, "lbz r0,0x1A8(r3)          HP"),
    (0x8003E94C, 0x28000000, "cmplwi r0,0               force 0? (EXP-19)"),
    (0x8003E968, 0x38630048, "addi r3,r3,0x48           force 6 = died list"),
    (0x8003E96C, 0x4BFD6E71, "bl 0x800157DC             prepend to force 6"),
    (0x8003E980, 0x60008000, "ori r0,r0,0x8000          died flag"),
    (0x8003E98C, 0x981F0234, "stb r0,0x234(r31)         chapter of death"),
    (0x8003E9F8, 0x4BFFCCF9, "bl 0x8003B6F0             free a non-player unit"),
    (0x801B70A0, 0x80840048, "lwz r4,0x48(r4)           GetDiedPlayerCount walks force 6"),
    # UnitEscape 0x800BA8F8(unit id) (script command): unit id byte in r3 -> escape worker (EXP-16 block 5)
    (0x800BA8F8, 0x9421FFF0, "stwu r1,-0x10(r1)         UnitEscape entry"),
    (0x800BA900, 0x5463063F, "clrlwi. r3,r3,24          unit id argument"),
    (0x800BA944, 0x4BF83675, "bl 0x8003DFB8             escape worker"),
    (0x80016C84, 0x38800005, "li r4,5                   to force 5 (roster)"),
    (0x8002E38C, 0x4BFE88CD, "bl 0x80016C58             from the chapter transition 0x8002E0D0"),
    # Phase-start cursor step 0x8002E444 (turn-loop script 0x80284EE8/0x80284F34, before 0x8002E738): phase 0 only,
    # option bit 0x40 of state+0x9E clear -> cursor to the first force unit with attribute bit 0 (F-51; EXP-20)
    (0x80284F34, 0x8002E444, ".data: turn-loop step = cursor step 0x8002E444"),
    (0x80284F54, 0x8002E738, ".data: next steps reach the human-proc start 0x8002E738"),
    (0x8002E45C, 0x88830011, "lbz r4,0x11(r3)           phase"),
    (0x8002E464, 0x40820098, "bne 0x8002E4FC            not phase 0 -> skip (EXP-20 hook)"),
    (0x8002E468, 0x8803009E, "lbz r0,0x9e(r3)           option byte"),
    (0x8002E46C, 0x5400D7FF, "rlwinm. r0,r0,26,31,31    option bit 0x40"),
    (0x8002E490, 0x480D7731, "bl 0x80105BC0             attribute bit 0 of unit+0x1BC"),
    (0x8002E4B0, 0x887F019E, "lbz r3,0x19e(r31)         cursor move from unit r31 (EXP-20 target)"),
    (0x8002E4F8, 0x4811E6E1, "bl 0x8014CBD8             move the cursor (state, f1 = x, f2 = y)"),
    (0x8002E4FC, 0x80010024, "lwz r0,0x24(r1)           epilogue (EXP-20 skip target)"),
    (0x800292AC, 0x4812392D, "bl 0x8014CBD8             Next Unit moves the cursor the same way"),
    # Ownership in the unit flag word (F-52; EXP-21/EXP-22): the card save keeps unit+0x1A0 raw, and every
    # chapter/map mask keeps bits 25-30
    (0x8003C994, 0x38BE01A0, "addi r5,r30,0x1a0          unit load: flag word ..."),
    (0x8003C998, 0x38800004, "li r4,4                    ... read as 4 raw bytes (0x8017A810)"),
    (0x8003CBBC, 0x38BE01A0, "addi r5,r30,0x1a0          unit save: flag word written raw (0x8017A430)"),
    (0x8002E038, 0x3C60FF89, "lis r3,-0x77               chapter transition mask 0xFF88C7FE ..."),
    (0x8002E040, 0x3803C7FE, "addi r0,r3,-0x3802         ... (keeps 0x7E000000)"),
    (0x8002EA10, 0x3800BBFF, "li r0,-0x4401              map start clears 0x4400 only"),
    (0x800291D8, 0x9421FFD0, "stwu r1,-0x30(r1)          human-phase input step entry (EXP-22 hook)"),
    (0x800AA794, 0x3C608033, "lis r3,0x8033              unit under the cursor (map grid 0x802CA518 +0xD)"),
    (0x800AA7DC, 0x8863000D, "lbz r3,0xd(r3)             unit id at the cursor tile"),
    (0x80105BC0, 0x9421FFF0, "stwu r1,-0x10(r1)          has attribute (bit set, index)"),
    (0x801475FC, 0x9421FFE0, "stwu r1,-0x20(r1)          sound effect (Next Unit's cursor sound)"),
    # EXP-23 (draft v2): park after EXP-21's apply, unpark after the acted bit and around the phase advance
    (0x8002E73C, 0x7C0802A6, "mflr r0                    phase-start step, 2nd instruction (EXP-23 park)"),
    (0x80028CC4, 0x8803009E, "lbz r0,0x9e(r3)            after the acted bit, before auto-end (EXP-23 unpark)"),
    (0x8002E65C, 0x4811ED59, "bl 0x8014D3B4              phase advance call (EXP-23 unpark)"),
    (0x80269175, 0x5346585F, ".data \"SFX_\" SYS_MISS1 (refusal sound)"),
    (0x802691DF, 0x5346585F, ".data \"SFX_\" SYS_UNIT_SELECT1 (Player 1 claim)"),
    (0x802747B5, 0x5346585F, ".data \"SFX_\" SYS_UNIT_CHANGE1 (Player 2 claim)"),
    (0x80269193, 0x5346585F, ".data \"SFX_\" SYS_UNIT_CANCEL1 (release)"),
    # Preparations (F-56, F-57): sortie slots in the state block, the Pick Units list and its toggle
    (0x8014CF60, 0x98030544, "stb r0,0x544(r3)           SallySetByGroup: slot count = 0"),
    (0x8014CCC0, 0x38060545, "addi r0,r6,0x545           slot (x, y) pairs at state+0x545"),
    (0x800B6DF8, 0x88630056, "lbz r3,0x56(r3)            SallyGetSurplus = state+0x56"),
    (0x8012C9E8, 0x800401A0, "lwz r0,0x1a0(r4)           Pick Units toggle callback ..."),
    (0x8012C9F0, 0x6C008000, "xoris r0,r0,0x8000         ... flips bit 0x80000000 (sortie)"),
    (0x8012C9D0, 0x90830054, "stw r4,0x54(r3)            list action callback slot"),
    (0x8012F074, 0x806301A0, "lwz r3,0x1a0(r3)           list row state from the flags ..."),
    (0x8012F098, 0x546003DF, "rlwinm. r0,r3,0,15,15      ... 0x10000 forced -> row state 0x13"),
    (0x80291088, 0x80275B0E, ".data E_SallyList proc header (name)"),
    (0x802910C0, 0x8012D6A4, ".data E_SallyList step: list input"),
    (0x8012D6B8, 0x808D84A0, "lwz r4,-0x7b60(r13)        list input reads the current pad (F-29)"),
    # Unit-list drawing (F-58; EXP-25)
    (0x8012F0D4, 0x8198004C, "lwz r12,0x4c(r24)          cell draw: column vtable (EXP-25 hook)"),
    (0x8012F154, 0x9421FFC0, "stwu r1,-0x40(r1)          data-page cell draw (EXP-25 colours only these)"),
    (0x8012F0DC, 0x8019003C, "lwz r0,0x3c(r25)           row records at list+0x3C"),
    (0x8012F0F0, 0x7C80EA14, "add r4,r0,r29              row record = list+0x3C + r29 (0x24 per row)"),
    (0x8012F54C, 0x807E0038, "lwz r3,0x38(r30)           column array at list+0x38"),
    (0x8012F224, 0x57C5063E, "clrlwi r5,r30,24           cell colour index -> text draw 0x8001003C"),
    (0x8018D91C, 0x38046088, "addi r0,r4,0x6088          text palette 0x80296088 (RGBA per index)"),
    (0x8029610C, 0x6DCFF6FF, ".data palette 0x21 light blue (Player 1)"),
    (0x802960C8, 0xFFC010FF, ".data palette 0x10 orange (transfer requested)"),
    (0x8012D6A4, 0x9421FFD0, "stwu r1,-0x30(r1)          list input step entry (EXP-26 hook)"),
    (0x8012DBE4, 0x881F0062, "lbz r0,0x62(r31)           highlighted row ..."),
    (0x8012DBFC, 0x7C83002E, "lwzx r4,r3,r0              ... unit = list+0x3C row record +0"),
    (0x80269183, 0x5346585F, ".data \"SFX_\" SYS_SELECT1 (transfer request)"),
    (0x802960A0, 0xFFFF64FF, ".data palette 0x06 yellow (Player 2)"),
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
