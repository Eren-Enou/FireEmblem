# Notes for coding agents (Codex and others)

- **Project rules:** `CLAUDE.md`. Treat its hard rules as binding:
  - the game image and user saves are read-only
  - never commit game data, saves or extracted files
  - every address needs evidence in `docs/RESEARCH.md` and a pinned signature
  - nothing is "working" without a passed entry in `docs/TESTING.md`
- **Current state and next steps:** `docs/HANDOFF.md` (drafting/preparations work, paused).
- **Branches:**
  - `main` is the stable Netplay release (COOP-P6 + EXP-16). Merge only verified work.
  - `draft-ownership` holds the paused ownership/prep work.
  - `experiment/alternating-actions` is parked; never merge it.
- **Gecko space:** Dolphin skips codes beyond ≈ 3248 bytes silently (F-59). Use `tools.install_codes`, which checks the budget.
- **Before committing:** `.venv/Scripts/python -m unittest tests.test_tools tests.test_cave_behaviour` and `.venv/Scripts/python -m tools.check_signatures`.
- **Changing a cave:** run `tests/test_cave_behaviour.py`. It executes the generated PowerPC in `tools/fe9/ppc_sim.py`, so behaviour changes show up without Dolphin.
- **Codes:** generated codes come from `tools/owner_code.py` (EXP-16), `tools/draft_code.py` (EXP-21/22/23) and `tools/prep_code.py` (EXP-25/26). Edit the generator, run its `--write`, and don't hand-edit those ini blocks.
