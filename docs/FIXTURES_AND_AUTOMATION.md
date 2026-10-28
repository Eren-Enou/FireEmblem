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

For Ch6, prefer the accepted native restart fixture from CAMP-F instead of the
synthetic redirect. Fresh boot the private NET02 card copy, select Restart Chapter
> Ch.6, use the normal Start skips for opening dialogue, then Fight > Begin now Yes.
work/ch6_native_start.s02.sav is the captured turn-1 baseline; its immutable source
card copy is work/saves/native_ch6_card_start.gci. Earlier card history is only
partly documented, so this is not labelled naturally progressed. Boyd is absent;
Oscar is the only stable table-owned Yellow, Shinon/Gatrie are away. Check the
fixture explicitly with `tools.state_expect SNAPSHOT campaign/fixtures/ch6_start.json`.
Escape itself has not yet been exercised. All personal cards remain read only.

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
