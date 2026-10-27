# Testing

## Automated (no emulator needed)

```bash
.venv/Scripts/python -m tools.verify_game          # identity + hashes; exit 1 on mismatch
.venv/Scripts/python -m tools.check_signatures     # every static claim in RESEARCH.md [S]
.venv/Scripts/python -m unittest -v tests.test_tools
.venv/Scripts/python -m tools.inspect_state <state.sNN>   # decode RAM from any Dolphin save state
```

| Date | Test | Result |
|---|---|---|
| 2026-10-26 | `verify_game` | OK: GFEE01 rev 0, main.dol SHA-1 `9d00d7d4…8851` |
| 2026-10-26 | `check_signatures` | 17/17 match |
| 2026-10-27 | `unittest tests.test_tools` | 9/9 pass (adds save-state decode/round-trip and runtime-model check) |

---

## Save inventory (2026-10-27)

| File | SHA-1 | Content (decoded with `inspect_state`) |
|---|---|---|
| `Dolphin-x64/User/StateSaves/GFEE01.s01` (**user original; never write**) | `b8a42f4337ad27d137a9baec8ed18f3737db6b38` | Dolphin 2609a, state v192. **Prologue** (chapter id 1), Player Phase, turn 1. Units: Ike (blue), Mist and Greil (green, force 2), Boyd (red). |
| `Dolphin-x64/User/GC/USA/Card A/01-GFEE-FIREEMBLEM8J.gci` (**user original**) | `a5558043cdb95deb5f060c1347a7c625e66206c4` | FE9 save file (GCI folder mode). Data is compressed/encoded and not decoded yet. Written ~1 min before s01, so it's most likely a new-game save. |

**There is no Chapter 9 save yet.** Backups of both originals, with `SHA1SUMS.txt`, are in `work/saves/2026-10-27_baseline/` (git-ignored).

Working slots (copies; safe to overwrite):

| Slot | File | Made by | Purpose |
|---|---|---|---|
| 2 | `GFEE01.s02` | byte copy of s01 | baseline for EXP-00 and EXP-02 |
| 3 | `GFEE01.s03` | `patch_state s01 → set 80330718=09` (copy also in `work/states/`) | EXP-03 (failed; keep for reference) |
| 4, 8 | — | tester | EXP-04 observations |
| 6 | — | tester | Chapter 9 fixture produced by EXP-05 |

Memory card: during the EXP-03 playthrough the **game itself** saved to the card at 00:44 (SHA-1 now `7afef93c…d325`, after Chapter 1 per slot 7). The pre-test card is still in `work/saves/2026-10-27_baseline/`, and the 00:44 version is backed up in `work/saves/2026-10-27_0044_card/`. Our tools never write the card.

States saved by the tester (backed up to `work/saves/`):

| Slot | Saved | Decoded content |
|---|---|---|
| 5 | 2026-10-27 00:11, EXP-02 enabled | Prologue (id 1), **turn 2**, phase 0, control `01 02 01 02` (code applied). Green units untouched at their start squares. |
| 7 | 2026-10-27 00:47, no codes | **Chapter 2** (id 3 = `bmap03`; previous id 2), turn 1, phase 0, control `01 02 02 02`. Ike, Oscar, Boyd, Rhys vs. Ikanau's bandits. |

Rebuild them at any time:
```bash
cp work/saves/2026-10-27_baseline/GFEE01.s01 Dolphin-x64/User/StateSaves/GFEE01.s02
.venv/Scripts/python -m tools.patch_state work/saves/2026-10-27_baseline/GFEE01.s01 work/states/GFEE01_prologue_ch9warp.s03 --set 80330718=09
cp work/states/GFEE01_prologue_ch9warp.s03 Dolphin-x64/User/StateSaves/GFEE01.s03
```

**Rule for testers:** never use *Save State → Slot 1* (Shift+F1). Save your observations to **slot 4–8**. I decode them with `inspect_state`, so a save state at the key moment works as a memory dump.

---

## Common setup (every manual experiment)

1. Close Dolphin.
2. Install exactly the codes for the experiment (this rewrites only `User/GameSettings/GFEE01.ini`):
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable EXP-02
   ```
   Use no `--enable` at all for "no codes".
3. Start Dolphin and check that **Config → General → Enable Cheats** is on. Optionally right-click the game → Properties → AR Codes to see which code is ticked.
4. Boot the game, then load the slot named in the experiment (**Emulation → Load State → Slot N**, default hotkey F*N*). Codes stay active across state loads.
5. Optional watches (Options → Configuration → Interface → *Enable Debugging UI*, then View → Memory / Watch):
   `80330718` chapter id, `80330719` phase, `8033071A` u16 turn, `8033071C..F` control bytes.

---

## EXP-00 — Baseline (runtime confirmation of the static model)

**Part A (snapshot, done by decoding slot 1 on 2026-10-27):**
control = `01 02 02 02`, phase = 0, turn = 1, force table ids 0–7 at `force+8`. Every unit's `+0x190` points at the matching force: Ike → 0, Mist/Greil → 2, Boyd → 1. Unit table decodes as predicted (PID/JID strings, coordinates, HP). → **F-01, F-03, F-04 (phase/turn) and the F-05 initial values are VERIFIED-RUNTIME** (Prologue). Regression test: `SaveStateTests.test_baseline_runtime_matches_static_model`.

**Part B (manual, Prologue, no codes):** load slot 2, end Ike's turn without acting (map menu → End). Save state to **slot 4** as soon as each new phase banner appears: Enemy Phase → slot 4, then the green/"Other" phase if one appears → slot 5. Send me the slots, or just tell me the banner names.
**Pass:** phases are 0 → 1 → 2, with the control bytes unchanged.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | Claude (state decode) | Part A **PASS** | slot 1 snapshot |
| — | — | Part B NOT RUN | |

## EXP-02 — Human-controlled green army on the Prologue (proxy for EXP-01)

Same mechanism as EXP-01, but on force 2. It is testable **now** with the existing save. The code writes control[2] = 1, which takes the same selection-classifier path as force 3 (`0x80028548` vs `0x80028578`).

1. Common setup with `--enable EXP-02`; load **slot 2**.
2. Player Phase: check whether Greil or Mist can be selected. *Expected: no* (classifier requires phase == 2).
3. End Ike's turn. Enemy Phase plays normally.
4. At the green/Other Phase, save to **slot 4** and record:
   a. cursor waits for input (instead of the AI acting)?
   b. Greil can be selected → moved → *Wait* (or attack Boyd if adjacent)?
   c. unit greys out after acting?
   d. the phase ends and turn 2 begins (via map menu → End, or automatically once everyone has acted)?
5. Save to **slot 5** right after any unexpected screen.

**Success:** a–d yes, and Ike plays normally. → The control-mode mechanism works, and EXP-01 only needs a Chapter 9 save.
**Partial:** cursor appears but a step fails. Note which step (this points at a routine hard-coded to force 0).
**Failure:** green units still act by AI, *or* no green phase exists in the Prologue (that makes this map unsuitable; it is not evidence against F-05), *or* a softlock/crash.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **INCONCLUSIVE** | The Prologue never shows a green/Other phase, so no attempt to control Greil was possible. Slot 5 proves the code was active (control[2]=1) when turn 2 began. Phase order is 0→3→1→2 (RESEARCH F-09), so phase 2 was skipped by a rule we haven't decoded yet. That rule doesn't matter for EXP-04/EXP-01, whose phases normally run. |

## EXP-03 — Chapter warp to reach Chapter 9 (test fixture, HYPOTHESIS)

**Idea:** at chapter clear, `0x8002E3A4` computes `next = state[0x10] + 1`. Slot 3 is the Prologue with `state[0x10]` changed from 1 to 9. If F-04's "chapter id" reading is right, clearing the Prologue should load chapter id 10 = **Chapter 9 (Gallia)**. (The JP chapter-select codes use the same numbering: Prologue 0x01, Ch9 0x0A.)

1. Common setup with **no codes**. Load **slot 3**.
2. Win the Prologue normally (defeat Boyd with Ike; Greil/Mist won't interfere).
3. Watch what loads next: intermission/base screens, story, then the map.
4. If Chapter 9's map appears (Gallia, Lethe and Mordecai as yellow units), make a save state at the first Player Phase in **slot 6**. That becomes the Chapter 9 fixture. Back it up: `cp Dolphin-x64/User/StateSaves/GFEE01.s06 work/saves/`.

**Expected side effects:** the army will only contain units recruited so far (Ike, maybe Boyd/Oscar). That's fine for a control test; use save states liberally.
**Failure modes:** Chapter 1 loads instead (state+0x10 is not the next-chapter source); crash or softlock (chapter id is used mid-battle). Either way, report it and we fall back to a real playthrough save, or I find the chapter-load function statically.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **FAILED** | Clearing the Prologue loaded Chapter 1 normally. Explanation: the next chapter is set by `SetChapter` (`0x8014D2B0`, called from script-library code), not by `state[0x10]+1` during battle. Chapter id N ↔ `zmap/bmap0N` is now verified (slot 7 = id 3 = bmap03). Superseded by EXP-05. |

---

## EXP-04 — Human-controlled RED army in the Prologue (smallest non-blue control test) ← **RUN THIS FIRST**

**Why this test:** the enemy phase definitely runs in the Prologue (Boyd attacks). Control mode is generic per force (`0x8033071C + force`). The turn-loop step at `0x8002E738` starts the human-input proc for *any* phase whose control byte is 1. The cursor classifier lets you select a unit when its force equals the current phase. So `control[1] = 1` should hand Boyd to the player during Enemy Phase, using exactly the code path EXP-01 needs for yellow.
**Change:** AR `0033071D 00000001`.

Steps:
1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable EXP-04
   ```
2. Start Dolphin and boot Path of Radiance. **Emulation → Load State → Slot 2** (Prologue, turn 1).
3. Player Phase: move the cursor onto Boyd and press A. *Expected:* his range is shown, but he can't be moved (he's hostile in phase 0). Move Ike somewhere **out of Boyd's reach** (e.g. stay put), choose **Wait**, then open the map menu (B or A on an empty square) → **End**.
4. When the **Enemy Phase** banner appears, immediately **save state to slot 4** (Shift+F4 or Emulation → Save State → Slot 4).
5. Record:
   a. Does a cursor appear and wait for you, instead of Boyd moving on his own?
   b. Can you select Boyd → move him → get an action menu (Attack if adjacent to Ike, otherwise **Wait**)?
   c. Does Boyd grey out after acting?
   d. Does the phase end (automatically, or via map menu → End) and turn 2 begin? Is the Ike-vs-Boyd tutorial still playable afterwards?
   e. During that Enemy Phase, can you select and move **Ike**? (*Expected:* no.)
6. Save state to **slot 8** at any unexpected screen (softlock, odd menu) and note what you pressed.

**Success:** a, b, c and d yes, and e no. → **Human control of a non-blue faction is demonstrated** with the engine's own control mode. EXP-01 then only needs the Chapter 9 fixture.
**Partial:** the cursor appears but a step fails. Slot 4/8 tell me exactly where. That points to the routine that assumes force 0.
**Failure:** Boyd still moves by himself (the code isn't reaching the turn loop), or a softlock/crash right at the banner.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **PASS (a, b, d); c, e not explicitly checked** | Only EXP-04 was enabled. The player controlled the enemy during the Enemy Phase, both for Boyd and in the follow-up tutorial fight against Greil. The tutorial played through to completion, and the game then loaded Chapter 1 normally (expected: EXP-05 was not enabled). Slot 4 (backup `work/saves/GFEE01.s04_exp04`) decodes as Prologue, turn 1, **phase 1**, control `01 01 02 02`, Boyd in force 1. Regression test: `SaveStateTests.test_exp04_enemy_phase_snapshot`. |

**Conclusion:** setting `0x8033071C + force` to 1 makes the game run that force's phase with the human-input process. No new selection, movement or menu code was needed. Still to confirm in a later run: (c) the unit greys out after acting, and (e) blue units can't be moved during the red phase.

## EXP-05 — Load Chapter 9 by redirecting the chapter id (fixture for EXP-01)

**Why:** the transition after the Prologue calls `SetChapter(2)`. The map loaded afterwards follows the chapter id (id N → `bmap0N`, verified). The conditional AR code below rewrites id 2 to id 10 (Chapter 9, `bmap10`) as soon as it appears. It never fires again because the id is then 10.
**Change:** `08330718 00000002` / `00330718 0000000A` ("if chapter id == 2, set it to 10").

Steps:
1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable EXP-05
   ```
2. Boot the game and **Load State → Slot 2** (Prologue).
3. Win the Prologue (defeat Boyd with Ike; it may take a few turns). Watch the following scenes.
4. **If the game offers to save to the memory card, choose No / don't save.** That card file is your original. A backup exists in `work/saves/2026-10-27_baseline/`, but don't rely on it.
5. When a battle map starts, look for Lethe and Mordecai (yellow) and Gallia's forest map. At the first Player Phase, **save state to slot 6**.
6. Close Dolphin and send me slot 6. I'll decode it and confirm chapter id 10, the yellow units and the control bytes before EXP-01.

**Success:** Chapter 9's map loads with Lethe/Mordecai as yellow (force 3) units. Expect only Ike and maybe a few units in your army, and odd story text; that's fine for a control test.
**Failure modes, and what each tells us:**
- Chapter 1 still loads → the map choice doesn't read `state+0x10` at that moment. Next I'd hook the chapter-load path statically (callers `0x800AA0E8`, `0x801D8804`, `0x801F8994`).
- Crash or softlock in a cutscene → note the last screen and save to slot 8. I'd then redirect later (on the map-load call instead of the id).

| Date | Tester | Result | Notes |
|---|---|---|---|
| — | — | NOT RUN | |

## EXP-01 — Human-controlled partner army in Chapter 9 (Phase 1 core experiment)

**Needs:** the Chapter 9 fixture from EXP-05 (slot 6), or any real save at Ch9 Player Phase, turn 1.
**Change:** AR `0033071F 00000001` (control[3] = human) via `--enable EXP-01`.
**Note:** phase order is 0 → **3** → 1 → 2, so the partner phase comes *right after* your Player Phase, before enemies move. Even a lone Ike can just Wait/End and the yellow phase follows immediately.

1. Common setup with `--enable EXP-01`; load the Ch9 fixture. First run `inspect_state` on it and confirm Lethe/Mordecai are listed as `yellow/partner`.
2. Player Phase: move Ike's units, then End. Lethe/Mordecai should *not* be selectable now.
3. Enemy Phase runs as usual.
4. Partner Phase: save to **slot 7**, then record a–d as in EXP-02 (selecting Lethe → move → Attack/Wait → greys out → phase ends → turn 2).

**Success (Phase 1 milestone):** a–d all yes, and Ike's army is unaffected. Repeat once and record a Dolphin input movie (.dtm) for proof.

| Date | Tester | Result | Notes |
|---|---|---|---|
| — | — | NOT RUN | blocked on Ch9 fixture |
