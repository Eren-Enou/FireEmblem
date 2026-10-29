# Campaign verification dashboard

PASS applies only to the named axis and evidence configuration. Parser/model passes do not imply gameplay. Old release reports remain in TESTING.md and are not promoted here. A fixture is runnable only after acceptance, not merely because a file exists. Ch17 stages share a script; stage-specific map assignment is still unresolved.

| Chapter/stage | CFG | Script model | Fixture | Original event | Cleared | Transition | Save/reload | Netplay local | Netplay two PCs |
|---|---|---|---|---|---|---|---|---|---|
| Prologue: Mercenaries | PASS | NOT TESTED | PASS | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.1: The Battle Begins | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.2: Rescue | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.3: Pirates Aground | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.4: Roadside Battle | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.5: Flight! | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.6: A Brief Diversion | PASS | PASS | PASS | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.7: Shades of Evil | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.8: Despair and Hope | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.9: Gallia | PASS | NOT TESTED | PASS | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.10: Prisoner Release | PASS | NOT TESTED | PASS | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.11: Blood Runs Red | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.12: A Strange Land | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.13: A Guiding Wind | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.14: Training | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.15: The Feral Frontier | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.16: The Atonement | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.17: Day Breaks stage 1 | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.17: Day Breaks stage 2 | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.17: Day Breaks stage 3 | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.17: Day Breaks stage 4 | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.18: Crimea Marches | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.19: Entrusted | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.20: Defending Talrega | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.21: Without a King | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.22: Solo | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.23: The Great Bridge | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.24: Battle Reunion | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.25: Strange Lands | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.26: Clash! | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.27: Moment of Fate | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.27-2: Moment of Fate | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.28: Twisted Tower | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Endgame: Repatriation | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |

## Evidence runs

- **cfg-02**: `static`; All 2075 scene CFGs across 43 containers decode; parser checks only; source GFEE01 rev0 DOL hash anchored.
- **escape-model-02**: `script_model`; Four C07 original escape-scene cases with mocked natives: actor, passenger, Ike, carried Ike; no Dolphin claim.
- **fixture-prologue-02**: `dolphin`; Copied Prologue restored in isolated Dolphin; original-unit state captured via UI Save State to File. All intended stable C2 bodies matched live RAM. No unit action demonstrated.
- **prologue-wait-03**: `dolphin`; Native Computer Use toggled port-1 TAS A, selected current tile, moved menu to Wait and confirmed. Enemy-phase Boyd dialogue observed. Capture phase 0 -> 1; Ike unchanged HP/lv/EXP/position; live stable C2 bodies match in both snapshots. prologue_smoke PASS. Analysis/tooling worktree dirty; production codes unchanged.
- **ch9-partner-wait-05**: `dolphin`; Restored copied historical EXP-05 Chapter 9 fixture. Ended Blue phase with TAS port 1; port 2 selected normal tutorial No. Lethe transformed to JID_CAT/F gauge20. Port 2 selected original Wait. Captures phase3/control3=1; only Lethe acted bit changes, other captured fields identical. All stable C2 bodies match live RAM. No combat, clear, cleanup, native recruitment, save/reload or Netplay claim.
- **ch6-native-start-06**: `dolphin`; Fresh boot from private NET02 card copy, original Restart Chapter Ch6, normal Start skips of opening dialogue, preparations Fight/Begin Yes. No redirect or RAM edits. Turn1 Blue snapshot has Oscar Yellow, 4 Blue, Shinon/Gatrie away, Boyd absent; all stable live hooks matched. state_expect campaign/fixtures/ch6_start.json PASS. Private card SHA1 unchanged 54b5a7f400b9ec68b6e315a0b2b89a78e5b7218d. Prior card history includes earlier debugging; no natural progression or Escape acceptance inferred.
- **ch6-yellow-escape-07**: `dolphin`; DBG-CAMP-POS guard moves living Emil from exit13,26 to vacant13,25 and Oscar from14,9 to13,26 through original UnitSetPos. No death/faction/completion command injected. Native port2 selects Oscar -> Escape -> Yes, observes original Oscar dialogue. Original event preserves slot2 in force5, escaped flag0x4000, HP28/lv6/EXP28 and all64 inventory-slot bytes. Chapter7 continues turn2 with Ike on-map. All stable and setup C2 bodies match RAM. 3168 Gecko bytes. First overlapping-tile fixture rejected; no gameplay fix or natural-route/clear/save/Netplay claim.
- **ch10-restart-redirect-rejected-10**: `dolphin`; REJECTED fixture route source7->target11 from copied native Chapter6 restart. RAM chapter11 but original Chapter6 title/map/Emil loaded; all three Chapter10 prisoners absent. Stable C2 bodies matched. state_expect prisoner presence FAIL. No Chapter10 event tested. Original/copied card SHA1 unchanged; private Dolphin stopped. Chapter byte is insufficient to identify a loaded scenario.
- **ch10-loader-manual-wait-12**: `dolphin`; Human restored and validated Chapter10 synthetic loader fixture; reported original Blue->Yellow, P2 Oscar Wait and P1 command lockout PASS without unusual behavior. Captures corroborate loaded C11.cmb, all live stable+loader C2 bodies, chapter11/turn1/phase0->3/control3=1, Oscar force3/slot2 at2,19, flags400->401 and unchanged HP28/lv6/EXP28/inventory. P1 lockout is human-reported, not established by these RAM fields. No prison traversal, original Talk, permanent recruitment, escape, clear/transition/save or Netplay claim. This configuration is separate from the new inside-cell Talk candidate.

## Highest-priority open cases

- Ch6 carried units and Ike-last completion, cleanup/transition and fresh native reload remain unverified; single Yellow Escape passed only in synthetic positioning fixture.
- Ch9 native partners: combat EXP, partner cleanup/eventual recruitment and natural chapter history remain unverified.
- Ch10 prisoner conversations, temporary Yellow and exit conditions.
- Ch17 all four stage transitions, reinforcements, turn resets and ownership.
- Ch18 Shinon and native Reinforce partners; Ch20 Jill branch conditions.
- Ch27-2 and Endgame special transitions; accepted multiplayer save workflow.
