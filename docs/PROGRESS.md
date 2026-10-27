# Progress Log

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
