# Campaign verification dashboard

PASS applies only to the named axis and evidence configuration. Parser/model passes do not imply gameplay. Old release reports remain in TESTING.md and are not promoted here. A fixture is runnable only after acceptance, not merely because a file exists. Ch17 stages share a script; stage-specific map assignment is still unresolved.

| Chapter/stage | CFG | Script model | Fixture | Original event | Cleared | Transition | Save/reload | Netplay local | Netplay two PCs |
|---|---|---|---|---|---|---|---|---|---|
| Prologue: Mercenaries | PASS | NOT TESTED | PASS | INCONCLUSIVE | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.1: The Battle Begins | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.2: Rescue | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.3: Pirates Aground | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.4: Roadside Battle | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.5: Flight! | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.6: A Brief Diversion | PASS | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.7: Shades of Evil | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.8: Despair and Hope | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.9: Gallia | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.10: Prisoner Release | PASS | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
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

## Highest-priority open cases

- Ch6 Yellow individual escape, Ike last, transition and fresh reload (natural campaign).
- Ch10 prisoner conversations, temporary Yellow and exit conditions.
- Ch17 all four stage transitions, reinforcements, turn resets and ownership.
- Ch18 Shinon and native Reinforce partners; Ch20 Jill branch conditions.
- Ch27-2 and Endgame special transitions; accepted multiplayer save workflow.
