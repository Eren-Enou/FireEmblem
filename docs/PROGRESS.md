# Progress Log

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
