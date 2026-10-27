# Roadmap

Each milestone is done only when its completion criteria are demonstrated by a repeatable test in TESTING.md.

## Phase 0 — Research & environment validation  *(in progress: static work done, runtime baseline pending)*
- [x] Identify the image: GFEE01 rev 0 NTSC-U; record hashes (`tools/verify_game.py`).
- [x] Reproducible tooling: CISO/ISO reader, LZ77, pack, dispos parser, DOL disassembly helpers, tests.
- [x] Survey community resources and record what each actually demonstrates (RESEARCH.md §1).
- [x] Locate the faction model: unit table, force table, phase byte, **per-force control-mode byte** (RESEARCH.md §4).
- [x] Feasibility assessment and the smallest experiment (EXP-01).
- [ ] EXP-00 baseline confirmed at runtime in Chapter 9.

**Done when:** EXP-00 passes.

## Phase 1 — Controllable partner army (offline, one controller)
- [ ] EXP-01: Lethe/Mordecai selectable, movable, can act, and the phase ends, during the Partner Phase.
- [ ] Blue army unaffected.
- [ ] Fix whatever EXP-01 shows to be hard-coded to force 0 (menus, End command, auto-end, AI fallbacks).
- [ ] Convert the per-frame AR write into a robust Gecko patch that sets control at map init (hook `0x8014D920` path).

**Done when:** a full Ch9 playthrough with a human-driven partner phase, recorded in TESTING.md, with a Dolphin input movie (.dtm) as proof.

## Phase 2 — Independent controller ownership (local, two emulated pads)
- [ ] Find the game's pad read (US counterpart of PAL `0x802F98E8`).
- [ ] Patch: during `phase==3` the game reads port 2. During `phase==0` it reads port 1. Other ports are ignored outside their phase.
- [ ] Test with two Dolphin-emulated controllers (keyboard + XInput, or TAS input).

**Done when:** pad 1 cannot move yellow units, pad 2 cannot move blue units, both verified in one session.

## Phase 3 — Online (Dolphin Netplay)
- [ ] Host syncs codes and save. P1 → port 1, P2 → port 2 via pad mapping.
- [ ] Play Ch9 to completion online. Document desyncs, disconnects and save handling.

**Done when:** two machines finish Ch9 with no desync, with a written test log.

## Phase 4 — Campaign integration
- [ ] Roster ownership model (force assignment per character, persisted across chapters).
- [ ] Deployment for both players; chapters without natural partners (move owned units to force 3 at load via the dispos force byte or a loader hook).
- [ ] Recruitment, events, objectives, saves.

## Phase 5 — Quality & balance
Deferred until Phases 1–3 work.
