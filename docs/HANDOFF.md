# Handoff: drafting, ownership and preparations (branch `draft-ownership`)

**Status (2026-10-28): paused as a documented experimental milestone.** No feature work is in progress. Resume once the later-chapter test fixtures (§5) exist. Project rules: `CLAUDE.md`. Details: `docs/PREP.md` (prep plan), `docs/RESEARCH.md` (F-entries), `docs/TESTING.md` (procedures and results).

## 1. Branches
| Branch | Commit | Role |
|---|---|---|
| `main` | `6a81522` | **Stable release.** Sequential Blue → Yellow → Enemy co-op, COOP-P6 + EXP-16 (fixed ownership table), Netplay verified on two PCs (NET-02). The friend ZIP (`tools/netplay_package.py`, fingerprint `8609ae9f49fd879f`) is built from here. Only verified work is merged in. |
| `draft-ownership` | this branch | In-game ownership, the draft and preparation-screen integration. **Not merged.** |
| `experiment/alternating-actions` | `b2fe2ba` | Parked experiment (EXP-24, docs/ALTERNATING.md). Untested. Never merge. |

## 2. What is implemented here
Ownership lives in each unit's saved flag word `unit+0x1A0`, in bits the game never touches (F-52):

| Bit | Meaning | Set by |
|---|---|---|
| `0x20000000` | owned (assigned to a player) | EXP-22/23/26 |
| `0x40000000` | owner is Player 2 | EXP-22/23/26 |
| `0x10000000` | parked green during the in-battle draft | EXP-23 only |
| `0x08000000` | transfer requested by the non-owner | EXP-26 |

The game's own bit `0x80000000` is toggled by Pick Units (`0x8012C9E8`). It probably means *benched* (F-58, unconfirmed).

| Code | What it does | Generator | Bytes | Runtime status |
|---|---|---|---|---|
| COOP-P6 | the stable co-op base (from main) | ini | 1328 | verified (NET-02 etc.) |
| **EXP-21** | ownership → forces: Player 2 units go 0 → 3 at each blue-phase start, back to 0 at chapter end and on escape. Replaces EXP-16 (same hooks; **never both**) | `tools/draft_code.py` | 784 | **verified** (DRAFT-01, PREP-03) |
| **EXP-22** | in-battle draft: L+R on turn 1, alternating picks, release = undo | `tools/draft_code.py` | 704 | **verified** (DRAFT-01) |
| EXP-23 | draft v2: green unassigned, distinct sounds, the draft ends at the first action. Replaces EXP-22 | `tools/draft_code.py` | 1496 | **unverified, and does not fit** the Gecko space with COOP-P6 + EXP-21 (§4) |
| **EXP-25** | native unit lists colour the data columns by owner: light blue = Player 1/Ike, yellow = Player 2, orange = transfer requested | `tools/prep_code.py` | 144 | **verified** (PREP-02; orange in PREP-03) |
| **EXP-26** | Choose Units: Z on your own controller claims (alternating), releases, requests a transfer; the owner accepts | `tools/prep_code.py` | 672 | **verified** (PREP-03) |
| DBG-01 / DBG-02 | test aids: enemies / Player 2 units at 1 HP. Never in packages | ini | 56 / 72 | n/a |

Regenerate after editing a generator: `python -m tools.draft_code --write`, `python -m tools.prep_code --write`. Tests check that the ini matches the generators.

## 3. Verified tests (TESTING.md)
- **DRAFT-01 PASS:** all seven checks: claim, release/reclaim, yellow control, EXP, chapter transition, normal save, fresh reload. The storage persists.
- **PREP-R1:** research run. It gave the Pick Units list layout, the highlighted row, the palette, and Normal difficulty (F-58).
- **PREP-02 PASS (run 2):** owner colours on every data page, in Choose Units and in battle Base Data.
- **PREP-03 PASS (run 3):** in Choose Units:
  - Z claims with alternating picks
  - transfer request (orange) → accept (Titania P1 → P2, Lv/EXP/HP unchanged)
  - cancel and release work
  - no request left over
  - transferred units yellow at turn 1

Unverified: DRAFT-02 (EXP-23), ALT-01 (experiment branch), and PREP-01 Steps 4–7 (§5).

## 4. Exact configurations and the Gecko budget (F-59)
Dolphin 2609a has **3256 bytes** for *all* enabled Gecko codes: `0x80001800…0x80003000`, minus the 2880-byte `Sys/codehandler.bin`, minus the 8-byte terminator (`GeckoCode.cpp` 2609a). **A code that doesn't fit is skipped silently, and later smaller codes still load**; that's what broke PREP-03 run 1. `install_codes` and `netplay_setup` now print the total and refuse an over-budget set (`--allow-over-budget` overrides; don't).

| Use | Install command (`.venv/Scripts/python -m tools.install_codes --user <dir> …`) | Bytes |
|---|---|---|
| Stable Netplay (main) | `--enable COOP-P6 --enable EXP-16` | 2536 |
| In-battle draft test bed (DRAFT-01) | `--enable COOP-P6 --enable EXP-21 --enable EXP-22 --enable DBG-01` | 2872 |
| **Prep draft test bed (PREP-03; installed now in `work/ch1/host`)** | `--enable COOP-P6 --enable EXP-21 --enable EXP-25 --enable EXP-26 --enable DBG-01` | 2984 |
| Prep play set, no debug | `--enable COOP-P6 --enable EXP-21 --enable EXP-25 --enable EXP-26` | 2928 |
| ✗ Prep + in-battle draft | `… EXP-21 EXP-22 EXP-25 EXP-26` | 3632: skips EXP-26 |
| ✗ DRAFT-02 | `… EXP-21 EXP-23 DBG-01` | 3664: skips EXP-23 (DBG-01 still loads) |

**Consequence:** the full feature set (base + ownership + the in-battle *and* prep drafts + a future deployment code) does not fit. Before more features, one of these is needed:
- slim the big caves: COOP-P6's parts, EXP-21's five near-identical caves, EXP-22/23
- or a loader that keeps large payloads outside the Gecko list (design not started)
- or drop EXP-22 where the prep draft covers it

## 5. Remaining acceptance tests (need fixtures)
| Test | Needs | What to verify |
|---|---|---|
| **PREP-04** persistence (Step 4) | Clear Ch6 with the PREP-03 bed (Escape objective; DBG-01 makes it quick), save over a test file, reach Ch7 prep | The Ch7 Choose Units colours match Ch6's ownership; after a fresh reload too. The storage is already proven by DRAFT-01; this confirms prep-made ownership |
| **PREP-05** fair deployment (Step 5, not built) | **A save at a prep screen where roster > cap.** Ch3–Ch7 force nearly everyone (audit). From Ch8 only Ike is forced; the first likely bench is around **Ch10** (cap 11 on Normal). Needs a campaign played that far | Confirm `0x80000000` = benched by toggling a non-forced unit (A in Choose Units). Then build the split: forced units first, optional slots alternate, each player toggles only their own, the native cap stays authoritative |
| PREP-06 confirmation (Step 6, not built) | same fixture | Both players ready (Start on their own pad) before Fight |
| PREP-07 Netplay (Step 7) | two instances (`netplay_setup`), then two PCs; a draft-branch package (the friend ZIP is still main's) | Identical ownership, transfers, deployment and controller routing on both machines; no desync |
| Story cases | later-chapter saves | Ch10 temporary partners (never offered), Ch18 Shinon to the enemy and back (ownership bits survive story transfers), mid-battle recruitment (unassigned until the next prep), an owned unit dying, suspend at prep |
| Player 2 cursor in prep | any prep save | Today the list cursor follows port 1, so Player 2 acts on the row Player 1 highlights (by design for Step 3) |

Fixtures: create only with `tools/patch_state.py` (slots 2+, refuses to overwrite), or by having the tester save at prep screens. Back up any test-bed card or state in `work/saves/` first. Decode with `python -m tools.inspect_state`. A lowered cap (`state+0x544`) in a state is acceptable only as a labelled test fixture, never as proof.

## 6. Known risks
- **Gecko space (§4).** The main blocker for adding anything.
- **`0x80000000` meaning:** likely "benched" (no picked unit has it); confirm before Step 5.
- **Story/event interactions** not yet seen at runtime: Ch10 partners, Ch18 Shinon, recruitment, Game Over.
- **Generic script commands** `0x800BD37C`/`0x800BD3D0` set/clear a script-supplied flag mask. No script is known to pass bits 25–30, but this isn't excluded (F-52).
- **EXP-26 only acts in the `E_SallyList` proc** (`list+0x14` = `0x80275B0E`). Other lists are unaffected.
- **Ike** is recognised as the lord by attribute 0 (EXP-22/26) or by unit id 1 (EXP-25 colour).

## 7. How to test (tester drives Dolphin; see `CLAUDE.md` / memory)
1. Close Dolphin, then install a configuration from §4 into a private user folder (`work/ch1/host`; its card is backed up as `work/saves/ch1_card_before_draft01.gci`).
2. `Dolphin-x64/Dolphin.exe --user work/ch1/host`. **Fresh boot**: a save state restores its old code list (F-25).
3. Keys on the one-PC test bed:
   - port 1: arrows, A = X, Z = D, L+R = Q+W
   - port 2: numpad, A = M, Z = E, L+R = O+P
4. Ask for screenshots and Shift+F*n* states at the key moments, then decode them.
5. Before committing: `.venv/Scripts/python -m unittest tests.test_tools tests.test_cave_behaviour` and `python -m tools.check_signatures` (176 match).
6. **Behavioural tests without Dolphin:** `tests/test_cave_behaviour.py` runs the generated caves in `tools/fe9/ppc_sim.py` (a small PowerPC interpreter: an integer subset plus stubs for `UnitTransferToForce`, the lord check, sound and cursor unit) against a synthetic world (`tests/sim_world.py`). It replays DRAFT-01's and PREP-03's steps. Use it before every cave change; it doesn't replace a runtime test.

## 8. Next steps when resuming
1. Get a later-chapter prep fixture with roster > cap (§5).
2. Resolve the Gecko budget: slim EXP-21/22 first, or design a payload loader. Keep `test_gecko_budget` current.
3. PREP-04 → confirm the benched bit → build Step 5 (fair split), with its own budget check → Step 6 → Netplay.
4. Only merge into `main` after a two-PC Netplay pass with a rebuilt friend package (new fingerprint).
