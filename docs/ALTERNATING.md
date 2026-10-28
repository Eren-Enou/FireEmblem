# Alternating unit actions — feasibility study (branch `experiment/alternating-actions`)

**Status:** static design and experiment code (EXP-24) ready; **runtime untested** (ALT-01 in TESTING.md).
This branch starts from `a293a40` (DRAFT-01 passed) and must not be merged into `main` or `draft-ownership`.
The sequential Blue → Yellow → Enemy co-op stays the stable mode.

## Goal
Player 1 completes one unit's activation, then Player 2 completes one, alternating until both armies are done.
Then exactly one Enemy Phase runs, and the next turn resets normally.

## How the original game structures a turn (evidence)
| Piece | Address | What it does | Ref |
|---|---|---|---|
| Phase byte | `state+0x11` = `0x80330719` | 0 blue, 3 yellow, 1 enemy, 2 green; advanced 0 → 3 → 1 → 2 → 0 by `0x8014D3B4` (one caller, `0x8002E65C`) | F-09 |
| Human control | `control[force]` = `0x8033071C+f`; turn loop step `0x8002E738` starts the human proc `0x80284AC8` when `control[phase] == 1` | | F-05, F-10 |
| Phase-start upkeep | `0x8002E780` clears the acted bit of **every** unit in forces 0–3 at each phase start | | F-16 |
| Who may act | `GetUnitSelectState` compares the unit's force with the phase (EXP-06); EXP-14 routes port 2 when phase = 3; EXP-17 Next Unit / auto-end use force 3 in phase 3 | | F-15, F-29, F-42 |
| **Activation complete** | The human proc's post-action path (`0x80284BE4…0x80284C18`) runs `E_TaikiToken`, the five post-action event checks (`0x800BF69C`, `0x800BF604`, `0x800BFF30`, `0x800C000C`, `0x800BE2F4`), **then** `0x80028C90`. That sets the acted bit on the current unit (`*0x802EF4C8`, `0x80028CBC`), runs the auto-end check, and returns to the idle loop | | F-55 |

So "a unit's activation has completed" has one native point: **`0x80028C90`**. It runs after the action (attack, staff, talk, item, rescue, Wait, …) and after any events it triggered, and the unit is already marked acted. Pressing Wait is just one way to reach it.

## Experiment (EXP-24, `tools/alt_code.py`)
Keep the blue phase's human proc running for the whole shared round, and flip only the phase byte. No phase transition runs, so acted flags, phase-start events, music and banners are not re-run.

1. **Handoff** (hook `0x80028CC4`, after the acted bit, before auto-end). The hook only acts when the phase is 0 or 3 and both armies are human-controlled.
   - Phase := the other army.
   - If `0x800AA5F0(0)` finds a unit of that army that can still act → stay switched, and move the cursor to that unit (the vanilla cursor move `0x8014CBD8`).
   - Otherwise switch back. If the current army still has a unit → it keeps playing.
   - If neither army has a unit left → phase := 3, so the normal auto-end, or a manual End, advances 3 → 1.
2. **End** (hook the phase-advance call `0x8002E65C`): End pressed in phase 0 during a shared round first sets phase := 3. The yellow phase start never runs, so the acted reset (F-16) can't give anyone a second action.

Selection, controller port, Next Unit, auto-end and the cursor cue follow the phase byte automatically. They are the existing verified hooks EXP-06/14/17/20.

## What should work (to verify in ALT-01)
- Blue → Yellow → Blue handoff with acted states kept (no transition clears them).
- One Enemy Phase per round. The round ends as phase 3, and 3 → 1 is the vanilla order.
- The next turn starts normally: blue phase start, acted reset, events.
- Ownership: works with EXP-16 or EXP-21. Ownership only decides the force; alternation only reads forces.
- Netplay: everything is driven by game state and synced inputs. No host-only data, and no timing beyond the frame loop.

## Known or likely breakages
1. **The yellow phase start is skipped.** Anything the game does at the start of an army's own phase won't happen for yellow units. Likely candidates (not yet traced):
   - terrain healing (forts)
   - status countdowns
   - **laguz gauge changes** (Lethe and Mordecai in Ch9)

   This changes gameplay for yellow units. A fix would run force 3's per-phase-start upkeep during the blue phase start. That needs the upkeep steps found first: the turn-loop steps after `0x8002E5B4`.
2. **Scripts that read the phase mid-round.** During a yellow activation, the post-action event checks see phase 3 (`BMGetPhase`). Chapters with phase-specific events (audit flag `phase`) need checking. Events scripted for the start of the partner phase never fire.
3. **Presentation:** the music and banner stay on Player Phase for the whole round. The handoff cue is the cursor jumping, plus the switched controller.
4. **Auto End off:** when the round is over (phase 3), Player 2's controller holds the End command, since port 2 is routed in phase 3.
5. **Suspend mid-round:** the phase byte (3) is saved. On resume the game may start a yellow human proc. Untested.
6. **Units that never finish through `0x80028C90`** (e.g. a unit removed mid-action by an event) only end the round through auto-end or End. Untested.

## Groups of two instead of one?
Handing off after every N activations is a one-counter change to the same hook. It doesn't avoid any of the risks above, which all come from switching inside one phase. It only reduces how often control switches. So it is not substantially safer. It could still be offered as a pacing option if strict single-unit alternation feels slow.

## Decision gates
1. ALT-01 steps 1–4 (one handoff each way, acted states kept) → the mechanism is viable.
2. ALT-01 steps 5–7 (one Enemy Phase, a normal next turn) → a full round is viable.
3. Then trace the phase-start upkeep (breakage 1) before any campaign use. Without it, yellow forts, statuses and laguz are wrong.
