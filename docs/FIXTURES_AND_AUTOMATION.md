# Private fixtures and Dolphin smoke testing

All commands run in the isolated campaign clone. Use its Python interpreter and
its copied Dolphin/image. Never point a generated profile at a personal card.
Generated profiles, states, movies and extracted evidence remain ignored in work/.

## Fixture classes

| Class | What it establishes | What remains missing |
|---|---|---|
| Naturally progressed | Original history through the recorded path | Other branches/configurations still need tests |
| Synthetic chapter redirect | Target loader/event behavior with the inherited minimal roster | Supports, inventory, recruitment and prior story conditions |
| Synthetic RAM edit | A controlled local precondition | Original loader/event reachability and global consistency |
| Copied baseline with synthetic input | Action behavior from that exact saved state | Earlier progression and other chapters |

The historical Ch9 card itself was created with EXP-05 (NET-00). A native GCI file
does not make its campaign history natural. Mid-battle chapter-byte editing failed
in EXP-03; it is not a general warp workflow. Suspend from a state with mismatched
card identity failed (F-31); copy a matched private card or boot from a native card
start instead. No undocumented GCI checksum/flag rewriting is implemented.

## Later-chapter bootstrap

The original script-selection `--redirect-kind loader-hook` route source7->11
is now accepted as a **synthetic** Chapter10 start (CAMP-L, user testing), unlike
the failed frame-polled AR restart route. Captures identify C11.cmb and all live
stable+loader hooks. Original P2 Oscar Wait passed; inherited weak army limits
normal prison traversal. This does not validate another chapter/route/history.

Original Talk local effect is now accepted from human captures (CAMP-N).
For preserved setup lineage use **CH10_TALK_FIXTURE.md**. The separate
inside-cell positioning profile/seed is prepared under
work/fixtures/ch10_oscar_kieran_v1,3240 bytes. Source start/profile/card preserved.
Local Talk state effect passed; permanent recruitment/escape/cleanup remain unverified. No tool
launches Dolphin or sends input; the user performs and captures the interaction.

For Ch6, prefer the accepted native restart fixture from CAMP-F instead of the
synthetic redirect. Fresh boot the private NET02 card copy, select Restart Chapter
> Ch.6, use the normal Start skips for opening dialogue, then Fight > Begin now Yes.
work/ch6_native_start.s02.sav is the captured turn-1 baseline; its immutable source
card copy is work/saves/native_ch6_card_start.gci. Earlier card history is only
partly documented, so this is not labelled naturally progressed. Boyd is absent;
Oscar is the only stable table-owned Yellow, Shinon/Gatrie are away. Check the
fixture explicitly with `tools.state_expect SNAPSHOT campaign/fixtures/ch6_start.json`.
Single Yellow Escape was exercised later in CAMP-G's synthetic positioning
fixture; this native starting state alone does not prove Escape. All personal
cards remain read only.

`python -B -m tools.fixture_bootstrap --root work/bootstrap/ch6 --target 7`
creates a NEW private profile and empty card directory. It refuses existing
destinations, requires this clone's work/ boundary, validates stable Gecko capacity,
and emits fixture.json with limitations. Existing generated profiles in this run:
ch6 (7), ch10 (11), ch17 (18), endgame (31). They are **NOT TESTED**.

Launch `Dolphin-x64/Dolphin.exe --user work/bootstrap/ch6/User`. Start New Game and
finish the original Prologue; the conditional AR seed changes the first internal
chapter 2 into the target. This generalizes the historically demonstrated Ch9
EXP-05 loader path; all other destinations remain hypotheses. Do not bypass the
target event using completion/death/debug cheats. Disable FIXTURE-REDIRECT before
further progression and accept the fixture only after inspecting its map, roster,
original event and snapshot. A missing mandatory character/item is a fixture
limitation, not a demonstrated campaign bug.

The bootstrap also supports `--source-chapter N --card INPUT.gci`. It reads the
GCI once, checks GFEE01 directory identity, copies bytes exclusively into the NEW
profile and records their SHA-256. It does not validate/rewrite GCI checksums or
certify the supplied source chapter/history. Non-default sources require a card;
equal source/target and invalid routes fail before profile creation. Actual INI
validation precedes directory/card mutation.

**CAMP-J rejected route:** source7 -> target11 from the copied Chapter6 restart
card (`work/bootstrap/ch10_from_ch6`). Original Restart Chapter still loaded the
Chapter6 title, forest/bridge map and Emil even though the AR code changed RAM's
chapter byte to11. Living Kieran/Brom/Nephenee were absent. All stable C2 bodies
matched, so the chapter byte and hook check alone would have falsely suggested a
valid Chapter10 candidate. The profile/state is diagnostic only; do not reuse it
for gameplay. No prisoner event or Chapter10 compatibility result was established.

`tools.state_expect SNAPSHOT campaign/fixtures/ch10_prisoner_presence.json`
rejects this candidate for all three missing prisoners. Those presence checks
are necessary, not sufficient: still inspect the map, original event setup and
flags. Active FIXTURE-/DBG-CAMP-/EXP-05 setup codes now appear explicitly in
snapshot provenance and require `allow_synthetic` in fixture expectations. Absence
of an active setup code never certifies natural history. The known historical
source2 -> target10 transition route remains separate from this failed restart
route; synthetic loader routes cannot be generalized from one success.

Snapshots also decode the original loaded-CMB chain (RESEARCH CAMP-009).
Accepted Ch6/Ch9 states independently show C07.cmb/C10.cmb. The rejected redirect
shows C07.cmb despite chapter11. `state_expect` rejects that contradiction even
when unit expectations alone would pass. Accepted fixture recipes now explicitly
require the expected loaded container. Invalid/partial chains are inconclusive;
container identity remains separate from map geometry and original event activation.

Priority fixture predicates:

- Ch6: original Escape at (13,26); Yellow escape and carried Yellow; Ike last or
  carried Ike; roster after original cleanup, private native save and fresh reload.
- Ch10: original prisoner conversations and escape at (6,2)/(7,2); distinguish
  temporary partner membership from permanent recruitment and ownership.
- Ch17: each of four stage clear/reload events independently; turn reset, inventory,
  fatigue/status, roster and newly arriving partners. A single redirected C18 start
  does not establish all four stages or their natural entry prerequisites.
- Endgame: validate mandatory units/items and prior flags before testing the final
  objective. A minimal Prologue roster is insufficient to certify final progression.

## New RAM-edited states

`python -B -m tools.patch_state SOURCE NEW --set ADDR=HEX` now validates all edits
inside complete 24 MiB MEM1, rejects empty/overlapping edits, creates the destination
exclusively, decodes it again, and emits NEW.json with old/new bytes, source/output
hashes, Dolphin version and synthetic classification. Existing manifests are also
protected. This protects file integrity; it does not make arbitrary RAM edits valid
game states. The original image and source state are read only.

## Original Escape event with synthetic positioning (CAMP-G)

Create a NEW fixture profile with tools.fixture_position_code --root NEW_WORK_DIR
--card work/saves/native_ch6_card_start.gci. It adds only DBG-CAMP-POS to stable
COOP-P6 + EXP-16, checks the actual enabled INI (3168 bytes), and copies the card
to that new profile. It refuses existing destinations. Production packages do not
include this code.

Create a NEW seed with tools.fixture_state work/ch6_native_start.s02.sav NEW_STATE.
The tool accepts only the pinned2609a handler and exact stable list, verifies
runtime C2 branch-backs, checks the free tail, appends setup code in Gecko memory,
and verifies the decoded state. All other payload bytes stay identical. This avoids
restoring an old code list that would discard a newly installed setup hook (F-25).
Launch the private profile with --exec the copied image and --save_state NEW_STATE.

Use port1 Map Menu > End. At turn1 Yellow, original UnitSetPos moves Emil from
(13,26) to vacant (13,25), checks the exit is empty, then moves Oscar there from
(14,9). The first trial omitted the boss move and overlapped two units; it was
rejected before Escape. Do not reuse that older seed/profile.

Port2 Next Unit locates Oscar. Select him, confirm the current tile, and observe
Escape in the original menu. Capture a NEW before state. Choose Escape > Yes,
advance Oscar's original speech, then capture a NEW after state. In CAMP-G this
reached turn2 Blue with Oscar preserved in slot2/force5, same HP/lv/EXP and all64
inventory-slot bytes. Capture JSONs with the fixture INI, then run
tools.escape_smoke BEFORE.json AFTER.json. Both states must match the live stable
AND setup C2 payloads; the configuration is explicitly debug/synthetic.

This shortcut skips map traversal and combat, but still exercises the original
Escape menu, confirmation, dialogue and unit cleanup. It does not certify a
natural chapter clear, carried-unit escape, Ike's completion, transition, native
save/reload or Netplay. Current accepted files/profile live in the ignored
work/fixtures/ch6_escape_native_v2 directory; the seed and GCI are never committed.

## Demonstrated GUI action path (CAMP-C)

1. Launch the private profile with `--exec` the copied image and `--save_state`
   work/runtime_observe.s02.sav. This exact source was captured in the earlier run.
2. Native Computer Use selects only windows whose executable path belongs to this
   clone. Movie > TAS Input opens port dialogs. Select **GameCube TAS Input 1**.
3. Check A. Observe the render window: Ike's movement range appears. Uncheck A,
   then check A again to confirm the current tile. Observe Items/Wait menu.
4. Uncheck A. Click below center on the Main Stick widget, then center it again.
   Observe the menu; continue only when the hand points at Wait. This is observed
   GUI control, not deterministic frame timing. Check A to confirm Wait.
5. Enemy-phase Boyd dialogue appears. Pause through the private main toolbar.
   Emulation > Save State > Save State to File creates a NEW work/runtime_wait.s02.sav.
   If focus metadata is stale, Alt+N and the visible filename caret select File name.
   Explicit .sav avoids Dolphin appending the extension to .s02.
6. Capture both states with tools.campaign_snapshot, using the private INI. Run
   `python -B -m tools.prologue_smoke work/runtime_before_wait.json work/runtime_wait.json`.
   It passed: chapter 1/turn 1, phase 0 -> 1; Ike HP/lv/EXP/position unchanged;
   all intended stable C2 bodies matched live RAM before and after. The raw flag
   delta was 0x20; it is not labelled the acted bit (phase start clears bit 0).

This meets a minimal launch/restore/action/capture/assert smoke path. It requires
observed UI selection and is not yet an unattended frame-accurate driver. Short
keyboard taps were unreliable. DTM playback restored the scenario but synthetic
A did not demonstrate an action; its cause remains unresolved. TAS persistent
button state is the successful fallback. Stop only this clone's Dolphin process
after capture; no personal game window/profile is used.

tools/dtm_script remains a separate prototype: one controller, poll counts (not
frames), copied project DTM settings header, unchanged paired source state,
exclusive outputs and manifest. Multi-controller poll ordering is unsupported.

No later chapter, chapter clear, story transition, native save/reload or Netplay
result is accepted by this smoke test. The generated verification dashboard keeps
those axes separate.

## Demonstrated Ch9 native-partner smoke (CAMP-E)

Restore the copied historical GFEE01.s06_ch9_fixture with the same private profile.
TAS port 1 opens Map Menu (Z), selects End, confirms A. At the original transformation
tutorial, port 2 selects No and confirms A. Lethe transforms at the Yellow phase.
Release A between each new confirmation. Select Lethe, confirm her current tile,
move the original action menu to Wait and confirm. Pause before/after captures
through Save State to File, as above. `tools.partner_smoke BEFORE.json AFTER.json`
checks that the phase remains 3, native partners remain unassigned, Lethe is a cat,
and only her acted bit changes among captured game fields. This passed in CAMP-E.

This fixture and its earlier Ch9 GCI descend from a Prologue chapter redirect.
They can test these local partner interactions; they cannot establish natural
recruitment/story history or certify a chapter clear/transition. Full gauges over
several phases, combat EXP and cleanup still require additional cases.

## Offline-only event regression and state inspection

No emulator is required: `python -B -m unittest tests.test_campaign_event_model`
executes pinned original C11/startup/C07 script branches with explicit native
models. `python -B -m tools.campaign_event_model --out work/NEW.json` emits the
24-case summary; the regression suite covers120 cleanup-prefix combinations.
The original native AllUnitEscape boundary is never called. No model result
certifies permanent recruitment, native save/load or natural campaign completion.

campaign_snapshot now exposes the current registered named flags for any chapter,
known escaped bits, and explicit UNKNOWN battle-stage identity. A missing name
is unknown, not false; other/global banks remain undecoded. Accepted source
states are read-only. `tools.campaign_verify --coverage-json work/coverage.json`
exports scope/evidence/limitations separately from the unchanged acceptance axes.
