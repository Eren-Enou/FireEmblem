# Testing

## Automated (no emulator needed)

```bash
.venv/Scripts/python -m tools.verify_game          # identity + hashes; exit 1 on mismatch
.venv/Scripts/python -m tools.check_signatures     # every static claim in RESEARCH.md [S]
.venv/Scripts/python -m unittest -v tests.test_tools
```

| Date | Test | Result |
|---|---|---|
| 2026-10-26 | `verify_game` | OK: GFEE01 rev 0, main.dol SHA-1 `9d00d7d4…8851` |
| 2026-10-26 | `check_signatures` | 17/17 match |
| 2026-10-26 | `unittest tests.test_tools` | 7/7 pass (LZ77 round-trip, header, DOL hash, signatures, Ch9 force bytes) |

## Manual test environment (Dolphin)

1. Launch `Dolphin-x64/Dolphin.exe` once so the portable `Dolphin-x64/User/` folder is created.
2. Config → General → enable **Enable Cheats**. For memory viewing: View → enable **Memory** and **Watch** (debugging UI: Options → Configuration → Interface → Enable Debugging UI).
3. Install codes (nothing is enabled unless named):
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable EXP-01
   ```
   This writes `Dolphin-x64/User/GameSettings/GFEE01.ini`. Check it under Properties → AR Codes.
4. **Never** overwrite the original `.ciso`. Use save states (F1–F8 = save slot, Shift+F1.. = load in Dolphin's defaults) and keep a backup copy of the memory card / GCI folder before testing.

### Watch addresses (add in the Watch panel)

| Address | Size | Meaning (RESEARCH.md) | Expected in Ch9 vanilla |
|---|---|---|---|
| `80330719` | u8 | current phase (force id) | 0 player, 1 enemy, 3 partner |
| `8033071A` | u16 | turn | 1, 2, … |
| `8033071C`..`8033071F` | u8 ×4 | control mode per force | `01 02 02 02` |
| `802CA26C` / `802CA278` / `802CA284` / `802CA290` | u8 | force id byte of forces 0–3 | 0 / 1 / 2 / 3 |

---

## EXP-00 — Baseline observation (do first, no codes)

**Goal:** confirm the static model at runtime before changing anything.
1. Load a save at the start of Chapter 9 (Gallia), with no cheats enabled.
2. Add the watches above. Play one full turn: Player Phase → Enemy Phase → Partner (yellow) Phase.
3. Record the value of `80330719` during each phase banner, and the `8033071C..F` bytes.

**Pass:** phase goes 0 → 1 → 3 (or 0 → 1 → 2 → 3 if a green phase exists), and control bytes = `01 02 02 02`.
**Fail:** different values, which means the state-block hypothesis F-04/F-05 is wrong. Report the values and stop.

| Date | Tester | Result | Notes |
|---|---|---|---|
| — | — | NOT RUN | needs a Chapter 9 save |

## EXP-01 — Human-controlled partner phase (Phase 1 core experiment)

**Change:** AR `0033071F 00000001`. Each frame this sets force 3's control mode from 2 (CPU) to 1 (human).
**Why:** F-05. The engine's own selection code allows force-3 units to be selected when `phase==3 && control[3]==1`. The phase loop starts the human-input process when `control[phase]==1`.

Procedure:
1. From the EXP-00 save state at Ch9 Player Phase, turn 1, enable EXP-01 (`install_codes --enable EXP-01`, restart the game or toggle the code).
2. Play Player Phase normally: move Ike's units, then **End** turn. Note whether Lethe or Mordecai can be selected during Player Phase (expected: **no**).
3. Let Enemy Phase run (CPU as usual).
4. At the start of the Partner Phase, observe and record:
   a. Does the game wait for input with a cursor (instead of the AI moving)?
   b. Can you select Lethe → move → choose an action (Attack/Wait) → confirm?
   c. Does the unit gray out after acting?
   d. After both partners act (or via the map menu → End), does the phase end and turn 2 start?
5. Take a save state before step 4 so each sub-step can be retried.

**Success (Phase 1 milestone):** a, b, c, d all yes, and Ike's army behaves normally in Player Phase.
**Partial:** the cursor appears but some step fails, e.g. no action menu, unable to end the phase, or wrong banner. Record exactly where. This is still progress: it tells us which routine hard-codes force 0.
**Failure:** the AI still moves the partners, or the game softlocks or crashes at the phase start. Record the last visible screen and `80330719` / `8033071F`. Next step: inspect proc `0x80284AC8` and `0x8002E6B0..0x8002E718` in the debugger.

| Date | Tester | Result | Notes |
|---|---|---|---|
| — | — | NOT RUN | |

## EXP-02 — Green force variant (only if useful)

Same as EXP-01 with `0033071E 00000001` (force 2), on a map where green units take their own phase.
