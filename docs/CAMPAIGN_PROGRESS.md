# Autonomous campaign engineering progress

Working clone: FireEmblemCampaignAudit. Branch: codex/campaign-compatibility.
Reference branches main/draft-ownership and source-checkout saves/profiles untouched.

## Completed checkpoint

- b9f3816 pushed: budget validation centralized; forced setup rejects before card
  deletion; shared C2 writers rejected; unknown code IDs rejected.
- Full container inventory: 31 internal campaign IDs, 43 scripts, suffix maps,
  message-derived chapter names; separate gameplay/clear/transition/Netplay axes.
- Snapshot comparator and byte-level Gecko report. Stable code fingerprint unchanged.
- Baseline validation: 64 tests, 184 signatures, DOL identity verified. See TESTING.

## Latest analysis correction (CAMP-H)

- Fixed a tracer soundness bug: repeated native queries now represent distinct
  observations, so a flag write cannot make a later feasible branch disappear as
  a false contradiction. Native reference arguments invalidate VM-local values.
- Three focused regressions include an independently executed mocked flag change.
  All97 tests pass; 240 signatures and nine runtime artifact hashes pass.
- Regenerated event report: 1338 finished local traces / 169 incomplete across
  1507 campaign scenes. Previous1334/173 counts are historical. No additional
  runtime, chapter-clear, progression or Netplay result is implied.

## Original Talk chain (CAMP-I)

- Reproducible tools.talk_audit follows actual MMM_TALK menu dispatch through
  adjacent occupancy enumeration and the kind8 conversation matcher. The
  inspected functions contain no faction comparison or force0 list traversal.
- Precomputed map direction-mask production, action/context gates, real Yellow
  conversation and prisoner cleanup remain open. No speculative patch added.
- Added reusable aligned direct-call references with explicit indirect-call
  limitation; signed/absolute/relative/wraparound regression cases.
- All99 tests pass; 264 original signatures match. Stable gameplay unchanged.

## Rejected restart redirect (CAMP-J)

- Extended isolated bootstrap with optional read-only native GCI copy/hash and
  explicit source chapter. Actual INI validates before creating the new profile.
- Runtime source7->11 on copied Ch6 restart **FAILED fixture acceptance**:
  RAM chapter11 but original Chapter6 title/map/Emil, no Chapter10 prisoners.
  Stable live C2 bodies matched. This is not a co-op gameplay failure.
- New prisoner-presence expectation rejects the candidate. Snapshot marks known
  active setup codes separately; expectations require explicit allow_synthetic.
- Diagnostic state/config hashes recorded; Chapter10 fixture INCONCLUSIVE.
  Immutable source and disposable card hashes unchanged; private Dolphin stopped.
- All103 tests pass; 264 signatures and nine accepted runtime artifact hashes pass.

## Second checkpoint (82e06d8, pushed)

- Instruction-aligned local CFG decoder: 2075 scenes / 125775 reachable local
  instructions across all scripts, no unknown opcode or invalid branch targets.
- Bounded symbolic predicates for C01..31: 1507 scenes; 1334 local traces finished,
  173 explicitly incomplete under bounds/unsupported operations. Native calls
  remain opaque; these are not world-state feasibility or gameplay results.
- Jill C21 scene 26: enemy transfer requires both Mist and Lethe relationship
  queries to differ from 3. Reyson C23 scene 25: force-6 setup requires an empty
  roster and Normal mode. Tests assert the decoded guards.
- 77 tests pass; 193/193 original DOL signatures match. Includes the script-only
  Ch6 escape model, synthetic DOL hook construction, and evidence claim gates.
- All 406 literal native script registrations recovered. Force-independent PID
  lookup and rescue-passenger UnitGet selector traced; native event activation open.
- Synthetic single-controller DTM builder uses a copied existing project recording
  settings header and refuses overwrite. Minimal settings caused a region warning;
  only the isolated process was stopped. No source configuration was changed.
- Offline DOL migration plan and synthetic-only patch construction implemented.
- Machine-readable verification ledger generates 34 chapter/stage status rows.

## Runtime evidence

- DTM playback restored the copied Prologue baseline. GUI Save State to File
  captured a fresh snapshot: chapter 1, phase 0, Ike's original state. Every intended
  COOP-P6 + EXP-16 C2 body matched live RAM, fingerprint 8609ae9f49fd879f.
- DTM synthetic A input remains INCONCLUSIVE. Native TAS Input succeeded in a
  later run: selected Ike, confirmed current tile, selected original Wait and
  observed enemy-phase Boyd dialogue. Fresh state phase 0 -> 1, Ike unchanged
  HP/lv/EXP/position; both states match all stable C2 bodies. prologue_smoke PASS.
  No Yellow-control, clear, transition, save/reload or Netplay claim. Processes stopped.

## Third checkpoint (d933312, pushed)

- 83 tests pass; 209/209 original DOL signatures match.
- Native Escape menu query traced: kind 5, coordinate pair, action 14 and pool key.
  Ch6 Escape tile (13,26); Ch10 tiles (6,2)/(7,2). No force read in this query,
  but a separate context veto and real Yellow execution remain to be tested.
- Generated native usage: 24032 calls, 327/406 native names used across 43 scripts.
  Escape/death counter helpers have no direct aligned script calls; indirect use open.
- State edits now bounded to complete MEM1, reject overlaps/empty edits; state
  writer creates exclusively; synthetic manifest records old/new bytes and hashes.
- New private bootstrap profiles for Ch6/10/17/Endgame; each 2536 Gecko bytes,
  empty private card. Construction passed; runtime NOT TESTED. No original roster
  or story prerequisites are manufactured. FIXTURES_AND_AUTOMATION.md records limits.

## Next independent work

1. Ch6 Yellow original single Escape now passed in synthetic setup (CAMP-G).
   Next: carried units, Ike-last completion and original cleanup/save paths.
2. Trace the remaining Escape context veto. Controlled original-positioning native
   calls may provide a supplemental synthetic event fixture; never skip Escape itself.
3. Improve frame stepping/recording. DTM input remains inconclusive; observed TAS
   controller holds work on both ports and GUI file capture is reliable.
4. Trace C11/C14/C19 conversation target eligibility before claiming Yellow recruits.
5. Expand per-event fixture requirements and coverage; later bootstrap destinations
   remain untested and may lack mandatory roster/story prerequisites.

## Fourth checkpoint (0fcaa64, pushed)

- 86 static/tooling tests; 222 signatures. Both runtime state artifact hashes checked.
- Decoded original kind-8 conversation actor/target, reversal and consumed key.
  Oscar/Kieran reversible; Astrid -> Gatrie directional; Jill/Shiharam alternatives
  share a key. Native matching compares character identity without a force read;
  upstream menu eligibility and actual recruitment remain unverified.
- Evidence PASS now requires explicit chapter/stage and axis scope. Missing or
  changed local artifacts fail the optional byte-verification command.
- Campaign matrix reads current runtime status from the same ledger/dashboard.

## Fifth checkpoint (50c2834, pushed)

- Original Ch9 fixture restored in private Dolphin. TAS port 1 ended Blue;
  port 2 selected normal tutorial No, native Lethe transformed into cat gauge20.
  Port 2 selected original Wait. Fresh captures: phase3/control3=1 remains;
  only Lethe acted bit changes. Mordecai and other captured fields unchanged.
- Both live stable C2 payload sets match. tools.partner_smoke PASS; 87 tests,
  222 signatures; four runtime artifact files hash-verified.
- Ch9 fixture/event axes accepted only for this synthetic partner smoke. Combat,
  gauge depletion, cleanup/recruitment, clear, transition, save/reload and Netplay
  remain open. No production code changed. Private process stopped.

## Sixth checkpoint (0706896, pushed)

- Fresh private-card boot -> original Ch6 restart -> prep -> Fight -> turn1,
  without a redirect or RAM edits. Captured accepted fixture; active roster is
  four Blue plus Yellow Oscar, Shinon/Gatrie away, Boyd absent. Live hooks match.
- Native private card SHA1 unchanged (54b5a7f4...), immutable ignored card copy
  retained. Earlier card history partly documented; not a natural-progress claim.
- Generic state_expect checks explicit fixture preconditions and rejects lost,
  duplicate/transferred characters or unknown fields. 89 tests/222 signatures;
  six local runtime artifacts hash-verified. Escape itself is still NOT TESTED.
- Short new DTM probe again failed to demonstrate A input; TAS remains the
  demonstrated automation route. All private Dolphin processes stopped.

## Seventh checkpoint validation

- Original port2 Oscar Escape menu > Yes > original speech ran in a controlled
  native-positioning fixture. Oscar preserved slot2, force3 -> force5, escaped
  flag set, HP28/lv6/EXP28 and all64 inventory-slot bytes unchanged. Same Chapter6
  continues turn2 with Ike on-map. Both full intended C2 sets match live RAM.
- First trial rejected: Emil occupied the gate, causing overlap. Corrected setup
  moves living boss to vacant adjacent tile, checks vacated exit, then Oscar;
  no kill/faction/escape/completion command injected. Total3168 Gecko bytes.
- Safe new-state C2 append verifies handler hash and exact stable list including
  dynamic branch-back targets; all non-Gecko payload bytes stay identical.
- Actual enabled-INI validator rejects truncated payloads, bad C2 return slots,
  missing names, conflicts and overflow for private generated codes too.
- 94 tests pass; 240 signatures; nine runtime artifact hashes checked. No native
  card write, production gameplay patch, chapter clear/transition/save or Netplay
  claim. All isolated Dolphin processes stopped.

No new gameplay assembly correction is accepted yet. Existing single-unit Escape
hand-back passed one synthetic original-event case; other assumptions still need
reachability/reproduction. No campaign completion,
next-chapter transition or new two-PC Netplay result is claimed.
