# Campaign integrity: manual tests and evidence collection

Start with **CH10-PARTNER-WAIT** below. The successful Oscar/Kieran Talk does
not need repeating. This pack tests survival, control, original events and save
integrity; it cannot guarantee an entire campaign from a handful of local tests.
Codex has not launched or controlled Dolphin. All new runtime cases are NOT TESTED.

Generated pack: `work/manual_campaign_v1/README.md`. It contains 17 targeted
cases and 34 original chapter/stage continuity cases. Each folder has exact
steps, required capture labels, observation fields and acceptance limits.
Unavailable later saves are labeled blocked; these are recipes, not fabricated
playable fixtures. Catalog source: `campaign/manual_cases.json`.

## First test: Kieran's Player2 control and original Wait

This needs no prison traversal, combat or door opening. The new private profile
`work/fixtures/ch10_partner_actions_v1` has its own card and a byte-identical
copy of your successful **after-Talk** state. No RAM/roster edits or new codes
were added. All source state/card/config/bindings hashes matched after copying.
Enabled configuration remains **3240/3248 bytes**, fingerprintc11089d39a0fe037.
Do not add codes or install a different set into this state-backed profile.

1. Close the existing Dolphin session normally. Open PowerShell:

   ```powershell
   Set-Location 'C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit'
   $py = '..\FireEmblemTwoHouses\.venv\Scripts\python.exe'
   $case = 'work/manual_campaign_v1/CH10-PARTNER-WAIT'
   $ini = 'work/fixtures/ch10_partner_actions_v1/User/GameSettings/GFEE01.ini'
   & '.\work\fixtures\ch10_partner_actions_v1\Launch.ps1'
   ```

   Only that last command launches Dolphin, when **you** execute it. It restores
   the copied after-Talk state. Do not select Restart Chapter. If PowerShell
   blocks a local script, use this equivalent direct command:

   ```powershell
   & '.\Dolphin-x64\Dolphin.exe' --user "$PWD/work/fixtures/ch10_partner_actions_v1/User" --exec "$PWD/Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso" --save_state "$PWD/work/fixtures/ch10_partner_actions_v1/seed.s02.sav"
   ```

2. You should be in turn1 Yellow, immediately after the original conversation.
   Oscar and Kieran are Yellow inside the cell. Player2 uses numpad8/5/4/6,
   confirm **M**, cancel **N**, Next Unit **B**, map menu **E**.
   Player1 uses arrows, confirm **X**, cancel **Z**.
   In the original map menu > Options, set **Auto End Off**, then return.

3. Attempt to command Kieran with Player1. An actual action must be denied;
   cursor movement alone is allowed. Select Kieran with Player2, confirm his
   **current tile** and leave the original action menu open. Do not move him.
   Pause, then **Emulation > Save State > Save State to File**. Save a NEW file:

   ```text
   C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit\work\manual_campaign_v1\CH10-PARTNER-WAIT\before.sav
   ```

4. Resume and select original **Wait** with Player2. Do not end the phase or
   advance a turn. Pause when the map returns and save a NEW file:

   ```text
   C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit\work\manual_campaign_v1\CH10-PARTNER-WAIT\after.sav
   ```

   If Wait is missing, control is wrong, the phase unexpectedly ends or anything
   crashes, preserve the state/screenshot and record the failure. Do not change
   flags or add cheats to make the test pass.

5. Record what you actually observed. Open the generated observation file:

   ```powershell
   notepad "$case/observations.json"
   ```

   Change the three `null` values under `observed` to `true` **only for checks
   you actually passed**: `p1_cannot_command_kieran`, `p2_original_wait` and
   `no_unexpected_behavior`. Use `false` for a failed check; leave unobserved
   checks `null`. Add difficulty, notes and runtime commit if known. Save it.

6. Collect and analyze. These commands print results directly; no `>` is needed:

   ```powershell
   & $py -B -m tools.campaign_test_pack capture $case before "$case/before.sav" --ini $ini
   & $py -B -m tools.campaign_test_pack capture $case after "$case/after.sav" --ini $ini
   & $py -B -m tools.campaign_test_pack review $case
   ```

   Capture commands say INCONCLUSIVE because they only preserve evidence.
   The final review can say PASS for this **one local Wait/control case**. It
   requires original C11 and live C2 matches, living Yellow Kieran, only his
   acted bit changing, intact roster/items/progression and unchanged Talk/door/
   chapter flags. Controller/UI observations cannot be inferred from RAM alone.

   Captures are immutable: rerunning `capture` refuses an existing label. To
   reread the verdict, rerun **review** only. For a second attempt generate a
   new pack directory; never replace the original captures.

Send back the final console result and any observed discrepancy. The files are
already available locally for analysis; no need to upload private saves to a
third-party service.

## Optional second test: native Suspend and fresh resume

Use the independent `work/fixtures/ch10_native_resume_v1`, not the Wait profile
or successful Talk source. Full case: `CH10-NATIVE-RESUME/README.md`.

1. Close Dolphin. Run `work/fixtures/ch10_native_resume_v1/Launch.ps1` yourself.
   At the restored post-Talk map save `CH10-NATIVE-RESUME/before.sav` before
   using original Map menu > Suspend. Record any refusal exactly.
2. If the game reports the original memory card is missing, **stop this test**,
   preserve a screenshot and note the inherited-state/card identity limitation.
   Do not replace a personal card or spoof identity. This outcome is
   INCONCLUSIVE for campaign save compatibility and identifies a fixture blocker.
3. If Suspend is accepted on the disposable card, close Dolphin completely.
   Run `work/fixtures/ch10_native_resume_v1/Boot-Native.ps1` yourself. This
   deliberately omits `--save_state`. Use original native resume from the title.
4. Capture `CH10-NATIVE-RESUME/after.sav` at the resumed map before actions.
   Fill that case's observations, collect both using the same CLI with the
   **resume profile's** INI and review. Preserve that profile's GCI after closing.

This case remains INCONCLUSIVE in the generic automated reviewer even with a
complete bundle: fresh native boot, expected roster changes and save provenance
need engineering review. A savestate restore is not a native save/load test.

## Priority order after these short tests

| Priority | Cases | Needed evidence |
|---|---|---|
| 1 | CH10-ESCAPE | Original prisoner Escape, direct/carried branches, door/Talk history, Ike-last cleanup, next roster and native reload |
| 1 | CH6-CARRIED-ESCAPE | Both carrier/passenger factions, original Escape, Ike-last, Chapter7 roster/reload |
| 1 | CORE-DEATH | Original Yellow fatal combat/death record; separate Ike defeat/Game Over branch |
| 1 | CH13-RECRUIT | Original Astrid/Gatrie conversations, faction routing and cleanup |
| 1 | CH17-STAGES | All four parts, each boundary, original reinforcements and deployment |
| 1 | CH18-SHINON, CH18-REINFORCE | Original prerequisites and separate permanent/enemy/summoned-partner behavior |
| 1 | CH19-RAVENS, CH20-JILL, CH22-REYSON | Original conditional story transfers, next phase and cleanup |
| 1 | CH23-24-ALLIES, LATE-SPECIALS | Allied Crimeans, Geoffrey, duel and Endgame restrictions/transitions |
| 2 | CH9-PARTNERS, CORE-PROGRESSION | Native partner cleanup; combat/healing/promotion/inventory persistence |
| 2 | NETPLAY-CONTINUITY | Paired two-PC checkpoints/logs and a new session from a native save |
| 3 | campaign-* | Every original chapter/stage clear and expected roster through natural progression |

The Ch10 escape case is **not ready to launch**. Its exit geometry, prisoner
conditions and private setup budget need separate engineering. Do not try to
fight through the current weak-army fixture or append another code to its eight
spare bytes. This pack makes that blocker explicit instead of asking you to
spend hours obtaining unsuitable data.

## Capturing any later case

Open its README, obtain a suitable copied native save, and use a separate
private profile. For natural campaign continuity use **stable COOP-P6 + EXP-16**
(2536 bytes); do not continue the campaign with the experimental loader/Talk
profile. No DBG-01/DBG-02 or faction/recruitment/objective cheats can verify the
event they bypass. Synthetic local-event tests stay labeled synthetic.

Record source save history, difficulty, story/support/recruitment choices,
Dolphin version, code fingerprint, machine, runtime commit and input ports.
An analysis commit in a snapshot describes the analyzer, not automatically the
commit whose codes originally ran; runtime provenance belongs in observations.
Record expected recruits/deaths/departures so a legitimate story transfer is
not mistaken for character loss. Save to unused slots on a disposable card;
if none are available, stop that save checkpoint instead of overwriting data.

For each README label, capture a new state at the indicated stable screen,
then use:

```powershell
$case = 'work/manual_campaign_v1/CH13-RECRUIT' # substitute actual case
$ini = 'work/YOUR_PRIVATE_PROFILE/User/GameSettings/GFEE01.ini'
& $py -B -m tools.campaign_test_pack capture $case before "$case/before.sav" --ini $ini
& $py -B -m tools.campaign_test_pack capture $case after "$case/after.sav" --ini $ini
# Collect cleanup/reloaded or other labels listed in that case too.
& $py -B -m tools.campaign_test_pack review $case
```

Each capture preserves a copied raw state, exact intended INI, SHA256 manifest
and decoded snapshot. The manifest also hashes the decoded snapshot; editing
that JSON after collection fails integrity review. Older bundles without the
analysis digest remain readable but are INCONCLUSIVE for automatic acceptance;
recollect original inputs into a NEW case directory instead of editing them.
These hashes detect changes; they are not independent proof that gameplay ran.
It validates Gecko capacity before writing and compares
live C2 bodies to the intended set. It never edits a card, state, INI or ledger.
Its output is printed on screen; missing captures are listed by name.

Generic review intentionally stays INCONCLUSIVE: different events require
different original predicates. It reports captured differences for review,
rather than declaring arbitrary faction changes safe. No automatic ledger PASS
is written. A reported failed human check or corrupt evidence yields FAIL;
an entirely unrun case is NOT TESTED. A fixture limitation can be INCONCLUSIVE
without establishing that production gameplay failed.

For Chapter17, internal parts may offer no independent preparations/native save
screen. Capture the first stable map and next-part map, record part number and
original transition, and mark unavailable save checkpoints in notes. Do not
manufacture a per-part save. C18.cmb alone does not identify which part ran.
For Endgame do not invent a postgame roster/save screen: preserve the original
completion/credits evidence and record any unavailable reload checkpoint.

## Netplay and campaign completion gates

Netplay uses original fresh boot/native cards. **Do not load a state** or run
these synthetic launchers in Netplay. If saving a diagnostic state is disabled,
collect paired screenshots, Dolphin logs, card/config hashes and original
action/turn notes instead; the snapshot collector is then unavailable. Label
two distinct computers. One-PC loopback cannot certify two-PC behavior.

Before claiming a complete campaign, review every chapter/stage original clear,
all transitions, surviving roster/progression/items, expected original story
branches, native save/reload, ownership and representative two-PC events. Recheck
affected paths after every gameplay fix or configuration change. A different
difficulty/branch/configuration remains outside the tested scope. The generated
VERIFICATION dashboard is the acceptance record; this checklist is the work queue.

Regenerate a NEW pack or isolated profile without overwriting existing evidence:

```powershell
& $py -B -m tools.campaign_test_pack prepare --root work/manual_campaign_v2
& $py -B -m tools.campaign_test_pack partner-profile --root work/fixtures/ch10_partner_actions_v2
```

Close Dolphin before copying a source profile. Neither command launches it.
Original game data, source saves, main and draft-ownership stay untouched.
