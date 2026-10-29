# Chapter10 Oscar–Kieran manual Talk fixture

Prepared independently of the validated Chapter10 profile. **Synthetic setup;
original Talk local effect now manually verified (CAMP-N), see recorded result below.** No Dolphin
launch or input is performed by the preparation or analysis tools.

The fixture is at:

```text
C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit\work\fixtures\ch10_oscar_kieran_v1
```

Its private User directory/card and copied source state are separate. The source
`work/bootstrap/ch10_loader_hook` was read only: all31 file hashes, including
start/after-Wait states, card, configuration and bindings, remained unchanged.
Production code definitions/generators remain unchanged.

## What the synthetic setup does

Start from the validated Chapter10 turn1 Blue state, with C11.cmb loaded.
End Blue through the original menu. At turn1's human Yellow phase, a guarded
private C2 calls original UnitSetPos for Oscar: **(2,19) -> (19,19)**. It requires
Oscar Yellow/unacted/alive/unrescued, Kieran Green/alive/unrescued at(20,19),
the original conversation key clear, and the destination empty. It does not run
again after Oscar has moved. It does not alter Kieran, any faction, door state,
ownership, recruitment, conversation/completion flags or objectives.

The relevant original layout and captured conditions were inspected:

- Kieran's original cell position is(20,19). Oscar's destination(19,19) is empty.
  Both tiles' original grid masks are0x000F: the right/left interaction edges are
  allowed. This places Oscar **inside the cell**, away from its door at(19,14).
- The actual door object at(19,14) has native state byte0x80, with the original
  open-worker marker unset. Both original door-event keys are clear. The setup
  leaves the object and keys unchanged. It bypasses reaching/opening the cell.
- Original Talk still checks native menu/action state, edge/occupancy, character
  identity and the unconsumed key. C11 scene29 permits Oscar/Kieran conversation
  in either direction; it has no additional door-key conditional. These static
  checks do not prove that the actual Talk menu will appear.

Enabled codes: COOP-P6 + EXP-16 + FIXTURE-LOADER + DBG-CAMP-TALK.
**3240/3248 Gecko bytes**,8 bytes spare; fingerprint **c11089d39a0fe037**.
Do not add other codes to this test configuration.

The NEW seed only appends setup code to verified unused Gecko storage. All
other decompressed state bytes are identical to the validated source state.
The original stable/loader hooks are retained. Merely enabling the new code and
restoring the old source state would discard it; use this fixture's seed.

## Launch and interact manually

1. Run the prepared launcher yourself in PowerShell:

   ```powershell
   & 'C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit\work\fixtures\ch10_oscar_kieran_v1\Launch.ps1'
   ```

   It launches the campaign clone's Dolphin with this NEW private User directory,
   copied image and seed.s02.sav. It does not modify or relaunch the source profile.
   If paused, resume. The state starts in Blue at turn1.

2. Use Player1's original map menu to **End** Blue. Do not play through enemy
   phases. On Yellow, use Player2's Next Unit until Oscar is selected. Confirm
   Oscar is at(19,19), Yellow, immediately left of Green Kieran at(20,19).

   | Input | Player1 keyboard | Player2 keyboard |
   |---|---|---|
   | Cursor | Arrow keys | Numpad8/5/4/6 |
   | Confirm | X | M |
   | Cancel | Z | N |
   | Next Unit | C | B |
   | Map menu | D | E |

   Bindings are copied from the validated profile. If they were customized, use
   those bindings. This new profile does not need TAS Input windows.

3. Select Oscar and confirm his **current tile**. Inspect the normal action menu.
   Before selecting Talk, pause and use Dolphin's **Emulation > Save State > Save
   State to File**. Save a NEW file at:

   ```text
   C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit\work\fixtures\ch10_oscar_kieran_v1\before.s02.sav
   ```

   Optional read-only setup check, from the campaign clone:

   ```powershell
   Set-Location 'C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit'
   $py = '..\FireEmblemTwoHouses\.venv\Scripts\python.exe'
   $fixture = 'work/fixtures/ch10_oscar_kieran_v1'
   & $py -B -m tools.ch10_talk_fixture check-setup "$fixture/before.s02.sav" --ini "$fixture/User/GameSettings/GFEE01.ini"
   ```

   PASS means the listed setup conditions hold, **not that Talk works**. If Oscar
   did not move, Talk is missing/disabled, or this check fails, preserve the state
   and report the result. Do not change flags, factions or the cell door to force it.

4. Resume. With Player2, choose the original **Talk** command and Kieran. Advance
   the original Oscar–Kieran conversation normally. After the dialogue completes
   and the map returns, observe whether Kieran becomes Yellow. Pause and save:

   ```text
   C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit\work\fixtures\ch10_oscar_kieran_v1\after.s02.sav
   ```

   Keep both files; do not end Yellow before this capture. Original Talk may
   change Oscar's acted flag; the comparison records it without assuming its value.

5. Analyze both captures:

   ```powershell
   & $py -B -m tools.ch10_talk_fixture compare "$fixture/before.s02.sav" "$fixture/after.s02.sav" --ini "$fixture/User/GameSettings/GFEE01.ini" --observed-original-talk > "$fixture/talk-result.json"
   Get-Content "$fixture/talk-result.json" -TotalCount 18
   ```

   Redirection with `>` writes the report silently. Run `Get-Content` above to
   display it; a successful comparison does not launch another step in Dolphin.

   Use `--observed-original-talk` only if you actually chose the original command
   and watched its conversation. Without that declaration the result remains
   INCONCLUSIVE even if captured state fields match expectations.

## Evidence and limits

The comparison requires matching live C2 sets, unchanged chapter/turn/Yellow
control and loaded C11.cmb, preserved slot/PID identities, Oscar remaining
Yellow, Kieran Green->Yellow, the original conversation key clear->set,
preserved positions/HP/class/EXP/inventory/rescue state, and unchanged door and
chapter completion flags. It reports both units' full flags and other captured
fields, plus named flag changes. Unrelated roster changes fail the check.

A PASS covers only this original Talk interaction from a synthetic inside-cell
setup. It does **not** verify door opening/access, combat traversal, permanent
recruitment, escape, chapter cleanup, progression, native save/reload or Netplay.
Those remain separate campaign tests. No production gameplay fix is claimed.

To reproduce preparation in a NEW directory:

```powershell
& $py -B -m tools.ch10_talk_fixture prepare --source work/bootstrap/ch10_loader_hook --root work/fixtures/ch10_oscar_kieran_NEW
```

Preparation refuses an existing destination. It checks source geometry/units,
keys, actual door, hooks and budget before creating the separate profile. Keep
generated states, cards and native game assets under ignored work/.

## Recorded manual result (CAMP-N)

The user supplied the before/after states and original-Talk observation.
Reanalysis with the corrected selected-actor occupancy check gives **PASS**:
Kieran Green->Yellow, original conversation key set, Oscar stays Yellow and
acts; identities/items/progression and door/chapter flags preserved. Original
Talk may be selected while Oscar's own occupancy entry is empty; the checker
requires the context actor to identify Oscar and the adjacent Kieran entry to
remain valid. See TESTING CAMP-N and RESEARCH CAMP-012. No gameplay code changed.

The first report and captures are preserved. Display the corrected report with:

```powershell
Get-Content 'work/fixtures/ch10_oscar_kieran_v1/talk-result-verified.json' -TotalCount 12
```

No repeat of this interaction is needed. Permanent recruitment, escape and
cleanup remain separate tests; do not infer them from this local Talk result.
