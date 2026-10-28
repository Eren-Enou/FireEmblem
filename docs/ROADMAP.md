# Roadmap

Each milestone is done only when its completion criteria are demonstrated by a repeatable test in TESTING.md.

## Development direction (authoritative, user 2026-10-28)

**Long-term objective:** a complete, stable, replayable two-player Path of Radiance campaign, plus optional features that make cooperation more enjoyable.

| Priority | Area | Branch | State |
|---|---|---|---|
| **1** | **Character drafting, ownership and deployment**: draft clarity, prep-screen integration, persistent ownership, voluntary transfers, fair per-chapter deployment | `draft-ownership` | **Active.** Ownership storage and the in-battle draft verified (DRAFT-01). Draft v2 (EXP-23) awaiting DRAFT-02 |
| **2** | **Complete campaign compatibility**: every chapter's events, victory conditions, recruitment, scripted transfers, progression, death, saving and phase behaviour | all | Overarching requirement. `tools/chapter_audit.py` covers all chapters statically; runtime verified: Prologue, Ch1–Ch5, Ch9, Ch6 partly (docs/CHAPTER_AUDIT.md) |
| 3 | Optional alternating-unit actions; sequential turns stay the default, with a mode switch only if safe | `experiment/alternating-actions` (never merged until proven) | Parked after static research. EXP-24 + ALT-01 ready (docs/ALTERNATING.md on that branch) |
| 4 | Optional shared tactical board: a separate companion interface (markers, notes, movement plans, EXP targets) that never touches the game simulation or Netplay, and is never required | none yet | Not started |

**Working rules:**
- Work on one priority at a time. Priority 2 work rides along where Priority 1 touches a chapter.
- Priorities 3 and 4 are not developed further until Priority 1's next milestone is done.
- `main` is the **known-good stable Netplay release**: COOP-P6 + EXP-16, package net02-3, NET-02 passed. It changes only by merging verified work.
- The friend ZIP is rebuilt reproducibly from `main` (`tools/netplay_package.py`).
- Experiments stay on their own branches until proven.
- Reliable gameplay before features. The smallest safe implementation that validates an idea before any complex UI or redesign.
- The game image and user saves are read-only.
- Every behaviour is labelled **working** (a passed TESTING.md entry), **experimental** (experiment branch) or **unverified** (static only).

### Next concrete milestone: PREP-01 — draft and deployment during preparations (Priority 1)
**Status (2026-10-28):** Milestone A (research) done statically; plan in **docs/PREP.md**.
- Pick Units = `E_SallyList`; "picked" = flag `0x80000000` toggled by `0x8012C9E8`.
- Cap = `state+0x544`; the audit now lists caps and forced units for every chapter.
- First non-forced chapter: Ch8; first likely bench: Ch10.

Next: Step 2, ownership shown in the Pick Units rows (runtime research needed first: the row-state visuals and the list's current-row field).
Move the verified in-battle draft (DRAFT-01/02) to where players naturally choose units: the chapter's preparation screen. Each player owns characters and picks who deploys, under the chapter's original deployment cap.

Steps, in order (each closes with a TESTING.md entry):
1. **Find a real choice.** Extend `tools/chapter_audit.py` to list, per chapter: the deployment cap, the forced PIDs (`UnitForcedSally*` arguments, decoded like the transfers, F-48), and the recruited roster at that point. Name the first chapter where optional slots exist (F-46: Ch3, Ch4 and Ch6 force every candidate).
2. **Map the prep screen.** Trace the original "Pick Units" flow: the sally (sortie) list (`BMapSallyCursorProc` and the `Sally*` script commands), where a unit's deployed state is toggled, and how the cap is enforced. Record it as F-entries with pinned signatures. Reuse the native list and cursor, not a new menu.
3. **Ownership in the prep list.** Show and change ownership on the prep unit list with the same L+R claim/release and alternating picks as EXP-23. Ownership already persists in the unit flag word (F-52), so this adds a second place to edit it, not new storage.
4. **Fair deployment split.** Within the original cap: the mandatory (forced) units count first, then the optional slots alternate P1, P2, P1, … Each player may only toggle their own characters. An odd slot goes to the player with fewer deployed units (Player 1 on a tie). Chapters with no optional slots skip the split. No cap is raised.
5. **Acceptance (PREP-01):** on one PC in the chosen chapter:
   - both players draft and deploy in prep
   - a benched owned character keeps their ownership and progression
   - the battle starts with blue and yellow as chosen
   - chapter end and a reload keep everything

   Then the same over two Dolphin instances (Netplay), then two computers.

Out of scope for PREP-01: owner-to-owner transfers with both players' consent (the next Priority 1 milestone after PREP-01), lifting the Ike-is-Player-1 rule, and any changes to Priorities 3 and 4.

---

## Phase 0 — Research & environment validation  *(done 2026-10-27)*
- [x] Identify the image: GFEE01 rev 0 NTSC-U; record hashes (`tools/verify_game.py`).
- [x] Reproducible tooling: CISO/ISO reader, LZ77, pack, dispos parser, DOL disassembly helpers, tests.
- [x] Survey community resources and record what each actually demonstrates (RESEARCH.md §1).
- [x] Locate the faction model: unit table, force table, phase byte, **per-force control-mode byte** (RESEARCH.md §4).
- [x] Feasibility assessment and the smallest experiment (EXP-01).
- [x] Runtime baseline confirmed from decoded save states (EXP-00 A; Prologue and Chapter 9).

## Phase 1 — Controllable partner army (offline, one controller)  *(core achieved 2026-10-27)*
- [x] Chapter 9 test fixture (EXP-05).
- [x] Non-blue human control proven (EXP-04, red army).
- [x] EXP-01: Lethe/Mordecai selectable, movable, can act (including transform) during the Partner Phase; locked in Player Phase.
- [x] EXP-06: no cross-control (blue locked in yellow phase), with blue unaffected on turn 2.
- [x] Leftover-unit behaviour (F-18): leftover yellow units **wait** (user decision). EXP-07 fully verified (A a–d, and vanilla control B).
- [x] Packaged as **COOP-P1** (EXP-08 phase-advance control hook + EXP-06 + EXP-07; no per-frame write). EXP-08 A passed at runtime (B, the Prologue check, not yet reported).
- [x] EXP-09: recorded a multi-turn Ch9 run with COOP-P1 (`work/movies/ch9_coop_p1.dtm`); the map was lost. Completing Ch9 is deferred to Phase 4 with a real army (recommendation).
- [x] Partner progression (user requirement): EXP-10 (CanGainExp), EXP-11 (GetExp), EXP-12 (battle write-back) and EXP-13 (level-up/result screen unit pickers). Verified at runtime: kill EXP, enemy-phase counter EXP, accumulation over turns, level-up (lv 3 → 4, stats grow, no crash). Blue EXP is unchanged and vanilla is unchanged with codes off (TESTING.md "EXP-13 / COOP-P2").
- [x] Packaged as **COOP-P2** = COOP-P1 + EXP-10..13 (one Gecko code; the parts stay for debugging).
- [ ] Still open: the stat-gain panel itself, the Direct command with human yellow, a real battle save/load round trip.

**Done when:** a full Ch9 playthrough with a human-driven partner phase, recorded in TESTING.md, with a Dolphin input movie (.dtm) as proof.

## Phase 2 — Independent controller ownership (local, two emulated pads)
- [x] Find the game's pad read: `PADStatus[4]` at `0x802EF408`, pad objects `0x802EF438`, current-pad pointer `0x80367240` (F-29).
- [x] Patch **EXP-14**: in a human yellow phase the game reads port 2; otherwise port 1. If port 2 has no controller, it falls back to port 1. Packaged as **COOP-P3** = COOP-P2 + EXP-14.
- [x] Local test with two keyboard-emulated controllers on one PC (`tools/setup_pads.py`): over two full turns each army answered only to its own port (TESTING.md "EXP-14 / COOP-P3").
- [x] Tester run with two keyboard-emulated controllers: PASS (2026-10-27). Port 2 stick now on the numpad.
- [ ] Still open: attacks/battle-animation skipping and the Start menu on controller 2, and a real gamepad.

**Done when:** pad 1 cannot move yellow units, pad 2 cannot move blue units, both verified in one session. *(Met with keyboard-emulated pads.)*

## Phase 3 — Online (Dolphin Netplay)
- [x] Chapter 9 start without save states: a native memory-card save, "Ch. 9: Gallia" (NET-00, F-31).
- [x] Reproducible host/client setup: `tools/netplay_setup.py` (private `--user` folders, F-32).
- [x] NET-01: one-PC loopback session (Claude, 2026-10-27): codes and save synced, P1 → GC1 and P2 → GC2, two turns in lockstep, no cross-control, identical game state in both instances.
- [x] Shareable Player 2 package: `tools/netplay_package.py` builds a ~7 KB ZIP (README with setup and checklist, private user folder, codes, manifest, code fingerprint), with no game, save data, Dolphin or launcher (net02-2). Verified at runtime on one PC over Direct (NET-02, 2026-10-27).
- [x] NET-02 on two computers via the Traversal Server room code (user + friend, 2026-10-27): Ch3 to turn 6 with combat and EXP, identical states on both PCs, no desync; Buffer 18 needed for full speed (F-50). The disconnect test was only run on one PC.
- [ ] Play Ch9 to completion online. Document desyncs, disconnects and save handling.

**Done when:** two machines finish Ch9 with no desync, with a written test log.

## Phase 5 — Character drafting, persistent ownership and deployment (Priority 1; branch `draft-ownership`)
- [x] **A. Ownership architecture** (static): ownership in the unit flag word, bits 0x20000000/0x40000000, saved raw with the character (F-52). EXP-21 translates it to forces with EXP-16's hooks; no table is regenerated.
- [x] **B. First in-game draft:** EXP-22, L+R on a deployed unit at turn 1, alternating picks, release = undo. **DRAFT-01 PASSED** (user, 2026-10-28, all seven checks).
- [ ] **C. Persistence and transfers:** survives chapter end, normal save and fresh reload (**DRAFT-01 PASSED**); owner-to-owner transfer with both players' consent (not started).
- [ ] **A2. Draft clarity:** EXP-23 (draft v2): green rings = unassigned, blue/yellow = owner, four distinct sounds incl. a refusal buzz, the draft ends at the first action. Whose pick is shown by counts plus the buzz. A pick-coloured cursor still needs research (F-54). Runtime test DRAFT-02 pending.
- [ ] **D. Deployment integration = PREP-01** (see the top of this file): prep-screen draft, fair split of optional slots under the original cap, benched owned characters kept.
- [ ] **E. Netplay acceptance:** the full workflow over two instances, then two computers.

**Done when:** two players draft, deploy, transfer and carry their own armies through chapters in-game, with no source edits, over Netplay.

## Phase 4 — Campaign integration (sequential two-army campaign from Chapter 1)
Design (user, 2026-10-27): strictly sequential phases (blue P1 → yellow P2 → enemy AI → green), reusing the game's phase system and COOP-P3 routing. Each character belongs to one player at a time and keeps their identity and progression. Ike stays blue.
- [x] Found the game's own force-transfer path: `UnitTransferToForce`, `SetUnitForce`, unit by PID (F-34). Chapter end moves only force 0 into the roster (F-35).
- [x] **Chapter-level proof, EXP-15 (fixed assignment), PASSED 2026-10-27 (v3):** Blue = Ike, Titania / Yellow = Boyd, Oscar in Chapter 1. Verify phases, ports, combat, EXP, victory/defeat/events, and the transition to Chapter 2 with no lost or duplicated characters. *(v1 and v2 lost Boyd and Oscar at the seize, through `AllUnitEscape` (F-39). v3 passed: Chapter 2 starts with Ike, Oscar (lv 4, 35 EXP), Boyd (47 EXP) and Rhys. Still unchecked: defeat (Game Over), a yellow unit dying, and Ch1 events on hard paths.)*
- [x] Separate ownership from tactical force: **EXP-16**, an ownership table (PID → player) generated by `tools/owner_code.py`, applied at every player-phase start in any chapter, and returned at every chapter-end path found plus single-unit escape. Storage: embedded in the code, so it is Netplay-synced and nothing is written to saves (RESEARCH "Ownership storage"). *(Run 1 passed through the Ch4 start, with automatic yellow in Ch2; Ch3–4 had forced all-blue line-ups.)*
- [x] **Milestone: Chapters 1–3** with two armies and automatic ownership between battles: Ch1 (EXP-15), Ch2–Ch4 and the Ch5 start (EXP-16), 2026-10-27. Yellow armies in every chapter, progression kept, no duplicates.
- [x] Player 2 characters treated as player units: Base Data (EXP-18), death record (EXP-19), EXP shown from turn 1 (EXP-16 `control[3]`). Package **COOP-P5**.
- [ ] Flexible deployment on a prep screen (needs a chapter whose script does not force every candidate; F-46).
- [x] Auto-end and Next Unit for the yellow phase: EXP-17 passed (F-42). Package **COOP-P4** = COOP-P3 + EXP-17; install it with EXP-16 (the ownership table).
- [ ] Edge cases 1–13 (TESTING.md "Edge-case status"), especially yellow death, Battle Save, recruitment, and the escape/death count commands (F-40).
- [ ] In-game assignment storage (option B or C) for the future assignment screen.
- [ ] Chapters with preparations/deployment, recruitment (new units default to blue), story events that move units, and battle saves.
- [ ] Pre-chapter assignment screen (only after fixed assignments and transitions are proven).

**Done when:** Chapter 1 is completed with two separately commanded armies and Chapter 2 starts normally, with every character's progression and assignment preserved.

## Later — Quality & balance
Deferred; reliable gameplay first.

## Priority 3 / 4 records
- Alternating actions: branch `experiment/alternating-actions` (its docs/ALTERNATING.md and TESTING.md ALT-01). Parked; runtime untested.
- Shared tactical board: not started. It must stay a separate companion that is never needed to finish a chapter and never touches the emulated game or Netplay.
