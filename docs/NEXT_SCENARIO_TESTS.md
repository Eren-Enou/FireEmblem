# Next short owner-operated tests

Prepared offline on `codex/campaign-compatibility`, 2026-10-29. **Runtime update:
CH7-PLAYER2-CONTROL PASS through agent Computer Use (CAMP-AG). The original
CH10-CHAPTER-COMPLETE configuration is rejected/quarantined (CAMP-AF): native
guards damage Brom and alarm reinforcements occupy the exit. Do not relaunch it.
CH6-YELLOW-RESCUE and CH6-YELLOW-COMBAT now have scoped agent runtime passes
(CAMP-AH/AI); Lethe combat and the one-attack fatal probe remain NOT TESTED.** The four previously accepted scenarios and
their captures are preserved; they do not need repeating. No Dolphin launch or
input occurred during this preparation.

Open PowerShell in `C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit`:

```powershell
.\Test-Scenario.ps1 -List
.\Test-Scenario.ps1 -Scenario CH10-CHAPTER-COMPLETE -Check
.\Test-Scenario.ps1 -Scenario CH10-CHAPTER-COMPLETE
```

Only the last command launches Dolphin, when the owner invokes it. `-List`,
`-Check`, `-Collect`, `-Capture`, `-Review` and observations never launch it.
Close any existing Dolphin normally before launching; the launcher never closes
another instance. P1: arrows/X/Z/D; P2: numpad8/5/4/6, M/N/E.

| Recommended order | Scenario | Owner actions | Gecko bytes / 3248 |
|---|---|---|---|
| 1 | CH10-CHAPTER-COMPLETE | End Yellow once; six original Blue Escapes, Ike last; original ending/save/fresh Load | 3216 |
| 2 | CH7-PLAYER2-CONTROL | Native Load, original battle, end Blue, P1 lockout and P2 Oscar Wait | 2536 |
| 3 | CH6-YELLOW-RESCUE | Original Oscar Rescue targeting Blue Rhys, if offered | 2928 |
| 4 | CH6-YELLOW-COMBAT | One original Oscar attack against an Archer | 2912 |
| 5 | CH9-PARTNER-COMBAT | One original transformed Lethe attack against an Archer | 2912 |
| 6 | CH6-YELLOW-FATAL | Separate disposable one-attack fatal probe; survival is possible | 2912 |

For each name substitute it in `-Scenario NAME -Check` and then `-Scenario NAME`.
The printed steps are scenario-specific. Set **Auto End Off** before actions.
Chapter6 seeds inherit an old Escape action menu. With P2, cancel the menu with
B and cancel Move with B again, then wait at the idle map for native positioning.
Never confirm that inherited Escape. Use original Next Unit to find Oscar's new
tile before selecting him. The Chapter6 seed has Auto End On: explicitly switch
it Off through Options; the selected value is green. Raw position-only setup
comparisons report flag0x20 screen-projection updates separately (RESEARCH CAMP-026).
Do not select Restart Chapter in redirected/state-backed fixtures. For the
native-only Chapter7 scenario, the original title menu **Restart Chapter >
Ch.7: Shades of Evil** is the normal native file-loading route; select that
verified Chapter7 file, never `source.sav`. The action probes must not advance phases or use
native Save/Suspend; their copied card is not a validated state/card pairing.
All profiles are separate. Stable COOP-P6 + EXP-16 remains 2536 bytes, fingerprint
`8609ae9f49fd879f`; no production gameplay code was changed.

## Where to save files and how to collect

Use Dolphin **Emulation > Save State > Save State to File**. These are savestates,
separate from the game's native memory-card Save. Save directly in:

`C:\Users\Aaron\CoderViber2\FireEmblemCampaignAudit\work\scenarios\human_v1\SCENARIO-NAME\`

Chapter10 completion needs **staged.sav, before.sav, after.sav, next_prep.sav,
reloaded.sav**. Every other new scenario needs **before.sav and after.sav**.
Never select files under `captures/`, `card-before/`, or an accepted older case
as save destinations. Never overwrite `seed.s02.sav` or `source.sav`.

After the final capture, close Dolphin normally and collect with one command:

```powershell
.\Test-Scenario.ps1 -Scenario CH10-CHAPTER-COMPLETE -Collect
```

It discovers the declared filenames, snapshots state/config/private card, and
reviews the bundle. Missing files produce NOT TESTED/INCONCLUSIVE. Running it
again retains existing captures; a raw file differing from its immutable capture
is refused. It never fabricates human observations. `-Review` remains available.

Declare only checks actually observed. You may add `-Passed`/`-Failed` and
`-Notes` to `-Collect`, for example:

```powershell
.\Test-Scenario.ps1 -Scenario CH7-PLAYER2-CONTROL -Collect -Passed original_battle,p1_cannot_command_oscar,p2_original_wait,normal_turn_cycle,no_unexpected_behavior
```

The exact observation names for every case are in its `case.json`; the table below
also lists them. A missing command, unexpected damage or refusal is useful
evidence: preserve the state and record the result instead of playing the map.

## Chapter10 ending

Source: accepted Kieran original Escape, SHA-256
`b9a50895bf2136aace6911b3d5295545a7d2ee1826b762ee4dd504cfef2fdeca`.
Kieran already has his original Escape key, force5 and escaped marker. Oscar is
Yellow and has already acted. Brom/Nephenee remain Green, their doors closed and
Escape keys false. Synthetic positioning bypasses traversal, not these histories.

1. Restored Yellow turn1: wait for staging, set Auto End Off, save **staged.sav**.
   Six Blue and three fixed-owned Yellow are placed near the genuine exit.
   Six living Reds are moved aside; no unit is weakened, killed or recruited.
2. End Yellow once. Allow one original enemy phase and turn2 prompts. If anyone
   is damaged or staging/queue fails, capture it and stop; no fighting is required.
3. The private queue presents **Titania, Rhys, Soren, Volke, Lethe, Ike** at `(6,2)`.
   With P1 select the current tile and execute original Escape/Yes each time.
   Before Ike's Escape, save **before.sav**. Ike is **last Blue**. Oscar, Shinon
   and Gatrie deliberately remain Yellow for stable AllUnitEscape hand-back.
4. Execute Ike's original Escape. At the first stable ending dialogue, after the
   map has been freed and before the next chapter, save **after.sav**. Do not skip
   the entire ending before capturing. If that checkpoint cannot be captured,
   preserve what is available; the full result remains inconclusive.
5. Continue original story. If offered Volke's original hiring choice, record the
   choice; do not edit its flags. Reach Chapter11 preparations, before combat or
   inventory changes. Inspect Kieran and the original army. Save **next_prep.sav**.
   Kieran should be permanently available; Brom/Nephenee have unmet conditions
   and should not be recruited. This is a hypothesis to test, not a runtime pass.
6. Use the game's original Save into an **unused slot on this private card**.
   Close Dolphin completely, then run:

   ```powershell
   .\Test-Scenario.ps1 -Scenario CH10-CHAPTER-COMPLETE -FreshBoot
   ```

   Choose original Load, never a state. Return to the same preparation context
   without acting, buying, equipping or rearranging items. Save **reloaded.sav**.
   If native saving is refused, preserve the refusal. Do not alter card identity.

Collect after closing Dolphin. If all listed checks were observed:

```powershell
.\Test-Scenario.ps1 -Scenario CH10-CHAPTER-COMPLETE -Collect -Passed remaining_blue_original_escapes,ike_last_blue,original_completion,expected_recruits,native_save_accepted,fresh_boot_without_state,native_load_selected,no_unexpected_behavior
```

Validator requires the position-only staged roster, genuine escaped Blue queue,
accepted prisoner histories, original container identities C11 then C12, retained
Kieran/Oscar identity/progression/items, no unexpected Brom/Nephenee recruitment,
changed private card, consistent reloaded permanent/away records and explicit
human observations. Changed chapter number alone cannot pass. Enemy slot
reconstruction is excluded. Inherited Shinon/Gatrie history is synthetic; their
possible original away status and optional Volke choice remain separately noted.

## Chapter7 control

This **always boots natively**, without a savestate argument, from a new copy of
the accepted Chapter7 GCI (`99446e1b...45e429ca`). `source.sav` exists for offline
inspection only and must never be loaded. Enter the original battle normally,
keep Oscar deployed, set Auto End Off, and end Blue without acting/fighting.
At Yellow turn1 attempt P1 command, then open Oscar's original Wait menu with P2;
save before.sav. Execute P2 Wait and save after.sav on the same Yellow turn.
The Blue-to-Yellow transition supplies `normal_turn_cycle`; no enemy phase needed.

## Original Rescue and action probes

**CH6-YELLOW-RESCUE:** Yellow Oscar `(13,24)`, Blue Rhys `(14,24)`. Both retain
original stats/items. Read-only original predicates admit this faction pairing
and capacity margin (33 versus8); both cells have open adjacency and valid terrain.
This is not proof that every runtime eligibility condition passes. Save before,
execute original Rescue if offered, save after **without Escape**. A local PASS
requires reciprocal unit pointers, original carrier/passenger bits2/4, co-located
identities and retained factions/HP/items. A carried Escape fixture remains
blocked until a genuine original relationship has been captured and reviewed.
The reverse pairing Blue Rhys carrying Oscar fails the capacity predicate; it is
not offered as a playable test. Blue carrier with a lighter Yellow passenger and
temporary-partner carried Escape still need suitable original states.

**CH6-YELLOW-COMBAT:** Oscar `(15,13)` attacks the original Steel Bow Archer at
`(15,14)` with his original Iron Lance. Save before at forecast, execute once,
save after once combat/EXP is done. Mounted Canto may remain active; do not move
or advance a phase. Validator measures damage, gained EXP and the original weapon
uses byte. It does not require or claim a level-up. Healing/status tests remain
unprepared, rather than substituting direct HP/EXP writes.

**CH9-PARTNER-COMBAT:** accepted transformed Lethe is positioned `(9,26)` beside
the original Archer `(8,26)`. One original attack; record displayed EXP and gauge.
She must remain native force3 with no persistent draft ownership. EXP/gauge changes
are reported; this case does not prove transformation depletion, original cleanup
or eventual recruitment. Those need another original ending/history source.

**CH6-YELLOW-FATAL:** disposable separate profile. Oscar remains beside original
Emil, who keeps IID_AXEBASTER. Inspect forecast, execute one original attack, and
capture after battle/death dialogue. No stat is forced; survival or HP0 without a
verified death record is INCONCLUSIVE. No repeated attacks to force the outcome.
A local PASS concerns the death record/chapter and identity only; later roster
removal, chapter cleanup and saving remain NOT TESTED.

| Scenario | Observation names (only declare what happened) |
|---|---|
| CH6-YELLOW-RESCUE | original_rescue, p2_command, no_unexpected_behavior |
| CH6-YELLOW-COMBAT | p2_original_attack, damage_observed, experience_gained, durability_consumed, no_unexpected_behavior |
| CH9-PARTNER-COMBAT | p2_original_attack, damage_observed, native_partner_unassigned, no_unexpected_behavior |
| CH6-YELLOW-FATAL | p2_original_attack, fatal_combat_observed, no_unexpected_behavior |

## Offline reproduction and remaining prerequisites

Builders refuse existing destinations. New independent trials use:

```powershell
$py = '..\FireEmblemTwoHouses\.venv\Scripts\python.exe'
& $py -B -m tools.next_scenarios CH10-CHAPTER-COMPLETE --root work/scenarios/NEW_trial/CH10-CHAPTER-COMPLETE
& $py -B -m tools.next_scenarios CH7-PLAYER2-CONTROL --root work/scenarios/NEW_trial/CH7-PLAYER2-CONTROL
& $py -B -m tools.action_scenarios CH6-YELLOW-RESCUE --root work/scenarios/NEW_trial/CH6-YELLOW-RESCUE
# Other action names use the same action_scenarios builder.
.\Test-Scenario.ps1 -Trial NEW_trial -Scenario CH6-YELLOW-RESCUE -Check
```

`tools.scenario_prerequisites` generates a read-only later-chapter gap report from
original instruction-aligned calls, directional conversations, MapLoad sites and
selected accepted snapshots. Prepared report: `work/scenarios/next_prerequisites_v2.json`.
All six later cases remain BLOCKED: Ch13 Astrid/Gatrie; all four Ch17 parts;
Ch18 Shinon/Reinforce; Ch20 Jill; Ch27-2/internal29; Endgame. No matching original
map/history source is available in the selected evidence, and a chapter/CMB name
alone cannot establish eligibility. No empty later-chapter profiles were made.

Full natural campaign completion, carried cleanup, later special objectives and
internet Netplay remain unresolved. Offline fixture safety and mocked original
call tests never count as a new gameplay PASS.

Optional offline integrity audit, without opening Dolphin:

```powershell
& $py -B -m tools.campaign_integrity --include-candidates --out work/scenarios/NEW_hook_integrity.json
```

This independently verifies saved C2 entry/body/return paths using the recorded
configuration fingerprint. Missing configuration is INCONCLUSIVE. Scenario
`-Review` also rechecks raw hook paths; accepted snapshots are never rewritten.
