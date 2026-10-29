# Short owner-operated campaign tests

Run PowerShell in `C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit`.
Codex has not launched Dolphin or performed these interactions. The owner has
now passed **CH10-PARTNER-WAIT** (TESTING.md CAMP-Y): original P2 Kieran Wait and
P1 lockout only. The other three scenarios remain **runtime unverified candidates**.
The earlier Oscar Talk and Oscar Escape evidence remains separate and accepted.

```powershell
.\Test-Scenario.ps1 -List
.\Test-Scenario.ps1 -Scenario CH10-PARTNER-WAIT -Check
.\Test-Scenario.ps1 -Scenario CH10-PARTNER-WAIT
```

`-Check` and `-List` never launch Dolphin. Omitting `-Check` launches the specified
private profile only when you invoke the script. Close any existing Dolphin first.
Each scenario has its own card, immutable starting state and pre-test card backup.
No profile reset or card overwrite occurs. A changed card prevents restoring the
old starting state; native `-FreshBoot` deliberately uses the changed private card.
Do not select **Restart Chapter** in redirected Chapter10 tests.

| Scenario | Original action | Expected duration | Gecko | Evidence folder under `work/scenarios/human_v1/` |
|---|---|---|---|---|
| CH10-PARTNER-WAIT | P2 Kieran Wait; P1 lockout | 1–2 minutes | 3240/3248 | `CH10-PARTNER-WAIT` |
| CH10-PRISONER-ESCAPE | P2 Kieran Escape | 1–2 minutes | 3240/3248 | `CH10-PRISONER-ESCAPE-v2` |
| CH6-IKE-COMPLETE | Three Blue allies Escape, then Ike LAST | Four short actions plus original story | 3168/3248 | `CH6-IKE-COMPLETE` |
| CH10-NATIVE-RESUME | Original Suspend, close, fresh native Resume | A few minutes if card accepted | 3240/3248 | `CH10-NATIVE-RESUME` |

P1: arrows, **X** confirm, **Z** cancel, **D** map menu.
P2: numpad **8/5/4/6**, **M** confirm, **N** cancel, **E** map menu.
Original gamepad mappings were copied for the Wait/native tests; these keys are
the supplied two-keyboard layouts. No controller inputs are automated.

## Recommended first test: CH10-PARTNER-WAIT

Starting state: original Talk already completed; Yellow Kieran stands beside
Oscar inside the closed cell. Oscar has acted; Kieran has not. No prison fighting.

1. Launch the command above. With P2, open map menu > Options > **Auto End Off**.
2. Try to command Kieran using P1. It must refuse commands; cursor movement alone
   is fine. With P2, select Kieran and confirm his **current** tile.
3. With his ordinary action menu open, use Dolphin **Emulation > Save State >
   Save State to File**. Save a new file named `before.sav` in the evidence folder
   printed by the launcher. Never select an accepted evidence file as destination.
4. With P2 choose original **Wait**. Save `after.sav` on the same turn1 Yellow map.
   Do not move, trade, end phase or repeat Talk. Close Dolphin before collection.

```powershell
$case = 'work/scenarios/human_v1/CH10-PARTNER-WAIT'
.\Test-Scenario.ps1 -Scenario CH10-PARTNER-WAIT -Label before -Capture "$case/before.sav"
.\Test-Scenario.ps1 -Scenario CH10-PARTNER-WAIT -Label after -Capture "$case/after.sav"
# Declare only checks you actually observed. Use -Failed NAME for a failed check.
.\Test-Scenario.ps1 -Scenario CH10-PARTNER-WAIT -Passed p1_cannot_command_kieran,p2_original_wait,no_unexpected_behavior
.\Test-Scenario.ps1 -Scenario CH10-PARTNER-WAIT -Review
```

Expected: Kieran stays Yellow/alive; only his acted bit changes. Missing Wait,
cross-control, disappearance or unexpected roster changes are failures to record.
PASS is limited to this local interaction; it proves no recruitment persistence,
chapter clear, natural progression or Netplay behavior.

## CH10-PRISONER-ESCAPE

```powershell
.\Test-Scenario.ps1 -Scenario CH10-PRISONER-ESCAPE
```

Setup: a new private hook moves Kieran from the accepted post-Talk cell to the
original empty exit `(6,2)` when map input runs. This is a **synthetic teleport**;
doors, Talk outcome, factions, recruitment, escaped and completion flags are not
written. Oscar remains Yellow inside the cell. The original C11 kind5/action14
Escape record, loaded scripts, actual occupancy and edge grid are checked offline.
The original menu context still has to work in Dolphin.

With P2 set Auto End Off, select Kieran, confirm his current exit tile. Save
`before.sav` with **Escape** available, choose Escape/Yes and let the original
dialogue finish. Save `after.sav` before ending phase. P1 should not command Kieran.
If setup fails, a command is missing, or the unit vanishes, capture that result;
do not compensate with cheats. Expected local result: Kieran retained in the
escaped roster with identity, HP, level, EXP and items preserved.

Use the same capture/review commands as above, replacing the scenario name and
setting `$case = 'work/scenarios/human_v1/CH10-PRISONER-ESCAPE-v2'`.
Observation names: `original_escape,p2_command,no_unexpected_behavior`.
The automatic verdict is limited to local original Escape. It cannot establish
permanent recruitment or cleanup; the original cell remains closed.

## CH6-IKE-COMPLETE

```powershell
.\Test-Scenario.ps1 -Scenario CH6-IKE-COMPLETE
```

The source is the accepted capture **after Oscar's genuine Yellow Escape**.
Oscar is already in the escaped roster. Titania, Rhys and Soren remain on-map;
skipping their escapes would not be an honest Ike-last test. The setup brings
Titania, Rhys, Soren and finally Ike to the vacant original exit, one at a time.
Emil remains alive beside the exit. No Escape or completion is injected.

Use P1 throughout. Set Auto End Off. Save `before_queue.sav`, select the ally at
the exit, confirm current tile, choose original Escape/Yes, finish dialogue.
Repeat for the next two allies. When Ike arrives, save `before.sav` and choose his
original Escape LAST. Save `after.sav` at the first stable completion screen.
Continue original story; capture `next_prep.sav` at Chapter7 before acting.
Record Oscar's identity, faction, inventory, level and EXP. Expected: the original
chapter completes and every escaped survivor is retained with normal ownership.

Use `$case = 'work/scenarios/human_v1/CH6-IKE-COMPLETE'`; collect each label with
the same `-Label LABEL -Capture "$case/LABEL.sav"` pattern. Observations:
`remaining_blue_original_escapes,ike_last,original_completion,oscar_present_next_chapter,fresh_native_load`.
For a native save, use only an unused slot offered by the original game. Close
Dolphin, then run the following and select original Load/Resume:

```powershell
.\Test-Scenario.ps1 -Scenario CH6-IKE-COMPLETE -FreshBoot
```

Save `reloaded.sav` at the equivalent Chapter7 screen. If no legitimate save is
available or card identity is refused, leave that observation/capture absent and
record the exact message. A missing ally or original completion failure requires
investigation. Review collects the transition comparison as INCONCLUSIVE pending
engineering analysis; it does not guess story-specific roster equivalence.
This synthetic clear cannot certify a naturally progressed Chapter6 campaign.

## CH10-NATIVE-RESUME

```powershell
.\Test-Scenario.ps1 -Scenario CH10-NATIVE-RESUME
```

This uses a separate post-Talk state/card, never the Wait profile. Capture
`before.sav`, inspect living Oscar and Kieran, then use original map menu >
**Suspend**. Save a screenshot of confirmation or exact card refusal. Do not
overwrite occupied slots. If refused, stop this scenario and report
`-Failed native_suspend_accepted -Notes 'Exact refusal text'`; review classifies
that inherited-card limitation INCONCLUSIVE, not a demonstrated campaign defect.

If accepted, close Dolphin completely and run:

```powershell
.\Test-Scenario.ps1 -Scenario CH10-NATIVE-RESUME -FreshBoot
```

This command supplies **no savestate**. Select the game's original Resume/Load,
capture `after.sav` before acting, close Dolphin and collect both captures using
`$case = 'work/scenarios/human_v1/CH10-NATIVE-RESUME'`. Observations:
`native_suspend_accepted,fresh_boot_without_state,native_resume_selected,same_roster_and_progression,no_unexpected_behavior`.
Review reports the decoded comparison for engineering review as INCONCLUSIVE;
equal savestate fields alone never prove native persistence. Card refusal is a
fixture limitation until reproduced from matched natural history.

## Evidence and boundaries

Collection creates exclusive `captures/LABEL/` bundles containing original state,
exact INI, decoded roster/event/script data, profile configuration and private GCI
bytes, with hashes. Collect after closing Dolphin so card files are stable.
Existing capture bundles are never overwritten. Observations retain immutable
revision history; leave unknown checks unset. Save screenshots beside the raw
captures and retain the exact error text in `-Notes`.

The new setup candidates have not been exercised in Dolphin. Offline PPC tests
execute generated guards and native-call arguments with mocked natives; those
tests prove neither actual UnitSetPos behavior nor original Escape activation.
The immutable seed remains **before** synthetic setup executes.

CH10 prisoner cleanup remains blocked on original Escape results and a valid
Ike-last source with known door history. CH17 requires actual stage-specific
near-clear states, original stage map, roster, difficulty, story/prior-stage
history and legitimate native save provenance; shared C18 scripts are insufficient.
Other later recruitment/defection cases still lack suitable original event states.
No placeholder profiles were generated for these cases.

For another trial, build all four into a NEW named directory, then select that
trial consistently for launch, capture, observations and review:

```powershell
& '..\FireEmblemTwoHouses\.venv\Scripts\python.exe' -B -m tools.test_scenario --trial human_v2 prepare
.\Test-Scenario.ps1 -Trial human_v2 -Scenario CH10-PARTNER-WAIT -Check
```

Never delete or reset a used profile to rerun; retain its card/evidence. The
fixture builders refuse existing destinations. The incomplete first Escape
preparation directory in human_v1 is preserved and is never referenced by the
launcher; the complete candidate uses the explicit `-v2` directory listed above.
