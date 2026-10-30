# Testing

## CAMP-AJ / CAMP-AK — Native Yellow combat and surviving fatal probe

2026-10-30, agent Computer Use, separate private profiles, runtime commit
`a0bc15e`. All six prepared scenarios have now been attempted: AG/AH/AI/AJ
scoped PASS; AF fixture FAIL/completion INCONCLUSIVE; AK fatal INCONCLUSIVE.
No natural-campaign, chapter clear, later roster, native saving or Netplay claim.

**CAMP-AJ PASS, synthetic original positioning:** CH9-PARTNER-COMBAT, PID117556,
2912-byte fingerprint `93cc716863b133a7`. Original Options Autoend Off; Next Unit
selected native Lethe, CURRENT tile9,26, Attack/Claw. Forecast against original
Archer8,26:21HP versus34HP,20x2 damage,100hit,5crit, no bow counter. Saved before,
executed ONE attack, observed target defeat and same Yellow turn1 with Lethe
34HP/gauge19. Saved after before another action/phase; closed private Dolphin.
Raw comparison: Lethe force3/slot26/JID_CAT/F unchanged, unassigned ownership,
EXP0 ->11, gauge20 ->19, acted bit0 ->1, inventory unchanged; target slot30
removed. No unrelated action record delta. Legacy chapter234 byte0 ->10 is
reported, not interpreted as death (CAMP-028). Transient EXP bar not captured.

Before SHA256 `dfcd7a10a33da34e3c0a226f03d29008b03ccbec2f56f27acfd951c48d40f4fa`;
after `f0bd421f9ed0e7ded64836728b8ba36dd9b344947a9fe21178018d86aa6d79ea`.
Evidence: CH9-PARTNER-COMBAT/captures and observation-history/0001.json;
partner-result.json plus five partner-*.png in work/agent_runtime_20261029_v1.
Ledger ch9-native-partner-combat-agent-30 accepts only independent combat
lifecycle, preserving all previous accepted claims/artifacts.

**CAMP-AK INCONCLUSIVE, fatal transition absent:** CH6-YELLOW-FATAL, PID144576,
2912-byte fingerprint `3eeff9026a3238a5`. Cancelled inherited Escape/Move,
Autoend Off, CURRENT tile Oscar13,26, original Iron Lance39. Actual forecast:
Emil32HP/Short Spear,8damage82hit1crit; Oscar28HP,6damage78hit1crit. Advanced
original Emil boss dialogue once and allowed ONE attack. Oscar survived and
mounted continuation returned. Raw OscarHP28 unchanged, EXP28 ->51, lance39 ->38;
EmilHP32 ->26. No death observed or declared. No repeated combat, movement,
Wait, phase advance, HP/death edit or native card write.

Before SHA256 `d507f075f3da9f0961866c2255d9e83885ca0b540d15ea2b7fed3259f9a07c57`;
after `197ce71a4b85d26b7db0d8b94959fd37673ee411a400d8fea747fa9930833a29`.
The first review rejected generic boss-talk plus discovery keys; original pinned
C07 scenes19/17 explain both precise forward effects (CAMP-028/027). Added strict
script regressions; revised verdict is INCONCLUSIVE, never a fatal PASS.
Unchanged raw evidence: CH6-YELLOW-FATAL/captures, observation-history/0001.json;
fatal-result.json and four fatal-*.png in the session folder. Diagnostic ledger
ch6-fatal-survived-agent-30 does not promote a runtime acceptance axis.

Both private card hashes unchanged. Original game/production codes unchanged.
Accepted integrity audit:90 artifacts,26 raw states,751 hook continuations PASS.
Automated validation:223 tests and450 original signatures PASS.

## CAMP-AI — Original P2 Oscar attack, damage, EXP and weapon use

**PASS, local synthetic-positioning combat**, 2026-10-30. Agent Computer Use
resumed verified private PID72516, CH6-YELLOW-COMBAT. Cancelled inherited Escape
and Move, allowed native positioning, changed original Autoend Turns On ->Off,
then Next Unit found Oscar15,13. Confirmed CURRENT tile, original Attack and his
existing Iron Lance39/45. Original forecast: Archer21HP, Oscar28HP,10 damage x2,
93hit/1crit and no bow counterattack. Saved before.sav, confirmed exactly ONE
attack command, and captured mounted movement continuation before moving/Wait.
R status was tried once there and ignored. No phase advance, repeated attack,
state restoration, game-memory outcome edit or native card write.

Before SHA256 `a51c47baed2ea55f3a1bb20dc548a166a715fb069b2a80b7a0a377e2e6f2c4c1`;
after `294113e5b9306992f5401d315c18f12403dea1e670a878b6432b49b8d01977d3`.
Original C07/internal7, Yellow turn1, live2912-byte fingerprint
`c480776d604082cb`. Oscar remains force3/slot2/PID_OSCAR, HP28/lv6 at15,13;
EXP28 ->45, first Iron Lance uses39 ->37. Archer slot13 stays force1 at15,14,
HP21 ->1. No unrelated roster action delta. Transient EXP bar was **not**
visually captured: original pre-action EXP/uses/forecast are photographed;
post-action damage/gain/consumption are independently decoded from raw states.
This is not a new EXP-bar-display or level-up test.

One original event key, `見つかるトリガ`, changed false ->true. The first review
rejected it under an overly strict no-event-change contract. Pinned original
C07 scene17 then established this precise effect through aligned bytecode/VM
branches (CAMP-027). Only that forward effect in the Chapter6 combat probes is
now admitted and reported. Other flag changes/reversal/wrong chapter still fail.
Native event dispatch and the later discovery presentation remain unverified.
All raw captures/snapshots remain unchanged; no production gameplay code changed.

Evidence: `work/scenarios/human_v1/CH6-YELLOW-COMBAT/captures/`, immutable
observation-history/0001.json, four screenshots and combat-result-v2.json under
`work/agent_runtime_20261029_v1/`. Ledger ch6-yellow-combat-agent-30 accepts an
independent combat lifecycle result, retaining earlier fixture/Escape/Rescue
claims. Natural campaign, chapter completion and Netplay remain untested.

Validation:221 tests PASS (required tests.test_tools51),438/438 signatures;
75 accepted artifacts,24 raw states and693 saved hook continuations rechecked PASS.
Stable2536 and this private2912-byte configuration remain unchanged.

## CAMP-AH — Original Yellow Oscar Rescue of Blue Rhys

**PASS, local synthetic-positioning action**, reviewed 2026-10-30. Codex used
authorized Computer Use/TAS in isolated `CH6-YELLOW-RESCUE/User` (PID146428).
The seed restores an old Escape menu: P2 B cancelled it and B cancelled Move,
allowing native setup to position Oscar13,24 and Rhys14,24. Autoend Turns was On;
P2 changed it Off through original Options. Original Next Unit found Oscar;
CURRENT-tile confirmation offered Rescue. The original target display showed
Oscar Wt33/HP28 and Rhys Wt8/HP22. P2 confirmed Rhys once. Captured the carrying
icon and mounted Move continuation before movement, Wait, Escape or phase advance.
No native card write, fabricated relationship, stat change or outcome edit.

Before SHA256 `ffb0bb56a94273eb26a82562af13a499679fa00683828a3ae5706f6979a8ce0c`;
after `33dc7fc1b2e1057870e881f07a38a84df71d16a1d277217a3611d1b85c24265d`.
Both are original C07/internal7 Yellow turn1 with all2928-byte live hooks matching
`ea5eb5fdbcd75004`. Oscar stays force3, flags10400 ->10402, link802B3564;
Rhys stays force0, flags10400 ->10404, reciprocal link802B1764, coordinates
14,24 ->13,24. Both retain HP/class/level/EXP/inventory/ownership and no death.
No unrelated decoded roster field changes during Rescue.

The first strict review failed its setup comparison: source versus pre-action
unit flags differed only in0x20 on slots10/14/16/17. Original projection code
subsequently established screen-bounds cache behavior (RESEARCH CAMP-026), with
10 newly pinned signatures. The corrected comparison excludes only that bit and
reports every delta; raw states, captured snapshots and declarations remain
unchanged. Regression mutations still reject other flags, force changes, missing
links, altered items/HP/ownership and wrong passenger coordinates. Native-save
and chapter-boundary verifiers do not inherit this exclusion.

Evidence: `work/scenarios/human_v1/CH6-YELLOW-RESCUE/captures/`, immutable
observation-history/0001.json, four screenshots and `rescue-result-v2.json` in
`work/agent_runtime_20261029_v1/`. Ledger `ch6-yellow-blue-rescue-agent-30`
records an independent Rescue lifecycle claim; earlier fixture/Escape evidence
remains accepted and hash-checked. Carried Escape, cleanup, native persistence,
natural campaign and Netplay remain unverified. Follow-up must use this genuine
relationship and original positioning/movement; never fabricate rescue links.

Validation:219 tests PASS (including required tests.test_tools51);438/438
signatures.61 accepted artifacts and22 raw states/635 hook continuations PASS.
Stable2536 bytes and all production generators remain unchanged.

## CAMP-AG — Chapter7 native initialization and P2 Oscar Wait

**PASS, scoped synthetic-history runtime.** On 2026-10-29 Codex used authorized
Computer Use and Dolphin's two TAS panels, with the isolated
`CH7-PLAYER2-CONTROL/User` profile (PID157244). Boot supplied no savestate. The
original title route is **Restart Chapter > Ch.7: Shades of Evil**; original
opening scenes, preparations, Fight/Yes and Blue End reached Yellow turn1.
Autoend Turns was Off. P1 A on Oscar was ignored. P2 selected his CURRENT tile,
opened Items/Wait, then executed the original Wait. No movement, combat, extra
phase, native save or state restoration occurred. The disposable card is unchanged.

Before SHA256 `01aff8ec5cf1c7fe440b8d526b832a38c92ec42b8af6fb6550497806c8a1b10e`;
after `e768b6239dc5ee7f420793edd009684e7d33f1d6a7924d5c754da12e52552eed`.
Both decode original C08/internal8, Yellow turn1, stable2536-byte configuration
`8609ae9f49fd879f`, and independently verified C2 entries/bodies/continuations.
Oscar slot2/PID_OSCAR remains force3, HP28/lv6/EXP28 with identical inventory;
only flags `0x10400 -> 0x10401` changes. The remaining decoded roster and event
flags/scripts match. `Test-Scenario.ps1 -Review` PASS includes explicit agent
attribution, not human observations.

Evidence: `work/scenarios/human_v1/CH7-PLAYER2-CONTROL/captures/{before,after}/`,
immutable observation-history/0001.json and
`work/agent_runtime_20261029_v1/ch7-control-result.json` plus six screenshots.
Ledger `ch7-p2-native-control-agent-29` accepts fixture/event/ownership scope only.
Chapter7 completion, natural campaign history and Netplay remain NOT TESTED.

Tooling validation:218 tests PASS, required tests.test_tools51 PASS,
428/428 signatures.47 accepted artifacts,20 raw states and577 saved hook paths
rechecked. All accepted raw hooks PASS; combined candidate report is INCONCLUSIVE
because the rejected C10 fixture is deliberately refused, rather than silently
omitted. Stable/production codes and Gecko size are unchanged.

## CAMP-AF — rejected Chapter10 ending staging

**FAIL, synthetic fixture; campaign completion INCONCLUSIVE.** Codex launched only
private `CH10-CHAPTER-COMPLETE/User` (PID157136), restored its supplied seed,
confirmed near-exit staging, and saved staged.sav. Original P2 End triggered
the native prison alarm. The staged original guards attacked Green Brom in his
cell; staged/result records show HP28 ->20. The original alarm also spawned Red
reinforcements, including an armor at exit `(6,2)` and units at `(7,2)/(8,2)`.
Result capture is still Red turn1. The trial stopped before Blue Escape or any
chapter outcome; no co-op defect is established.

The old separation test covered staged Blue/Yellow versus six initial Reds, but
omitted native Green prisoners and original reinforcement arrival tiles. Therefore
3216-byte fingerprint `92f0ad0562beaef9` is now refused by both launch checks and
new preparation. Existing seed/profile/captures remain intact. A future corrected
fixture must use a NEW trial, inspect all native actors and alarm/event geometry,
and allow original events without faking discovery, recruitment or completion.

Evidence: staged SHA256
`ebd566c3ec31c653c36f2d7f188f13d8b8b0ccc7a374d1e01c50e6afee353458`;
`work/agent_runtime_20261029_v1/ch10-enemy-interference.sav` SHA256
`60eed92be58d01153ca50ac4a2eb515d47356b96aecc92aa2f6ee85f96322a22`;
paired decoded snapshots and screenshot in the same session directory.
No original card, accepted earlier evidence, production code or ownership logic
was changed. No original Escape/ending/retention was accepted from this trial.

Latest owner-operated result: **CAMP-AC**, synthetic Ch6 Ike-last -> Ch7 preparations
and fresh native Chapter7 Load PASS for survivor/away roster retention.
CAMP-AB records standalone Ch10 Suspend/fresh Resume.
CAMP-Z records original Kieran Escape, CAMP-Y Wait/P1 lockout. Single-command launch/capture
instructions: [SCENARIO_TESTS.md](SCENARIO_TESTS.md).

## CAMP-AE — independent saved hook-path audit, OFFLINE only

2026-10-29. Fixed evidence verification that previously omitted the final C2
return branch. Entry/body/return now must match the expected original continuation;
link/absolute branches, corrupt/truncated payloads and Gecko-area overflow fail.
Scenario reviews re-read raw states and cannot accept a stale cached verification.

New read-only campaign_integrity audit:31 accepted artifacts hash-verified;
18 raw states,521 hooks, all saved entry/body/return paths PASS. Six new candidate
inspections also PASS offline, with runtime NOT TESTED. Existing accepted snapshots
and profiles are unchanged. No production code, Gecko budget or campaign acceptance
axis changed. **This is not a new gameplay or chapter-completion PASS.**

215 tests PASS, including8 new regressions: bad entry/return forms and targets,
payload bounds, raw-state corruption on a disposable copy, exact-fingerprint-only
configuration resolution, missing configuration and cached-true verdict rejection.
Required tests.test_tools51 PASS;428 signatures match;31 accepted artifacts intact.
Two existing manifest tests now mock raw decoding explicitly because their byte
sentinels are not emulator states; actual decoding has a separate mutation test.

Reproduce without launching Dolphin; use a NEW output filename:

```powershell
$py = '..\FireEmblemTwoHouses\.venv\Scripts\python.exe'
& $py -B -m tools.campaign_integrity --include-candidates --out work/scenarios/NEW_hook_integrity.json
```

Next campaign evidence remains the original C11 ending/permanent Kieran retention
and Ch7 P2 battle initialization. The prepared owner-only scenarios are unchanged.

## CAMP-AD — next human-operated batch, OFFLINE preparation only

2026-10-29. **No new runtime PASS.** Six separate candidates pass offline preflight:
CH10-CHAPTER-COMPLETE3216bytes; CH7-PLAYER2-CONTROL2536; CH6-YELLOW-RESCUE2928;
CH6-YELLOW-COMBAT2912; CH6-YELLOW-FATAL2912; CH9-PARTNER-COMBAT2912.
Owner guide: [NEXT_SCENARIO_TESTS.md](NEXT_SCENARIO_TESTS.md).

207 automated tests PASS, including14 new fixture/validator/launcher regressions;
required tests.test_tools51 PASS;428/428 original signatures match. All31 accepted
runtime artifacts still hash-match. Stable gameplay fingerprint8609ae9f49fd879f,
2536bytes, unchanged. No emulator launch/input, original game/save write, accepted
profile/capture modification, production patch change or branch merge occurred.

- Actual accepted sources redecoded, exact source hashes checked. New seeded
  state game fields equal source snapshots; only private C2 layout/hooks and
  documented clean cache valid bits differ. New Chapter7 case boots from its
  copied accepted GCI; source.sav is inspection-only, never a launch argument.
- Original Rescue filter/capacity/pair construction and weapon-use decrement
  paths pinned (RESEARCH CAMP-023). Oscar/Rhys bounded predicates admit the
  candidate,33 versus8; actual original command remains NOT TESTED.
- Compact position/queue execution tests mock native calls and verify guards,
  one-at-a-time Blue queue, blocked destinations, GPR/special-register restoration,
  and refusal to alter stable code. They do not establish runtime setup/AI safety.
- Verdict mutations reject wrong faction/script, lost Kieran, incorrect prisoner
  history, invalid Escape order, inventory/progression loss, absent card-write
  proof, one-sided Rescue links, missing combat EXP/uses and unmarked fatal HP0.
  Human observations remain required; no generated run promotes the ledger.
- Root launcher adds idempotent immutable `-Collect` plus explicit observations;
  listing preserves scoped human PASS even when a changed card blocks seed restore.
  Later original call-site prerequisite report covers six requested areas; all
  remain BLOCKED without matching map/history sources. No unusable profiles made.

Next runtime evidence needed: original C11 ending/permanent Kieran/native load;
Ch7 P2 battle initialization; genuine Rescue before carried Escape; ordinary
Yellow combat and separate death; native Lethe combat. Full campaign, level-up,
healing/status effects, temporary partner cleanup and internet Netplay remain
unverified. The fatal candidate does not force a death; survival is INCONCLUSIVE.

## CAMP-AC — Ch6 completion through native Chapter7 save/fresh Load

**PASS, scoped synthetic sequence and native persistence.** Human clarified that
the earlier next_prep was direct continuation, then saved Chapter7 through the
original game, closed Dolphin and used -FreshBoot with original Load/Resume,
capturing reloaded.sav. Codex collected only the new reloaded capture, preserved
all four earlier bundles, independently decoded the new raw file and matched its
stored snapshot. No emulator launch/input by Codex.

- Reload SHA256:2d44d83b55f51a7d376fc6e6e28a6f7eed46cd236b4a4166fc32b9dbb9c5bd66;
  next_prep:d01eb4effd9660e312f88828ea766ea646fac7b098988adddb5c7a5ea422e453.
  Original loaded C08/internal chapter8 (Chapter7), turn1, Blue/preparations;
  exact live hooks match e60e83a81d994e3b,3168/3248bytes.
- Ike, Oscar, Titania, Rhys and Soren complete decoded records match exactly
  between next_prep and reloaded. Shinon and Gatrie away force7 records also match.
  Oscar remains slot2/PID_OSCAR, HP28/lv6/EXP28 with unchanged nonempty inventory
  across all five captures, including native Load. Blue at prep is expected;
  Chapter7 P2 battle control has not yet been exercised.
- Private GCI changed from immutable b415a97e... baseline to
  99446e1b65ed44ec60e10da9232d5ab894b48a6cc018a8e7eb6fc24445e429ca,
  preserved inside the reloaded capture. Enemy physical unit slots rebuild on
  native Load; no whole-engine/enemy-slot equivalence is claimed or required.
- Evidence: work/scenarios/human_v1/CH6-IKE-COMPLETE/captures/ and exclusive
  native-ch7-load-confirmed-v1.json, containing explicit human checkpoint confirmation.
  Ledger run ch6-ch7-native-load-29 records synthetic local completion, selected
  next-roster initialization and native save/load. Natural chapter_clear/transition
  axes remain untested. Rhys's prior story item addition remains outside the
  Oscar inventory proof; native prep->reload Rhys inventory matches exactly.

The scenario verifier now checks five distinct checkpoints, original scripts/live
codes, four prior escaped allies with unacted Ike at the original exit, five
escaped survivors afterward, retained progression and Oscar items across the
transition, seven exact prep/native-load records, explicit original gameplay/
fresh-load observations and a hash-verified private card write. Mutation tests
reject losses/duplicates, wrong exit/order, altered progression/items, away-unit
revival, stale scripts/hooks and absent native-load evidence. Starting-seed
restoration remains refused after legitimate card changes; fresh native boot is
the supported continuation. 193 offline tests/378 signatures;31 accepted runtime
artifact hashes verified. Netplay, carried Escape and natural campaign remain open.

## CAMP-AB — Original Ch10 Suspend and fresh native Resume

**PASS, scoped standalone native Suspend/fresh Resume.**
The human supplied the original "Saved suspended data. Select Resume Chapter to
continue your game" screenshot, before.sav and after.sav, and declared all five
case observations true. Codex collected the previously missing before file,
preserved the existing after bundle, and independently redecoded both raw states
with exact captured-snapshot matches. Codex did not launch or control Dolphin.

- Before SHA256:d1a4ad28c57cabb68d77ac34de9af99c38bb24a91c26449d963a350d51fecd8a;
  after130c7353b0eecc98c6e2c258b9b5b5d2511520339852a72a0ad96410fbfcbb97.
  Both are C11 turn1 Yellow/human, original complete loaded C11 chain, matching
  live C2 bodies/fingerprintc11089d39a0fe037,3240/3248bytes.
- Oscar slot2 force3 at19,19 HP28/lv6/EXP28 flags401; Kieran slot19 force3
  at20,19 HP30/lv12/EXP0 flags80000. Both full records/inventories preserved;
  Talk key and door/event fields retained. Remaining roster identities retained.
  Two enemy records gain flag0x20 and menu context resets; that bit's native
  serialization meaning is not established by this comparison.
- The immutable pre-test GCI b415a97e9645e83f60bdc7380a2e86dd4686077549c6ce1863e30de6ad51de12
  is unchanged. Active private GCI is now
  b6ad7112c1a9eb5a9c0da48f8c236af706754730d1fcd2113679ed8ec55ec74e,
  also preserved in capture profile copies. This demonstrates standalone card
  writes despite the profile's Netplay WriteSaveData=False setting (CAMP-021).
- Evidence: work/scenarios/human_v1/CH10-NATIVE-RESUME/captures/ and exclusive
  native-save-evidence-v1/ (copied screenshot, hashes and scoped analysis).

The human explicitly clarified that after.sav was captured **after fresh boot
and Resume Chapter**, establishing the previously ambiguous checkpoint. The
earlier provisional save-only analysis remains unchanged; the explicit reply,
observation snapshot and final scoped verdict are retained in exclusive
native-resume-confirmed-v2.json. The narrow native verifier now returns PASS
only with all five human observations, a hash-verified changed private card,
matching original scripts/live codes, identical Oscar/Kieran records and matching
roster identities. Regression mutations reject lost/duplicated units, altered
items/HP/factions/acted flags, stale hooks/scripts, missing flags and absent human
fresh-load evidence. A card write alone remains INCONCLUSIVE.

Campaign run ch10-native-resume-28 records the scoped save_reload/native_save/
native_reload evidence. Synthetic local native persistence does not certify
natural history, permanent recruitment, chapter-transition saving, whole-engine
serialization equivalence or Netplay write-back. Two enemy0x20 flag changes remain
outside this selected-unit claim. 191 offline tests and378 signatures pass;
22 accepted runtime artifact hashes checked.

## CAMP-AA — Synthetic Ch6 Ike-last and Ch7 preparations (2026-10-28)

**Local original Escape sequence/completion/next-roster evidence accepted;
native reload INCONCLUSIVE.** Human supplied before_queue.sav, before.sav,
after.sav and next_prep.sav and declared the original Blue escapes, Ike-last,
completion and Oscar present in the next chapter. Screenshot shows the five
survivors in Pick Units, including Oscar lv6/EXP28/HP28. Codex collected the
three previously uncollected files, preserved the existing after bundle, and
independently redecoded all four bundles with exact stored-snapshot matches.
No emulator launch or input by Codex.

- All four captures match original loaded C07/C08 script chains and all intended
  live C2 bodies, fingerprint e60e83a81d994e3b,3168/3248 Gecko bytes.
- Before_queue: C07 turn2 Blue; Oscar already force5/escaped from the earlier
  genuine Yellow Escape; Titania is at13,26. Before final Escape: Titania/Rhys/
  Soren/Oscar are force5/escaped, Ike is living unacted Blue at13,26.
- After: all five living survivors, including Ike, are force5/escaped. Next_prep:
  internal chapter8 (original Chapter7), loaded C08, turn1, all five retained as
  Blue in preparations. This does not yet demonstrate Oscar's P2 battle control.
- Oscar stays slot2/PID_OSCAR/JID_SOCIALKNIGHT_L, HP28/lv6/EXP28, same complete
  64-byte nonempty inventory across all captures. All five named survivors retain
  unique PID/slot identity, HP/lv/EXP. Rhys has an additional item in next_prep;
  that separate story/item change is not classified as an inventory corruption
  or claimed as an audited grant here. No exact whole-roster item-equality claim.
- Raw SHA256s: before_queue3220c7610b3913a819aafd31e58e260d7d66bfaaeb7a22436687e9b4e630bae9;
  beforea9d91815ce30959763ac4eb7f23db7d4eaa8a286d05af05905a7bb5f8ff5ab64;
  after8c6f855a5f80f2c595400a7ae57799ed3914dad8f189f1ad5ee8b4914616a1e0;
  next_prepd01eb4effd9660e312f88828ea766ea646fac7b098988adddb5c7a5ea422e453.
  Immutable bundles: work/scenarios/human_v1/CH6-IKE-COMPLETE/captures/.

Native load was declared true, but no reloaded.sav exists and the current private
GCI remains byte-identical to the pre-test b415a97e... baseline. Clarification
requested: direct story continuation versus fresh native Load without a state.
No native save/reload acceptance, natural campaign-clear/transition certification,
carried-unit escape or Netplay result. The general review correctly remains
INCONCLUSIVE with missing_captures=[reloaded]; the four collected checkpoints
nevertheless supply the bounded synthetic runtime evidence described above.

## CAMP-Z — Human original Yellow Kieran Escape (2026-10-28)

**PASS, synthetic local original Escape only.** Human reports the correct original
dialogue/animations, and explicitly declares original_escape, p2_command and
no_unexpected_behavior. Review returned PASS with no failures. Codex independently
redecoded both raw capture bundles and matched the stored snapshots exactly;
no Dolphin launch or input by Codex.

- Original loaded C11 complete chain, turn1 Yellow/human control, all intended
  C2 bodies match fingerprintefc52ab6c1471602;3240/3248 Gecko bytes.
- Kieran slot19/PID_KEVIN changes force3 -> force5, flags80000 ->84011, escaped
  false ->true, position6,2 ->6,0. HP30/lv12/EXP0, class, identity and unrescued/
  living status preserved. His64-byte inventory is empty before and after;
  nonempty prisoner inventory persistence remains untested.
- Oscar and Ike records unchanged. Original consumed Oscar/Kieran Talk key stays
  set. No chapter-completion or permanent-recruitment conclusion follows.
- Before raw SHA256:3134870229a43b173745708c78e1d6dfb7bc79028da7edad69fd24959040ca41.
  After raw SHA256:b9a50895bf2136aace6911b3d5295545a7d2ee1826b762ee4dd504cfef2fdeca.
  Immutable evidence: work/scenarios/human_v1/CH10-PRISONER-ESCAPE-v2/captures/.
  Capture analysis commit2563f325dc6d9f6029b018de36fcf61514bfb721; original
  setup package4648a2b. The source saves were found in the similarly named directory
  without-v2 and copied, never moved/overwritten, into the matching case bundle.

No Escape failure demonstrated. The observed endpoints support the bounded native
retention model; the intermediate Blue transfer is inferred from original scripts,
not separately observed. Permanent recruitment still requires original cleanup,
next-chapter roster and native reload evidence. Natural campaign and Netplay
remain untested. Next practical independent test: CH6-IKE-COMPLETE.

## CAMP-Y — Human original Kieran Wait and P1 lockout (2026-10-28)

**PASS, synthetic local original action only.** Human ran CH10-PARTNER-WAIT,
captured before/after, and explicitly declared p1_cannot_command_kieran,
p2_original_wait and no_unexpected_behavior. Review returned PASS. Codex reran
review and independently decoded both preserved raw captures; fresh snapshots
exactly matched the immutable captured analysis. No emulator launch/input by Codex.

- Source package/analysis commit4648a2bb42fa3839323fe84215abb434431bebc4;
  exact live C2 bodies match fingerprintc11089d39a0fe037,3240/3248bytes,
  Dolphin2609a, original loaded C11 complete chain, turn1 Yellow/human control.
- Kieran slot19/PID_KEVIN stays force3 at20,19, HP30/lv12/EXP0; flags80000->80001
  (only acted bit). Class, inventory, rescue state and complete other-unit roster
  unchanged. Oscar slot2 stays force3 at19,19, HP28/lv6/EXP28, flags401.
- Original consumed Talk key remains set; cell door and registered chapter/event
  flags unchanged. Private GCI/profile copies agree in both capture bundles.
- Before raw SHA256:74fb969af738a4f7522bd75cf9c59aad2129b1ecba0f98b14e81ae40f07b75d4.
  After raw SHA256:c3392ae56bc2d0d36fdf96e044b405c1ad60bed137d02c7071d4d9c6ab7e363d.
  Bundles: work/scenarios/human_v1/CH10-PARTNER-WAIT/captures/before|after/.

Scope: P2 can perform original Wait with the talked-to temporary Yellow Kieran;
P1 cannot command him. No permanent recruitment, Escape, chapter cleanup/clear,
transition, native save/reload or Netplay acceptance. Existing campaign dashboard
axes retain their earlier original-Talk evidence; this additional local action is
recorded here and in the immutable case evidence, not substituted for those runs.
Subsequent original Escape result: see CAMP-Z; its scope remains local only.

## CAMP-W — Cross-boundary lifecycle fragments and save audit

After82a5b9c, offline only. Four sequence regressions cover cleanup/availability/
map flags/fixed ownership, original enemy/away priority, no implicit recruit owner,
and ownership mask mutation. Individual owned Escape ambiguity first FAILED
then passed after rejecting duplicate ownership before mutation. Three save-audit
regressions check exact native field/width pins, missing fields, changed ownership
flags and profile sync/write-back distinction without touching source files.
Complete native saving, deployment, reconstruction and Netplay remain unknown.
Original references: RESEARCH CAMP-020/021. No gameplay generator changed.
**177 tests PASS;378/378 signatures and16 accepted runtime artifact hashes
verified.** Native save/reload remains UNTESTED; matching field views alone
remain INCONCLUSIVE.


## CAMP-V — Original campaign transition connection graph

After68cf1a2, offline only. Five regressions cover43 script identities and34
chapter/stage contracts, original aligned call sites, unresolved cross-chapter
gates, special paths/Endgame, and no transitive promotion of runtime evidence.
Graph output in ignored work/campaign_transition_graph_v1.json. Reproduce:
`tools.campaign_graph --path chapter:11 Scripts/C12.cmb [--allow-unresolved]`.
169 tests PASS at the graph checkpoint;360 signatures match.
No accepted runtime artifact changed. Native arithmetic pins and exact scope:
RESEARCH CAMP-019. No gameplay patch or emulator input.


## CAMP-U — Chapter17 prefix contracts and lifecycle acceptance facets

Offline only, aftere2244a1. Original C18 identity pinned. Five stage regressions
execute turn accumulation, guard clear, Red cleanup and next-part openings
before explicit native boundaries; a wrong-reset mutation is detected. Part3
remaining cutscene and full stage4 clear remain unmodeled. Complete18 native
request and BMSetTurn stores pinned (RESEARCH CAMP-018). Snapshot request bytes
never imply current part. Lifecycle facets reuse the existing ledger/evidence;
runtime facets must reference an accepted axis run. Model/blocked classification
regressions prevent promotion. Future capture contracts in
LIFECYCLE_TEST_CONTRACTS.md; no new fixture, GUI or physical action.
A declared cleanup oracle catches six controlled mutations: Yellow loss, guest
retention, item loss, new owner assignment, dead revival and duplicate slot.
**164 tests PASS;355/355 signatures and16 accepted runtime hashes verified.**


## CAMP-T — Native force fragment and bounded unit lifecycle

Offline only, afterece1e2e. Native transfer-status regression first FAILED, then
passed with the pinned original masks. Bounded original-PPC flag executor checks
8x36 inputs and detects an OR mutation. Stateful lifecycle tests distinguish
fixed-owned Yellow from native partners, projected escape/disposal, original
C11 direct recruitment/escape/cleanup branches, dead/away exclusion, duplicate
slots/PIDs and rejection of rescue/unknown native proof. Accepted Talk capture
imports read-only and is preserved. Full native cleanup/save/recruitment remains
unverified. **154 tests PASS** before milestone documentation; original game
addresses and limitations: RESEARCH CAMP-016/017. No emulator or gameplay patch.


## CAMP-S — Jill original directed event regressions

Offline only, after0bae363. Three regressions add64 original C21 scene26/27
cases across directions, force0/3 and explicit relationship inputs0..3. Both
transfer iff neither relevant query equals3; distinct directed records share
a key. Only scene26 explicitly installs its attack sequence. Missing/wrong
actor and repeated key fail selection. Original startup helper executes, native
effects remain modeled. Yellow Jill is hypothetical ownership input; no stable
owner table change or runtime/AI/cleanup/save claim (RESEARCH CAMP-015).
**141 automated tests PASS;316 signatures and16 accepted runtime artifact hashes
verified.** Stable remains2536 bytes; prep2928; private Talk/action fixtures3240.


## CAMP-R — Decoded evidence integrity correction

Afterec74992, offline only. A failing regression demonstrated that manual edits
to snapshot.json were not checked by the collector's raw-state/config hashes:
review still returned PASS. Each NEW capture manifest now pins snapshot SHA256;
review rejects mismatches. A matching digest preserves narrow valid-case PASS.
Legacy bundles missing this field remain readable but INCONCLUSIVE, never
silently upgraded or overwritten. A regression checks both behaviors. Existing
accepted runtime states, artifacts, profiles and ledger claims remain unchanged.
**138 tests PASS;316 signatures and16 accepted runtime artifacts verified.**
This corrects evidence tooling, not gameplay or cryptographic authenticity.

## CAMP-Q — Offline event-state decoder, comparison and coverage scopes

After763e739. Generic current-name-table decoding reuses CAMP-011 signatures;
Ch6 capture has36 names and Ch10 has64. Accepted Talk captures retain identical
local and generic values. Malformed pointers/strings/duplicates produce UNKNOWN,
not false. Original escaped flag is exposed; battle stage remains UNKNOWN.
Comparator regression catches arbitrary new/missing schema fields. Classification
regressions prevent models or copied history from appearing natural. Dashboard
reports blocked prerequisites and rejected diagnostics separately. **137 tests
PASS;316 signatures and16 accepted runtime artifact hashes verified.** No emulator
launch/input, source artifact change, new runtime claim or gameplay patch.


## CAMP-P — Pinned original prisoner event regression model

Offline only, after81c91b3; no Dolphin launch/input or artifact edits. Nine new
regressions execute original C11/startup/C07 bytecode (RESEARCH CAMP-013).
Coverage includes 120 cleanup-prefix cases, original helper faction comparisons,
identity/key/reversal matching, three prisoner direct/carried escape branches,
Ike completion, door keys, wrong-force mutation, missing prerequisites, unknown
natives and instruction bounds. Prefix boundary is required and never invoked.
131 automated tests PASS;316/316 original signatures and16 runtime artifact
hashes verified. Native effects are explicit models; no new gameplay or permanent-recruitment
acceptance. Report command emits24 summary cases, while regression tests cover120.


## CAMP-O — Manual campaign test pack and private post-Talk copies

2026-10-28. Prepared `work/manual_campaign_v1`: 17 targeted cases plus all34
chapter/stage continuity cases from the existing verification ledger. Every
case lists captures, human observations, prerequisites and acceptance limits.
Later missing saves are explicitly blocked; no new runtime PASS is recorded.
Exact user instructions: [CAMPAIGN_MANUAL_TESTS.md](CAMPAIGN_MANUAL_TESTS.md).

Prepared separate `ch10_partner_actions_v1` and `ch10_native_resume_v1`
private profiles/cards under work/fixtures. Both seed copies are byte-identical
to the accepted after-Talk state SHA256
558cfc791b073e8f1cd39f8d7cf3bc85aee95b14e95059c909ce334693ca9a74.
No state edits, positioning, event calls or new codes. All copied source
state/card/config/bindings hashes rechecked unchanged. Both **3240/3248 bytes**,
fingerprintc11089d39a0fe037. Launchers are user-run only; native-resume launcher
omits --save_state. Inherited card identity can make Suspend inconclusive.

tools.campaign_test_pack preserves raw state + intended INI + hashes + snapshot
in new capture directories, refuses replacement and prints output directly.
Only the narrow Kieran original Wait/control case has an automated event
verdict; it requires explicit human observations and matching live codes/C11.
Other complete bundles remain INCONCLUSIVE for event-specific review. No tool
automatically modifies the campaign verification ledger or any source profile.

**122 tests PASS; 316/316 signatures match; 16 accepted runtime artifact hashes
verified.** New regressions reject unit/item loss, stale scripts/hooks, missing
or false controller observations, invalid paths, overwrite and corrupt evidence;
every ledger stage has a case. A complete generic bundle still cannot auto-PASS.
Read-only real-state negative self-check in work/manual_campaign_validation_v1
captured the identical seed twice: live hooks matched, but review correctly
FAILed unchanged hashes/no Wait; recapture correctly refused. This is tooling
verification, not a gameplay execution. No Dolphin launch or input sent.

**NOT TESTED:** Kieran Wait, native post-Talk Suspend/resume, new prisoner escape,
chapter clear/transition and all newly planned runtime cases. Main and paused
draft-ownership untouched. Next user action: CH10-PARTNER-WAIT, then optional
native Suspend attempt; separate geometry-checked prisoner exit setup is needed
before asking the user to test Ch10 escape/cleanup.

## CAMP-N — Human Chapter10 original Oscar/Kieran Talk: local PASS

2026-10-28. User executed the supplied manual test, created before/after captures
and declared `--observed-original-talk`. Codex analyzed files only; no Dolphin
launch/input. Synthetic inside-cell fixture from CAMP-M, original Talk event;
COOP-P6 + EXP-16 + FIXTURE-LOADER + DBG-CAMP-TALK, **3240/3248 bytes**,
fingerprintc11089d39a0fe037. Both captures match live C2 bodies and loaded C11.cmb.

- Before SHA256: e920c5b05c5206aa3d8535469a94b9734e7d13d24077ffd7cff34fc43238b85b.
- After SHA256: 558cfc791b073e8f1cd39f8d7cf3bc85aee95b14e95059c909ce334693ca9a74.
- Oscar slot2/PID_OSCAR remains Yellow at(19,19), HP28/lv6/EXP28;
  flags0x400->0x401. Kieran slot19/PID_KEVIN at(20,19) changes Green2->Yellow3,
  HP30/lv12/EXP0, flags0x80000 unchanged. Both classes/items/rescue unchanged.
- Original `オスカーケビン` key false->true. All roster slot/PID identities
  preserved; no unrelated unit-field changes. Chapter11/turn1/Yellow and human
  control unchanged; actual door object, door keys and completion flags unchanged.
- Initial redirected report falsely rejected Oscar's empty own occupancy while
  selected. Context actor identifies Oscar slot2; original Talk collector checks
  neighboring occupancy, not actor occupancy (RESEARCH CAMP-012). Narrow checker
  correction has negative regressions for wrong/missing actor and missing target.
  Existing captures reanalyzed: **PASS** in `talk-result-verified.json`.
  Original captures and user's first report preserved; no interaction repeat needed.

**114 tests PASS; 316/316 signatures match; 16 accepted runtime artifacts
hash-verified.**

Evidence run ch10-original-talk-14 records state/config hashes. Explicit human
observation remains required; automated state evidence alone is INCONCLUSIVE.
**NOT TESTED:** permanent recruitment, prisoner escape, cleanup, chapter clear,
transition, native save/reload, natural campaign history and Netplay.


## CAMP-M — Inside-cell Chapter10 Talk fixture prepared; runtime pending

2026-10-28. NEW work/fixtures/ch10_oscar_kieran_v1, separate private User/card,
copied source state and append-only Gecko seed. Source is CAMP-L's user-validated
start, never the acted after-Wait state. All31 source-profile files hash unchanged.
No Dolphin launch or input performed. Production definitions/generators unchanged.

Original map, actual closed door object, grid edge/occupancy, original Talk
matcher/menu/action gates and clear named flags inspected first (RESEARCH
CAMP-011). Move only Oscar by original UnitSetPos from(2,19) to empty(19,19),
inside the existing cell next to unchanged Green Kieran(20,19). Door(19,14),
Kieran state/faction, conversation and completion keys are untouched. Hook
guards turn1/humanYellow, source positions/factions, living/no-rescue, Oscar
unacted, clear conversation key and vacant destination. Native calls are
restricted to get flag, PID lookup, empty-position query and UnitSetPos.

**3240/3248 Gecko bytes**, fingerprintc11089d39a0fe037. Seed SHA256
19313403d28362cab55c1bdbb0e0a275570969063be31ceb215043539aee9005.
Regression proves all non-Gecko-tail decompressed bytes match the source; live
execution of the appended hook remains NOT TESTED. No flags/roster RAM edits.

User instructions: CH10_TALK_FIXTURE.md and the prepared directory's README.md /
Launch.ps1. check-setup verifies local fields after manual setup. compare reports
Oscar/Kieran factions/positions/flags/identities plus preserved HP/EXP/items,
unchanged door and original key clear->set. A local Talk PASS requires explicit
human observation; matching state fields without it remain INCONCLUSIVE.

**112 tests PASS; 313/313 signatures match; 13 accepted runtime artifacts
hash-verified.** Synthetic verifier tests do not establish actual Talk availability.
**NOT TESTED:** setup execution, original Talk, permanent recruitment, escape,
cleanup, chapter transition/save/reload and Netplay in this new configuration.

## CAMP-L — Human Chapter10 synthetic fixture and Yellow Wait

2026-10-28 user physical testing report: validated Chapter10 start restored;
original Blue->Yellow transition, P2 Oscar Wait and P1 command lockout PASS,
without unusual behavior. Prison traversal blocked by weak inherited army;
this is a fixture limitation, not a demonstrated co-op defect.

Original script-selection hook (CAMP-010) configuration COOP-P6 + EXP-16 +
FIXTURE-LOADER,2608 bytes, fingerprint5b5f1dfe00ac8959. Both captures match all
intended live C2 bodies and C11.cmb. State fields corroborate chapter11/turn1,
phase0->3/control3=1; Oscar slot2/force3 at(2,19), flags0x400->0x401, same
HP28/lv6/EXP28 and all64 inventory-slot bytes. P1 lockout is human-reported,
not proved by these RAM fields. Source start SHA256c6e2ae86782fc95df14fdba33109629033bbb7e390481b7ee5c25209cf930b8e;
after-Wait f9940810bb053ba6f9b27a035d041cc86a32c63cd37970e3f6cbb80f147a4382.
Evidence run ch10-loader-manual-wait-12 stores artifact hashes/config/card.
Talk, prisoners' permanent recruitment and chapter progression remain NOT TESTED.

## CAMP-K — Loaded event-script identity cross-check

2026-10-28 after72d11a9; read-only analysis of existing captured states, no new
Dolphin action. Pinned original script iterator and SDA root; added bounded
loaded-CMB-chain decoder. Captured Ch6: startup.cmb -> C07.cmb, chapter7.
Captured Ch9: startup.cmb -> C10.cmb, chapter10. Rejected CAMP-J capture:
startup.cmb -> **C07.cmb**, chapter byte**11**. The latter now fails both loaded
script identity and required-prisoner checks. No event acceptance is promoted.

Regenerated Ch6 snapshot passes updated ch6_start.json (now requires C07.cmb).
Ch10 minimum checks now require C11.cmb in addition to the prisoners. Synthetic
regressions cover contradictory chapter identity, malformed headers, invalid
pointers, cycles, chain bounds and missing chains; a local optional regression
reads all three private captures. Missing private captures skip that regression.
Snapshot comparisons include event-container evidence; a missing field in one
snapshot cannot silently compare equal. Header identity does not prove actual
map geometry, activation, natural flags, event completion or Netplay.

**106 tests PASS; 270/270 signatures match; nine accepted runtime artifacts
hash-verified.** Stable gameplay fingerprint remains8609ae9f49fd879f.

## CAMP-J — Restart-card redirect rejected; fixture acceptance hardened

2026-10-28, HEADccc71ac with dirty bootstrap/snapshot tools, Dolphin2609a.
Fresh own profile booted copied native_ch6_card_start.gci; original Restart
Chapter selected Ch6. Stable COOP-P6 + EXP-16 plus synthetic AR source7->11,
2536 Gecko bytes, configuration fingerprint214f6ada685dfde5.

**Fixture FAIL, not co-op gameplay FAIL:** original title remained Chapter6
A Brief Diversion and its forest/bridge map loaded. Captured state chapter byte
was11, phase0/turn1; Ike(13,9), Oscar(14,9), living Emil(13,26) were original
Ch6 units. All stable C2 bodies matched live RAM. Kieran/Brom/Nephenee absent.
`tools.state_expect` with ch10_prisoner_presence.json explicitly FAILS all three
missing PIDs. No Chapter10 conversation, escape, clear or progression was tested.

Diagnostic state work/bootstrap/ch10_from_ch6/diagnostic.s02.sav SHA-256
8528bc530b3210471b7621890d97d2ddffe9ee22edabfebe453f0cffb8442dde;
attempt-config.ini preserves the exact attempted configuration. Rejected attempt
and artifact hashes are in the ledger; Chapter10 fixture stays INCONCLUSIVE.
Both immutable source and new private card retained SHA1
54b5a7f400b9ec68b6e315a0b2b89a78e5b7218d. Only this clone's Dolphin was stopped.

Tool regressions cover read-only GCI input/copy/hash, invalid routes/identity,
budget rejection before creating a profile, explicit synthetic-code provenance,
and refusal to accept the chapter byte when required prisoners are absent.
GCI validation checks directory identity only, not internal checksums/history.
Other routes remain NOT TESTED; the historical EXP-05 transition route does not
establish that a native Restart Chapter can be redirected this way.

**103 tests PASS; 264/264 signatures match; nine accepted runtime artifacts
hash-verified.** Rejected diagnostic state hash independently recorded above.

## CAMP-I — Original Talk eligibility chain, static only

2026-10-28, campaign branch after5487d9a. Read-only `tools.talk_audit` follows
original Talk menu table -> availability -> adjacent occupancy candidates ->
kind8 matcher callback. Table links/direct calls are pinned and regression
checked against the owned image. The reusable direct-call decoder has synthetic
tests for signed, absolute and relative PPC branches, wraparound, non-link b
exclusion and indirect bctrl exclusion. Missing direct callers never excludes
indirect calls. See RESEARCH CAMP-007 and generated TALK_AUDIT.md.

**99 tests PASS; 264/264 signatures match.** Stable production code unchanged.

The inspected local path has no force0-only comparison. Precomputed adjacency
mask production, action/context gates and actual Yellow Talk remain unresolved.
**NOT TESTED:** prisoner event execution, permanent recruitment, chapter cleanup,
save/reload and Netplay. No production gameplay change or new runtime PASS.

## CAMP-H — Stateful-query symbolic tracer correction

2026-10-28, campaign branch after 857261f. Static/tooling PASS: **97 tests**,
**240/240 signatures**, nine runtime artifact hashes verified. No new Dolphin run.

Regression: get(FLAG)==0, set(FLAG), then get(FLAG)!=0 can reach a faction
transfer. The old tracer gave both queries the same expression and could prune
that feasible path as contradictory. Each call now has an offset/visit identity;
only contradictions about the same captured sample can prune a path. Native
calls with VM-local reference arguments invalidate those locals. Constant equality
and nonzero integer branches are folded without assuming arbitrary native effects.
The flag regression also executes independently with the concrete mocked-native VM.

Regenerated C01..31 report: 1507 scenes / 106136 reachable local instructions;
**1338 finished local traces, 169 INCONCLUSIVE** at the same 24-state/1500-step
bounds. Earlier checkpoint counts describe the old tracer and are superseded.
Native state effects, pointer aliases retained by native code, inter-scene calls,
activation and world-state feasibility remain opaque. Finished traces establish
only bounded local analysis, never campaign compatibility or event execution.

## CAMP-G — Original Yellow individual Escape, synthetic positioning fixture

2026-10-28, source HEAD0706896 with dirty analysis/setup tools; Dolphin2609a.
Stable COOP-P6 + EXP-16 plus separate DBG-CAMP-POS setup: **3168 Gecko bytes**,
fingerprint **1c319ccbd9a5d46a**. Production patch generators are unchanged.

The seed is a NEW copy of CAMP-F's Chapter6 start. tools.fixture_state verified
the pinned handler, complete stable GCT list and runtime branch-backs, then
appended only the setup C2 in free Gecko storage. A regression checks all other
decompressed payload bytes remain identical. The setup executes original native
UnitSetPos under chapter7/turn1/humanYellow/position/faction/rescue guards.

**Rejected setup trial:** Emil originally occupies the escape tile (13,26).
First version overlapped him with Oscar; original target selection exposed the
bad fixture. Stopped that process without executing Escape. This is a fixture
FAIL, not a co-op gameplay failure. Corrected setup requires vacant (13,25),
moves Emil there alive, verifies that (13,26) is vacant, then moves Oscar there.
No death/faction/escaped/completion flags or commands are injected.

**Runtime PASS — narrow event:** native Computer Use/TAS port1 ended Blue;
port2 Next Unit located Oscar. Original A selection/current tile produced an
action menu with **Escape**. Selected Escape, changed original confirmation
from No to Yes, observed Oscar's original escape speech, advanced it normally.
The original event removed Oscar from the map; phase cycle reached turn2 Blue.

Before: work/fixtures/ch6_escape_native_v2/before.s02.sav,
SHA-256 a3faa84307fd86e444b10d5a6a62dea9f09c110a7a86db6bd732fa21def9a8d3.
Internal7/turn1/phase3; Oscar slot2, force3, (13,26), HP28, lv6, EXP28,
flags0x10400. Emil force1 at (13,25), HP32.

After: work/fixtures/ch6_escape_native_v2/after.s02.sav,
SHA-256 0da66dbf0ffd922d836976ee765d639df7157466ae3a756cb1a029b2c2f3fe9c.
Internal7/turn2/phase0; Oscar **still slot2**, now **force5**, flags0x14411
(escaped0x4000 set, not dead), HP28/lv6/EXP28 unchanged. All64 bytes of his
eight raw inventory slots match. Emil remains alive/enemy, HP32; Ike remains
on-map. Both captures match ALL intended stable and setup C2 bodies in RAM.
tools.escape_smoke PASS. Private card SHA1 unchanged 54b5a7f4...; no native save
made. Stopped only this clone's Dolphin afterward.

This validates EXP-16's existing single-unit hand-back for this original event
in the synthetic fixture. **NOT TESTED:** original traversal/combat to the gate,
carried units, Ike-last completion, chapter cleanup/transition, native save/reload,
Netplay or EXP-21 ownership. No new gameplay fix was needed or claimed.

Static/tooling: **94 tests PASS**, **240/240 signatures match**; nine runtime
artifact files hash-verified. Actual enabled-INI validation now also rejects
truncated assembly payloads, missing C2 return slots and undefined enabled names,
including generated private fixture INIs, before profile mutation.

## CAMP-F — Native Chapter 6 restart fixture

2026-10-28, clean runtime source 50c2834; private work/runtime/host, stable
COOP-P6 + EXP-16, no debug/redirect codes. Fresh boot loaded the copied NET02
card through original Restart Chapter > Ch.6. Normal Start skipped opening
dialogue, then preparations > Fight > Begin now Yes. Observed original Escape
objective and turn 1. Captured NEW work/ch6_native_start.s02.sav through the UI.

**PASS fixture preconditions only:** internal7/phase0/turn1; Ike, Titania, Rhys,
Soren Blue; Oscar Yellow; Shinon and Gatrie force7; Boyd absent. Ike lv10/44EXP,
HP26 at (13,9); Oscar lv6/28EXP, HP28 at (14,9). All intended C2 bodies match RAM.
tools.state_expect with campaign/fixtures/ch6_start.json PASS. It rejects lost,
duplicate or wrongly transferred expected characters and unknown expectation keys.
It checks listed fields, not a whole game's consistency or event success.

State SHA-256 5f5b35af05abd05df810d7bc3a96161ed6ae687c8b8596b1f47c4311a1a98ef7.
Private card SHA-1 unchanged before/after:
54b5a7f400b9ec68b6e315a0b2b89a78e5b7218d. An immutable ignored copy is preserved
as work/saves/native_ch6_card_start.gci. No card save was made. Only private
Dolphin was stopped; personal/source profiles and cards were untouched.

Class: native_restart_from_copied_card_history_partly_documented. The restart
path itself used no state edits or redirect, but earlier card history includes
debug-assisted development tests. This is not a natural-progression certificate.
Oscar's owner-flag fields are unset because EXP-16 uses a fixed PID table, not
EXP-21's saved flag bits. No ownership loss is inferred from those fields.

**Escape menu/event, roster preservation, clear, transition and native save/reload
remain NOT TESTED.** This fixture removes the need to manually replay Chapters1–5
for that investigation. Current validation: 89 tests PASS, 222/222 signatures;
six local runtime artifacts hash-verified.

## CAMP-E — Chapter 9 native-partner transformation and port-2 Wait

2026-10-28. Isolated runtime at clean source commit 0fcaa64, Dolphin 2609a,
COOP-P6 + EXP-16 fingerprint 8609ae9f49fd879f; no debug codes. Restored the copied
historical EXP-05 work/saves/GFEE01.s06_ch9_fixture. **Synthetic redirected history**,
not a naturally progressed campaign. Private profile work/runtime/host only.

Native Computer Use/TAS port 1: Map Menu > End advanced Blue -> Yellow. The
original Transformation tutorial Yes/No appeared. TAS port 2 moved the choice to
No and confirmed it (normal tutorial option); Lethe transformed into a cat.
Port 2 selected Lethe, confirmed her original tile and chose original Wait.
Observed her grey acted sprite while Mordecai remained available. Paused and
captured new before/after state files using Save State to File. No card save made.
Stopped only the isolated process afterward.

**PASS, narrow native-partner smoke:** both captures are internal chapter 10,
turn 1, phase 3, control[3]=1. Lethe is force 3, unassigned, JID_CAT/F, gauge20,
HP34, lv3, EXP0, (25,18). Only her captured flags change 0x80000 -> 0x80001.
Mordecai remains force 3, unassigned, JID_BEAST_T, gauge4, HP41, (24,18), flags
0x80000. All other captured game fields are identical; all intended stable C2
bodies match live RAM before/after. `tools.partner_smoke` PASS.

Before: work/ch9_yellow_before.s02.sav,
SHA-256 54f141736b839b4c1c09cf8944a9fde4c08defacf91285b3b7f0ced2c82a3af5.
After: work/ch9_yellow_after.s02.sav,
SHA-256 4e57bd16d676cda66e7ddf8f935e8928dda1dac2a9b1c44b0840fa54f65b3676.
`tools.campaign_verify --check-artifacts` verifies all four current runtime files.

NOT TESTED here: combat EXP, full transformation depletion/reversion, explicit
negative cross-control, end-phase leftover behavior, recruitment, cleanup,
chapter clear/transition, native save/reload or Netplay. The tutorial prompt
responding to port 2 is an observation, not full controller isolation coverage.

Static/tooling validation after adding this smoke verifier: 87 tests PASS,
222/222 signatures match. No production patch/generator changed.

## CAMP-D — conversation metadata and evidence scope

2026-10-28. Static/tooling: 86 tests PASS; 222/222 original DOL signatures match.
Decoded original kind-8 actor/target PID records, reversible direction and shared
event keys. Regression cases: Oscar/Kieran, Astrid/Gatrie, opposite Jill/Shiharam
initiators. These are matching records, not proof the Talk menu or recruitment
works for Yellow. Original matching query has no unit-force read; upstream target
eligibility remains open (CAMP-004).

Evidence validation rejects the wrong chapter/stage or axis and rejects missing or
changed local runtime artifacts. `tools.campaign_verify --check-artifacts` verified
both recorded Prologue state files. Campaign matrix runtime columns now read the
same validated ledger as VERIFICATION.md; the inventory no longer invents a
separate all-untested status. No additional Dolphin run is claimed in this checkpoint.

## CAMP-C — Escape tile metadata, fixture safety and original Wait action

2026-10-28, isolated campaign clone. **83 tests PASS**, 209/209 signatures match.
Suite: tests.test_tools, tests.test_campaign, tests.test_dol_patch,
tests.test_verification, tests.test_fixture_safety. New coverage: original kind-5
Escape tiles, all-container native-call cross-reference, bounded MEM1 edits,
exclusive state writer, existing-manifest protection and private bootstrap profiles.

**Runtime PASS, narrow Prologue Wait smoke:** native Computer Use, private
work/runtime/host, Dolphin 2609a, stable COOP-P6 + EXP-16 fingerprint
8609ae9f49fd879f. TAS Input port 1 persistent A selected Ike, confirmed the current
tile; Main Stick selected Wait; A executed it. Observed enemy-phase Boyd dialogue.
Paused and saved a NEW work/runtime_wait.s02.sav through the GUI. Original card
and source states were not written. Stopped only the isolated Dolphin process.

Before hash: 8728032b2d3dd931cbcd5889ae4ca59448fb1fdfdbcd56b1be0130ef812d1733.
After hash: 6e1115df705c8d7031fd5df60398b93a41ac3adbd4ce6dbcec27f468a55839f5.
tools.prologue_smoke PASS: chapter 1/turn 1, phase 0 -> 1; Ike still force 0,
(3,9), HP19, lv1, EXP0. Both snapshots match ALL intended stable C2 bodies in RAM.
Raw flags 0x80500 -> 0x80520; this delta is not asserted to be the acted bit.

This demonstrates an original action through observed GUI automation and state
verification. It does not accept Yellow control, chapter clear, transition,
gameplay save/reload or Netplay. DTM synthetic-input action remains INCONCLUSIVE.
Reproduction and synthetic later-chapter workflow: FIXTURES_AND_AUTOMATION.md.
Four new bootstrap profiles exist but are NOT TESTED runtime fixtures.

## CAMP-B — CFGs, script models, evidence gates and offline DOL proof

2026-10-28, isolated campaign branch. Latest validation: 77 tests pass across
tests.test_tools, tests.test_campaign, tests.test_dol_patch, tests.test_verification;
193/193 signatures match. Tests cover all 2075 scene CFGs, signed operands,
Jill/Reyson guards, four Ch6 escape cases with mocked natives, native registration
recovery, synthetic DOL hook/return construction, and rejection of unsupported
gameplay/Netplay claims. These are static/tooling passes.

Runtime: native DTM playback restored the copied Prologue scenario. The UI
Emulation > Save State > Save State to File flow produced
work/runtime_observe.s02.sav (the dialog appended .sav). Decoding confirms
chapter 1 / phase 0 and original Ike state. Snapshot inspection matched ALL
intended stable COOP-P6 + EXP-16 C2 bodies in live RAM, fingerprint
8609ae9f49fd879f. Merely reading an intended INI is no longer enough: snapshot
reports contain live hook/body observations and intended_c2_verified.

Still INCONCLUSIVE: synthetic movie A input did not demonstrate unit selection
or a completed action. The isolated process was stopped. No later chapter,
objective, transition, gameplay save or Netplay result is claimed here.

The DTM prototype requires an existing project recording's settings header;
minimal settings caused a region/config warning. It refuses existing destinations
and clears disc-change/card-clear flags. Tests validate format and file safety,
not gameplay. Original recordings/states were read only.

Generated artifacts: CAMPAIGN_EVENTS.md, VERIFICATION.md, campaign/verification.json.
Offline executable migration findings and synthetic-only proof: NATIVE_PATCHING.md.

## CAMP-A — isolated campaign/tooling milestone (2026-10-28)

Clone `FireEmblemCampaignAudit`, branch `codex/campaign-compatibility`, baseline
`10d2496`. Handoff snapshot read from source commit `53fc0b6`.

| Check | Result | Scope |
|---|---|---|
| `python -B -m unittest tests.test_tools tests.test_campaign` | PASS, 64 tests | Static/tooling, including copied baseline-state decoding; not gameplay |
| `python -B -m tools.check_signatures` | PASS, 184/184 | GFEE01 rev 0 original DOL instructions/data |
| `python -B -m tools.verify_game --skip-file-hash` | PASS | GFEE01 rev 0; DOL SHA-1 9d00d7d407750b82cb1cfccc56f8aa8a89cc8851 |
| `python -B -m tools.campaign_audit` | PASS | 31 chapter IDs, 43 script containers, suffix maps, message-derived names |
| `python -B -m tools.netplay_package --out work/stable-client-regression.zip` | PASS | Package validation/reproducibility suite; stable enabled fingerprint still 8609ae9f49fd879f |
| Oversized library/package/installer rejection | PASS | No invalid config emitted; installer sentinel and backup untouched |
| Oversized `netplay_setup --force` | PASS | Temporary sentinel card preserved; validates before deletion |
| Isolated Dolphin boot | Observed title sequence | Separate executable/image/profile/card only |
| Campaign runtime, objective, clear, transition, save, Netplay | NOT PERFORMED | Synthetic key taps did not reliably operate menu; snapshot hotkey produced no fixture |

Interpreter: existing Python 3.12.6 venv executable used with `-B`; installed
Capstone metadata 5.0.9 differs from requirements pin 5.0.7, LZ4 4.4.5. No install
or environment modification. Outputs and runtime copies are ignored in this clone.

Handler measured 2880 bytes, SHA-256
2b2ff0716aeb9b806cc61181e559041312957f25f04c435bd7da80a78917b33b.
See CAMPAIGN_FINDINGS.md for limitations, GECKO_AUDIT.md for storage accounting,
CAMPAIGN_MATRIX.md for separate chapter evidence axes. No gameplay patch changed.

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
| 2026-10-27 | `unittest tests.test_tools` | 41/41 pass (adds `NetplayPackageTests`: client ZIP contents, reproducibility, rejection, fingerprint, PowerShell match) |
| 2026-10-27 | `netplay_package` | ZIP built and verified: 8 files + empty card folder, 11.5 KB, fingerprint `7031af10d740f4ed` |
| 2026-10-27 | `netplay_package` (net02-2, no launcher) | ZIP built and verified: 5 files + empty card folder, 7.3 KB; `Get-FileHash` of the extracted code file equals the README value; tests 40/40 |

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
| 2026-10-27 | Claude (computer use) | **FAIL: no EXP** | Installed COOP-P1 + EXP-10 with Dolphin closed and loaded slot 6. Ended turn 1 (Lethe gauge 20 → transformed by turn 2). At the turn-2 yellow phase, Lethe's status showed `EX --`, both in the player phase and in the yellow phase with `control[3]=1`. In the yellow phase Lethe (cat, Lv 3) attacked the Lv 13 swordsman at (23,24) from (23,23) and killed him (forecast 18×2, 100 % hit, 27 HP). **Slot 4** (pre-confirm, backup `work/saves/GFEE01.s04_exp10_pre`, SHA-1 `fc6f3a43…0cce`) and **slot 5** (after battle, `work/saves/GFEE01.s05_exp10_post`, SHA-1 `35783b84…5f34`): both decode as phase 3, turn 2, control `1 2 2 1`. Lethe is **lv=3 exp=0 in both** (gauge 17→16, flags bit 0 set = acted), Mordecai lv=2 exp=0 in both, and the swordsman is gone in slot 5. The status screen still shows `EX --` after the kill. I saw no EXP bar, though a 3 s gap between screenshots could have missed one; the unchanged EXP byte settles it. Slot 4 RAM shows the hook is live (`0x8003D180` = `4BFC5258`, a branch to the code handler), so a missing patch isn't the cause. Questions c/d/e were not reached. **Cause found statically (F-23):** `GetExp` (`0x800386B0`) returns `0xFF` for force 3, so CanGainExp fails at `0x8003D1A8` even after EXP-10. Fix: EXP-11. Side observation: in the yellow phase, Next Unit (X) moved the cursor to Ike (blue). I didn't try to select him. Old slots 4/5 are backed up in `work/saves/pre_exp10/`. `inspect_state` now prints `lv`/`exp`/`gauge` per unit (F-22 offsets). |

## EXP-11 — GetExp lets human-controlled yellow units have EXP (with EXP-10)

**Cause (static, F-23):** `GetExp(unit)` (`0x800386B0`) reports `0xFF` ("--") for forces 1/2/3. CanGainExp treats that as "no EXP", and so do the status screen and AddExp.
**Change:** Gecko `C20386C8` hook (annotated in `codes/GFEE01.ini`). A force-3 unit reads its real EXP byte **only while `control[3] == 1`**. CPU yellow armies are unchanged. Static check: `test_exp11_gecko_hook`, 45/45 signatures.

Steps (same as EXP-10, from slot 4 = the saved pre-attack forecast):
1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable COOP-P1 --enable EXP-10 --enable EXP-11
   ```
2. Boot the game and load **slot 4** (the forecast for Lethe vs. the swordsman at (23,24), turn 2, yellow phase). Optionally restore it first from `work/saves/GFEE01.s04_exp10_pre`.
3. Before confirming, back out to the map, then open Lethe's status screen: does `EX` show `0` instead of `--`? Return to the attack and confirm it.
4. After the battle, save to **slot 5** and decode both slots: `exp` for Lethe should be > 0 in slot 5. An EXP bar should appear after the battle.
5. If possible, also check d (an enemy-phase counter gives EXP) and e (blue units still gain EXP).

**Success:** Lethe's `exp` increases and the status screen shows a number. **Failure modes:** still 0 (yet another gate; trace AddExp `0x800351FC` with a breakpoint), a crash at the EXP bar, or wrong EXP on CPU-controlled yellow units in vanilla chapters.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | Claude (computer use) | **PARTIAL: EXP calculated, not kept** | Installed COOP-P1 + EXP-10 + EXP-11 with Dolphin closed. **Loading the EXP-10 slot 4 did not apply EXP-11** (`0x800386C8` still held the original instruction; F-25), so I replayed from **slot 6** (both hooks live, peeked via scratch slot 8, old slot 8 backed up in `work/saves/pre_exp10/`). Same inputs as EXP-10: Lethe's status read **`EX 0`** (was `--`) in the turn-1 and turn-2 yellow phases. Turn-2 yellow phase: same forecast vs. the swordsman at (23,24); saved **slot 4** (`work/saves/GFEE01.s04_exp11_pre`, SHA-1 `59940a65…3b79`) and confirmed. He hit once (Lethe 34→30) and died. **An "Exp" bar appeared, showing 15.** **Slot 5** (`work/saves/GFEE01.s05_exp11_post`, SHA-1 `8e5f1d60…3dd`): Lethe's unit lv=3 **exp=0** and status `EX 0`, but the battle copy at `0x80330EAC` has exp 15 and gain `+0x2C9` = 15. **Cause (F-24):** the battle write-back `0x80034F40` copies level/EXP back only for force 0/5. Fix: EXP-12. Questions c/d/e were not reached. |

## EXP-12 — Battle write-back keeps yellow EXP (with EXP-10 + EXP-11)

**Cause (static + runtime, F-24):** `0x80034F40` writes level and EXP from the battle copy back to the unit only for force 0/5.
**Change:** Gecko `C2034F68` hook, the same cave as EXP-10. Static check: `test_exp12_gecko_hook`, 50/50 signatures.

Steps:
1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable COOP-P1 --enable EXP-10 --enable EXP-11 --enable EXP-12
   ```
2. Boot the game and load **slot 6** (not slot 4: a state saved with codes restores the old code list, F-25).
3. End the player phase (map menu → End). In the yellow phase, end the phase. In the turn-2 player phase, end the phase.
4. Turn-2 yellow phase: Lethe → (23,23) → Attack → Claw on the swordsman at (23,24). Save **slot 4** at the forecast, confirm, then save **slot 5**.
5. Decode both. Lethe's `exp` should be > 0 in slot 5 (15 last time), and the status screen should show the same number.
6. If you can, also check c (level-up at 100), d (an enemy-phase counter gives EXP) and e (blue units still gain EXP).

**Success:** the unit's `exp` byte keeps the battle gain. **Failure modes:** still 0 (another write-back path; trace stores to `+0x19B` with a breakpoint) or a crash at the EXP bar or level-up.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | Claude (computer use) | **PASS (a, b)** | Installed COOP-P1 + EXP-10 + EXP-11 + EXP-12 with Dolphin closed, then booted and loaded slot 6. All three hooks are live in scratch slot 8 (`0x8003D180` = `4BFC5258`, `0x800386C8` = `4BFC9D40`, `0x80034F68` = `4BFCD4D0`). I replayed with the same inputs; the turn-2 yellow position was identical (swordsman at (23,24)). The forecast showed `EX 0`. Saved **slot 4** (`work/saves/GFEE01.s04_exp12_pre`, SHA-1 `24db47a7…d362`), confirmed and killed him. This time he missed (Lethe HP 34). **(a) An "Exp" bar appeared** after the battle. **Slot 5** (`work/saves/GFEE01.s05_exp12_post`, SHA-1 `21fd8470…7203`): **Lethe lv=3 exp=0 → exp=15** in the unit record, matching the battle copy (`+0x2C9` = 15). **(b) The status screen shows `EX 15`.** Ike (blue) is unchanged at lv 2 / exp 67 (he didn't fight). c (level-up), d (enemy-phase counter) and e (blue units still gain EXP) are **not yet tested**. |

## EXP-13 / COOP-P2 — Progression regression on the packaged code

**COOP-P2** = COOP-P1 + EXP-10 + EXP-11 + EXP-12 + EXP-13, one Gecko code (`test_coop_p2_package`: identical lines, no duplicate hook address). **EXP-13** (F-26) fixes the level-up crash found in check 3. Install with Dolphin closed:
```bash
.venv/Scripts/python -m tools.install_codes --enable COOP-P2
```
Always start from **slot 6** (F-25). Replay inputs for Ch9 (about 2.5 min): End → *Transformation tutorial: No* → End (yellow) → Lethe's conversation (Start skips it) → *Direct tutorial: No* → End → turn-2 yellow: Lethe (25,18) → (23,23) → Attack → Claw on the swordsman (23,24). Fixtures: `work/saves/GFEE01.s04_coopp2_pre` (forecast, COOP-P2 incl. EXP-13 in RAM, SHA-1 `44fec0b8…c756`) and `work/saves/GFEE01.s08_lvlup_fixture` (the same state with Lethe EXP patched to 95 via `patch_state --set 802B54FF=5F`, SHA-1 `696943b9…817e`).

| # | Check | Result (2026-10-27, Claude, computer use) | Evidence |
|---|---|---|---|
| 1 | Kill EXP (yellow phase) | **PASS**: Lethe exp 0 → 15, EXP bar shown | COOP-P2 without EXP-13, slot 5 decode |
| 2 | Counter EXP (enemy phase) and accumulation | **PASS**: Lethe 15 → 27 after countering and killing the soldier (20,25) in the turn-2 enemy phase; 0 → 15 → 27 over two phases | `work/saves/scratch/GFEE01.s07_p2_turn3` (SHA-1 `ae6d2114…7ec1`, turn 3) |
| 3 | Level-up (100 EXP), **without EXP-13** | **FAIL**: as the bar passed 100, Dolphin reported *Invalid read from 0x0000018C, PC = 0x801B5E6C*, then *0x0000019A, PC = 0x801B5E90* (a NULL unit in the level-up screen). Cause: F-26 | screenshots; `work/saves/scratch/GFEE01.s08_lvlup_fixture_oldcodes` |
| 3b | Level-up **with EXP-13** (COOP-P2) | **PASS**: "Level Up!" banner, no warning; unit lv 3 → 4, exp 95 → 10, growth bytes `+0x1AB`, `+0x1AE`–`+0x1B2` 0 → 1, max HP 34 → 35; the status screen shows Lv 4, EX 10. I didn't capture the stat-gain panel in a screenshot (3 s gaps), so the *presentation* isn't confirmed yet | `work/saves/GFEE01.s05_coopp2_lvlup` (SHA-1 `ceaddf10…c47c3b`) |
| 4 | Blue EXP unchanged | **PASS**: Ike 67 → 68 (attacked and missed, turn-3 enemy phase), then 68 → 80 attacking the mage at (22,21) in turn 4. A blue level-up was not run at runtime (EXP-10..13 only change the force-3 path; static) | `work/saves/GFEE01.s08_coopp2_ike_attack` (SHA-1 `398f54d8…0090`) |
| 5 | Vanilla with codes disabled | **PASS**: `install_codes` with nothing enabled, slot 6. The partner phase ran under the AI (no cursor; Lethe/Mordecai moved (25,18)/(24,18) → (22,24)/(23,24) and fought), control = `1 2 2 2`, and every hook site held its original instruction (`0x8014D3B4`, `0x8003D180`, `0x801B610C`). Lethe exp stayed 0 (vanilla: no partner EXP) | `work/saves/GFEE01.s08_vanilla_t2` (SHA-1 `461034b4…1fa1`) |
| 6 | Ownership: Next Unit in the yellow phase | **Cosmetic only**: X cycles the cursor through **blue units only** (Ike → Mist → Rolf → Ike), never Lethe or Mordecai. Pressing A on Ike does nothing (EXP-06 blocks it; the button hint still says "Move"). No cross-control | COOP-P2 run, turn 1 yellow |
| 7 | Ownership: Ike's **Direct** command | Observed in Ike's menu (Items/Order/Direct/Wait). It is vanilla's way of setting the partner AI's orders. With human yellow it should have no effect; **not yet tested** | turn 3/4 screenshots |

Not yet covered: the stat-gain panel itself, save/load across a real battle save (F-13 says control bytes are saved), healing EXP and promotions (no yellow healer or promotable unit in this fixture).

**Phase 1 status:** the core interaction is achieved on one controller, now including progression (COOP-P2, table above). The yellow army is human-controlled in its own phase, the blue army in its own, with no cross-control in either direction.

| Date | Tester | Result | Notes |
|---|---|---|---|
| — | — | NOT RUN | blocked on Ch9 fixture |

## EXP-14 / COOP-P3 — Controller port 2 drives the yellow phase (Phase 2)

**Change (F-29):** the game reads all gameplay input through one "current pad" pointer (`0x80367240` = `r13-0x7B60`). EXP-14 (C2 hook at the pad-update epilogue `0x80025B8C`) points it at **pad object 1 (port 2)** while `phase == 3 && control[3] == 1` and port 2 has a controller, and at pad object 0 (port 1) otherwise. **COOP-P3** = COOP-P2 + EXP-14 (`test_coop_p3_package`). Static: `test_exp14_gecko_hook`, 73/73 signatures.

Tools: `tools/setup_pads.py --port2 keyboard|device|none` sets Dolphin port 2 (`[Core] SIDevice1`) and, for `keyboard`, a second key layout on the same PC: **A=M B=N X=B Y=V Z=E Start=Y, stick numpad 8/5/4/6, L=O R=P** (top-row 8/5/4/6 until 2026-10-27; Dolphin names the keypad keys `NUMPAD8` etc., F-33). Port 1 keeps X/Z/C/S/D/Enter/arrows. It backs up `Dolphin.ini`/`GCPadNew.ini` to `*.ini.bak` and refuses to run while Dolphin is open.

### Local run (2026-10-27, Claude, computer use; two keyboard-emulated pads on one PC, codes COOP-P2 + EXP-14)

| Test | Result | Evidence |
|---|---|---|
| A. Port 2 = None (Dolphin default), human yellow phase | **PASS (fallback)**: PADStatus[1].err = `0xFF`, current pad stays at object 0, port 1 moves the yellow cursor as before. A single-controller setup cannot softlock | slot 8 peek at 03:23 |
| B1. Player phase, port 2 input | **PASS**: port 2 stick/A did nothing; port 1 moved the cursor, moved Ike and chose Wait, then ended the phase via the Z menu | screenshots |
| B2. Yellow phase prompt (Transformation tutorial) | **PASS**: port 1 right + A ignored; port 2 moved to *No* and confirmed | screenshots |
| B3. Yellow phase, port 1 input | **PASS**: port 1 stick/A/Z ignored (no movement, no menu) on turns 1 and 2 | screenshots |
| B4. Yellow phase, port 2 control | **PASS**: port 2 selected Lethe, moved her, chose Wait; selected Mordecai, chose Wait; opened the map menu (Z) and chose End, both turns | screenshots; `work/saves/GFEE01.s08_exp14_yellow_port2` (current pad = `0x802EF45C`, SHA-1 `d7042611…fecd`) |
| B5. Turn-start conversation after the yellow/enemy phases | **PASS**: port 2 Start ignored, port 1 Start skipped it | screenshots |
| B6. Two full turns, ownership kept | **PASS**: turn 3 reached, current pad back to `0x802EF438`, Mordecai gained 1 EXP in the enemy phase (progression still works) | `work/saves/GFEE01.s08_exp14_turn3` (SHA-1 `bc582e96…3972`) |

The Dolphin config was restored afterwards from `work/saves/config_backup/`. Not covered yet: attacks and battle animations driven by port 2, the Start/pause menu in the yellow phase, a real second device (gamepad), and a chapter that ends during the yellow phase.

### Two-controller test for the tester (real devices)

1. Close Dolphin. Run:
   ```bash
   .venv/Scripts/python -m tools.install_codes --enable COOP-P3
   ```
   ```bash
   .venv/Scripts/python -m tools.setup_pads --port2 device
   ```
2. Open Dolphin → **Controllers**: Port 1 = Standard Controller mapped to device 1 (keyboard or pad), Port 2 = Standard Controller mapped to **a different device** (for example an XInput gamepad). Don't map the same device to both.
3. Boot the game and load **slot 6** (not a state saved with other codes; F-25).
4. Player phase: on **controller 2**, try to move the cursor and press A on Ike. Expected: nothing happens. On **controller 1**: move Ike, then Wait, then map menu (Z) → End.
5. Yellow phase: on **controller 1**, try the cursor, A, Z and Start. Expected: nothing. On **controller 2**: answer any tutorial prompt, move Lethe next to an enemy, **Attack**, watch the battle (try skipping the animation with controller 2), Wait with Mordecai, then Z → End.
6. Repeat for at least two more turns. On turn 2 or 3, also open the **Start menu** with controller 2 in the yellow phase, then with controller 1 in the player phase.
7. Save state to **slot 9 or 8** (not 1 or 6) at any surprise, and note which controller you pressed.
8. Afterwards: `.venv/Scripts/python -m tools.setup_pads --port2 none` (or restore the `*.ini.bak` files) to return to one controller.

**Success:** each army only answers to its own controller for every action above, over 3+ turns. **Failure modes to report:** a prompt that only one controller can answer when it shouldn't, input "leaking" for one frame at phase changes, or the Start menu in the yellow phase answering to controller 1.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user | **PASS** | Two keyboard-emulated controllers (`setup_pads --port2 keyboard`, stick then on top-row 8/5/4/6): blue answered only to controller 1 and yellow only to controller 2. Usability issue: the port 2 stick should be on the numeric keypad, now changed (F-33). Still open from the list above: attacks/animation skip and the Start menu on controller 2. |

**Numpad recheck (tester, 30 s):** with Dolphin closed run `.venv/Scripts/python -m tools.setup_pads --port2 keyboard`, open Dolphin → Controllers → Port 2 **Configure**, and press numpad 8/5/4/6 with Num Lock on, then off. Expected: the Control Stick dot moves up/down/left/right both times. Not run yet.

## Phase 3 — Netplay

**Facts so far (F-31, F-32):** Dolphin refuses to load save states during Netplay, and a Suspend made from the slot 6 state is rejected ("not the original Memory Card"). So a Netplay session starts from a **memory card**. `tools/netplay_setup.py` makes two private Dolphin user folders (`work/netplay/host`, `work/netplay/client`, launched with `--user`). `Dolphin-x64/User` (your card, states, config) is never used.

| Folder | Player | Pad 1 keys (its own port 1) | Codes | Card |
|---|---|---|---|---|
| `work/netplay/host` | P1-Blue | X/Z/C/S/D, Enter, arrows | COOP-P3 (synced to client) | Chapter 9 card (NET-00) |
| `work/netplay/client` | P2-Yellow | M/N/B/V/E, Y, numpad 8/5/4/6 | none (receives host's) | empty (receives host's) |

Both have Background Input on, so two windows on one PC can share one keyboard. Netplay settings are preset: direct connection, 127.0.0.1:2626, sync saves and codes, and save data discarded at session end.

### NET-00 — Chapter 9 memory-card start (2026-10-27, Claude, computer use; user healed Ike in the Greil fight)

| Step | Result |
|---|---|
| Suspend in the slot 6 state, host card | **FAIL (expected after the fact):** "This is not the original Memory Card…" (F-31 b) |
| Fresh boot in `work/netplay/host`, codes COOP-P3 + EXP-05, New Game (Easy, file 1), win the Prologue, save at the prompt to **file 2** | **PASS:** the card holds "Prologue: Mercenaries" (file 1) and **"Ch. 9: Gallia"** (file 2). A state at the base (`work/netplay/host/StateSaves/GFEE01.s02`) decodes as chapter id 10, turn 1, Ike Ranger lv 3 |
| Fresh boot, codes COOP-P3 only, Title → **Restart Chapter → Ch. 9** | **PASS:** the Chapter 9 base menu appears, with no save state involved |
| Base → End → first player phase with Lethe/Mordecai yellow | **PASS (user, 2026-10-27):** from the card start (one instance, no Netplay), Lethe and Mordecai appeared as yellow units and were controllable in the yellow phase |

Card backup: `work/saves/netplay_ch9_card/01-GFEE-FIREEMBLEM8J.gci` (SHA-1 `d93a22ae26227976a7a07c2097aca713f0899086`). `netplay_setup` copies it into the host card. The user's card (`7afef93c…`), slot 1 (`b8a42f43…`) and slot 6 (`d8430d71…`) were unchanged afterwards. To remake the card: `install_codes --user work/netplay/host --enable COOP-P3 --enable EXP-05`, then repeat the row above.

### NET-01 — First Netplay session, two instances on one PC (tester)

1. Close all Dolphin windows. Run:
   ```bash
   .venv/Scripts/python -m tools.netplay_setup --force
   ```
   (`--force` recreates both folders; the host card is restored from the backup.)
2. Start both instances (two terminals):
   ```bash
   Dolphin-x64/Dolphin.exe --user work/netplay/host
   ```
   ```bash
   Dolphin-x64/Dolphin.exe --user work/netplay/client
   ```
3. **Host window:** Tools → **Start NetPlay…** → **Host** tab → select *Fire Emblem: Path of Radiance*, port 2626, direct connection → **Host**.
4. **Client window:** Tools → Start NetPlay… → **Connect** tab → IP `127.0.0.1`, port 2626 → **Connect**.
5. In the host's NetPlay dialog:
   - Save data: choose the mode that **loads the host's save data and discards changes** ("Write Save Data" off).
   - **Sync AR/Gecko codes** on.
   - **Pad mapping:** GC port 1 = P1-Blue, GC port 2 = P2-Yellow, ports 3 and 4 empty.
   - Note the Dolphin version shown for both players.
   - Click **Start**.
6. In the game: Title → **Restart Chapter → Ch. 9** → base → **End → Yes**. Skip the scenes with Enter (P1).
7. Player phase: the P1 keys (arrows, X, D) move Ike and choose Wait, then D → End. The P2 keys (numpad, M) should do nothing.
8. Yellow phase: the P2 keys (numpad, M, E for the map menu) move Lethe, **Attack** if possible, Wait with Mordecai, then E → End. The P1 keys should do nothing.
9. Play 3+ turns. Keep an eye on the NetPlay chat for **"desync"** messages.
10. End the session from the host (Stop). Report the following, with screenshots of the NetPlay dialog and of any desync message:
    - the Dolphin version shown in the NetPlay dialog
    - the turn reached
    - Lethe's and Mordecai's HP/EXP in both windows at the end (the Status screen is fine)

**Success:** both windows show the same map and units every turn, each army answers only to its own player, and no desync is reported over 3+ turns. **Failure modes to report:** the client hangs on "waiting for players", the client boots with no save file (save sync failed), codes not active on the client (a yellow phase played by the AI), or a desync message (note the turn and action).

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | Claude (computer use; one PC, two instances; host COOP-P5 + EXP-16 + DBG-01; client stick on top-row digits so computer use could drive it) | **PASS (first Netplay session, 2 turns, Ch9)** | **Session:** the host's NetPlay Setup showed the presets (direct, 127.0.0.1:2626, P1-Blue); hosting with the game selected worked, and the client connected. Dolphin **auto-mapped P1-Blue → GC1, P2-Yellow → GC2**. Data menu: "Load Host's Save Data Only" and "Sync AR/Gecko Codes" were ticked. Client chat: "Synchronizing save data… Data received! Synchronizing Gecko codes… Codes received! … Started game". Both games ran in lockstep from boot. **Save sync:** the client saw the host's card (Restart Chapter → Prologue / Ch. 9) and both loaded Ch9 → base → prep → battle. **Cross-control:** blue phase, P2's A and right did nothing; yellow phase, P1's right and A did nothing on the Transformation prompt while P2 answered it; P2 used Next Unit (→ Mordecai), moved Lethe, Wait, Wait; the phase auto-ended; the enemy phase and the turn-2 conversation ran identically. **Desync check:** a state saved in each instance during turn 2's yellow phase (4 s apart) decodes identically (phase 3, turn 2, control `01 02 02 01`, every unit's force, position, HP, EXP and gauge). The force table and the Gecko code area are byte-identical. The only differing bytes are time-varying (`unit+0x74/75`, partner `+0x0/1`, `state+0x5C`). No desync message appeared. The host card was unchanged after the session (SHA-1 `d93a22ae…`). Backups `work/saves/GFEE01.net01_host_t2` and `GFEE01.net01_client_t2`. **Not covered:** combat under Netplay, a full chapter, two machines, Ch1-style ownership (the Ch9 card's army has no table PIDs). |

Two machines come after NET-01. NET-02 below replaces the "copy the client folder" plan with a shareable ZIP and Dolphin's Traversal Server.

### NET-02 — Two computers over the internet with the Player 2 ZIP (host + friend)

**What the friend gets:** `dist/FE9-Coop-Client-<fingerprint>.zip`, about 7 KB, built by `tools/netplay_package.py`. Since package `net02-2` (user request) it has **no launcher or script**; the friend already has Dolphin 2609a. It contains:
- `README.txt`: start Dolphin with `--user <package>\User` from a shortcut, add the game folder, check the code file's SHA-256 with `Get-FileHash`, join, controls, checklist and test steps
- a private Dolphin user folder:
  - `Config/Dolphin.ini`: cheats on, port 1 = controller, Traversal Server preset, nickname P2-Yellow, Background Input off
  - `Config/GCPadNew.ini`: the port-1 keyboard layout
  - `GameSettings/GFEE01.ini`: every code definition, **COOP-P6 + EXP-16** enabled (COOP-P5 + EXP-16 up to net02-2)
  - an empty `GC/USA/Card A/`
- `MANIFEST.txt`: Dolphin version, game, code fingerprint, and a SHA-256 for every file

The ZIP holds **no** game image, extracted asset, save file, memory card, Dolphin binary or launcher script. `verify()` enforces the exact file list, rejects save/disc/program/script extensions (`.exe .dll .bat .cmd .ps1 …`) and local paths, and checks the codes, manifest and settings. The friend supplies Dolphin **2609a** and their own GFEE01 rev 0 copy. Starting Dolphin with `--user <package>\User` keeps their own settings and cards untouched (F-32).

**Matching definitions:** the *code fingerprint* is the first 16 hex digits of a SHA-256 over the enabled codes (name and normalised code lines). The host checks it with `netplay_package --fingerprint`. The friend checks the code file's SHA-256 (printed in their README and `MANIFEST.txt`) with Windows' `Get-FileHash`. For COOP-P6 + EXP-16 (package net02-3) it is **`8609ae9f49fd879f`**; the first internet session ran COOP-P5 + EXP-16 (`7031af10d740f4ed`). Netplay runs the host's codes ("Sync AR/Gecko Codes"); the fingerprint lets both players confirm the definitions before starting.

#### Automated checks (before sending the ZIP)
```bash
.venv/Scripts/python -m tools.netplay_package
```
This builds and verifies the ZIP, prints every entry and the ZIP's SHA-256. Rebuild whenever `codes/GFEE01.ini` changes, since the file name carries the fingerprint. `NetplayPackageTests` (4 tests) cover: exact contents with no launcher, the README hash matching the code file, reproducible bytes, rejection of a ZIP with a `.gci`, a `.bat` or other codes, fingerprint rules, and that the NET-01 defaults are unchanged.

#### Host setup (Player 1, this PC)
1. Close Dolphin. Make the host folder. It reads the memory card in `work/saves/net02_card/`, a copy of the `work/ch1/host` card: Prologue, Ch. 9, Ch. 6, Ch. 3, Ch. 4; SHA-1 `54b5a7f4…`.
   ```bash
   .venv/Scripts/python -m tools.netplay_setup --root work/netplay_net --host-only --traversal --card work/saves/net02_card --enable COOP-P6 --enable EXP-16 --force
   ```
2. Confirm the host's codes match the package (expect "matches the client package"):
   ```bash
   .venv/Scripts/python -m tools.netplay_package --fingerprint work/netplay_net/host
   ```
3. Build the ZIP (above) and send it to the friend. The friend follows `README.txt` steps 1–4 (extract, shortcut with `--user`, add the game folder, optional hash check).
4. Start the host:
   ```bash
   Dolphin-x64/Dolphin.exe --user work/netplay_net/host
   ```
5. Tools → Start NetPlay… → **Host** tab. Connection Type: Traversal Server (preset); leave "Show in server browser" off. Select *Fire Emblem: Path of Radiance (GFEE01)* → **Host**.
6. In the NetPlay window, the drop-down at the top of the player list shows the **Room ID**. Click **Copy** and send the 8-character code to the friend privately.

#### Validation checklist (both players, before Start)
| # | Check | Where | Expected |
|---|---|---|---|
| 1 | Same Dolphin version | NetPlay player list, "Revision" column | both `2609a` |
| 2 | Same game | host: **Checksum → Current game** (SHA1 Digest) | "The hashes match!", digest `a30eca37…0309ace` |
| 3 | Same code definitions | host: `netplay_package --fingerprint` = the fingerprint in the friend's README; friend: `Get-FileHash` (README step 4) | `8609ae9f49fd879f` (net02-3); hash as in the README |
| 4 | Codes synced | host: Data → **Sync AR/Gecko Codes** ticked | ticked (preset) |
| 5 | Host save data, nothing written back | host: Data → **Load Host's Save Data Only** | ticked (preset; `WriteSaveData = False`) |
| 6 | Player 1 → GC port 1, Player 2 → GC port 2 | player list "Mapping"; host: **Assign Controller Ports** | P1-Blue `GC1`, P2-Yellow `GC2`, ports 3–4 empty |
| 7 | Friend's pad and settings | friend: Help → About; Config → General → Enable Cheats; Controllers → Port 1 | `2609a`; ticked; Standard Controller |

**Port assignment:** Dolphin maps the first player to GC1 and the second to GC2 by default (F-47). If not, the host opens **Assign Controller Ports**, puts P1-Blue in GameCube Port 1 and P2-Yellow in Port 2, and leaves Ports 3 and 4 as None. Each player's *local* controller 1 plays the GC port assigned to them. EXP-14 then routes port 2 to the yellow phase and port 1 to everything else.

#### Manual test plan (two computers; about 30 minutes)
Before Start, the host sets **Buffer** to about 18 (higher with a higher ping). The default 5 held both games at about 40 FPS over the internet (F-50); the buffer can also be changed during play. Start: the host clicks **Start**. Both chats must show "All players' saves synchronized" and "All players' codes synchronized" (friend: "Data received!", "Codes received!").

| Step | Action | Expected | Record |
|---|---|---|---|
| T1 | Host: Title → Restart Chapter → **Ch. 3: Pirates Aground** → skip scenes (Enter) → Begin now? Yes | both screens reach the turn 1 map together | time to reach the map |
| T2 | Blue phase, friend presses X and the arrows | nothing happens on either screen | — |
| T3 | Host moves Ike and Titania (arrows, X, Wait), then D → End | units move on both screens; a **yellow (partner) phase** starts | — |
| T4 | Yellow phase, host presses arrows/X | nothing happens | — |
| T5 | Friend moves Shinon and Gatrie (yellow rings); one **attacks** a bandit; then D → End | moves and combat play identically on both screens; the EXP bar fills | the unit's EXP before/after (Status) |
| T6 | Enemy phase | enemy moves and counters are identical on both screens | any counter EXP |
| T7 | Play turns 2–4 the same way; note any level-up screen | level-up shows on both screens with the same stat gains | the stats gained |
| T8 | Turn 3, yellow phase: **both** press Shift+F1 (save state; allowed in Netplay, F-47) and send the `.s01` files | `tools.inspect_state` output identical except the file line | — |
| T9 | Keep playing toward the boss, or stop after turn 4 | — | turn reached, any "desync" chat line (with the turn and last action) |
| T10 | **Disconnect:** in a new session, in the yellow phase, the friend closes their NetPlay window → Yes | host chat "P2-Yellow has left"; both games stop | what each screen did |
| T11 | Afterwards, the host checks the card | `work/netplay_net/host/GC/USA/Card A/*.gci` SHA-1 still `54b5a7f4…` | — |

**Success:** every Expected holds over 3+ turns with combat and EXP on both sides, no desync message, and T8 identical. **Failure modes:**
- Traversal join fails ("Could not communicate with host"): retry with a new room code. Then try host Direct Connection on 2626 with port forwarding (the client switches its Connection Type to Direct).
- Version mismatch: install the same Dolphin build on both.
- Digest mismatch: wrong dump or revision.
- AI plays the yellow phase: codes did not sync.
- A desync line in the chat.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user (host, this PC) + friend (own PC, the net02-1 ZIP with launcher); codes COOP-P5 + EXP-16 | **PASS (two computers over the internet; disconnect not reported)** | The friend joined by **room code** (Traversal Server). Both players `2609a Windows`, P1-Blue `GC1`, P2-Yellow `GC2`, saves and codes synchronized, ping 23–33 ms, Host Input Authority off. **Speed:** with Buffer 5, both games ran at about 40 FPS/VPS (stretched audio, slow animations), the same on both PCs. Buffer 26 gave 59.9 FPS/VPS, and **Buffer 18 stayed stable at 58–60**, the recommended setting. The user reported that everything ran well. **State comparison:** host and friend each saved two states (backups `work/saves/GFEE01.net02_inet_host_s01/_s02` and `GFEE01.net02_friend_s01/_s02`). Ch. 3 **turn 4, blue phase** and **turn 6, yellow phase** both decode **identically** on the two PCs (control `01 02 02 01`; every unit's force, position, HP, level and EXP). **Combat/EXP under Netplay:** between turns 4 and 6, the yellow units' EXP rose identically on both PCs (Shinon 67, Gatrie 14 → 55), and Ike reached 83 EXP. No desync message. The host card was unchanged afterwards (SHA-1 `54b5a7f4…`). **Not reported:** the disconnect test (T10) on two PCs; it passed on one PC. |
| 2026-10-27 | Claude (computer use; **one PC**: host `work/netplay_net/host`, client = the extracted ZIP started by its own `Start-FE9-Coop.bat`) | **PARTIAL: package PASS over Direct; Traversal join not verified** | **Launcher:** `Start-FE9-Coop.bat` found Dolphin, took the game folder, printed all `[OK]` and fingerprint `7031af10d740f4ed`, and started Dolphin with the package's user folder. `Check-Setup.bat` flagged a wrong exe ("not version 2609a") and a missing game folder correctly. **Traversal:** the host registered and received an 8-character Room ID. The packaged client (Traversal preset, room code pasted) failed twice with "Failed to connect to server: Could not communicate with host". A same-PC/same-NAT join like this relies on NAT loopback; this run doesn't establish whether two separate networks would connect, and the real two-PC run decides. **Direct 127.0.0.1:2626:** connected. Player list: P1-Blue `GC1`, P2-Yellow `GC2`, both `2609a`. **Checksum → Current game: "The hashes match!"**, digest `a30eca376ab9b2b4dd8b1a9136772a62c0309ace` (= `DolphinTool verify`). Data menu: Load Host's Save Data Only and Sync AR/Gecko Codes ticked. Chats: saves and codes synchronized / Data received / Codes received. The client saw the host card (Prologue, Ch. 9, Ch. 6, Ch. 3, Ch. 4). In Ch. 3 turn 1, Shinon and Gatrie had yellow rings on both screens. Blue phase: the client's X and arrows did nothing; the host ended the phase. Yellow phase: the host's keys did nothing; the client's keys moved the (yellow) cursor, opened the map menu and chose End. The enemy phase was identical on both screens: Ike was attacked, killed with a counter and reached Lv 5, HP 13/21 on both. **Turn 2 states** (host `work/saves/GFEE01.net02_host_t2`, client `GFEE01.net02_pkgclient_t2`) decode **identically** (chapter id 4, phase 0, turn 2, control `01 02 02 01`, every unit's force/position/HP/level/EXP). **Disconnect:** the client quit NetPlay in turn 2 → host chat "P2-Yellow has left" and **both games stopped**; the host's room stayed open with P1 only. The host card was unchanged (SHA-1 `54b5a7f4…`); the client's own card folder stayed empty (Netplay used `GC/NetPlayTemp`). **Driver note:** under Netplay, very short synthetic key taps were sometimes missed; 0.15–0.3 s holds worked. **Not covered:** a Traversal connection between two networks, a yellow-unit attack under Netplay, 3+ turns, two machines. |

## PREP-R1 — Pick Units research run (user, 2026-10-28)
**Steps:**
- Ch. 6 file → preparations → Choose Units.
- Slot 2 with the cursor on row 1, slot 3 on row 3.
- A on a row.
- Each prep option.
- Slot 4 at the formation map.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-28 | user | **Done (research)** | Normal difficulty. Screenshots of Choose Units ("You can select 1 more. 5/6"), the prep menu, Reposition, Items, Conditions and Options. A on a row did nothing (all forced). States backed up to `work/saves/GFEE01.prepR1_s02..s04`. They gave the list object layout, the row table, the highlighted-row field and the palette (F-58). |

## PREP-03 — Draft and transfers in Choose Units (EXP-26; PREP-01 Step 3)

**What it is:** in preparations, each player presses **Z on their own controller** with a character highlighted in **Choose Units**:
- **Unassigned** → claimed on your pick. Picks alternate, Player 1 first (as DRAFT-01).
- **Yours** → released, unless the other player has requested it; then pressing Z **accepts the transfer**.
- **The other player's** → **request** it (row turns **orange**). Press again to cancel.

Ike and unavailable characters are refused with the buzz. EXP-25's colours show the result at once: light blue = Player 1, yellow = Player 2, orange = transfer requested. Nothing changes forces in prep; EXP-21 turns Player 2's characters yellow at the first blue phase.

**Limit (by design for this step):** the list cursor follows Player 1's controller. Player 2 acts on the row Player 1 highlights.

**Static:** `test_exp26_prep_draft_code`, `test_gecko_budget`, 176/176 signatures. **Test bed (run 2):** `work/ch1/host` = COOP-P6 + EXP-21 + EXP-25 + **EXP-26** + DBG-01, 2984 of 3248 Gecko bytes. EXP-22 is off, so there is no L+R draft in battle in this bed.

**Keys:**
- Player 1: Z = **D**, cursor = arrows
- Player 2: Z = **E**

### Procedure (tester, one PC, ~10 minutes)
1. Fresh boot: `Dolphin-x64/Dolphin.exe --user work/ch1/host` → Restart Chapter → **Ch. 6** → Choose Units. Ike's row is light blue, the rest unassigned.
2. Highlight **Titania**, press **D** (P1). Sound; her row data turns **light blue**.
3. Highlight **Soren**, press **D**. **Buzz** (Player 2's pick). Press **E** (P2): sound; **yellow**.
4. Highlight **Ike**, press **E**: buzz.
5. **Rhys:** D → light blue. **Oscar:** E → yellow.
6. **Transfer:** highlight **Titania** (Player 1's). Press **E** (P2 requests): sound; row **orange**. Press **D** (P1 accepts): a different sound; **Titania turns yellow**.
7. **Cancel:** highlight **Rhys**. **E** → orange; **E** again → back to light blue.
8. **Release:** highlight **Soren**, **E** → back to unassigned (green).
9. Press **Shift+F2**. **Fight.** Turn 1, blue phase. Expected: **Titania and Oscar yellow rings**; Ike, Rhys and Soren blue. In the yellow phase, port 2 moves Titania and Oscar. Press **Shift+F3**.

**Report:** each step's outcome, screenshots of steps 6 (orange, then yellow) and 9, and slots 2 and 3.

**Failure modes:**
- Z does nothing: the gate or input is wrong.
- The wrong row changes: the row → unit mapping is off.
- Z also opens something in the list.
- Colours right in prep but wrong rings in battle.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-28 | user (run 1) | **FAIL: EXP-26 not loaded** | D/E did nothing on any row, not even the refusal buzz on Ike. State `GFEE01.prep03_s02`: the list was open (`E_SallyList` at `0x802A7468`, row 4), but `0x8012D6A4` held the original `stwu`, while EXP-25/21/22's hooks were patched. **Cause: the enabled codes (4000 bytes) exceeded Dolphin's Gecko space (≈ 3248), and EXP-26 came last** (F-59). The units were not protected. **Fix:** EXP-26 rewritten compactly (984 → 672 bytes; same behaviour). The bed drops EXP-22 (DRAFT-01 already verified; the prep draft replaces it here): COOP-P6 + EXP-21 + EXP-25 + EXP-26 + DBG-01 = 2984 bytes. `install_codes` now refuses over-budget sets. Retest = run 2, same steps. |
| 2026-10-28 | user (run 2, compact EXP-26, 2984-byte bed) | **PARTIAL PASS (steps 1–5)** | Choose Units after the claims: **Ike, Titania, Rhys light blue; Soren, Oscar yellow**. Battle Base Data matches (Titania, Rhys light blue; Oscar, Soren yellow). So the Z claims on each player's own controller, the alternating picks and the owner → battle carry-over work. Steps 6–8 (transfer request/accept, cancel, release) are not shown: the screenshots match the state after step 5, and no new states were saved (slots 2/3 are still run 1's, 01:06). Re-checked the code paths statically; still to confirm at runtime. |
| 2026-10-28 | user (run 3, steps 6–9) | **PASS** | Screenshots: Titania **orange** after Player 2's request, then **yellow** after Player 1 accepted. Rhys orange, then back to light blue (cancelled). Soren back to native green (released). **Slot 2** (prep, backup `GFEE01.prep03r3_s02`): Oscar and Titania `0x6000xxxx` (Player 2), Rhys `0x2000xxxx` (Player 1), Soren bits clear, **no OFFER left**. Titania's Lv 4 / 62 EXP / 36 HP unchanged by the transfer. **Slot 3** (turn 1, `GFEE01.prep03r3_s03`): **Titania and Oscar in force 3 (yellow)**, `control[3]` = human; Ike, Rhys and Soren blue. The draft, consent-based transfer, cancel and release in preparations all work, and the result carries into battle. |

## PREP-02 — Ownership colours in the unit lists (EXP-25; PREP-01 Step 2)

**What it is (v2):** in the native unit lists, each character's **data columns on every page** (Class, Lv, EXP, HP, Equipment, …) are coloured by owner. The **name keeps its native colour** (green = forced, and the pick state in Choose Units). That covers Choose Units in preparations and the map menu's Unit list (Base Data) in battle.
- Player 1, and Ike: **light blue**
- Player 2: **yellow**
- unassigned: unchanged (white; green if forced)
- unavailable: grey

It is display only. Ownership itself is still made with the verified in-battle draft (EXP-22).

**Static:** `test_exp25_list_ownership_colours`, 170/170 signatures.

**Test bed:** `work/ch1/host` = COOP-P6 + EXP-21 + **EXP-22** + **EXP-25** + DBG-01. EXP-23 is off for this test, so only the new display is being tested. Keys: Player 1 L+R = Q+W, Player 2 L+R = O+P.

### Procedure (tester, one PC, ~10 minutes)
1. Close Dolphin. Fresh boot:
   ```bash
   Dolphin-x64/Dolphin.exe --user work/ch1/host
   ```
   Then Restart Chapter → **Ch. 6** → preparations → **Choose Units**.
   Expected: **Ike's row data (Class, Lv, …) light blue**; names unchanged (green, since they are forced). Page through with R/L: the colour stays on every page. Screenshot.
2. Back → **Fight**. Turn 1, blue phase: draft with L+R.
   - Titania **Q+W**
   - Oscar **O+P**: ring turns yellow
   - Soren **Q+W**
   - Rhys **O+P**: yellow
3. Map menu (D) → **Unit** (the unit list).
   Expected: the data columns of **Ike, Titania, Soren light blue; Oscar, Rhys yellow**, on **every page** (page through). Names keep their native colour. Screenshot.
4. Press **Shift+F2**.
5. Optional (persistence preview):
   - Clear Ch. 6, the Escape objective; DBG-01 keeps enemies at 1 HP.
   - Save at the prompt over **"Ch. 9: Gallia"** (file 2, a test copy).
   - At **Ch. 7**'s Choose Units, Oscar and Rhys should be **yellow** and Titania and Soren **light blue** before anything else happens. Screenshot.

**Report:** whether each expectation held, the screenshots, and slot 2.

**Failure modes:**
- Wrong rows coloured: the row/unit mapping is off; slot 2 tells me.
- Colours in other columns.
- A crash when opening a list.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-28 | user (run 1, played Ch. 3 instead of Ch. 6) | **PARTIAL: ownership right, wrong column** | Choose Units before the draft: Ike light blue. In battle, Base Data after the draft: **Ike and Titania light blue, Shinon yellow, Gatrie (unassigned) unchanged**. So the row → unit mapping and the owner rule work. But the colour was on the **Class/Lv/Exp/HP** cells, not the names. On other pages (Equipment Data) there was no colour at all. Cause: `list+0x38[0]` is the first *data page*, not the Name column. **Fix (v2):** colour every data-page cell (column draw `0x8012F154`, all pages) and keep the Name column's native colour, so forced/picked stay readable. Retest = run 2. |
| 2026-10-28 | user (run 2, EXP-25 v2, Ch. 6) | **PASS** | Choose Units before the draft: **Ike's row data light blue on pages 1, 3 and 6**. The unassigned forced characters keep the native green; names are native everywhere; Ike stayed blue after leaving and re-entering. In battle after the draft, Unit Stats (page 2) and Personal Data (page 4): **Ike, Titania, Soren light blue; Oscar, Rhys yellow**. The owner colour holds on every data page and the names keep their own colour. |


## DRAFT-02 — Draft clarity (EXP-23 = draft v2; replaces EXP-22)

**What changes for the players (Priority A, user request "understandable without instructions"):**
- **Green = still in the draft.** On turn 1 of the blue phase, every deployed, unassigned character except Ike has a **green ring** and can't be moved yet. Blue = Player 1, yellow = Player 2.
- **L+R** on a green unit claims it on your pick: it turns blue (Player 1) or yellow (Player 2). L+R on your own unit releases it, back to green.
- **Whose pick:** the side with fewer drafted units (blue without Ike vs yellow) picks; Player 1 on a tie.
- **Sounds:**
  - Player 1 claim: unit-select sound
  - Player 2 claim: unit-change sound
  - release: unit-cancel sound
  - **any refusal**: the game's "miss" buzz (not your pick, Ike, a partner, the other player's unit, no unit, draft over)
- **The draft ends at the first action** (any unit finishing Wait, an attack, …) or when the phase ends. Every remaining green unit turns blue and can act. After that, L+R only buzzes.

**⚠ Not runnable as written (F-59):** COOP-P6 + EXP-21 + EXP-23 + DBG-01 is 3664 bytes, over Dolphin's ≈ 3248-byte Gecko space, so EXP-23 would be silently skipped. `install_codes` now refuses this set. EXP-23 must be slimmed, or another code dropped, before DRAFT-02 can run.

**Static:** `test_exp23_draft_v2_code`, 151/151 signatures. **Test bed:** `work/ch1/host` = COOP-P6 + EXP-21 + **EXP-23** + DBG-01 (EXP-22 off). The card is untouched since DRAFT-01's backup (`ch1_card_before_draft01.gci`). Keys: Player 1 L+R = **Q+W**, Player 2 L+R = **O+P**.

### Procedure (tester, one PC, ~10 minutes)
1. Close Dolphin, then fresh boot: `Dolphin-x64/Dolphin.exe --user work/ch1/host` → Restart Chapter → **Ch. 3**.
2. Turn 1, blue phase. Expected: **Ike blue; Titania, Shinon, Gatrie green.** Put the cursor on Titania and press X (A): she can't be selected to move.
3. Titania, **O+P** (P2). Expected: **buzz** (it's Player 1's pick).
4. Titania, **Q+W** (P1). Unit-select sound; **blue**.
5. Shinon, **O+P** (P2). A different sound; **yellow**.
6. Ike, **O+P**: buzz. Shinon, **Q+W**: buzz (not yours).
7. Shinon, **O+P**: release sound, **green**. **O+P** again: yellow. Leave **Gatrie green**. Press **Shift+F2**.
8. Move **Ike** and choose Wait. Expected: **Gatrie turns blue at once** and can now be moved by Player 1; the phase does not end early. **Q+W** anywhere now: buzz (draft over).
9. End the blue phase. Yellow phase: Shinon is yours (port 2); **O+P** buzzes. Press **Shift+F3**.
10. Optional, a second run: Restart Chapter → Ch. 3 again → claim one unit → **End the phase without acting** (D → End). Expected: any green unit turns blue before the yellow phase, and no green unit moves on its own later in the turn.

**Report:** each "Expected" that did or didn't happen, plus slots 2 and 3. **Failure modes:**
- Units green at turn 2 or later.
- A green unit moved by the AI.
- The blue phase ending after Ike's Wait in step 8, with Gatrie never acting.
- No sounds at all, or a crash on L+R.

| Date | Tester | Result | Notes |
|---|---|---|---|

## DRAFT-01 — In-game draft with persistent ownership (EXP-21 + EXP-22; drafting Milestones A–C, first pass)

**What it is:**
- **Ownership** is stored in each unit's own flag word: `0x20000000` assigned, `0x40000000` Player 2 (F-52). It is saved with the character, so nothing is regenerated, and progression is untouched.
- **EXP-21** replaces EXP-16's PID table, using the same hooks.
- **EXP-22** is the draft. On **turn 1 of the blue phase**, a player puts the cursor on a deployed unit and presses **L+R** on their own controller:
  - **Claim** an unassigned unit, only on your pick. Picks alternate, Player 1 first.
  - **Release** your own unit; this also gives the pick back.
  - Ike, native partners and the other player's units are refused.
  - A cursor sound confirms each change. A Player 2 claim turns the ring yellow at once.

**Static:** `test_ownership_flag_bits_unused`, `test_exp21_flag_ownership_code`, `test_exp22_draft_code`; 144/144 signatures.

**Test bed:** `work/ch1/host` = COOP-P6 + **EXP-21 + EXP-22** + DBG-01 (EXP-16 off). The card was backed up first (`work/saves/ch1_card_before_draft01.gci`, SHA-1 `54b5a7f4…`). Keys: Player 1 L+R = **Q+W**, Player 2 L+R = **O+P** (port 2 stick = numpad, A = M).

### Procedure (tester, one PC, ~15 minutes)
1. Close Dolphin. Fresh boot (not a save state):
   ```bash
   Dolphin-x64/Dolphin.exe --user work/ch1/host
   ```
2. Title → **Restart Chapter → Ch. 3: Pirates Aground** → skip to the turn 1 map. Expected: all four units (Ike, Titania, Shinon, Gatrie) blue. Nobody is owned yet; EXP-16's table is gone.
3. **Draft**, with the cursor on each unit in turn (arrows move the cursor):
   - **a.** Titania, **Q+W** (P1). Sound; she stays blue.
   - **b.** Shinon, **Q+W** (P1 again). Nothing: it's Player 2's pick.
   - **c.** Shinon, **O+P** (P2). Sound; **Shinon's ring turns yellow**.
   - **d.** Ike, **O+P**. Nothing: Ike is refused.
   - **e.** Gatrie, **Q+W** (P1). Sound.
   - **f.** Shinon, **O+P** again. Released: sound, blue again. Then **O+P** once more: yellow again.
4. Press **Shift+F2** (slot 2). End the blue phase (D → End).
5. **Yellow phase:** the cursor jumps to Shinon, and only port 2 moves him. Attack a bandit with Shinon and note his EXP. End the phase.
6. Turn 2: L+R does nothing any more (the draft is only on turn 1).
7. Clear the chapter: defeat the boss. DBG-01 keeps enemies at 1 HP. At the **Save Data** prompt, save over **"Ch. 9: Gallia"** (file 2; a test copy, backed up).
8. **Ch. 4** turn 1, blue phase: **Shinon is yellow automatically**; Titania and Gatrie are blue (Ch. 4's line-up is forced, F-41). Press **Shift+F3** (slot 3).
9. **Reload check:** close Dolphin, fresh boot → Restart Chapter → the file you saved in step 7 → Ch. 4 turn 1: Shinon is **still yellow**, with the EXP from step 5. Press **Shift+F4** (slot 4).
10. Tell me when slots 2–4 are saved, and what happened at each step. Screenshots of steps 3c, 8 and 9 help.

**Failure modes, and what each tells us:**
- The sound plays but nothing changes, or L+R does nothing at all: the input read (port/bits) is wrong. Slot 2 tells me the flags.
- Shinon is blue in Ch. 4: the bit was lost at the chapter end or the save. Slots 3/4 tell me which.
- A crash or freeze on L+R: stop, and tell me which unit and which step.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-28 | user | **PASS (all seven checks)** | User report: character claiming, release and reclaim, Yellow control, EXP progression, chapter transition, normal save, and a fresh reload all behaved correctly. No state slots or card changes from this run are on the development PC (`work/ch1/host` card still SHA-1 `54b5a7f4…`, no new states), so the evidence is the user's report. |

## EXP-20 / COOP-P6 — Cursor jumps to a yellow unit when the yellow phase starts

**Goal (user):** a clear "your turn" cue for Player 2. At the start of a human yellow phase, the cursor (and camera) moves to a yellow unit that can still act. Vanilla only does this for Ike in the player phase (F-51). **COOP-P6** = COOP-P5 + EXP-20. Static: `test_exp20_yellow_cursor_hook`, `test_coop_p6_package`, 133/133 signatures. Runtime: **PASS** (user, 2026-10-27).

Installed in the one-PC test bed `work/ch1/host` with COOP-P6 + EXP-16 + DBG-01. After the pass below, the Netplay host and the friend ZIP moved to **COOP-P6 + EXP-16** (package net02-3, fingerprint `8609ae9f49fd879f`).

### Procedure (tester, one PC)
1. Close the Dolphin that uses `work/ch1/host` if it is open. Start it from a **fresh boot**, not a save state: a state restores the code list it was saved with (F-25).
   ```bash
   Dolphin-x64/Dolphin.exe --user work/ch1/host
   ```
2. Title → **Restart Chapter → Ch. 3: Pirates Aground** → skip to the turn 1 map.
3. Blue phase: the cursor starts on Ike, as in vanilla. Move the cursor away from the yellow units (e.g. a few tiles up), then end the phase (D → End).
4. **Yellow phase starts:** expected, the cursor and camera jump to **Shinon or Gatrie**. Press Shift+F2 (state slot 2) right there.
5. Act with one yellow unit (port 2 keys), end the phase. Next turn's yellow phase: the cursor should again start on a yellow unit.
6. Optional (option-bit check): Options → turn off the cursor option (the one that makes the cursor start on Ike) → next blue phase **and** next yellow phase: no jump in either.
7. Optional (vanilla unchanged): Prologue or any chapter with no yellow units. The blue phase still starts on Ike, and nothing else changes.

**Report:** which unit the cursor landed on in step 4, and step 5's result. Send a screenshot from step 4 and tell me slot 2 is saved.

**Failure modes:**
- The cursor stays where the blue phase left it: the hook didn't run, or the option bit is set.
- The cursor goes to a blue unit: EXP-17 is not active.
- A crash or freeze at the start of the yellow phase: stop and send what you saw.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user (one PC, `work/ch1/host`, COOP-P6 + EXP-16 + DBG-01; fresh boot, Ch. 3) | **PASS** | User: at the start of the yellow phase the cursor swapped to a yellow unit. **Slot 3** (phase 3, turn 2, backup `work/saves/GFEE01.exp20_s03`): cursor `state+0x524/0x528` = (15.5, 21.5) = tile (15,21), which is **Shinon's tile**. Ike, where the vanilla blue-phase step puts the cursor, is at (15,23). Slot 2 (turn 1 yellow phase, `GFEE01.exp20_s02`) has the cursor on (15,21), the tile Shinon moves to in that phase, so it was probably saved mid-move. Option byte `state+0x9E` = `0x15` (bit 0x40 clear). For contrast, the Netplay yellow-phase state without EXP-20 (`GFEE01.net02_inet_host_s02`) has the cursor on Titania's tile (13,8), where the blue phase left it. Not checked: the cursor option turned off, and vanilla chapters without yellow units. |

## EXP-15 — Chapter 1 with two armies (Phase 4 proof, fixed assignment)

**Goal (user):** play Chapter 1 with **Blue = Ike, Titania** (player 1, port 1) and **Yellow = Boyd, Oscar** (player 2, port 2), strictly in sequence (blue phase, then yellow phase, then enemy phase), and carry everyone into Chapter 2 with their progression.

**Change (F-34, F-35):** EXP-15 reuses the game's own script command `UnitTransferToForce`:
- **Block 1**, at the start of the Chapter 1 player phase (chapter id 2, phase 0): Boyd (`PID_BOLE`) and Oscar move force 0 → 3, only if they are in force 0, so it runs once.
- **Blocks 2–4** (v3), at the entry of every chapter-end path found (F-38, F-39): they move 3 → 0. The paths are the seize/clear event command `AllUnitEscape` (`0x800BA784`), the transition `0x8002E0D0` and the chapter sequence `0x80005F04`. Earlier versions ran too late: v1 used the roster move `0x80016C58`, and v2 lacked `AllUnitEscape`.

Everything else is COOP-P3: yellow phase human-controlled, ownership, leftover units wait, partner EXP and level-up, and port 2 input. Static: `test_exp15_gecko_hooks`, 97/97 signatures. **v3 PASSED** (user, 2026-10-27). Runs 1 (v1) and 2 (v2) were PARTIAL.

Test bed (already created; `--force` recreates it):
```bash
.venv/Scripts/python -m tools.netplay_setup --root work/ch1 --enable COOP-P3 --enable EXP-15 --force
```
`work/ch1/host` is a private Dolphin user folder:
- Port 1 keys: X/Z/C/S/D, Enter, arrows. Port 2 keys: M/N/B/V/E, Y, numpad 8/5/4/6.
- Its card has file 1 = Prologue and file 2 = Ch. 9.
- Its save states go to `work/ch1/host/StateSaves`, so your own slots are untouched.

### Procedure (tester)
1. Close Dolphin. Start it with the test bed:
   ```bash
   Dolphin-x64/Dolphin.exe --user work/ch1/host
   ```
2. Boot the game. **Restart Chapter → file 1 (Prologue)**. Play the Prologue (Vulnerary in the Greil fight). At the **Save Data** prompt, save to **file 3**. Expected: "Ch. 1".
3. Chapter 1 battle, first player phase (turn 1): press **Shift+F3** (state slot 3). Check:
   - Boyd and Oscar have **yellow** map rings; Ike and Titania have blue.
   - Port 1 (X) on Boyd does nothing; port 2 (numpad, M) does nothing in this phase.
4. Move Ike and Titania with port 1 and end the phase (D → End).
5. Expected: a **yellow (partner) phase** starts. Press **Shift+F4**.
   - Port 1 does nothing.
   - With port 2, move Boyd and Oscar. **Attack** an enemy with one of them and note the EXP shown. End the phase with E → End.
6. Enemy phase: enemies may attack either army. Note any counter EXP.
7. Repeat for 2+ turns, then clear the chapter by defeating the boss with anyone. Note any conversation or event that looks wrong.
8. At the end-of-chapter **Save Data** prompt, save to **file 4**. Expected: "Ch. 2".
9. Chapter 2, first player phase: press **Shift+F5**. Check that Boyd and Oscar are present, blue, and keep their level/EXP, with no duplicate units. (EXP-15 only reassigns in Chapter 1, so they are blue again in Chapter 2.)
10. Send screenshots of steps 3, 5 and 9 and tell me when the slots are saved. I'll decode slots 3–5.

**Optional defeat check:** from slot 3, let Ike be defeated. Expected: the normal Game Over.

**Success:** every check above holds: blue only in the blue phase and yellow only in the yellow phase, each on its own port, never at the same time; both armies fight the same enemies; EXP is gained and kept; the chapter clears normally; and Chapter 2 has the full roster once each.

**Failure modes, and what each tells us:**
- Boyd or Oscar still blue at turn 1 → block 1 did not run (slot 3 tells).
- No yellow phase → the phase skip rule (F-11) needs more than units in force 3.
- Boyd or Oscar missing in Chapter 2 → block 2 did not run, or roster bookkeeping needs more. Nothing is lost: it is a test card.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user (v1) | **PARTIAL** | **Passed:**<br>• Chapter 1's first fight: blue, yellow and red phases alternated as intended (screenshot: Boyd and Oscar with yellow rings, turn 2).<br>• Slot 3 (Ch1, turn 1, phase 0) decodes as Oscar (unit 2) and Boyd (unit 3) in force 3; Ike and Titania in force 0.<br>**Failed:** Boyd and Oscar were **lost** at the transition.<br>• Slot 4 (chapter id 3 base, turn 3): the roster (force 5) holds only Ike and Titania, and unit slots 2 and 3 are empty.<br>• Slot 5 (Ch2 turn 1): Ike and Rhys in force 0, Titania in force 7.<br>• The next battle's Base Data lists Ike, Titania, Shinon and Gatrie. In vanilla Chapter 2 (old slot 7) Oscar and Boyd are deployed.<br>Cause and fix: F-38, v2. The test card was not written (no save at the prompts). |

| 2026-10-27 | user (v2) | **PARTIAL** | Suspend shortcut worked: suspend from the Ch1 turn 1 state, close, reopen, resume. Phases and controls as in run 1. **Boyd and Oscar missing again in Chapter 2** (Base Data: Ike, Rhys). The v2 hooks are patched in RAM (slots 6/7). Slot 6, taken during the ending conversation, already has Ike and Titania in force 5 and unit slots 2 and 3 empty: the drop happens at the seize, in `AllUnitEscape` (F-39). v3 hooks it and passed. |
| 2026-10-27 | user (v3, DBG-01) | **PASS (no yellow EXP)** | Suspend from slot 8, then fresh boot and resume. Chapter 1 cleared with blue → yellow → red phases. Chapter 2 Base Data lists **Ike, Oscar, Boyd, Rhys**. Slot 6 (ending conversation) has Oscar and Boyd in force 5 (roster); slot 7 (Ch2 turn 1) has them in force 0, with no duplicates. Boyd and Oscar weren't used, so EXP stayed 0. |
| 2026-10-27 | user (v3, DBG-01) | **PASS** | Rerun with Boyd and Oscar fighting in the yellow phase. Slot 6 (11:54): **Oscar lv 3 → 4, EXP 35**; **Boyd EXP 0 → 47**; Ike lv 4 EXP 2; Titania EXP 20; all four in force 5. Slot 7 (Ch2 turn 1): Ike, Oscar (lv 4, 35, max HP 27), Boyd (lv 2, 47) and Rhys in force 0. Titania in force 7, as in vanilla Ch2 (old slot 7). The Base Data screenshot matches. The user reports every check passed: phases, separate ports, shared enemies, the chapter events, and the transition. |

### Retest of v3 (tester)
EXP-15 v3 is installed in `work/ch1/host`. Slot 3 now holds a Chapter 2 state, so the Chapter 1 turn 1 state (Dolphin's `lastState.sav`, SHA-1 `11569207…db7d`, backup `work/saves/GFEE01.ch1_turn1_exp15`) has been copied to **slot 8**.
**Speed aids (test bed only):**
- **DBG-01** is enabled in `work/ch1/host`: every red unit's HP is held at 1, so any hit kills. It is a per-frame C0 routine (`test_dbg01_enemy_hp`). It is never part of a COOP package; a test checks that.
- It only takes effect after a **fresh boot**. A state restores the code list it was saved with (F-25), which is why the suspend/resume route is used below.
- Also: turn off battle animations in the game's Options, and hold Dolphin's frame-limit hotkey (Tab by default) to fast-forward.

1. **Shortcut:** open the test bed, load **slot 8** (F8). In the map menu choose **Suspend → Yes**. Close Dolphin.
2. Start the test bed again (fresh boot = v2 codes) and **resume** the suspended chapter from the title. If the suspend failed, replay from file 1 (Prologue) as in the main procedure.
3. Play Chapter 1 as before.
4. **Right after the seize**, during the ending conversation, press **Shift+F6**.
5. Save at the end-of-chapter prompt to **file 3**. At the first Chapter 2 player phase, press **Shift+F7**.
6. Tell me who is deployed, and send the Base Data screen. Expected: Oscar and Boyd are back as blue units in Chapter 2, as in vanilla. (Same state slots as before: Shift+F6 right after the seize, Shift+F7 in Chapter 2.)

## EXP-16 — Army ownership table across Chapters 1–3 (Phase 4)

**Change:** ownership is separated from the tactical force. `tools/owner_code.py` holds the table (PID → player) and generates EXP-16. The table is currently **Oscar, Boyd → Player 2**; everyone else is Player 1. EXP-16 has five blocks, all using the game's `UnitTransferToForce`:
- **Apply** at the start of **every** player phase, in any chapter: Player 2 characters in force 0 → 3.
- **Return** at the entry of `AllUnitEscape`, the chapter transition and the chapter sequence: 3 → 0.
- **Single-unit return** at the entry of `UnitEscape`, for the escaping unit only (F-40).

It replaces EXP-15: same hook sites, so never enable both. The table is embedded in the code, so Netplay clients get the identical table and nothing is written to save data (RESEARCH "Ownership storage"). Static: `test_exp16_ownership_code` (the ini must match the generator), 100/100 signatures. **Run 1 PASSED through the Ch4 start** (yellow army only in Ch2, because the story forced the Ch3 and Ch4 line-ups).

Test bed: `work/ch1/host` now has **COOP-P3 + EXP-16 + DBG-01**. Its card (backup `work/saves/ch1_card_after_exp15.gci`, SHA-1 `9eb0dd49…f6f6`) holds the end-of-Chapter-1 save from the EXP-15 v3 run.

### Procedure (tester): Chapter 2 and Chapter 3 in one campaign
1. Start the test bed:
   ```bash
   Dolphin-x64/Dolphin.exe --user work/ch1/host
   ```
   Fresh boot → **Restart Chapter → the "Ch. 2" file** (the one you saved at the end of Chapter 1).
2. **Chapter 2, turn 1, player phase:** Shift+F2. Expected: Oscar and Boyd are yellow with no code change; Ike and Rhys are blue.
3. During the chapter, try each of these and note what happens:
   - **Rhys heals** Oscar or Boyd with his staff (a blue healer on a yellow ally), and gains EXP.
   - **Counterattack EXP:** an enemy attacks a yellow unit in the enemy phase.
   - **End the yellow phase** with one yellow unit not yet acted (it should just wait).
   - **Titania's arrival** around turn 3 (she should be blue): Shift+F3 after she appears.
4. Seize or clear. During the ending conversation press Shift+F4, then save at the prompt to a **new file** ("Ch. 3").
5. **Chapter 3, turn 1:** Shift+F5. Expected: Oscar and Boyd yellow again (if the story deploys them), newly met characters blue.
6. Clear Chapter 3. Shift+F6 during the ending conversation, then save to a new file ("Ch. 4"). At the Chapter 4 start, Shift+F7.
7. Send the Base Data screen at each chapter start and tell me which slots were saved. I'll decode them: forces, levels, EXP, no duplicates.

**Optional edge checks (from any state above; tell me which you tried):**
- Let Ike fall. Expected: Game Over as normal.
- Let a yellow unit (Boyd) fall. Note the death message and whether he is listed as dead or missing afterwards.
- Battle Save or Suspend mid-chapter during the yellow phase, then resume after a fresh boot.

### Edge-case status (campaign integrity)

| # | Case | Status | Evidence |
|---|---|---|---|
| 1 | Ike's defeat → Game Over | Untested (optional step offered) | Ike is never moved (Player 1, rejected in the table) |
| 2 | Yellow-owned character dies | **Verified with EXP-19:** the unit goes to force 6 with the died flag and the chapter id, as a blue unit would. Without EXP-19 it was freed (Boyd) | F-44, F-45 |
| 3 | Yellow character escapes / seizes | Seize: only Ike seizes in Ch1–3. Escape: handled by the EXP-16 `UnitEscape` hand-back, untested | F-40 |
| 4 | Single-unit `UnitEscape` | Static only | F-40, EXP-16 block 5 |
| 5 | `AllUnitEscape` and chapter cleanup | **Verified** for Chapter 1 → 2 (EXP-15 v3) | F-38, F-39 |
| 6 | Save/load mid two-army battle | **Verified** mid yellow phase (phase, `control[3]`, forces and done-flags kept). This game has no Battle Save, only Suspend | EXP-15, F-44 |
| 7 | Ending a phase with yellow units unacted | **Verified** (EXP-07, Ch9) | EXP-07 |
| 8 | Chapter with zero yellow units | **Verified once**: no yellow phase (Prologue) | F-37 |
| 9 | Recruitment / story appearances | **Verified** Ch2–4: Rhys, Shinon, Gatrie and Soren joined blue (default); Titania's mid-chapter arrival was blue; Marcia behaved as in the original story | EXP-16 run, F-41 |
| 10 | Units under AI/script control | Only forces 0/3 and table PIDs are moved, by design. Untested | — |
| 11 | Levelling, healing EXP, promotion | Level-up **verified** (Oscar in Ch1, Boyd twice in Ch2, Lethe in Ch9). Healing EXP plausible (Rhys 0 → 11 in Ch2; target not recorded). Promotion untested | EXP-13, EXP-15, EXP-16 |
| 12 | Repeated chapter loading without duplicates | **Verified** Ch1 → 2 → 3 → 4 (each Base Data shows everyone once; benched units in force 7) | EXP-15, EXP-16 |
| 13 | Controller ownership through transitions | **Verified** Ch1 → 2 (port routing follows the phase) | EXP-14, EXP-15 |

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user (COOP-P3 + EXP-16 + DBG-01) | **PASS Ch2 → Ch3 → Ch4 start** (yellow army only in Ch2; see notes) | **Ch2** (id 3; slots 2–4): Oscar and Boyd were yellow at turn 1 with no code change, Ike and Rhys blue, Titania arrived blue. Oscar 35 → 82 EXP; Boyd lv 2 → 4, 47 → 82; Rhys 0 → 11 (a heal); Ike 2 → 91. **Ch3** (id 4, slot 5): the story forced the line-up to Ike, Titania, Shinon and Gatrie (all with flag `0x10000`, F-41). Oscar, Boyd and Rhys were benched (force 7) with progression intact; Shinon and Gatrie joined blue. **Ch4** (id 5; slots 6–7): Soren joined blue; six deployed, all forced; Oscar and Boyd benched. All four Base Data screens match: everyone appears exactly once, nothing reset. Marcia left after talking to Ike in Ch3, consistent with the original story (F-41). **Not exercised:** no yellow phase in Ch3–4 (no Player 2 character deployed). User request: auto-end for the yellow phase. |

### EXP-16 run 2: Chapter 3 → Chapter 5 start with a yellow army (tester)
The table is now **Oscar, Boyd, Shinon (`PID_CHINON`), Gatrie (`PID_GATRIE`) → Player 2**. Shinon and Gatrie are forced into the Ch3/Ch4 line-ups (F-41), so Player 2 has units there. Installed in `work/ch1/host` (COOP-P3 + EXP-16 + DBG-01). Card backup before this run: `work/saves/ch1_card_after_exp16_run1.gci` (SHA-1 `8eb1d955…6610`). The card is full (5 files), so overwrite the later files as below.
1. Start the test bed (fresh boot) → **Restart Chapter → "Ch. 3: Pirates Aground"**. Prep: Fight.
2. **Ch3, turn 1, player phase:** Shift+F2. Expected: Ike and Titania blue; **Shinon and Gatrie yellow**.
3. Blue phase with port 1, then the **yellow phase with port 2** (numpad, M, E): move or attack with Shinon and Gatrie. Shift+F3 during the yellow phase.
4. Clear Ch3. Shift+F4 during the ending conversation, then save over the **"Ch. 4" file** (5th slot).
5. **Ch4** prep: Fight. Turn 1: Shift+F5. Expected: Shinon and Gatrie yellow; Ike, Titania, Rhys and Soren blue. Play a yellow phase.
6. Clear Ch4. Shift+F6 during the ending conversation, then save over the **"Ch. 2" file** (3rd slot) → "Ch. 5". At the Ch5 start: Shift+F7.
7. Send the Base Data screens and tell me which slots you saved.

**Expected at each transition:** Shinon and Gatrie are back in the roster with their EXP; nobody is duplicated or missing.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user (run 2: table Oscar, Boyd, Shinon, Gatrie → P2) | **PASS Ch3 → Ch4 → Ch5 start** | **Ch3** (id 4; slots 2–3): Shinon and Gatrie yellow at turn 1; a yellow phase ran (slot 3, phase 3). **Ch3 → Ch4** (slots 4–5): all four Ch3 units in the roster; Shinon 0 → 21 EXP, Gatrie 0 → 41. In Ch4 Shinon and Gatrie were yellow again, and Ike, Titania, Rhys and Soren blue (map screenshot: yellow rings on the knight and archer). **Ch4 → Ch5** (slots 6–7): Shinon 44, Gatrie 85, Soren 57, Ike lv 7. **Ch5 (id 6) turn 1: Oscar, Boyd, Shinon and Gatrie yellow; Ike, Titania, Rhys and Soren blue**, eight deployed. Each unit appears exactly once; benched units keep progression. **UI finding:** the in-battle Base Data list shows only force 0, so Player 2's units are missing from it while they are yellow (they appear on the prep screen). **No auto-end in the yellow phase** (user). |

## EXP-17 — Auto-end and Next Unit in the yellow phase

**Change (F-42):** the auto-end check after each action asks "is there a next unit that can act?" through `0x800AA5F0`, which only looked at blue units. Next Unit uses the same function. EXP-17 makes both use the yellow army in the yellow phase; other phases are vanilla. Static: `test_exp17_next_unit_hooks`, 108/108 signatures. **PASSED** (user, 2026-10-27). Installed in `work/ch1/host` (COOP-P3 + EXP-16 + EXP-17 + DBG-01).

1. Fresh boot of the test bed (a state would restore the old code list, F-25) → **Restart Chapter → the "Ch. 5" file**. Map Menu → Options: **Auto End = On**.
2. Blue phase: move all blue units. Expected: the phase ends by itself, as before.
3. Yellow phase: press **Next Unit** (port 2 X = the **B** key). Expected: the cursor jumps between **yellow** units only.
4. Move every yellow unit. Expected: **the yellow phase ends by itself** after the last one waits; the enemy phase starts.
5. Set Auto End = Off and repeat one turn. Expected: no automatic end, and E → End still works.
6. If anything is off, press Shift+F2 at that moment.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user (COOP-P3 + EXP-16 + EXP-17 + DBG-01, Ch5) | **PASS** | Yellow phase: **Next Unit jumped through yellow units only**. After every yellow unit had moved, **the phase ended on its own**. With Auto End off, no phase ended automatically once all units had acted. Packaged as **COOP-P4** = COOP-P3 + EXP-17 (`test_coop_p4_package`). |

## EXP-18 + edge cases 1, 6, 7: Base Data, suspend mid yellow phase, yellow death (tester, one session)

**EXP-18 (F-43):** the in-battle Base Data (map menu → **Unit**) is built from force 0 only. EXP-18 makes its two list walks continue into force 3, keeping only units with the game's own "deployed player" flag `0x400`. The game sets that flag on every force 0 unit at map start (`0x8002EA48`), before EXP-16 moves Player 2's units, so native partners (Lethe, Mordecai) never have it. Static: `test_exp18_base_data_hooks`, 114/114 signatures. Installed in `work/ch1/host`: COOP-P4 + EXP-16 + EXP-18 + DBG-01. Card backup: `work/saves/ch1_card_after_exp16_run2.gci`.

Note: this game's map menu has **Suspend**, not a Battle Save, so "save/load mid-battle" = Suspend → fresh boot → resume.

1. Fresh boot of the test bed → **Restart Chapter → "Ch. 5"** → prep → Fight.
2. **Base Data (EXP-18):** turn 1, Map Menu → **Unit**. Expected: **all 8 units** (Ike, Titania, Rhys, Soren, Oscar, Boyd, Shinon, Gatrie) with their real level, EXP and HP. Open **Status** (Y) on a yellow unit, and try any sort or page buttons. Screenshot the list.
3. **Suspend mid yellow phase (edge 6, 7):** in the yellow phase, after moving one yellow unit, press Shift+F2, then Map Menu → **Suspend → Yes**. Close Dolphin, start the test bed again (fresh boot) and **resume**. Expected: still the yellow phase; the moved unit is done; the others can be moved with port 2 only; port 1 does nothing. Press Shift+F3 after resuming.
4. **Yellow death (edge 1):** let **Boyd** die. Enemies still hit at 1 HP, so park him next to several enemies and end turns, or keep attacking into counters. Press Shift+F4 right **before** the fatal enemy phase, and Shift+F5 right **after** his death message.
5. Map Menu → Unit: is Boyd gone from the list? Then clear the chapter. Press Shift+F6 during the ending conversation and save to the "Ch. 5" file (overwrite).
6. Chapter 6 prep: screenshot the unit list, then press Shift+F7. Expected (vanilla rule): **Boyd is gone for good**: not in the roster, not revived, not duplicated. Everyone else keeps their progression.

**Optional (edge 2):** from slot 4 or 5, let **Ike** fall. Expected: the normal Game Over.

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | user (COOP-P4 + EXP-16 + EXP-18 + DBG-01, Ch5 → Ch6) | **PASS with findings** | **Base Data:** all 8 listed (Ike, Titania, Oscar, Boyd, Rhys, Shinon, Gatrie, Soren) with real level and HP, and the Status screen works for yellow units. But yellow units showed **EXP "--"** at turn 1: `control[3]` is still 2 until the first phase change, so the EXP display hook (EXP-11) does not apply yet (F-44). Fixed: EXP-16's apply step now sets `control[3]` = 1 (not yet re-run). **Suspend mid yellow phase:** slot 2 → resume → slot 3: still phase 3 with `control[3]` = 1, units and done-flags kept, play continued on port 2. **Boyd's death:** slot 4 (before) has him; slot 5 (after) has his unit slot **freed** (backups `work/saves/GFEE01.ch5_before/after_boyd_death`). After Ch5 (slots 6–7) Boyd is gone for good, nobody was revived or duplicated, and the rest kept progression (Oscar lv 6, Gatrie lv 11). **Ch6 prep listing 5 units** is the original story: Ch6's ally data (`bmap07`) has no Shinon or Gatrie, and they wait in force 7. Whether vanilla also frees a dead **blue** unit is the open comparison (next test). |

### Follow-up (tester): vanilla death comparison and the EXP "--" fix
1. **Blue death comparison:** load **slot 4** (Ch5, before Boyd died; the old code list is fine for this). Let a **blue** unit die (Soren or Rhys) during an enemy phase, then press **Shift+F8** right after the death message.
2. **EXP display:** fresh boot → Restart Chapter → "Ch. 5" → Fight. At turn 1, before moving anyone, Map Menu → Unit. Expected: the yellow units show **real EXP** (Oscar 82 and so on), not "--".

| Date | Tester | Result | Notes |
|---|---|---|---|
| 2026-10-27 | Claude (computer use; COOP-P4 + EXP-16 + EXP-18 + EXP-19 + DBG-01/02; Ch6 from the card) | **PASS** | **EXP display:** at turn 1 in the blue phase, Base Data showed Oscar with **EXP 28** (not "--"); `control[3]` fix confirmed. **Death record (EXP-19):** Oscar (yellow, held at 1 HP by DBG-02, DBG-01 off) attacked a soldier and died to the counter ("The enemy was better…"). Slot 2 (before): force 3, flags `0x00010400`. Slot 3 (after): **force 6, flags `0x01018409` (died `0x8000`), +0x234 = 7**, the same record a dead blue unit gets (F-45). Also seen: the yellow phase **auto-ended** after Oscar's Wait; **Next Unit** jumped to Oscar; port 1 was ignored in the yellow phase. Ch6's prep forces all 5 candidates (F-46). The vanilla blue-death comparison was replaced by the disassembly of the death routine (F-45). The card was not written. |
## CAMP-X: owner-operated scenario package (2026-10-28)

Status: **OFFLINE CHECKS PASS; NEW GAMEPLAY NOT TESTED**. Root Test-Scenario.ps1
was exercised only with -List/-Check/-Review (no Dolphin launch/input).
Procedures/captures/failure boundaries: [SCENARIO_TESTS.md](SCENARIO_TESTS.md).

Prepared candidates: Kieran post-Talk Wait (3240bytes), original prisoner Escape
(3240bytes), Ch6 remaining Blue Escape queue/Ike-last (3168bytes), and isolated
native Suspend/fresh boot (3240bytes). All fit3248; stable2536-byte code and
production fingerprint8609ae9f49fd879f remain unchanged. No merge or new runtime
acceptance. 189 offline tests,378 signatures,16 prior accepted artifact hashes
verified. Setup interpreter uses mocked natives; original positioning/event
execution must be demonstrated by owner captures. Native reload and next-chapter
roster retention still need original gameplay evidence.
