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

## Second checkpoint validation

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
- Synthetic A input did not demonstrate unit selection/action. This remains
  INCONCLUSIVE. No later-chapter fixture accepted. All isolated processes stopped.

## Next independent work

1. Commit the validated second checkpoint.
2. Prove a DTM-driven unit action and capture/compare a state; otherwise retain
   explicit blocker and pursue fixture/bootstrap research independently.
3. Trace native force-0 event eligibility, especially actual Ch6 escape reachability.
4. Expand per-event fixture requirements and risk coverage beyond script strings.
5. Improve verification provenance and artifact checks as runtime evidence grows.

No gameplay assembly correction is accepted yet: identified engine assumptions
still require normal-path reachability/reproduction. No campaign completion,
next-chapter transition or new two-PC Netplay result is claimed.
