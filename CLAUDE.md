# FE9 Two-Army Co-op — Project Guide for Claude Code

## Goal
An online two-player co-op mod for *Fire Emblem: Path of Radiance* (GameCube, FE9) on Dolphin.
- Player 1 controls Ike's **Blue** army (force 0).
- Player 2 controls the **Yellow** partner army (force 3).
- The CPU controls **Red** enemies (force 1). Green "other" units are force 2.

The original campaign, mechanics and story stay recognisable. Netplay comes from Dolphin's lock-step input sync.

## Current milestone
**Phase 1 complete on one controller (2026-10-27): install `python -m tools.install_codes --enable COOP-P2`.** COOP-P2 = COOP-P1 (EXP-08 phase-change control hook + EXP-06 ownership + EXP-07 leftover units wait) + EXP-10..13 (partner EXP: CanGainExp, GetExp, battle write-back, level-up/result screen unit pickers; F-21, F-23, F-24, F-26). Runtime-verified: yellow human control without cross-control, kill and counter EXP, accumulation, level-up, blue EXP unchanged, and vanilla unchanged with codes off. Open: stat-gain panel, Direct command, battle save/load round trip. Test new codes from slot 6, because states saved with codes restore the old code list (F-25). **Now: Phase 2** (controller port 2 drives the yellow phase).

History: **Phase 1.** **EXP-04 PASSED**: the red army was human-controlled in its own phase via `control[1]=1`, which proves the engine's control-mode mechanism. EXP-02 was inconclusive (no green phase in the Prologue) and EXP-03 failed (a mid-battle chapter patch is ignored). **EXP-05 PASSED**: the Chapter 9 fixture is in slot 6 (backup `work/saves/GFEE01.s06_ch9_fixture`). **EXP-01 PARTIAL PASS**: Lethe/Mordecai are human-controlled in the yellow phase, but blue units were also movable then. Next: **EXP-06** (Gecko ownership hook in `GetUnitSelectState`) from slot 7. Gecko hooks are documented instruction-by-instruction in `codes/GFEE01.ini` and validated by a disassembly test. Controller routing/Netplay is deferred until a non-blue army is human-controlled. See `docs/TESTING.md`.

## Saves and states
- User originals (never write): `Dolphin-x64/User/StateSaves/GFEE01.s01`, `Dolphin-x64/User/GC/USA/Card A/*.gci`. Backups with SHA-1 are in `work/saves/` (git-ignored).
- Create new states only with `tools/patch_state.py` (refuses to overwrite), in slots 2+.
- Decode any state with `python -m tools.inspect_state <file>`. Ask the tester to save a state at key moments instead of describing memory by hand.

## Architecture decisions (so far)
1. **Reuse FE9's own per-force control mode** (`0x8033071C + force`: 1 = human, 2 = CPU) rather than writing new selection/menu logic. Evidence: docs/RESEARCH.md F-05.
2. **Deliver changes as Dolphin AR/Gecko codes first** (`codes/GFEE01.ini`). The host syncs them in Netplay. Move to a patched DOL only if codes become unwieldy.
3. **Controller ownership (Phase 2)** = patch the game's pad read to use port 2 during the yellow phase. Dolphin Netplay maps P2 → port 2. No Dolphin fork unless evidence requires one.
4. Python for tooling. PowerPC assembly for in-game patches.

## Local development environment
- Emulator: `./Dolphin-x64/Dolphin.exe` (portable build; `portable.txt` present → user data in `./Dolphin-x64/User/`, created on first launch). `./Dolphin-x64/DolphinTool.exe` for header/verify/extract.
- Game: `./Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso`: **GFEE01 rev 0 NTSC-U**, main.dol SHA-1 `9d00d7d407750b82cb1cfccc56f8aa8a89cc8851`.
- `Dolphin-x64/` is git-ignored but available for local inspection and testing.
- Python venv: `.venv` (`python -m venv .venv && .venv/Scripts/python -m pip install -r requirements.txt`).

## Constraints (hard rules)
- Treat the original `.ciso` and the user's saves as **read-only**. Experiment on copies or save states.
- Never commit game images, extracted files (`*.dol`, `*.cmp`, …), saves or copyrighted assets. Commit only original tools, docs and patch/code files.
- Don't invent offsets or behaviour. Every address goes in docs/RESEARCH.md with evidence and a confidence label. Static claims get a pinned signature in `tools/check_signatures.py`.
- Nothing is called "working" without a repeatable test in docs/TESTING.md.
- Extracted game files for analysis go to a scratch directory outside the repo (or the ignored `/work/`).

## Conventions
- Addresses are written as full 32-bit virtual addresses (`0x8033071F`) and refer to GFEE01 rev 0 unless labelled PAL/JP.
- Experiment ids `EXP-NN` are shared across codes/GFEE01.ini, TESTING.md and PROGRESS.md.
- Run before committing: `.venv/Scripts/python -m unittest tests.test_tools` and `python -m tools.check_signatures`.

## Key docs
- `docs/RESEARCH.md`: findings, sources, confidence.
- `docs/ROADMAP.md`: phases and completion criteria.
- `docs/PROGRESS.md`: session log, blockers, next steps.
- `docs/TESTING.md`: procedures and results.
