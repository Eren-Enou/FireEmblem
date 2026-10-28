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

1. Commit conversation metadata and stronger evidence-scope/artifact validation.
2. Repeat the TAS action path with deterministic frame stepping/recording; DTM
   polling issue remains open, and GUI control still needs observation.
3. Trace the remaining Escape context veto and test Yellow original-menu eligibility.
4. Expand per-event fixture requirements and risk coverage beyond script strings.
5. Improve verification provenance and artifact checks as runtime evidence grows.

## Fourth checkpoint validation

- 86 static/tooling tests; 222 signatures. Both runtime state artifact hashes checked.
- Decoded original kind-8 conversation actor/target, reversal and consumed key.
  Oscar/Kieran reversible; Astrid -> Gatrie directional; Jill/Shiharam alternatives
  share a key. Native matching compares character identity without a force read;
  upstream menu eligibility and actual recruitment remain unverified.
- Evidence PASS now requires explicit chapter/stage and axis scope. Missing or
  changed local artifacts fail the optional byte-verification command.
- Campaign matrix reads current runtime status from the same ledger/dashboard.

No gameplay assembly correction is accepted yet: identified engine assumptions
still require normal-path reachability/reproduction. No campaign completion,
next-chapter transition or new two-PC Netplay result is claimed.
