# Campaign investigation milestone — 2026-10-28

## Isolation and baseline

Work lives in a separate, non-hardlinked clone, `FireEmblemCampaignAudit`, on
`codex/campaign-compatibility`, based on `10d2496`. No changes or merges were made
to main, draft-ownership, Claude's profiles, original image or original saves.
The later `docs/HANDOFF.md` was read from the source checkout at `53fc0b6` and
copied here as a reference snapshot, without importing ownership code changes.
Ownership work is paused; PREP-03 passed, PREP-04/05/06/07 remain open.

Two baselines must stay separate:

- Stable release: main `6a81522`, COOP-P6 + EXP-16, 2536 Gecko bytes.
- Ownership candidate: `10d2496`, COOP-P6 + EXP-21 + EXP-25 + EXP-26,
  2928 bytes; PREP-03 test bed adds DBG-01 (2984). Not a stable campaign release.

The documented two-PC NET-02 gameplay used COOP-P5 + EXP-16; COOP-P6's cursor
addition passed locally afterward. Neither establishes current ownership Netplay.

## Confirmed tooling defects corrected

1. `netplay_setup --force` removed host/client folders before checking capacity.
   Reproduction uses a temporary profile with a sentinel GCI and an oversized
   selection. Validation now precedes deletion; the regression proves the GCI
   survives. No personal card was used for reproduction.
2. Direct `build_ini` callers, including package generation, bypassed capacity
   enforcement. The shared builder now rejects overflow and unknown code IDs.
3. C2 hook conflicts were accepted. The shared builder now rejects two enabled
   writers of the same C2 address (for example EXP-16 + EXP-21, or a package plus
   one of its component hooks). Adjacent/control-flow conflicts still need review.
4. Budget skip prediction incorrectly consumed space for a skipped code. It now
   models Dolphin's skip-and-continue behavior. Configurations with any skipped
   patch remain rejected regardless of which later small codes fit.
5. The old campaign labels mapped internal 29 to Chapter 28 and internal 31 to
   Chapter 30. Names now come from the game message table: 29 is Ch.27-2,
   30 is Chapter 28, and 31 is Endgame. The full inventory includes suffix maps,
   C00, special C80..96 containers, startup and ending.
6. The prior literal decoder put unresolved arguments AFTER known suffixes.
   A computed unit followed by literal force 0 was represented [0, unknown],
   instead of [unknown, 0]. The bounded decoder preserves suffix position and
   file order and does not scan the string pool as executable code.

No gameplay assembly or ownership generator changed. No campaign gameplay bug
is claimed fixed by these tooling corrections.

## Prioritized engine and campaign research

| Priority | Finding | Evidence | Status / next valid test |
|---|---|---|---|
| P1 | Individual Escape: synthetic local PASS, carried/cleanup runtime untested | CAMP-001/003 below | Escape an owned Yellow at (13,26) in Ch6, then Ike last; clear, save and reload Ch7. Mask helpers exclude Yellow but have no direct script calls in all 43 containers |
| P1 | Full-campaign event semantics remain unresolved | CAMPAIGN_MATRIX and JSON checklist | Decode condition records/branches and test actual interactions; command presence is not proof |
| P1 | Native Yellow becomes human whenever force 3 is nonempty | EXP-08/07/14; F-18/F-29 | Ch9 partners, Ch10 prisoners, Tanith reinforcements and late partners need separate behavior decisions and acceptance |
| P1 | Player classification uses deployed-player flag 0x400 | F-43/F-45, EXP-18/19 | Newly recruited P2 units may lack this bit until next map; test recruit, ownership, death and roster preservation |
| P1 | Multiplayer persistent campaign saving is not accepted | netplay_setup WriteSaveData=False | Use private card copies to establish intended host write-back and fresh-session resume; test modes currently discard writes |
| P2 | Ownership bits coexist with story transfers | EXP-21 moves only force 0/3 | Test Shinon and Jill after original conditions, including save/reload during unavailability; do not force-complete flags |
| P2 | List slot counts are not simultaneous forced roster counts | Ch5 9 scripted forced PIDs vs 8 slot entries | Reconstruct branch/phase membership and final roster; negative optional-slot counts removed |
| P2 | Generic script flag setters can use supplied masks | F-52 | Symbolically trace masks, including computed arguments, before claiming ownership bits universally unused |

### CAMP-001: escape masks — verified static, runtime impact unproven

`PlayerEscapeCount` at 0x801B7188 and `PlayerEscapeCheck` at 0x801B7260 build the
mask [1,0,0,0,0,1,0,0] using 0x800152F8. This includes Blue and roster, excludes
Yellow. They inspect unit flag 0x4000 (PPC mask bit 17); one counts escaped units,
the other returns false for an included unit lacking that flag. Eight exact
instructions are pinned in check_signatures; tests independently verify mask
construction. See the captured disassembly procedure below.

This confirms routine behavior, NOT a reproduced Ch6 failure. No direct branch
caller was found in the DOL scan, and the chapter's local escape handler does not
call either helper by that command name. The full aligned scan now finds neither
helper in any of the 43 script containers (NATIVE_USAGE.md). Their indirect normal
reachability is open.
Patching an unused helper would add bytes without demonstrating campaign benefit.

C07 function 1 reads MindGetMe, resolves Ike, reads/updates BM variable 4, runs
TalkEvent/DefaultEscapeTalk, moves/fades the escaping unit, calls UnitEscape at
file offset 0xE66, then has gf_complete setters at 0xE76/0xE86. Local branch/model
analysis now shows completion only for Ike or a unit carrying Ike; carried units
increment the escape count separately. Scene 2 calls this helper from the original
kind-5 Escape tile at (13,26). Original menu availability queries the same event
kind and coordinates without a force read (CAMP-003); a separate context veto and
normal runtime execution still need testing. The existing
ownership UnitEscape hand-back remains the roster-preservation mechanism to test.

### Native factions and important ordering

- **Ch9 / C10:** Lethe and Mordecai are native force-3 units. EXP-21 does not
  permanently assign them, but COOP control/EXP hooks still affect them. Retest
  laguz transformation, remaining-unit behavior, cleanup and eventual recruitment.
- **Ch10 / C11:** Kieran's force-3 transfer is in function 29 at 0x2C5B, after
  TalkEvent MS_11_TK02. Function 57 contains computed-unit transfers back to Blue.
  Brom/Nephenee have their own paths. CAMP-013 now executes original Talk and
  direct/carried escape branches plus120 cleanup-prefix cases offline. The original
  startup existence helper accepts forces0..3. Non-Maniac open-door/non-escaped
  fallback returns qualifying prisoners to Blue before AllUnitEscape. Native
  cleanup/permanent recruitment/save behavior remains unverified.
- **Ch13 / C14:** Naesala/Nealuchi go to force 3 at 0x319D/0x31A7 in function 54.
  Later in the SAME function are force-2 escape iteration, force-1 crow checks,
  ending conversations, AllUnitEscape, UnitsPush_Uninitialize and UnitsPop.
  This is strong ending-event context. It does not prove a normal playable
  partner phase exists between those transfers and cleanup. Astrid/Gatrie and
  Green Begnion allies require independent recruitment/survival tests.
- **Ch17 / C18:** both bmap18 and bmap18_3 exist. Complete18 calls with literal
  stages 1/2/3 appear at 0x57C4, 0x5F00 and 0x713A. Following functions reset turn
  to 1 at 0x57F2/0x5F2E/0x7166 and reload bmap18. All four stages need separate
  status, acted/upkeep/event checks, carried inventory and roster checks. Suffix
  maps alone do not map one-to-one to gameplay stages.
- **Ch18 / C19:** Shinon's away/Blue/enemy transfers occupy different functions,
  not one unconditional sequence. Test the original conversation and battle
  requirements and subsequent ownership restoration. Tanith/Reinforce's native
  partner lifecycle is not yet traced; PID_MELTY appearing as force 3 does not
  prove when or how it is spawned.
- **Ch19 / C20:** Naesala appears in force-2 groups and scripted transfers. Test
  the original raven dialogue/withdrawal conditions. Green is not ownership.
- **Ch20 / C21:** Jill's enemy transfers are at 0x21B1 and 0x22BD in separate
  functions 26/27. Preceding calls query PersonGetYellLevel with Mist and Lethe
  and branch into different conversation messages. These support conditional
  relationship-related paths, not an unconditional Jill defection. Exact
  predicates are now decoded: scene 26 requires BOTH Mist and Lethe query values
  to differ from 3 (CAMPAIGN_EVENTS.md). The gameplay interpretation of value 3
  and the separate scene 27 activation still require confirmation.
- **Ch22 / C23:** Reyson -> 6 at 0x1910 is in function 25, preceded by a DBG flag
  query, roster count and always_dbg_mik_* Join calls. This may be fixture/debug
  setup rather than a normal story death. Do not equate force 6 with a confirmed
  permanent death; compare death flags and chapter record, trace reachability.
- **Ch23/24 / C24/C25:** dispositions include Green Lucia/Bastian/Geoffrey and
  generic allied actors, plus native Yellow groups. Track original survival and
  relief/arrival events separately from ownership translation.
- **Ch27-2 / C29:** a separate special encounter, not Chapter 28. Test forced
  availability, unusual completion/escape branches and which result selects the
  next chapter's roster. Preserve Ike's original role.
- **Endgame / C31:** MapLoad bmap31_2 at 0x5691 and bmap31_3 at 0x6D83/0x8382
  demonstrate extra scripted maps. They must not be omitted or assumed separate
  playable battles without tracing. Verify final boss phases, native allies,
  final cleanup, ending.cmb and saved completion progression.

## Accelerated regression workflow

1. Copy a known project test card/profile into this clone only; retain its hash.
   Record source commit, DOL hash, Dolphin version and enabled-code fingerprint.
2. Validate the configuration BEFORE profile creation. Production configurations
   exclude DBG codes. Fresh boot is required for new codes: states restore old
   patches. Record intended INI separately from observed live hook instructions.
3. Reach the original interaction. DBG-01/02, or a labelled position/movement
   fixture, may accelerate setup; never set completion/recruitment flags as proof.
4. Capture states before/after with a unique run ID and original gameplay outcome.
   `tools.campaign_snapshot` captures identity, owner, force, coordinates, HP,
   level, EXP, gauge, flags and death record. It labels INI configuration as
   intended, not proof that an old state applied it.
5. For Netplay, compare snapshots at the same turn/phase using --compare. A
   match covers captured fields only, not all RAM, RNG, inventory or event flags.
6. Compare events before/after with explicit expectations; for transitions inspect
   surviving, dead and away characters. Then clear the chapter, save and fresh
   reload the next chapter. Maintain each acceptance axis separately.
7. Retest fixes without debug acceleration. Two instances and two PCs are distinct
   runs; do not claim the latter from local testing.

Example capture: `python -m tools.campaign_snapshot STATE --ini PROFILE/GameSettings/GFEE01.ini --out work/RUN/after.json`.
Comparison: `python -m tools.campaign_snapshot --compare work/RUN/host.json work/RUN/client.json`.

## Runtime automation attempt and blockers

The Computer Use skill's supported Windows API was available. A copied Dolphin
2609a installation, copied image and copied NET-02 card were booted in this clone.
The game reached the title sequence. Synthetic Return/X taps did not reliably
operate the title menu; Shift+F2 produced no state file. No chapter, original
objective, save/reload or Netplay acceptance is claimed. The isolated executable
was stopped by exact path; existing source-checkout Dolphin processes were untouched.

Next method: map/verify a reliably held controller input in the isolated profile,
or use a supported deterministic Dolphin input movie verified at the title/menu
before campaign use. Until demonstrated, tester-captured prep and event states
remain the reliable fixture source. No unsafe input helper was introduced.

## Continuation

First: decode C07's escape-event branch predicates and obtain before/after Yellow
escape states; that also supplies PREP-04's Ch7 fixture. Next, reach a genuine
bench chapter without raising caps. Then prioritize C11 prisoners, C18's four
stages, C19 Shinon, C21 Jill, C29 and Endgame. The generated matrix covers every
chapter as an evidence index; its 15 semantic checklist fields are intentionally
unresolved where research is incomplete. This milestone is not a completed full
campaign compatibility audit.
