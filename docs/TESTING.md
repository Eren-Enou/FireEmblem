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
| 6 | `GFEE01.s06` | tester (EXP-05) | **Chapter 9 fixture.** Restore with `cp work/saves/GFEE01.s06_ch9_fixture Dolphin-x64/User/StateSaves/GFEE01.s06` |
| 7 | `GFEE01.s07` | tester (EXP-01) | Chapter 9, turn 1, yellow phase banner (start point for yellow-phase tests) |
| 9 | — | tester | free. If saving to slot 9 fails, use Emulation → Save State → Save State to Selected Slot after picking slot 9, or use slot 8. |

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
| 2026-10-27 | user | **PASS** | After the tutorial, Chapter 9's map loaded directly. Slot 6 (backup `work/saves/GFEE01.s06_ch9_fixture`, SHA-1 `d8430d71353537c78628ae9029118c48b70525a0`) decodes as chapter id 10, turn 1, phase 0, control `01 02 02 02`. **Lethe (25,18) and Mordecai (24,18) are in force 3 (yellow)**. Blue: Ike, Mist, Rolf. Red: 17 Daein units and 1 bandit. The memory card was not written. Regression test: `SaveStateTests.test_ch9_fixture`. |

**Chapter 9 fixture:** slot 6. Treat it as read-only from now on; save experiment states to other slots. To restore it: `cp work/saves/GFEE01.s06_ch9_fixture Dolphin-x64/User/StateSaves/GFEE01.s06`.

## EXP-01 — Human-controlled partner army in Chapter 9 (Phase 1 core experiment)

**Needs:** the Chapter 9 fixture from EXP-05 (slot 6), or any real save at Ch9 Player Phase, turn 1.
**Change:** AR `0033071F 00000001` (control[3] = human) via `--enable EXP-01`.
**Note:** phase order is 0 → **3** → 1 → 2, so the partner phase comes *right after* your Player Phase, before enemies move. Even a lone Ike can just Wait/End and the yellow phase follows immediately.

1. Close Dolphin. Run `.venv/Scripts/python -m tools.install_codes --enable EXP-01` (EXP-05 is no longer needed).
2. Boot the game and **Load State → Slot 6** (Chapter 9 fixture; verified: Lethe/Mordecai are yellow).
3. Player Phase:
   a. Put the cursor on Lethe and press A. *Expected:* not controllable now (it isn't her phase).
   b. Move Ike, Mist and Rolf (or just Wait each), then map menu → **End**.
4. The next phase is the **Partner (yellow) Phase**, because the phase order is 0 → 3 → 1 → 2. As soon as its banner appears, **save to slot 7**.
5. Record:
   a. A cursor waits for you instead of Lethe/Mordecai moving on their own.
   b. You can select Lethe → move → action menu (Attack if next to an enemy, otherwise Wait; also check whether she can **Shove**) → confirm.
   c. Lethe greys out after acting. Repeat with Mordecai.
   d. The phase ends (automatically after both act, or via map menu → End) and the **Enemy Phase** follows normally.
   e. During the yellow phase, Ike/Mist/Rolf **cannot** be moved.
   f. Bonus: does the laguz transform gauge behave normally? (Lethe/Mordecai start untransformed and won't attack until transformed.)
6. Save to **slot 8** at any unexpected screen.

**Success (Phase 1 milestone):** a–e yes, and Ike's army plays normally on turn 2. For proof, repeat once while recording a Dolphin input movie (Movie → Start Recording, then load slot 6 → save the .dtm to `work/`).

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **PARTIAL PASS**: a, b, c, f yes; **e FAILED**; d not reported | Lethe/Mordecai weren't selectable in Player Phase. In the Partner Phase the cursor waited for input, Lethe transformed at phase start, and both moved and acted. **Ike, Mist and Rolf could also be moved during the yellow phase.** Slot 7 (`work/saves/GFEE01.s07_exp01_banner`): phase 3, control `01 02 02 01`. Slot 8 (`…s08_exp01_bluemoved`): Ike (23,14), Mist, Lethe (now `JID_CAT/F`) and Mordecai all have the "acted" bit set. Root cause in RESEARCH F-15; fix = EXP-06. |

## EXP-06 — Ownership fix: units selectable only during their own force's phase

**Problem (EXP-01 e):** `GetUnitSelectState` (`0x800284B4`) has "not your phase" checks only for forces 2 and 3. Force-0 units fall through to "selectable" in any human-controlled phase.
**Change:** Gecko `C202858C` hook (9 instructions, annotated in `codes/GFEE01.ini`). If `unit.force != phase`, it returns 3 ("allied unit, not yours"). Otherwise it continues with the original instruction. In Player Phase this changes nothing: blue units match the phase, and red/green/yellow units are already filtered earlier.
Static check: `tests/test_tools.py::test_exp06_gecko_hook` disassembles the cave and confirms it replays the original instruction. Signatures pin the registers it relies on (`r30` force id, `r31` state).

Steps:
1. Close Dolphin. Run (installs both codes):
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable EXP-01 --enable EXP-06
   ```
2. Boot the game. Check under Properties → **Gecko Codes** that EXP-06 is ticked (it's a Gecko code, not an AR code).
3. **Load State → Slot 7** (yellow phase banner, turn 1). This saves replaying the Player Phase.
4. Yellow Phase checks:
   a. Put the cursor on Ike and press A. *Expected:* he **cannot** be moved (you may see his range/info, like with a green ally).
   b. Same for Mist and Rolf.
   c. Lethe and Mordecai can still be selected, moved and act.
   d. End the phase (or let it end after both act). The **Enemy Phase** runs by AI.
5. Turn 2 Player Phase checks:
   e. Ike, Mist and Rolf can be moved normally.
   f. Lethe/Mordecai can't be moved.
6. Let the turn-2 yellow phase start, then **save to slot 9** (Shift+F9 if you have that hotkey, or Emulation → Save State → Slot 9). Save to **slot 8** at any odd screen; I'll back up the old slot 8 first.

**Success:** a, b, c, d, e and f all hold → the Phase 1 milestone (yellow army human-controlled, blue army unaffected, no cross-control) is reached on one controller.
**Failure modes:** a game freeze when EXP-06 activates (bad hook; report it immediately), or blue still movable in the yellow phase (another selection path exists, e.g. the R "next unit" button; tell me which input you used).

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **PASS** (a–f) | Codes EXP-01 + EXP-06, from slot 7. Yellow phase: Ike, Mist and Rolf couldn't move; Lethe and Mordecai could. The Enemy Phase ran normally. Turn 2: blue movable, yellow locked. The tester couldn't save to slot 9 and saved to **slot 6** instead. That state is backed up as `work/saves/GFEE01.s06_exp06_turn2` (SHA-1 `e8f52444…8a8d`) and decodes as Ch9, **turn 2, phase 3**, control `01 02 02 01`. The Chapter 9 fixture was restored to slot 6 afterwards (SHA-1 `d8430d71…25a0` re-checked). Regression test: `SaveStateTests.test_exp06_turn2_snapshot`. |

**Observation (open, F-18):** if Lethe or Mordecai hadn't acted when the player ended the yellow phase, **the AI moved them** after End. This is not a failure of EXP-06, but it matters for co-op: player 2 ending the phase early hands the leftover units to the AI. See ROADMAP Phase 1 remaining items.

## EXP-07 — Leftover yellow units wait instead of being moved by the AI (fix for F-18)

**Cause (static):** the phase-end handler `0x8002E670` launches the computer-player proc **`E_CP_PhaseMain`** (`0x8028E7F8`). For phases 1/2 it does so only if `control[phase] == 2` (`0x8002E708`; EXP-04 showed this at runtime). For phase 3 it **doesn't check control at all** (`0x8002E6DC`).
**Change:** Gecko `C202E6DC` hook (annotated in `codes/GFEE01.ini`). For phase 3, launch `E_CP_PhaseMain` only if `control[3] == 2`; otherwise jump to the handler's epilogue. A CPU-controlled yellow army (vanilla) takes the original path unchanged. Static check: `test_exp07_gecko_hook`, plus 5 new signatures.

**A. Human yellow (main test):**
1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable EXP-01 --enable EXP-06 --enable EXP-07
   ```
2. Boot the game. Check that EXP-06 and EXP-07 are ticked under Properties → Gecko Codes. Load **slot 7** (Ch9, turn 1, yellow banner).
3. Act with **Lethe only** (move + Wait). **Leave Mordecai untouched.** Map menu → **End**.
4. Save to **slot 8** right after End, then watch.
   a. *Expected:* Mordecai **stays on his square** and the Enemy Phase begins.
   b. The Enemy Phase runs normally (AI).
   c. Turn 2 Player Phase: blue units movable, yellow locked.
   d. Turn 2 yellow phase: choose End immediately without acting. *Expected:* nobody moves and the Enemy Phase begins.
5. Save to **slot 9** (or slot 4 if 9 fails) at the start of turn 3's Player Phase.

**B. Vanilla unaffected (control test):**
1. Close Dolphin. Run `.venv/Scripts/python -m tools.install_codes --enable EXP-07` (only EXP-07).
2. Load **slot 6** (Ch9 fixture). End the Player Phase without acting.
3. *Expected:* the yellow phase plays **by AI** as in the unmodded game (Lethe/Mordecai move on their own).

**Success:** A(a–d) and B hold → F-18 fixed: leftover yellow units wait, as in the Player Phase.
**Failure modes:** the game hangs after End in the yellow phase (the phase may need `E_CP_PhaseMain` to finish; I'd then switch to the phase-0 variant that launches it in "mode 8"), or Mordecai still moves (another AI path exists).

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **PASS: A(a–d) and B** | A(b–d): the Enemy Phase ran normally; on turn 2, blue was movable and yellow locked; ending turn 2's yellow phase immediately moved nobody. B (EXP-07 alone, slot 6): the vanilla yellow AI acted normally. Details for A(a): | Codes EXP-01 + EXP-06 + EXP-07, from slot 7. Lethe acted, Mordecai was left, then End. Mordecai stayed put and the phase advanced without a hang. Slot 8 (backup `work/saves/GFEE01.s08_exp07_afterEnd`): Ch9, turn 1, **phase 1 (Enemy)**, Mordecai at his start square (24,18), Lethe at (25,19). Regression test: `SaveStateTests.test_exp07_leftover_waits`. |

## EXP-08 / COOP-P1 — Packaged Phase 1 code set (no per-frame write)

**What changed:** EXP-01 (an AR write of `control[3]=1` every frame) is replaced by **EXP-08**, a C2 hook on the phase-advance function `0x8014D3B4`. It runs once per phase change, before the next phase starts. It sets `control[3]` = 1 if force 3 has units (first-unit pointer `0x802CA288` ≠ 0), otherwise 2 (vanilla CPU). **COOP-P1** = EXP-08 + EXP-06 + EXP-07, with identical lines (`test_coop_p1_package`). Static checks: `test_exp08_gecko_hook`, 35/35 signatures.
**Why it's robust:** it repairs states and saves made without the mod (slot 6 holds `control[3]=2`) at the first phase change, and chapters with no yellow units keep the vanilla CPU setting, so no empty human phase appears.
**Known limit:** a state saved *during* a yellow phase with `control[3]=2` stays CPU for that one phase.

**A. Recovery from a pre-mod state**
1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable COOP-P1
   ```
   This enables only COOP-P1; no AR codes.
2. Boot the game. Under Properties → Gecko Codes, only **COOP-P1** should be ticked. Load **slot 6** (Ch9 fixture; `control[3]=2` in RAM).
3. Player Phase: Lethe/Mordecai can't be moved. End the turn.
4. Yellow phase: save to **slot 8** at the banner. *Expected:* you control Lethe/Mordecai, Ike/Mist/Rolf are locked, and leftover units wait after End.

**B. No yellow units → vanilla**
1. Same codes. Load **slot 2** (Prologue; no force-3 units).
2. *Expected:* the tutorial plays exactly as in the unmodded game. The Enemy Phase is AI-controlled, and no extra empty phase waits for input between your turn and the enemy's.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **A PASS**; B not reported | The game ini had COOP-P1 as the only enabled code (written 01:43). Slot 8 (backup `work/saves/GFEE01.s08_exp08_banner`) was saved after loading slot 6, which holds `control[3]=2`. It decodes as Ch9, turn 1, **phase 3, control `01 02 02 01`**, so control was set by the phase-advance hook with no per-frame write. The tester then played yellow phases under COOP-P1 during EXP-09. |

## EXP-09 — Full Chapter 9 playthrough with COOP-P1, recorded as a Dolphin input movie (Phase 1 proof)

1. Codes: COOP-P1 only (as in EXP-08). Boot the game and **load slot 6**.
2. **Movie → Start Recording Input.** Starting while a game runs makes Dolphin record from a save state (it writes a companion `.dtm.sav`).
3. Play Chapter 9 to the end, controlling Lethe and Mordecai yourself in every yellow phase. Leave at least one yellow unit unacted at least once, to exercise EXP-07.
4. **Decline any memory-card save prompt** after the chapter.
5. **Movie → Stop Recording**, then **Movie → Export Recording…** and save to `work/movies/ch9_coop_p1.dtm`. Keep the `.dtm.sav` next to it; both are git-ignored.
6. Note anything odd: menus, conversations (e.g. Lethe/Mordecai talk events), shoves, transform behaviour, the boss, the chapter end.
7. Optional proof check: **Movie → Play Input** with *Read-Only Mode* on, and with COOP-P1 still the only enabled code. It should replay identically.

**Success:** Chapter 9 is completed with a human-controlled yellow army, the recording replays, and issues are noted. → Phase 1 complete.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **PARTIAL: recorded, run lost** | `work/movies/ch9_coop_p1.dtm` (SHA-1 `6739974c…8614`) + `.dtm.sav` (SHA-1 `e2ec6aa8…73d6`; decodes as Ch9, turn 1, Player Phase = slot 6). The DTM header's game MD5 (`f9d17c23…b31f`) matches our image file. The tester controlled the partners for several turns under COOP-P1 and lost the map deliberately to see the outcome. The warp fixture's army is only Ike (Lv 2), Mist and Rolf, so winning is hard. **Finding:** the partners gained no EXP from combat (F-21, vanilla behaviour). Fix: EXP-10. |

**Recommendation:** treat this recorded multi-turn run as the Phase 1 control proof. Defer "complete Chapter 9" to Phase 4, using a save with a real campaign army instead of the warp fixture.

## EXP-10 — Human-controlled yellow units gain EXP

**Cause (static, F-21):** `CanGainExp(unit)` (`0x8003D13C`) only allows force id **0 or 5**. All 25 EXP-related callers go through it (battle EXP `0x80036248`, `AddExp` `0x800351FC`, which writes `0xFF` = "--" otherwise, level-up, UI). So partner units never earning EXP is vanilla behaviour.
**Change:** Gecko `C203D180` hook (annotated in `codes/GFEE01.ini`). A force-3 unit is treated like force 5 **only while `control[3] == 1`**. CPU-controlled yellow armies (vanilla) are unaffected. Static check: `test_exp10_gecko_hook`, 39/39 signatures.

Steps:
1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable COOP-P1 --enable EXP-10
   ```
2. Boot the game. Under Gecko Codes, COOP-P1 and EXP-10 should be ticked. Load **slot 6**.
3. Before any partner fights, open Lethe's status screen (cursor on her → R or the info button). Note what the EXP field shows. (*Vanilla:* "--".)
4. Play until Lethe or Mordecai (transformed) can attack an enemy in a yellow phase. Save to **slot 4** just before confirming the attack.
5. After the battle, save to **slot 5**, then check:
   a. Does an EXP bar appear after the partner's battle?
   b. Does the status screen show a number instead of "--"?
   c. If EXP passes 100: does the level-up screen appear, and do stats rise?
   d. Does an enemy-phase counterattack by a partner also give EXP?
   e. Do blue units still gain EXP normally?
6. Send me slots 4 and 5. I'll compare the EXP byte (`unit+0x19B`) and the level (`unit+0x19A`).

**Success:** a, b and e yes (c and d if they happen). **Failure modes:** still no EXP (EXP is also gated somewhere else, e.g. when the battle copy is written back to the unit; I'd trace that next), or a crash at the EXP/level-up screen.

| Date | Tester | Result | Notes |
|---|---|---|---|
| — | — | NOT RUN | |

**Phase 1 status:** the core interaction is achieved on one controller. The yellow army is human-controlled in its own phase, the blue army in its own, with no cross-control in either direction, over two full turns, using EXP-01 + EXP-06.

| Date | Tester | Result | Notes |
|---|---|---|---|
| — | — | NOT RUN | blocked on Ch9 fixture |
