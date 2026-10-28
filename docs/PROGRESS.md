# Progress Log

## 2026-10-27 — Session 1l: partner progression complete, COOP-P2

- **EXP-10 alone failed.** The trace found two more force gates, `GetExp` (F-23, EXP-11) and the battle write-back (F-24, EXP-12). With all three, Lethe kept 15 EXP.
- **Regression pass with the package** (TESTING.md "EXP-13 / COOP-P2"): counter EXP and accumulation pass (0 → 15 → 27). The **level-up crashed** (NULL unit, invalid read at `0x801B5E6C`) because five battle-result pickers only accept force 0/5 (F-26). **EXP-13** fixes it; the level-up then passed (lv 3 → 4, growth bytes +1, max HP 34 → 35). Blue EXP and vanilla (codes off) are unchanged.
- **COOP-P2** = COOP-P1 + EXP-10..13 in one code. Tests 22/22, signatures 65/65.
- F-25: a state saved with codes restores the old code list, so always test new codes from slot 6. F-27: unpatched force 0/5 checks are listed. F-28: Next Unit cycles blue units only (cosmetic).
- Next: Phase 2, port-2 controller ownership.

## 2026-10-27 — Session 1m: Phase 2, controller ownership (EXP-14, COOP-P3)

- Traced the pad pipeline statically (F-29): every gameplay read goes through one current-pad pointer (`0x80367240`, 320 loads, one store at init). EXP-14 retargets it each frame: port 2 in a human yellow phase, port 1 otherwise, and port 1 when port 2 has no controller.
- `tools/setup_pads.py` configures port 2 (keyboard layout for one-PC tests, or a device the tester maps).
- **Local two-pad run PASSED** (two keyboard layouts, two full Ch9 turns): port 1 had no effect in the yellow phase (cursor, A, Z, tutorial prompt), port 2 had no effect in the player phase or the turn-start conversation, and each army completed move/Wait/End on its own port. Memory confirms the pointer switch. The port-2-absent fallback also passed.
- **COOP-P3** = COOP-P2 + EXP-14. Tests 25/25, signatures 73/73. The Dolphin config was restored and the user's slot 1 and memory card are unchanged (hashes match).
- Blocked on the tester: a real two-device run (procedure in TESTING.md). Phase 3 (Netplay) prep notes are in TESTING.md. The main open question is how to start Ch9 under Netplay without save states.

## 2026-10-27 — Session 1n: tester two-pad pass, numpad layout, Netplay Chapter 9 start

- **Tester PASS (EXP-14 / COOP-P3):** with two keyboard-emulated controllers, blue answers only to controller 1 and yellow only to controller 2.
- Port 2 stick moved to the keypad (`NUMPAD8/5/4/6`, F-33). The rest of the port 2 layout is unchanged. Dolphin loads the bindings as valid; pressing the keys still needs the tester's 30-second check (TESTING.md).
- **Chapter 9 start for Netplay solved (NET-00, F-31):**
  - Dolphin blocks state loads in Netplay.
  - A Suspend from the slot 6 state is rejected ("not the original Memory Card").
  - So a native card was made in a private user folder: fresh game + EXP-05 → Prologue won → saved at the prompt as **"Ch. 9: Gallia"** → after a fresh boot, *Restart Chapter* reaches the Ch9 base. The card is backed up in `work/saves/netplay_ch9_card/`.
- `tools/netplay_setup.py`: reproducible host/client Dolphin user folders (`--user`, F-32) with game path, cheats, Background Input, Netplay presets (127.0.0.1:2626, sync saves and codes, no write-back), per-player pad 1 layouts, and COOP-P3 plus the Ch9 card on the host. `install_codes` gained `--user`. Tests 26/26, signatures 73/73.
- The user prefers to drive in-game checks; Claude prepares configs and procedures.
- Next: tester runs NET-01 (one-PC loopback Netplay, TESTING.md), including the first Ch9 battle check (Lethe/Mordecai yellow from the card start). Then two machines.

## 2026-10-27 — Session 1o: sequential campaign goal, Chapter 1 fixed assignment (EXP-15)

- User: from the Chapter 9 card start, Lethe and Mordecai appeared yellow and were controllable in the yellow phase (NET-00 complete).
- **New goal (user):** a sequential two-player campaign from Chapter 1. The first proof is a fixed assignment: Blue = Ike, Titania; Yellow = Boyd, Oscar.
- Static findings:
  - The game's own script command `UnitTransferToForce` (`0x800BCA38`), `SetUnitForce` (`0x8003D60C`), the force list layout, and unit-by-PID `0x80016BDC` (F-34).
  - At chapter end, only force 0 goes to the roster (`0x80016C58` from `0x8002E0D0`; F-35).
  - PIDs: Boyd = `PID_BOLE`, Titania = `PID_TIAMAT` (F-36).
  - The Prologue with COOP-P3 had no yellow phase when force 3 was empty (F-37).
- **EXP-15** (two C2 hooks, the game's own command, PID strings in the cave): in the Chapter 1 player phase, Boyd and Oscar go 0 → 3. At chapter end, before the roster move, they go 3 → 0. Tests 27/27, signatures 85/85.
- `netplay_setup`: the host now also has port 2 (numpad layout), so `--root work/ch1 --enable COOP-P3 --enable EXP-15` gives a one-window, two-controller Chapter 1 test bed.
- Next: the tester runs EXP-15 (TESTING.md). Then replace the hard-coded PIDs with a persistent owner table.
- **EXP-15 v1 run 1 (user): PARTIAL.** The Chapter 1 sequence blue → yellow → red works, and Boyd and Oscar were yellow (slot 3 decoded). But both were **deleted** at the chapter transition: Chapter 2 started with Ike and Rhys only, and the next battle's Base Data showed Ike, Titania, Shinon and Gatrie.
- The proc script and the chapter-sequence step show the hand-back at `0x80016C58` ran too late (F-38). **v2** hands back at the entry of both chapter-end steps (`0x8002E0D0`, `0x80005F04`). Tests 27/27, signatures 92/92. Installed in `work/ch1/host`; retest steps are in TESTING.md.

## 2026-10-27 — Session 1k: COOP-P1 verified, EXP gate found

- **EXP-08 A PASS**: from slot 6 (`control[3]=2`), the yellow phase came up human-controlled with COOP-P1 only (slot 8 decoded).
- **EXP-09**: the tester recorded `work/movies/ch9_coop_p1.dtm` and lost the run deliberately; the warp-fixture army is too weak to win. Recommendation: accept it as the Phase 1 proof and finish Ch9 in Phase 4 with a real army.
- **Requirement (user):** player-controlled partners must gain EXP. Vanilla `CanGainExp` (`0x8003D13C`) only allows force 0/5 (F-21). **EXP-10** (C2 hook at `0x8003D180`) lets force 3 gain EXP while `control[3]==1`. Static checks 39/39, tests pass. Not yet run.
- Unit layout: level `+0x19A`, EXP `+0x19B`, laguz gauge `+0x19C` (F-22).
- Next: EXP-10 runtime test (slots 4/5 before and after a partner battle); EXP-08 B (Prologue) when convenient.

## 2026-10-27 — Session 1j: COOP-P1 package

- **EXP-08**: C2 hook on phase advance (`0x8014D3B4`) sets `control[3]` = 1 if force 3 has units, otherwise 2. It replaces EXP-01's per-frame AR write.
- **COOP-P1** = EXP-08 + EXP-06 + EXP-07, a single Gecko code to enable. Tests: disassembly of every cave, package equality, 35/35 signatures, 17/17 tests.
- Next: EXP-08 A (recovery from slot 6) and B (Prologue unchanged), then EXP-09 (full Ch9 with .dtm).

## 2026-10-27 — Session 1i: EXP-07 PASS (A and B)

- Update: the tester confirmed EXP-07 A(b–d) and B (vanilla yellow AI unaffected with EXP-07 alone). F-18 is closed.
- Remaining Phase 1 items: a full Chapter 9 run with a .dtm, and packaging into one code set.

- With EXP-01 + EXP-06 + EXP-07, ending the yellow phase with Mordecai unacted left him in place, and the Enemy Phase began. Slot 8 verifies it by decoding; regression test added.
- Note: Dolphin rewrote `User/GameSettings/GFEE01.ini` with duplicated `[Gecko_Enabled]` entries (seen after the tester opened Properties). It's harmless, and `install_codes` regenerates the file anyway.
- Remaining Phase 1 checks: EXP-07 A(b–d), B (vanilla yellow AI still works with EXP-07 alone), a full-chapter run with a .dtm, and packaging.

## 2026-10-27 — Session 1h: F-18 traced, EXP-07 drafted

- Decision (user): leftover yellow units should **wait**, not be handed to the AI.
- Cause found statically: the phase-end handler `0x8002E670` always launches `E_CP_PhaseMain` for phase 3, while phases 1/2 require control==2 (F-18, F-19).
- **EXP-07**: 8-instruction Gecko hook at `0x8002E6DC` that mirrors the phase 1/2 gate for phase 3. Disassembly test plus 32/32 signatures. Not yet run.
- Next: run EXP-07 A (human yellow) and B (vanilla control) per TESTING.md.

## 2026-10-27 — Session 1g: EXP-06 PASS (Phase 1 core achieved)

- With EXP-01 + EXP-06, the yellow army is human-controlled in its own phase and blue in its own, with no cross-control, verified over turns 1–2 of Chapter 9.
- The tester's save landed in slot 6 (fixture slot). It's backed up as `work/saves/GFEE01.s06_exp06_turn2` (Ch9, turn 2, yellow phase), and the fixture is restored to slot 6.
- New: proc names in the binary (`E_BMapMain`, `E_BMapPlph`, `E_PhaseChange`, …).
- Open: F-18, the AI moves yellow units the player didn't act with after End. Its cause isn't located yet.
- Next (pick one): resolve F-18, or start **Phase 2** (local controller ownership: pad 2 drives the yellow phase).

## 2026-10-27 — Session 1f: EXP-01 partial pass, ownership fix drafted

- **EXP-01:** the yellow army was human-controlled in its own phase. Lethe transformed, both units moved and acted, and the yellow units were locked in the Player Phase. **Bug: blue units were also movable in the yellow phase.**
- Root cause: `GetUnitSelectState` has no force-0 ownership check (F-15). The "acted" bits of forces 0–3 are cleared at every phase start (F-16).
- **EXP-06** (Gecko hook, 9 instructions at `0x8002858C`): units are selectable only when `force == phase`. Statically validated (disassembly test, 27 signatures). Not yet run.
- Slots 7/8 backed up as `work/saves/GFEE01.s07_exp01_banner` / `…s08_exp01_bluemoved`. Fixture slot 6 unchanged (SHA-1 re-checked).
- Next: run EXP-06 from slot 7. If it passes, Phase 1 is complete on one controller → Phase 2 (per-phase controller port).

## 2026-10-27 — Session 1e: EXP-05 PASS, Chapter 9 fixture

- The conditional AR redirect (`08330718 00000002` / `00330718 0000000A`) loaded Chapter 9 straight after the tutorial. Slot 6 has been verified by decoding: chapter id 10, Lethe/Mordecai in force 3, control `01 02 02 02`. Backup and SHA-1 are in TESTING.md, and a regression test was added.
- **Next: EXP-01** on slot 6 (yellow army human-controlled).

## 2026-10-27 — Session 1d: EXP-04 PASS

- **First runtime demonstration of human control of a non-blue army.** With only `0033071D 00000001` (control[1] = human), the user controlled Boyd, and then Greil, during the tutorial's Enemy Phases. The tutorial completed and Chapter 1 loaded normally. Evidence: user report and slot 4 (phase 1, control `01 01 02 02`), with a regression test added.
- F-05 upgraded to VERIFIED-RUNTIME for force 1.
- EXP-05 (Chapter 9 redirect) has **not** been run; it was not enabled in this session.
- Next: EXP-05 → slot 6 Chapter 9 fixture → EXP-01 (yellow). Also confirm EXP-04 (c) greying out and (e) blue can't move during the red phase.

## 2026-10-27 — Session 1c: EXP-02/EXP-03 results, new plan

### Results
- **EXP-02 INCONCLUSIVE:** the Prologue has no green phase to test. Slot 5 confirms the code was active (control[2]=1) when turn 2 began.
- **EXP-03 FAILED:** patching the chapter id mid-Prologue didn't change the next chapter, because the next chapter comes from `SetChapter` calls. Slot 7 (Chapter 2) verified the **chapter id ↔ bmap mapping** (id N → `bmap0N`; Chapter 9 = id 10).

### New static findings
Phase order 0→3→1→2 (F-09), turn-loop proc script (F-10), SetChapter and its callers (F-12), control bytes saved in save data (F-13), script phase/turn accessors (F-14). Signatures: 23/23.

### Plan (smallest demonstrations first)
1. **EXP-04:** human-controlled red army in the Prologue (`0033071D 00000001`, slot 2). Shows non-blue human control with no new fixture needed.
2. **EXP-05:** conditional AR redirect of chapter id 2 → 10 after clearing the Prologue → Chapter 9 fixture in slot 6.
3. **EXP-01** on that fixture.

### Not doing yet
Controller routing / Netplay (per user priority).

## 2026-10-27 — Session 1b: save inventory, runtime confirmation, test fixtures

### Done
- Inventoried user saves: one state `GFEE01.s01` (**Prologue**, turn 1; not Chapter 9) and one GCI memory-card file (encoded, likely a new-game save). Both backed up with SHA-1 to `work/saves/2026-10-27_baseline/`. Originals untouched (hash re-checked).
- New tools: `tools/fe9/savestate.py` (Dolphin v192 state reader/writer, LZ4), `tools/inspect_state.py` (decode RAM: chapter/phase/turn/control/forces/units), `tools/patch_state.py` (write a *new* state with patched bytes; refuses to overwrite).
- **EXP-00 Part A passed** by decoding the state: the force model and control bytes are confirmed at runtime (RESEARCH.md §4 "Runtime confirmation").
- Created working slots: s02 = baseline copy, s03 = Prologue with chapter id 9 (EXP-03 warp fixture).
- Wrote exact procedures for EXP-00B, EXP-02 (green control on the Prologue, testable now), EXP-03 (warp to Ch9) and EXP-01.

### Blockers (need the user)
- Run EXP-02 and EXP-03 in Dolphin (procedures in TESTING.md). Save states at key moments to slots 4–7.

### Next steps
1. EXP-02 result → confirms or refutes the control-mode mechanism without needing Chapter 9.
2. EXP-03 result → Chapter 9 fixture (slot 6) → EXP-01.
3. If EXP-03 fails: find the chapter-load routine statically (callers of `0x8014D2B0`).

## 2026-10-26 — Session 1: Phase 0 setup and static research

### Done
- Verified Dolphin (portable, `Dolphin 2609a` string in binary) and the image: **GFEE01 rev 0, NTSC-U**.
  Recorded image and `main.dol` hashes (RESEARCH.md §0).
- Repository tooling (all read-only on game data):
  - `tools/fe9/disc.py`: CISO/ISO reader, FST and DOL extraction (cross-checked byte-for-byte against DolphinTool).
  - `tools/fe9/lz77.py`, `tools/fe9/pack.py`, `tools/fe9/dispos.py`: FE9 data formats.
  - `tools/fe9/ppc.py`: capstone-based DOL disassembly helpers.
  - CLIs: `verify_game`, `dump_dispos`, `check_signatures`, `install_codes`. Tests: `tests/test_tools.py`.
- Reviewed community resources (RESEARCH.md §1). Decoded Ralf's PAL unit-control codes and located their US equivalents.
- **Key finding:** FE9 has a per-force control-mode byte (`0x8033071C + force`, 1 = human, 2 = CPU). Its selection code already supports human control of forces 2/3 during their own phase (RESEARCH.md F-05).
- Chapter 9 data: Lethe and Mordecai have force index 3 in every difficulty variant (F-02).
- Drafted EXP-00 (baseline) and EXP-01 (one-byte partner-control experiment).

### Failed / dead ends
- Serenes Forest thread (and dolphin-emu.org netplay guide) returned HTTP 403 to automated fetch. Not yet read.
- Redump hash comparison is impossible from a CISO (padding not preserved).
- `DolphinTool convert` to ISO stalled without output; stopped. Not needed, since `tools/fe9/disc.py` reads CISO directly.

### Blockers (need the user)
1. **A Chapter 9 save** (memory card save or Dolphin save state at Ch9 Player Phase, turn 1). Without one, EXP-00 and EXP-01 can't run.
2. Someone to run EXP-00/EXP-01 in Dolphin and report the watch values, with screenshots at the Partner Phase.
3. Optional: paste the relevant posts of the Serenes Forest thread, since automated fetch is blocked.

### Next steps
1. Run EXP-00 then EXP-01 (TESTING.md).
2. Depending on the result: trace proc `0x80284AC8` and the End-turn menu for force-0 assumptions.
3. Start Phase 2 research: locate the US pad-read buffer.
- **EXP-15 v2 run 2 (user): PARTIAL.** The suspend/resume shortcut works, but Boyd and Oscar were lost again. RAM shows the v2 hooks active. A state from the ending conversation shows the drop already happened at the seize, through the script command `AllUnitEscape` (`0x800BA784`), which escapes only the force 0 list into the roster and runs the escape worker on forces 1–3 too (F-39).
- **v3** adds a hand-back at `AllUnitEscape`'s entry (4 blocks). Tests 27/27, signatures 97/97. Installed. The Ch1 turn 1 state was recovered from `lastState.sav` into the test bed's slot 8 (backup `work/saves/GFEE01.ch1_turn1_exp15`).
- **DBG-01** test aid (user request: speed through the tests): a per-frame C0 routine holds every red unit's HP at 1. It is enabled only in the `work/ch1/host` test bed, and a test keeps test aids out of the COOP packages. Tests 28/28.
- **EXP-15 v3 PASSED (user, two runs).** Run A skipped Boyd and Oscar (0 EXP) but kept them. In run B, where they fought in the yellow phase, slot 6 (roster at the ending conversation) shows Oscar lv 3 → 4 with 35 EXP and Boyd with 47 EXP. Chapter 2 turn 1 (slot 7) has Ike, Oscar, Boyd and Rhys blue with identical values, and Titania off-map in force 7 as in vanilla. **Chapter-level success criterion met** for the fixed assignment.
- Still unchecked: defeat (Ike falls → Game Over), a yellow-assigned unit dying, the single-unit `UnitEscape` command, and battle save/load during a two-army chapter.
- Next: a persistent owner table (per PID, applied at every chapter start, returned at every chapter-end path) to replace EXP-15's hard-coded PIDs and Chapter 1 check. Then NET-01 (Netplay) with the campaign start.

## 2026-10-27 — Session 1p: reusable army ownership (EXP-16)

- Goal (user): persistent two-player ownership for the whole campaign; first milestone is Chapters 1–3.
- **EXP-16** replaces EXP-15's Chapter 1-only pair:
  - `tools/owner_code.py` holds `OWNERS` (PID → player; now Oscar and Boyd → Player 2) and writes the code into `codes/GFEE01.ini`.
  - Five blocks: apply at every player-phase start (any chapter); return at `AllUnitEscape`, the transition and the chapter sequence; single-unit return at `UnitEscape` (F-40, new).
  - Everyone not in the table, including new recruits, is Player 1. Ike can't be assigned to Player 2 (the generator refuses).
- Ownership storage evaluated (RESEARCH): the table is embedded in the code (Netplay-synced, no save writes) for now. A save field or card record is needed later for an in-game assignment screen.
- Tests 29/29 (`test_exp16_ownership_code` checks the ini against the generator), signatures 100/100. Installed in `work/ch1/host` with COOP-P3 and DBG-01. The test card is backed up (`work/saves/ch1_card_after_exp15.gci`).
- An edge-case matrix (13 cases, verified vs untested) is now in TESTING.md.
- Next: the tester plays Chapter 2 → Chapter 3 → Chapter 4 start from the "Ch. 2" card file.
- **EXP-16 run 1 (user): PASS through the Chapter 4 start.**
  - Ch2 had a yellow army automatically: Oscar and Boyd yellow at turn 1, Boyd lv 2 → 4, Rhys gained heal EXP, and Titania arrived blue.
  - Ch3 and Ch4 line-ups were forced by the story (`UnitForcedSally` flag `0x10000`, F-41). Oscar and Boyd were benched (force 7) with progression intact, so there was no yellow army there.
  - Recruits Shinon, Gatrie and Soren joined blue. Everyone appears exactly once in every Base Data screen.
  - Marcia leaving in Ch3 matches the original data: her only dispos entry is Ch10.
- Open from this run:
  - **Auto-end for the yellow phase** (user request). The vanilla check is not found yet; the phase-start scan is already generic, so it is elsewhere.
  - A test assignment that covers forced line-ups, so Ch3–4 get a yellow army (for example Shinon/Gatrie → Player 2).
  - Prep-screen locking compared against a codes-off run.
- Ownership table extended (user): **Shinon and Gatrie → Player 2**, so the forced Ch3/Ch4 line-ups include a yellow army. Regenerated with `tools.owner_code --write`; tests 29/29, signatures 100/100. Installed in the test bed; the card is backed up. Run 2 procedure is in TESTING.md (Ch3 → Ch5 start).
- **EXP-16 run 2 (user): PASS Ch3 → Ch5 start.** Shinon and Gatrie were yellow in Ch3 and Ch4, and all four Player 2 characters were yellow in Ch5. EXP carried across every transition (Shinon 0 → 21 → 44, Gatrie 0 → 41 → 85). **The Chapters 1–3 milestone is met.**
- Findings: the in-battle Base Data list shows force 0 only (UI gap). There is no auto-end in the yellow phase. Static search for the auto-end check (human-phase proc steps, acted-bit tests, `GetUnitSelectState` callers) found none of the routines it would sit in; next is locating the option byte with a two-state memory diff.
- **Auto-end found (F-42)** from the user's two option states: Auto End = `state+0x9E` bit 0x20. The after-action step `0x80028C90` ends the phase when the next-unit search `0x800AA5F0` finds nobody, but that search was hard-wired to force 0 (and also drives Next Unit, F-28). **EXP-17** (2 tiny C2 blocks) uses force 3 in phase 3. Tests 30/30, signatures 108/108. Installed in the test bed; procedure is in TESTING.md.
- **EXP-17 PASSED (user, Ch5):** Next Unit cycles yellow units, the yellow phase auto-ends after the last yellow unit acts, and with Auto End off nothing ends automatically. **COOP-P4** = COOP-P3 + EXP-17 is packaged (`test_coop_p4_package`). Install COOP-P4 + EXP-16. Tests 31/31, signatures 108/108.

## 2026-10-27 — Session 1q: playable-roster classification (EXP-18), edge-case session

- **Why yellow characters were missing from Base Data (F-43):** the map menu's Unit command lists the force 0 list only (`0x8012C9FC(0)` → builder `0x8012DFA8`). This is part of a broader pattern: the game's "player army" is forces 0 and 5 (mask query 4).
- **Central criterion:** the game's own flag `0x400` (set at map start on every force 0 unit) marks deployed player units and survives the EXP-16 move. Native partners never have it.
- **EXP-18:** both list walks continue from force 0 into force 3 units with `0x400`, only for the force 0 list (2 C2 blocks). Tests 32/32, signatures 114/114.
- Installed: COOP-P4 + EXP-16 + EXP-18 + DBG-01 in the test bed. One tester session is written (TESTING.md): Base Data, suspend/resume mid yellow phase (edges 6/7; there is no Battle Save in this game), and a yellow death through to the next chapter (edge 1), with optional Game Over.
- Next, depending on results: the death handling for force 3; the other query-4 users (save path, item check) once a runtime failure shows they matter; then the first flexible prep screen and NET-01.
- **EXP-18 session (user): PASS with findings.** Base Data now lists all 8 units, but yellow EXP showed "--" at turn 1 because `control[3]` = 2 until the first phase change; EXP-16's apply step now also sets `control[3]` = 1 (F-44). Suspend/resume mid yellow phase works. A yellow death frees the unit slot (Boyd gone for good, no revival or duplicate). Ch6's 5-unit prep list is the original story (no Shinon or Gatrie in `bmap07`). Next: compare with a vanilla blue death, and confirm the EXP display fix.
- **Session 1q, continued (Claude, autonomous, computer use):**
  - The **EXP display fix** is verified: Base Data showed Oscar with real EXP at turn 1.
  - **Yellow death record:** the death routine `0x8003E8DC` keeps dead force 0 units in force 6 with flag `0x8000` and the chapter id, but frees other forces (F-45). **EXP-19** treats deployed Player 2 units (force 3 + `0x400`) as force 0 there. **Runtime-verified:** Oscar died in Ch6 and got exactly that record.
  - New test aid: DBG-02 (Player 2 units at 1 HP).
  - Prep screens operate on the vanilla roster before ownership applies (F-46). Ch3, Ch4 and Ch6 force every candidate.
  - Tests 34/34, signatures 122/122.
- **NET-01 PASSED (first real Netplay session; Claude, one PC, two instances).**
  - Host COOP-P5 + EXP-16 + DBG-01. The codes and the host's Ch9 card were synced to the client; P1 → GC1 and P2 → GC2 were mapped automatically.
  - Two turns of Ch9 ran in lockstep: each army answered only to its own player (prompts, Next Unit, moves, auto-end), and the enemy phase and conversations were identical.
  - States saved in both instances decode identically (F-47).
  - Next: combat and a full chapter under Netplay, then the two-machine procedure.
- **Chapter audit (Priority 5):** `tools/chapter_audit.py` reads every chapter's dispos data and event script (command names and PIDs are plain strings in `Scripts/CNN.cmb`). It writes `docs/CHAPTER_AUDIT.md`, which marks each chapter as runtime verified, statically inspected only, or needing a targeted check (escape objective, transfers, native partners, scripted phases). The "…ByPID" commands are script helpers over the native ones, so the existing hooks apply. Native partner `PID_MELTY` (force 3) appears in Ch18–30.
- Next: decode the `.cmb` bytecode, so the audit can say which PIDs each `UnitTransferToForce` call moves and to which force; play Ch6's escape objective; flexible deployment in a later chapter; NET-02.
- **Script bytecode decoded enough for transfers (F-48):** the audit now lists every `UnitTransferToForce[ByPID]` call per chapter as PID → force, with Player-2 characters in bold. This confirms from the script itself the benching seen at runtime (Ch3/Ch4/Ch6). It also flags what to test next: **Ch18 Shinon turning enemy (→ 1)** and **Ch10's temporary story partners (Kieran, Nephenee, Brom → 3)**.

## 2026-10-27 — Session 1r: shareable Netplay client package (NET-02 prep)

- **`tools/netplay_package.py`** builds `dist/FE9-Coop-Client-<fingerprint>.zip` (~12 KB), which the friend unzips next to their own Dolphin 2609a and game copy:
  - `README.txt`, `Start-FE9-Coop.bat` / `Check-Setup.bat` → `tools/client.ps1`
  - a private `User/` folder: Traversal Server preset, cheats on, port 1 keyboard, COOP-P5 + EXP-16
  - `MANIFEST.txt`
  - Sources are in `netplay/client/`. The build is reproducible, and `--verify` enforces the exact contents with no game or save data.
- **Code fingerprint** (SHA-256 of the enabled codes, 16 hex digits): computed identically by Python and the PowerShell launcher (tested). `--fingerprint <user dir>` checks the host folder. Current value: `7031af10d740f4ed`.
- `netplay_setup` gains `--host-only --traversal --card`. The NET-02 host is `work/netplay_net/host`, with the card `work/saves/net02_card/`. The NET-01 defaults and folders are unchanged (tested).
- **One-PC runtime check (Claude):**
  - The packaged client, started by its own launcher, connected over Direct.
  - Game digest match, saves and codes synced, P1 → GC1 and P2 → GC2.
  - Ch3 yellow phase controlled only by the client.
  - Identical turn 2 states.
  - Disconnect stops both games.
  - The traversal Room ID was issued, but a same-PC traversal join failed (F-49), so the internet path still needs the real two-PC run.
- Tests 41/41, signatures 122/122.
- Next: the user and a friend run NET-02 (TESTING.md) and report the results; then Ch6 escape, Ch18/Ch10 checks, flexible deployment.
- **Package net02-2 (user request):** the ZIP no longer includes the launcher (`Start-FE9-Coop.bat`, `Check-Setup.bat`, `client.ps1`, now removed from the repo). The friend is assumed to have Dolphin 2609a. The README gives manual steps instead:
  - a Dolphin shortcut with `--user <package>\User`
  - Config → Paths for the game
  - `Get-FileHash` on the code file against the hash in the README/manifest
  `verify()` now also rejects `.exe/.dll/.bat/.cmd/.ps1/.vbs/.lnk`. The ZIP is 7.3 KB, the fingerprint is unchanged (`7031af10d740f4ed`), and tests are 40/40.
- **First two-computer Netplay session (user + friend, net02-1 ZIP):** the Traversal room-code join works between two networks. Mapping, versions and sync are correct, and play reached Ch3 turn 3 with no desync. Buffer 5 held both games at ~40 FPS; **Buffer 26 gave 59.9 FPS/VPS** (F-50). The README troubleshooting and the NET-02 procedure now say to raise the buffer. Pending: combat/EXP, the state comparison, disconnect.
- Buffer tuning (user): **18 holds a stable 58–60 FPS** at 23–33 ms ping; it is now the recommended value in the NET-02 procedure and the client README.

## 2026-10-27 — Session 1s: yellow-phase cursor cue (EXP-20, COOP-P6)

- User request: when the yellow phase starts, the cursor should move to a yellow unit as a turn cue.
- Static finding (F-51): the phase-start step `0x8002E444` moves the cursor to the lord only in phase 0. Next Unit uses the same cursor move (`0x8014CBD8`) after `0x800AA5F0`.
- **EXP-20**: one C2 hook at `0x8002E464`. In phase 3 with `control[3] == 1` (and the same option bit clear), it moves the cursor to `0x800AA5F0(0)`, the first yellow unit that can act (EXP-17). Phase 0 is unchanged. **COOP-P6** = COOP-P5 + EXP-20.
- Tests 42/42, signatures 133/133. Installed in `work/ch1/host` (COOP-P6 + EXP-16 + DBG-01) for the tester's one-PC check (TESTING.md EXP-20).
- The Netplay host and the friend ZIP stay on COOP-P5 + EXP-16 until EXP-20 passes. After that: move the package to COOP-P6 and rebuild the ZIP (the fingerprint changes).
- **EXP-20 PASSED** (user, one PC). At the start of the yellow phase the cursor swaps to a yellow unit; slot 3 has the cursor on Shinon's tile (F-51).
- **NET-02 PASSED on two computers over the internet** (user + friend, COOP-P5 + EXP-16). Ch3 reached turn 6 with yellow combat and EXP, and the turn 4 and turn 6 states are identical on both PCs, with no desync (TESTING.md NET-02).
- The Netplay package and host moved to **COOP-P6 + EXP-16**: package net02-3, fingerprint `8609ae9f49fd879f`, ZIP `dist/FE9-Coop-Client-8609ae9f49fd879f.zip`. The friend needs the new ZIP for the fingerprint/hash check, though the synced host codes are what actually run. The README's Gecko-code check now names the enabled codes from the build.

