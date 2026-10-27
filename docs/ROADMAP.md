# Roadmap

Each milestone is done only when its completion criteria are demonstrated by a repeatable test in TESTING.md.

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
- [ ] NET-01: one-PC loopback session (tester). Host syncs codes and save. P1 → port 1, P2 → port 2 via pad mapping.
- [ ] Play Ch9 to completion online. Document desyncs, disconnects and save handling.

**Done when:** two machines finish Ch9 with no desync, with a written test log.

## Phase 4 — Campaign integration
- [ ] Roster ownership model (force assignment per character, persisted across chapters).
- [ ] Deployment for both players; chapters without natural partners (move owned units to force 3 at load via the dispos force byte or a loader hook).
- [ ] Recruitment, events, objectives, saves.

## Phase 5 — Quality & balance
Deferred until Phases 1–3 work.
