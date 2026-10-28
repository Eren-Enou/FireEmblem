# Campaign event predicates

Static local CFG/symbolic analysis. Native calls are opaque; event registration, scene activation, global effects, world-state feasibility and gameplay are NOT proven. Infeasible combinations may remain; exact repeated contradictory predicates are pruned. Incomplete traces may omit later events. Full evidence is in ignored work/event_paths.json.

VM format corroboration: https://feuniverse.us/t/fe9-and-fe10-event-script-doc-notes/6143. Signed operands and interpreter dispatch were independently read from this game's DOL.

Totals: {'functions': 1507, 'instructions': 106136, 'complete_local_traces': 1334, 'incomplete_local_traces': 173}

## Prologue: Mercenaries — Scripts/C01.cmb

### Scene 6: function_6

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x16D7 UnitTransferToForceByPID('PID_BOLE_MAP1', 2)`: 2 explored alternative(s). Example local guards: get('ボーレ死亡') != 0 AND !(get('グレイル参戦')) != 0 AND get('ボーレ死亡オンバト') != 0.
- `0x1850 UnitTransferToForceByPID('PID_GREIL_MAP1', 1)`: 8 explored alternative(s). Example local guards: get('ボーレ死亡') != 0 AND !(get('グレイル参戦')) != 0 AND get('ボーレ死亡オンバト') != 0 AND Normal() != 0 AND Comeback() != 0.

### Scene 13: function_13

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 14: function_14

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [759]}`. Local trace: all explored local paths returned

- `0x19F6 set('gf_gameover')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.

### Scene 18: function_18

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [792]}`. Local trace: all explored local paths returned

- `0x1B12 set('gf_complete')`: 2 explored alternative(s). Example local guards: (GetBattleType() & -2147483648) != 0.

### Scene 19: function_19

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [1741]}`. Local trace: all explored local paths returned

- `0x1C70 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !(get('グレイル死亡オンバト')) != 0.

### Scene 20: function_20

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 21: function_21

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 22: function_22

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 23: function_23

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


## Ch.1: The Battle Begins — Scripts/C02.cmb

### Scene 0: function_0

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [8, 5, 13, 0], 'tile_event': {'x': 8, 'y': 5, 'action_code': 13, 'key_pool_offset': 0, 'key': ''}}`. Local trace: all explored local paths returned

- `0xBE6 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 1: function_1

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [4, 11, 9, 17], 'tile_event': {'x': 4, 'y': 11, 'action_code': 9, 'key_pool_offset': 17, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [4, 11, 37, 17], 'tile_event': {'x': 4, 'y': 11, 'action_code': 37, 'key_pool_offset': 17, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [12, 15, 9, 195], 'tile_event': {'x': 12, 'y': 15, 'action_code': 9, 'key_pool_offset': 195, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [12, 15, 37, 195], 'tile_event': {'x': 12, 'y': 15, 'action_code': 37, 'key_pool_offset': 195, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 10: function_10

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0xF2C UnitEscapeByPID('PID_GREIL_EV')`: 2 explored alternative(s). Example local guards: Comeback() != 0.
- `0xF34 UnitEscapeByPID('PID_KILROY')`: 2 explored alternative(s). Example local guards: Comeback() != 0.
- `0xF3C UnitEscapeByPID('PID_SENERIO')`: 2 explored alternative(s). Example local guards: Comeback() != 0.
- `0x1263 AllUnitEscape()`: 2 explored alternative(s). Example local guards: Comeback() != 0.
- `0x126D AllUnitEscape()`: 2 explored alternative(s). Example local guards: Comeback() != 0.

### Scene 11: function_11

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1322 AllUnitEscape()`: 2 explored alternative(s). Example local guards: Normal() != 0.

### Scene 12: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1731 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 13: function_13

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 14: function_14

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 15: function_15

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 16: function_16

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 20: function_20

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [1]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1BD7 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 28: function_28

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.2: Rescue — Scripts/C03.cmb

### Scene 6: function_6

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0xFE1 UnitEscapeByPID('PID_OSCAR')`: 2 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0.
- `0xFEE UnitEscapeByPID('PID_BOLE')`: 2 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0.
- `0xFF6 UnitEscapeByPID('PID_GREIL_EV')`: 3 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0.
- `0xFFE UnitEscapeByPID('PID_MIST_EV')`: 3 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x1006 UnitEscapeByPID('PID_LOFA_EV')`: 3 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x100E UnitEscapeByPID('PID_CHINON_EV')`: 3 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x1016 UnitEscapeByPID('PID_GATRIE')`: 3 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x101E UnitEscapeByPID('PID_SENERIO')`: 3 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x13D1 AllUnitEscape()`: 6 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0.
- `0x13DB AllUnitEscape()`: 6 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND 1 != 0 AND 1 != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0.

### Scene 8: function_8

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x14A9 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 9: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1905 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1949 UnitTransferToForceByPID('PID_TIAMAT', 7)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND UnitCheckLiveByPID('PID_TIAMAT') != 0.

### Scene 10: function_10

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 11: function_11

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned

- `0x1ACF UnitTransferToForceByPID('PID_TIAMAT', 5)`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) == 0.

### Scene 12: function_12

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 13: function_13

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1291, 1791, 1, 28], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_TIAMAT', 'reversible': True, 'key': 'アイクティアマト'}}`. Local trace: all explored local paths returned


### Scene 18: function_18

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1DAB set('gf_complete')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.

### Scene 19: function_19

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [2180]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2346 UnitEscape(UnitGetByPID('PID_ZAKO_EV1'), 0)`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(get('シノンガトリー配置')) != 0 AND (ForceGetCount(6) == 0) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitGetByPID('PID_TIAMAT') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_TIAMAT')) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitGetByPID('PID_OSCAR') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_OSCAR')) != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_IKE')) != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitGetByPID('PID_BOLE') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_BOLE')) != 0 AND UnitGetByPID('PID_ZAKO_EV1') != 0.
- `0x2552 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(get('シノンガトリー配置')) != 0 AND (ForceGetCount(6) == 0) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitGetByPID('PID_TIAMAT') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_TIAMAT')) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitGetByPID('PID_OSCAR') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_OSCAR')) != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_IKE')) != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitGetByPID('PID_BOLE') != 0 AND UnitGetWeaponCount(UnitGetByPID('PID_BOLE')) != 0 AND UnitGetByPID('PID_ZAKO_EV1') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND (UnitSetWeaponAway(UnitGetByPID('PID_TIAMAT')) != -(1)) != 0 AND (UnitSetWeaponAway(UnitGetByPID('PID_IKE')) != -(1)) != 0 AND (UnitSetWeaponAway(UnitGetByPID('PID_OSCAR')) != -(1)) != 0 AND (UnitSetWeaponAway(UnitGetByPID('PID_BOLE')) != -(1)) != 0.

### Scene 21: function_21

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 22: function_22

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.3: Pirates Aground — Scripts/C04.cmb

### Scene 0: function_0

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [20, 20, 9, 0], 'tile_event': {'x': 20, 'y': 20, 'action_code': 9, 'key_pool_offset': 0, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 1: function_1

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [20, 20, 37, 0], 'tile_event': {'x': 20, 'y': 20, 'action_code': 37, 'key_pool_offset': 0, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [8, 13, 44, 247], 'tile_event': {'x': 8, 'y': 13, 'action_code': 44, 'key_pool_offset': 247, 'key': ''}}`. Local trace: all explored local paths returned

- `0xD19 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [8, 12, 44, 247], 'tile_event': {'x': 8, 'y': 12, 'action_code': 44, 'key_pool_offset': 247, 'key': ''}}`. Local trace: all explored local paths returned

- `0xD69 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 13: function_13

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1211 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0.
- `0x1552 UnitEscapeByPID('PID_OLDMAN_1')`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND UnitCheckLiveByPID('PID_TIAMAT') != 0.
- `0x157F UnitEscapeByPID('PID_TIAMAT_EV')`: 2 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND UnitCheckLiveByPID('PID_TIAMAT') != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0.

### Scene 14: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1726 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1752 UnitTransferToForceByPID('PID_OSCAR', 7)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x175C UnitTransferToForceByPID('PID_BOLE', 7)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1766 UnitTransferToForceByPID('PID_KILROY', 7)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1779 UnitTransferToForceByPID('PID_OSCAR', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1783 UnitTransferToForceByPID('PID_BOLE', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x178D UnitTransferToForceByPID('PID_KILROY', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 15: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x18BA UnitEscapeByPID('PID_MARCIA')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x18F7 UnitTransferToForceByPID('PID_OSCAR', 7)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x1901 UnitTransferToForceByPID('PID_BOLE', 7)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x190B UnitTransferToForceByPID('PID_KILROY', 7)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 16: function_16

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 17: function_17

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [17, 2111, 0, 351], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_MARCIA', 'reversible': False, 'key': 'マーシャ会話アイク'}}`. Local trace: all explored local paths returned

- `0x1BBA UnitEscapeByPID('PID_MARCIA')`: 2 explored alternative(s). Example local guards: (UnitGetXByPID('PID_MARCIA') == (UnitGetXByPID('PID_IKE') + 1)) != 0.

### Scene 21: function_21

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [1159]}`. Local trace: all explored local paths returned

- `0x1CEC set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 22: function_22

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [2500]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1D5D AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.

### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 27: function_27

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.4: Roadside Battle — Scripts/C05.cmb

### Scene 13: function_13

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x19CB UnitEscapeByPID('PID_OSCAR')`: 1 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND 1 != 0.
- `0x19D8 UnitEscapeByPID('PID_BOLE')`: 1 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x19E5 UnitEscapeByPID('PID_KILROY')`: 1 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x19F2 UnitEscapeByPID('PID_CHINON_EV')`: 1 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x19FF UnitEscapeByPID('PID_GATRIE')`: 1 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1C78 AllUnitEscape()`: 1 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0.
- `0x1C82 AllUnitEscape()`: 1 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0.

### Scene 14: function_14

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2046 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x29AC UnitEscapeByPID('PID_TIAMAT_EV')`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_KILROY')) != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_GATRIE') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_CHINON') != 0 AND Normal() != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0.

### Scene 15: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2B89 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x2B98 UnitTransferToForceByPID('PID_OSCAR', 7)`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x2BA2 UnitTransferToForceByPID('PID_BOLE', 7)`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x2BA7 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x2C14 UnitTransferToForceByPID('PID_OSCAR', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x2C1E UnitTransferToForceByPID('PID_BOLE', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 16: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2CB0 UnitTransferToForceByPID('PID_OSCAR', 7)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x2CBA UnitTransferToForceByPID('PID_BOLE', 7)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 21: function_21

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [1737]}`. Local trace: all explored local paths returned

- `0x2E89 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 22: function_22

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [3110]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2EF5 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.

### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 27: function_27

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.5: Flight! — Scripts/C06.cmb

### Scene 0: function_0

Trigger metadata: `{'kind': 4, 'argc': 0, 'parameters': [16, 10, 16, 10, 1, 0]}`. Local trace: all explored local paths returned

- `0xC91 set('gf_gameover')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 10: function_10

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1135 UnitEscapeByPID('PID_OSCAR')`: 6 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0.
- `0x1142 UnitEscapeByPID('PID_BOLE')`: 6 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0 AND 1 != 0.
- `0x114F UnitEscapeByPID('PID_KILROY')`: 6 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x115C UnitEscapeByPID('PID_CHINON_EV')`: 4 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1169 UnitEscapeByPID('PID_GATRIE')`: 4 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1176 UnitEscapeByPID('PID_SENERIO')`: 3 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x12F6 AllUnitEscape()`: 5 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1300 AllUnitEscape()`: 5 explored alternative(s). Example local guards: Comeback() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.

### Scene 11: function_11

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1510 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x152D AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x1A2E UnitEscapeByPID('PID_GREIL_EV')`: 6 explored alternative(s). Example local guards: !(Normal()) != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND Normal() != 0 AND Normal() != 0.
- `0x1A11 UnitTransferToForceByPID('PID_GREIL_EV', 1)`: 4 explored alternative(s). Example local guards: !(Normal()) != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND Normal() == 0 AND UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitCheckLiveByPID('PID_SENERIO') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_TIAMAT') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND Normal() == 0.

### Scene 12: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1B75 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1BA1 UnitTransferToForceByPID('PID_OSCAR', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1BAB UnitTransferToForceByPID('PID_BOLE', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1BB5 UnitTransferToForceByPID('PID_KILROY', 5)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 14: function_14

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 15: function_15

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 19: function_19

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 2], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 2}}`. Local trace: all explored local paths returned

- `0x1E13 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 20: function_20

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [2422]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1F57 AllUnitEscape()`: 1 explored alternative(s). Example local guards: get('ボス倒した') != 0 AND !(Normal()) != 0.

### Scene 22: function_22

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 23: function_23

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.6: A Brief Diversion — Scripts/C07.cmb

### Scene 1: function_1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0xE66 UnitEscape(MindGetMe(), 0)`: 4 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0.
- `0xE76 set('gf_complete')`: 4 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_IKE')) != 0.
- `0xE86 set('gf_complete')`: 4 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_IKE')) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0.

### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [13, 26, 14, 191], 'tile_event': {'x': 13, 'y': 26, 'action_code': 14, 'key_pool_offset': 191, 'key': '', 'action': 'Escape'}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1EB9 UnitEscapeByPID('PID_LOFA_EV')`: 16 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_OSCAR') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.
- `0x1EC1 UnitEscapeByPID('PID_MIST')`: 16 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_OSCAR') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.
- `0x1EC9 UnitEscapeByPID('PID_DUMMY1')`: 16 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_OSCAR') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.
- `0x1ED1 UnitEscapeByPID('PID_TIAMAT_EV')`: 16 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_OSCAR') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.
- `0x1ED9 UnitEscapeByPID('PID_SENERIO_EV')`: 16 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_OSCAR') != 0 AND UnitCheckExistsByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.

### Scene 13: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1F6D AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1F8D AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1FB9 UnitTransferToForceByPID('PID_GREIL', 7)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1FC3 UnitTransferToForceByPID('PID_CHINON', 7)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1FCD UnitTransferToForceByPID('PID_GATRIE', 7)`: 3 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 15: function_15

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2216 UnitEscapeByPID('PID_DAYNE_SOL_1')`: 3 explored alternative(s). Example local guards: get('見つかるイベント') == 0 AND !(get('見つかるイベント')) != 0 AND !(get('見つかるトリガ')) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND !(get('見つかるイベント')) != 0 AND get('見つかるトリガ') != 0.

### Scene 16: function_16

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 21: function_21

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [175]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2543 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.7: Shades of Evil — Scripts/C08.cmb

### Scene 0: function_0

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [7, 8, 12, 0], 'tile_event': {'x': 7, 'y': 8, 'action_code': 12, 'key_pool_offset': 0, 'key': '宝箱２'}}`. Local trace: all explored local paths returned


### Scene 1: function_1

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [9, 8, 12, 61], 'tile_event': {'x': 9, 'y': 8, 'action_code': 12, 'key_pool_offset': 61, 'key': '宝箱３'}}`. Local trace: all explored local paths returned


### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [17, 8, 12, 80], 'tile_event': {'x': 17, 'y': 8, 'action_code': 12, 'key_pool_offset': 80, 'key': '宝箱４'}}`. Local trace: all explored local paths returned


### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [23, 10, 44, 103], 'tile_event': {'x': 23, 'y': 10, 'action_code': 44, 'key_pool_offset': 103, 'key': ''}}`. Local trace: all explored local paths returned

- `0x170A UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [23, 11, 44, 103], 'tile_event': {'x': 23, 'y': 11, 'action_code': 44, 'key_pool_offset': 103, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1762 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 15: function_15

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1BAF AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x20E0 UnitEscapeByPID('PID_SENERIO_EV')`: 3 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0.
- `0x20E8 UnitEscapeByPID('PID_TIAMAT_EV')`: 3 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0.

### Scene 16: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2309 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 18: function_18

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 19: function_19

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2769 UnitEscape(UnitGetByPos(4, 7), 0)`: 1 explored alternative(s). Example local guards: get('グレイルプラハ登場') == 0 AND !(get('グレイルプラハ登場トリガ')) == 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPos(4, 7) != 0 AND UnitGetByPos(4, 7) != 0 AND (get('gf_canceled') == 0) != 0.
- `0x29BD UnitEscapeByPID('PID_PRAGUE')`: 8 explored alternative(s). Example local guards: get('グレイルプラハ登場') == 0 AND !(get('グレイルプラハ登場トリガ')) == 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPos(4, 7) != 0 AND UnitGetByPos(4, 7) != 0 AND (get('gf_canceled') == 0) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND (UnitGetStatus(UnitGetByPID('PID_IKE')) & 4) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND Normal() != 0.
- `0x29C5 UnitEscapeByPID('PID_GREIL_EV')`: 8 explored alternative(s). Example local guards: get('グレイルプラハ登場') == 0 AND !(get('グレイルプラハ登場トリガ')) == 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPos(4, 7) != 0 AND UnitGetByPos(4, 7) != 0 AND (get('gf_canceled') == 0) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND (UnitGetStatus(UnitGetByPID('PID_IKE')) & 4) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND Normal() != 0.
- `0x29D4 UnitEscapeByPID('PID_DAYNE_SOL_5')`: 4 explored alternative(s). Example local guards: get('グレイルプラハ登場') == 0 AND !(get('グレイルプラハ登場トリガ')) == 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPos(4, 7) != 0 AND UnitGetByPos(4, 7) != 0 AND (get('gf_canceled') == 0) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND (UnitGetStatus(UnitGetByPID('PID_IKE')) & 4) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND Normal() != 0 AND Normal() != 0.
- `0x29DC UnitEscapeByPID('PID_DAYNE_SOL_6')`: 4 explored alternative(s). Example local guards: get('グレイルプラハ登場') == 0 AND !(get('グレイルプラハ登場トリガ')) == 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPos(4, 7) != 0 AND UnitGetByPos(4, 7) != 0 AND (get('gf_canceled') == 0) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND (UnitGetStatus(UnitGetByPID('PID_IKE')) & 4) != 0 AND (UnitGetYByPID('PID_IKE') <= 5) == 0 AND (UnitGetXByPID('PID_IKE') >= 20) != 0 AND (UnitGetYByPID('PID_IKE') <= 17) != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND Normal() != 0 AND Normal() != 0.

### Scene 20: function_20

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 21: function_21

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 22: function_22

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1079, 2044, 1, 439], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_WAYU', 'reversible': True, 'key': '会話アイクワユ'}}`. Local trace: all explored local paths returned

- `0x2BF7 UnitTransferToForceByPID('PID_WAYU', 0)`: 2 explored alternative(s). Example local guards: !(get('グレイルプラハ登場')) != 0.

### Scene 23: function_23

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1079, 2291, 1, 403], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_CHINON', 'reversible': True, 'key': '会話アイクシノン'}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1079, 2280, 1, 420], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_GATRIE', 'reversible': True, 'key': '会話アイクガトリー'}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2DEB set('gf_complete')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.

### Scene 34: function_34

Trigger metadata: `{'kind': 0, 'argc': 2, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2F1C UnitEscape(ForceGetFirst(1), 0)`: 8 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) == 0 AND UnitQueryPID(ForceGetFirst(1), v0) == 0 AND UnitQueryJID(ForceGetFirst(1), v1) != 0.

### Scene 35: function_35

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2F9B AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 37: function_37

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x485A UnitEscapeByPID('PID_GREIL_EV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x48D8 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 39: function_39

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x4E07 UnitEscapeByPID('PID_BLACKKNIGHT_EV1')`: 4 explored alternative(s). Example local guards: !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0 AND UnitGetByPID('PID_BLACKKNIGHT_EV1') != 0.
- `0x4F49 AllUnitEscape()`: 4 explored alternative(s). Example local guards: !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0 AND UnitGetByPID('PID_BLACKKNIGHT_EV1') != 0.

### Scene 40: function_40

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x5087 UnitEscapeByPID('PID_OSCAR')`: 3 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0.
- `0x5094 UnitEscapeByPID('PID_BOLE')`: 3 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0 AND 1 != 0.
- `0x50A1 UnitEscapeByPID('PID_KILROY')`: 3 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x50AE UnitEscapeByPID('PID_CHINON')`: 3 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x50BB UnitEscapeByPID('PID_GATRIE')`: 3 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x50C8 UnitEscapeByPID('PID_SENERIO')`: 2 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x5399 AllUnitEscape()`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0.
- `0x53A3 AllUnitEscape()`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0.

### Scene 41: function_41

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [3023]}`. Local trace: all explored local paths returned

- `0x549C AllUnitEscape()`: 4 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND (UnitGetXByPID('PID_IKE') <= 13) != 0.

### Scene 43: function_43

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 44: function_44

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 45: function_45

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.8: Despair and Hope — Scripts/C09.cmb

### Scene 7: function_7

Trigger metadata: `{'kind': 4, 'argc': 0, 'parameters': [12, 11, 12, 11, 1, 354]}`. Local trace: all explored local paths returned

- `0x1737 set('gf_gameover')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 12: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x18EE AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x190F AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1B24 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1ECF UnitTransferToForceByPID('PID_CHINON', 7)`: 9 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !((GCST() & 1)) != 0 AND Comeback() != 0 AND UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND 1 != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND 1 != 0 AND UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitGetByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitGetByPID('PID_GATRIE') != 0.
- `0x1ED9 UnitTransferToForceByPID('PID_GATRIE', 7)`: 9 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !((GCST() & 1)) != 0 AND Comeback() != 0 AND UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND UnitCheckLiveByPID('PID_BOLE') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitCheckLiveByPID('PID_OSCAR') != 0 AND 1 != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND 1 != 0 AND UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckLiveByPID('PID_CHINON') != 0 AND UnitGetByPID('PID_CHINON') != 0 AND UnitCheckLiveByPID('PID_GATRIE') != 0 AND UnitGetByPID('PID_GATRIE') != 0.

### Scene 13: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1F61 UnitEscape(UnitGetByPos(14, 20), 0)`: 1 explored alternative(s). Example local guards: UnitGetByPos(14, 20) != 0.
- `0x2084 AllUnitEscape()`: 1 explored alternative(s). Example local guards: UnitGetByPos(14, 20) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0.

### Scene 15: function_15

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [8, 8, 1], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 16: function_16

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 17: function_17

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 18: function_18

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 19: function_19

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 0], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 20: function_20

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 0], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 21: function_21

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2301, 3098, 0, 376], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_ELAICE', 'reversible': False, 'key': 'イレース仲間'}}`. Local trace: all explored local paths returned

- `0x296B UnitTransferToForceByPID('PID_ELAICE', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 27: function_27

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 2], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 2}}`. Local trace: all explored local paths returned

- `0x2B5F set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 29: function_29

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2CF0 UnitEscapeByPID('PID_KAMURA')`: 8 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND UnitGetByPos(10, 12) != 0 AND UnitGetByPos(14, 11) != 0 AND get('ボス死亡') != 0.

### Scene 31: function_31

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2E03 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x2E34 UnitEscapeByPID('PID_MIST_EV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x30AB UnitEscapeByPID('PID_DAYNE_SOL_1')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0.
- `0x30B3 UnitEscapeByPID('PID_DAYNE_SOL_2')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0.
- `0x30BB UnitEscapeByPID('PID_DAYNE_SOL_5')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0.
- `0x30C3 UnitEscapeByPID('PID_DAYNE_SOL_9')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0.
- `0x30CB UnitEscapeByPID('PID_DAYNE_SKN_4')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0.
- `0x3215 UnitEscapeByPID('PID_DAYNE_SOL_1')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0.
- `0x321D UnitEscapeByPID('PID_DAYNE_SOL_2')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0.
- `0x3225 UnitEscapeByPID('PID_DAYNE_SOL_5')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0.
- `0x322D UnitEscapeByPID('PID_DAYNE_SOL_9')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0.
- `0x3235 UnitEscapeByPID('PID_DAYNE_SKN_4')`: 1 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0.
- `0x36BC UnitEscape(UnitGetByPID('PID_DAYNE_ARM_1'), 0)`: 4 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0 AND !(UnitGetByPID('PID_KAMURA')) != 0 AND !((GCST() & 1)) != 0 AND !(get('ボス死亡')) != 0 AND (UnitGetByPID('PID_KAMURA') == 0) != 0 AND UnitGetByPID('PID_DAYNE_ARM_1') != 0.
- `0x374A AllUnitEscape()`: 8 explored alternative(s). Example local guards: (get('gf_canceled') == 0) != 0 AND (get('gf_canceled') == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND !(get('ボス死亡')) != 0 AND !(get('ボス死亡')) != 0 AND !(UnitGetByPID('PID_KAMURA')) != 0 AND !((GCST() & 1)) != 0 AND !(get('ボス死亡')) != 0 AND (UnitGetByPID('PID_KAMURA') == 0) != 0 AND UnitGetByPID('PID_DAYNE_ARM_1') != 0.

### Scene 32: function_32

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x37DD UnitEscapeByPID('PID_ELAICE')`: 2 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND UnitCheckLiveByPID('PID_WAYU') != 0 AND 1 != 0.
- `0x3A17 AllUnitEscape()`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND UnitCheckLiveByPID('PID_WAYU') != 0 AND 1 != 0.
- `0x3A21 AllUnitEscape()`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND UnitCheckLiveByPID('PID_WAYU') != 0 AND 1 != 0.

### Scene 36: function_36

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 37: function_37

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.9: Gallia — Scripts/C10.cmb

### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 23, 13, 255], 'tile_event': {'x': 6, 'y': 23, 'action_code': 13, 'key_pool_offset': 255, 'key': ''}}`. Local trace: all explored local paths returned

- `0x138B set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [3, 5, 9, 268], 'tile_event': {'x': 3, 'y': 5, 'action_code': 9, 'key_pool_offset': 268, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [3, 5, 37, 268], 'tile_event': {'x': 3, 'y': 5, 'action_code': 37, 'key_pool_offset': 268, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [4, 9, 9, 430], 'tile_event': {'x': 4, 'y': 9, 'action_code': 9, 'key_pool_offset': 430, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [4, 9, 37, 430], 'tile_event': {'x': 4, 'y': 9, 'action_code': 37, 'key_pool_offset': 430, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 19: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x17EA AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 20: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x18FB AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x1F8A UnitEscapeByPID('PID_TIAMAT_EV')`: 3 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND Normal() != 0.
- `0x1F92 UnitEscapeByPID('PID_SENERIO_EV')`: 3 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND Normal() != 0.
- `0x1F9A UnitEscapeByPID('PID_MIST_EV')`: 3 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND Normal() != 0.
- `0x1FA2 UnitEscapeByPID('PID_LOFA_EV')`: 3 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND Normal() != 0.
- `0x1FAA UnitEscapeByPID('PID_DUMMY1')`: 3 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND Normal() != 0.

### Scene 21: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2291 UnitTransferToForceByPID('PID_MIST', 0)`: 7 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0.
- `0x229B UnitTransferToForceByPID('PID_LOFA', 0)`: 7 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0.
- `0x22C8 UnitEscapeByPID('PID_BOLE_EV')`: 7 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND (0 == 1) != 0.
- `0x22F5 UnitEscapeByPID('PID_OSCAR_EV')`: 7 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_KILROY') != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND (0 == 1) == 0 AND (0 == 2) != 0.

### Scene 22: function_22

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 23: function_23

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 27: function_27

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 28: function_28

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1510, 2876, 1, 654], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_MARCIA', 'reversible': True, 'key': 'マーシャ仲間'}}`. Local trace: all explored local paths returned

- `0x2942 UnitTransferToForceByPID('PID_MARCIA', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 29: function_29

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1586, 2600, 0, 667], 'conversation_event': {'actor': 'PID_BOLE', 'target': 'PID_LOFA', 'reversible': False, 'key': 'ヨファボーレ'}}`. Local trace: all explored local paths returned


### Scene 30: function_30

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [154, 2600, 0, 680], 'conversation_event': {'actor': 'PID_OSCAR', 'target': 'PID_LOFA', 'reversible': False, 'key': 'ヨファオスカー'}}`. Local trace: all explored local paths returned


### Scene 44: function_44

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [256]}`. Local trace: all explored local paths returned

- `0x2E87 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 47: function_47

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 48: function_48

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 3], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 3}}`. Local trace: all explored local paths returned


### Scene 49: function_49

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 50: function_50

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.10: Prisoner Release — Scripts/C11.cmb

### Scene 5: function_5

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x15D8 UnitTransferToForceByPID('PID_KEVIN', 0)`: 1 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_KEVIN')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_KEVIN')) != 0.
- `0x15FA UnitTransferToForceByPID('PID_CHAP', 0)`: 3 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_KEVIN')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_KEVIN')) != 0 AND (MindGetMe() == UnitGetByPID('PID_CHAP')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_CHAP')) != 0.
- `0x161C UnitTransferToForceByPID('PID_NEPENEE', 0)`: 8 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_KEVIN')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_KEVIN')) != 0 AND (MindGetMe() == UnitGetByPID('PID_CHAP')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_CHAP')) != 0 AND (MindGetMe() == UnitGetByPID('PID_NEPENEE')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_NEPENEE')) != 0.
- `0x1625 UnitEscape(MindGetMe(), 0)`: 12 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_KEVIN')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_KEVIN')) != 0 AND (MindGetMe() == UnitGetByPID('PID_CHAP')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_CHAP')) != 0 AND (MindGetMe() == UnitGetByPID('PID_NEPENEE')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_NEPENEE')) != 0.
- `0x1635 set('gf_complete')`: 12 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_KEVIN')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_KEVIN')) != 0 AND (MindGetMe() == UnitGetByPID('PID_CHAP')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_CHAP')) != 0 AND (MindGetMe() == UnitGetByPID('PID_NEPENEE')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_NEPENEE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_IKE')) != 0.
- `0x1645 set('gf_complete')`: 24 explored alternative(s). Example local guards: UnitGet(MindGetMe(), 4) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_KEVIN')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_KEVIN')) != 0 AND (MindGetMe() == UnitGetByPID('PID_CHAP')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_CHAP')) != 0 AND (MindGetMe() == UnitGetByPID('PID_NEPENEE')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_NEPENEE')) != 0 AND (MindGetMe() == UnitGetByPID('PID_IKE')) != 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0.

### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [2, 5, 12, 483], 'tile_event': {'x': 2, 'y': 5, 'action_code': 12, 'key_pool_offset': 483, 'key': '宝箱１'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [2, 3, 12, 543], 'tile_event': {'x': 2, 'y': 3, 'action_code': 12, 'key_pool_offset': 543, 'key': '宝箱２'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [3, 3, 12, 564], 'tile_event': {'x': 3, 'y': 3, 'action_code': 12, 'key_pool_offset': 564, 'key': '宝箱３'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [4, 3, 12, 587], 'tile_event': {'x': 4, 'y': 3, 'action_code': 12, 'key_pool_offset': 587, 'key': '宝箱４'}}`. Local trace: all explored local paths returned


### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [19, 3, 12, 609], 'tile_event': {'x': 19, 'y': 3, 'action_code': 12, 'key_pool_offset': 609, 'key': '宝箱５'}}`. Local trace: all explored local paths returned


### Scene 11: function_11

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 2, 14, 629], 'tile_event': {'x': 6, 'y': 2, 'action_code': 14, 'key_pool_offset': 629, 'key': '', 'action': 'Escape'}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [7, 2, 14, 629], 'tile_event': {'x': 7, 'y': 2, 'action_code': 14, 'key_pool_offset': 629, 'key': '', 'action': 'Escape'}}`. Local trace: all explored local paths returned


### Scene 13: function_13

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [8, 14, 11, 630], 'tile_event': {'x': 8, 'y': 14, 'action_code': 11, 'key_pool_offset': 630, 'key': 'F0814'}}`. Local trace: all explored local paths returned


### Scene 14: function_14

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [11, 7, 11, 658], 'tile_event': {'x': 11, 'y': 7, 'action_code': 11, 'key_pool_offset': 658, 'key': 'F1107'}}`. Local trace: all explored local paths returned


### Scene 15: function_15

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [19, 14, 11, 677], 'tile_event': {'x': 19, 'y': 14, 'action_code': 11, 'key_pool_offset': 677, 'key': 'F1914'}}`. Local trace: all explored local paths returned


### Scene 16: function_16

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [19, 5, 11, 702], 'tile_event': {'x': 19, 'y': 5, 'action_code': 11, 'key_pool_offset': 702, 'key': 'F1905'}}`. Local trace: all explored local paths returned


### Scene 23: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1CD2 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1EA7 Join('always_lete')`: 6 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND Comeback() != 0 AND !((GCST() & 3)) != 0 AND (1 == 0) != 0 AND !(get('G_レテ死亡')) != 0 AND !(get('G_モウディ死亡')) != 0 AND !(get('G_レテ死亡')) != 0.
- `0x1EBA Join('always_mordy')`: 5 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND Comeback() != 0 AND !((GCST() & 3)) != 0 AND (1 == 0) != 0 AND !(get('G_レテ死亡')) != 0 AND !(get('G_モウディ死亡')) != 0 AND !(get('G_レテ死亡')) != 0 AND !(get('G_モウディ死亡')) != 0.

### Scene 25: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x23AD AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x26D5 UnitTransferToForceByPID('PID_VOKE', 0)`: 2 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0.
- `0x27EE UnitEscapeByPID('PID_LAY')`: 2 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0 AND (DialogGetRes() == 2) == 0.
- `0x28F5 UnitEscapeByPID('PID_TIAMAT_EV')`: 7 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0 AND (DialogGetRes() == 2) == 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0.
- `0x28FD UnitEscapeByPID('PID_SENERIO_EV')`: 7 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0 AND (DialogGetRes() == 2) == 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0 AND !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) == 0.
- `0x2761 UnitEscapeByPID('PID_VOKE')`: 1 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) == 0 AND (DialogGetRes() == 1) != 0.

### Scene 27: function_27

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 2], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 2}}`. Local trace: all explored local paths returned


### Scene 28: function_28

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [220, 3261, 1, 826], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_CEPHERAN_FAKE', 'reversible': True, 'key': 'アイクセフェラン'}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [3379, 241, 1, 843], 'conversation_event': {'actor': 'PID_OSCAR', 'target': 'PID_KEVIN', 'reversible': True, 'key': 'オスカーケビン'}}`. Local trace: all explored local paths returned

- `0x2C5B UnitTransferToForceByPID('PID_KEVIN', 3)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 30: function_30

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [220, 260, 0, 858], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_NEPENEE', 'reversible': False, 'key': 'アイクネフェニー'}}`. Local trace: all explored local paths returned

- `0x2CA3 UnitTransferToForceByPID('PID_NEPENEE', 3)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 31: function_31

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [220, 251, 0, 875], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_CHAP', 'reversible': False, 'key': 'アイクチャップ'}}`. Local trace: all explored local paths returned

- `0x2CEB UnitTransferToForceByPID('PID_CHAP', 3)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 37: function_37

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 57: function_57

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [471]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x3494 UnitTransferToForce(UnitCheckExistsByPID2('PID_KEVIN'), 0)`: 1 explored alternative(s). Example local guards: !(Maniac()) != 0 AND get('扉チャップケヴィン') != 0 AND !(get('ケヴィン離脱')) != 0 AND UnitCheckExistsByPID2('PID_KEVIN') != 0.
- `0x34B8 UnitTransferToForce(UnitCheckExistsByPID2('PID_CHAP'), 0)`: 1 explored alternative(s). Example local guards: !(Maniac()) != 0 AND get('扉チャップケヴィン') != 0 AND !(get('ケヴィン離脱')) != 0 AND UnitCheckExistsByPID2('PID_KEVIN') != 0 AND !(get('チャップ離脱')) != 0 AND UnitCheckExistsByPID2('PID_CHAP') != 0.
- `0x34E6 UnitTransferToForce(UnitCheckExistsByPID2('PID_NEPENEE'), 0)`: 1 explored alternative(s). Example local guards: !(Maniac()) != 0 AND get('扉チャップケヴィン') != 0 AND !(get('ケヴィン離脱')) != 0 AND UnitCheckExistsByPID2('PID_KEVIN') != 0 AND !(get('チャップ離脱')) != 0 AND UnitCheckExistsByPID2('PID_CHAP') != 0 AND get('扉ネフェニー') != 0 AND !(get('ネフェニー離脱')) != 0 AND UnitCheckExistsByPID2('PID_NEPENEE') != 0.
- `0x34EB AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(Maniac()) != 0 AND get('扉チャップケヴィン') != 0 AND !(get('ケヴィン離脱')) != 0 AND UnitCheckExistsByPID2('PID_KEVIN') != 0 AND !(get('チャップ離脱')) != 0 AND UnitCheckExistsByPID2('PID_CHAP') != 0 AND get('扉ネフェニー') != 0 AND !(get('ネフェニー離脱')) != 0 AND UnitCheckExistsByPID2('PID_NEPENEE') != 0.
- `0x3776 UnitTransferToForceByPID('PID_VOKE', 7)`: 8 explored alternative(s). Example local guards: !(Maniac()) != 0 AND get('扉チャップケヴィン') != 0 AND !(get('ケヴィン離脱')) != 0 AND UnitCheckExistsByPID2('PID_KEVIN') != 0 AND !(get('チャップ離脱')) != 0 AND UnitCheckExistsByPID2('PID_CHAP') != 0 AND get('扉ネフェニー') != 0 AND !(get('ネフェニー離脱')) != 0 AND UnitCheckExistsByPID2('PID_NEPENEE') != 0 AND UnitCheckLiveByPID('PID_KEVIN') != 0 AND UnitCheckLiveByPID('PID_KEVIN') != 0 AND 1 != 0 AND 1 != 0 AND UnitCheckLiveByPID('PID_KEVIN') != 0 AND UnitCheckLiveByPID('PID_CHAP') != 0 AND UnitCheckLiveByPID('PID_NEPENEE') != 0 AND get('アイクセフェラン') != 0 AND get('フォルカ仲間C11') != 0 AND UnitCheckLiveByPID('PID_VOKE') != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) == 0.

### Scene 62: function_62

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 63: function_63

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 64: function_64

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.11: Blood Runs Red — Scripts/C12.cmb

### Scene 0: function_0

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [26, 6, 9, 0], 'tile_event': {'x': 26, 'y': 6, 'action_code': 9, 'key_pool_offset': 0, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 1: function_1

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [15, 16, 9, 219], 'tile_event': {'x': 15, 'y': 16, 'action_code': 9, 'key_pool_offset': 219, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [14, 24, 9, 266], 'tile_event': {'x': 14, 'y': 24, 'action_code': 9, 'key_pool_offset': 266, 'key': '訪問３'}}`. Local trace: all explored local paths returned


### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [15, 16, 37, 219], 'tile_event': {'x': 15, 'y': 16, 'action_code': 37, 'key_pool_offset': 219, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [14, 24, 37, 266], 'tile_event': {'x': 14, 'y': 24, 'action_code': 37, 'key_pool_offset': 266, 'key': '訪問３'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [26, 6, 37, 0], 'tile_event': {'x': 26, 'y': 6, 'action_code': 37, 'key_pool_offset': 0, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [23, 26, 44, 331], 'tile_event': {'x': 23, 'y': 26, 'action_code': 44, 'key_pool_offset': 331, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1B21 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 7, 41, 331], 'tile_event': {'x': 6, 'y': 7, 'action_code': 41, 'key_pool_offset': 331, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1B4B set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 19: FinalDisposition

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1FE7 UnitEscapeByPID('PID_NASIR')`: 2 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0.

### Scene 21: function_21

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x21CF UnitEscapeByPID('PID_LETHE_EV')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0.
- `0x21DC UnitEscapeByPID('PID_MORDY_EV')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x21E9 UnitEscapeByPID('PID_OSCAR')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x21F6 UnitEscapeByPID('PID_BOLE')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2203 UnitEscapeByPID('PID_KILROY')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2210 UnitEscapeByPID('PID_WAYU')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x221D UnitEscapeByPID('PID_ELAICE')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x222A UnitEscapeByPID('PID_MARCIA')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2237 UnitEscapeByPID('PID_MIST')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2244 UnitEscapeByPID('PID_LOFA')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2251 UnitEscapeByPID('PID_CHAP')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x225E UnitEscapeByPID('PID_NEPENEE')`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x226B UnitEscapeByPID('PID_KEVIN')`: 3 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2278 UnitEscapeByPID('PID_VOKE')`: 3 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.

### Scene 22: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x248E Join('always_dbg_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND Normal() != 0.
- `0x24B9 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND Normal() != 0.
- `0x2650 AllUnitEscape()`: 9 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND Normal() != 0 AND ForceGetCount(5) != 0 AND (ForceGetFirst(5) == 0) != 0 AND Comeback() != 0.
- `0x265A AllUnitEscape()`: 9 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND Normal() != 0 AND ForceGetCount(5) != 0 AND (ForceGetFirst(5) == 0) != 0 AND Comeback() != 0.

### Scene 23: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x28A9 UnitEscapeByPID('PID_LETHE_EV')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0.
- `0x28B6 UnitEscapeByPID('PID_MORDY_EV')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x28C3 UnitEscapeByPID('PID_OSCAR')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x28D0 UnitEscapeByPID('PID_BOLE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x28DD UnitEscapeByPID('PID_KILROY')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x28EA UnitEscapeByPID('PID_WAYU')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x28F7 UnitEscapeByPID('PID_ELAICE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2904 UnitEscapeByPID('PID_MARCIA')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2911 UnitEscapeByPID('PID_MIST')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x291E UnitEscapeByPID('PID_LOFA')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x292B UnitEscapeByPID('PID_CHAP')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2938 UnitEscapeByPID('PID_NEPENEE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2945 UnitEscapeByPID('PID_KEVIN')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2952 UnitEscapeByPID('PID_VOKE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_TIAMAT')) != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_SENERIO')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_MIST')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.

### Scene 24: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x3A34 UnitEscapeByPID('PID_NASIR')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x3CC0 UnitEscapeByPID('PID_LAY')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x3D0E UnitEscapeByPID('PID_DAYNE_SKN_1')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x3D16 UnitEscapeByPID('PID_DAYNE_SKN_2')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x3D1E UnitEscapeByPID('PID_DAYNE_SOL_1')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x3D26 UnitEscapeByPID('PID_DAYNE_SOL_2')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 25: function_25

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 27: function_27

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 28: function_28

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 30: function_30

Trigger metadata: `{'kind': 0, 'argc': 1, 'parameters': []}`. Local trace: all explored local paths returned

- `0x4248 UnitTransferToForceByPID('PID_ZIHARK', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 31: function_31

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [17, 3953, 0, 766], 'conversation_event': {'actor': 'PID_LETHE', 'target': 'PID_ZIHARK', 'reversible': False, 'key': 'ツイハーク仲間'}}`. Local trace: all explored local paths returned


### Scene 32: function_32

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [40, 3953, 0, 766], 'conversation_event': {'actor': 'PID_MORDY', 'target': 'PID_ZIHARK', 'reversible': False, 'key': 'ツイハーク仲間'}}`. Local trace: all explored local paths returned


### Scene 33: function_33

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [3953, 17, 0, 766], 'conversation_event': {'actor': 'PID_ZIHARK', 'target': 'PID_LETHE', 'reversible': False, 'key': 'ツイハーク仲間'}}`. Local trace: all explored local paths returned


### Scene 34: function_34

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [3953, 40, 0, 766], 'conversation_event': {'actor': 'PID_ZIHARK', 'target': 'PID_MORDY', 'reversible': False, 'key': 'ツイハーク仲間'}}`. Local trace: all explored local paths returned


### Scene 47: function_47

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [570]}`. Local trace: all explored local paths returned

- `0x48D4 set('gf_gameover')`: 4 explored alternative(s). Example local guards: (BMGetPhase() == 0) != 0 AND (MindGetTarget() == UnitGetByPID('PID_BLACKKNIGHT')) != 0.

### Scene 53: function_53

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [408]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x4B15 AllUnitEscape()`: 1 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_JILL') != 0.
- `0x4B93 UnitEscape(ForceGetFirst(0), 0)`: 2 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_JILL') != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) != 0) != 0.
- `0x4BA6 UnitEscapeByPID('PID_BLACKKNIGHT')`: 1 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_JILL') != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) != 0) != 0 AND (ForceGetCount(0) - 1) == 0.
- `0x4BF8 UnitEscape(UnitGetByPos(5, 5), 0)`: 2 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_JILL') != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) != 0) != 0 AND (ForceGetCount(0) - 1) == 0 AND (5 <= 25) != 0 AND (5 <= 20) != 0 AND UnitGetByPos(5, 5) != 0.
- `0x4FC8 UnitEscapeByPID('PID_LAY')`: 2 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_JILL') != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) != 0) != 0 AND (ForceGetCount(0) - 1) == 0 AND (5 <= 25) != 0 AND (5 <= 20) != 0 AND UnitGetByPos(5, 5) != 0 AND ((5 + 1) <= 20) == 0 AND ((5 + 1) <= 25) == 0 AND !(UnitCheckExistsByPID('PID_MAKKOYAR')) != 0 AND (get('gf_canceled') == 0) != 0 AND UnitCheckExistsByPID('PID_JILL') != 0.
- `0x51FC AllUnitEscape()`: 3 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_JILL') != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) != 0) != 0 AND (ForceGetCount(0) - 1) == 0 AND (5 <= 25) != 0 AND (5 <= 20) != 0 AND UnitGetByPos(5, 5) != 0 AND ((5 + 1) <= 20) == 0 AND ((5 + 1) <= 25) == 0 AND !(UnitCheckExistsByPID('PID_MAKKOYAR')) != 0 AND (get('gf_canceled') == 0) != 0 AND UnitCheckExistsByPID('PID_JILL') != 0 AND UnitCheckExistsByPID('PID_MAKKOYAR') != 0 AND UnitCheckExistsByPID('PID_MAKKOYAR') != 0.

### Scene 57: function_57

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.12: A Strange Land — Scripts/C13.cmb

### Scene 1: function_1

Trigger metadata: `{'kind': 14, 'argc': 0, 'parameters': [0, 94, 3]}`. Local trace: all explored local paths returned

- `0x1107 Join('always_saza')`: 1 explored alternative(s). Example local guards: Check() == 0 AND (DialogGetRes() == 0) != 0.

### Scene 10: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x19B6 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 11: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1AD0 AllUnitEscape()`: 1 explored alternative(s). Example local guards: get('G_ジル仲間条件') != 0.
- `0x1F54 UnitEscapeByPID('PID_SENERIO_EV')`: 12 explored alternative(s). Example local guards: get('G_ジル仲間条件') != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND UnitGetByPos(21, 11) != 0 AND UnitGetByPos(20, 12) != 0 AND UnitGetByPos(22, 12) != 0 AND UnitGetByPos(21, 13) != 0 AND UnitGetByPos(21, 17) != 0 AND UnitGetByPos(23, 17) != 0 AND UnitGetByPos(20, 18) != 0 AND UnitGetByPos(22, 18) != 0 AND UnitGetByPos(21, 19) != 0 AND !((GCST() & 3)) != 0 AND (0 < 90) != 0 AND ((0 + 1) < 90) == 0 AND (UnitGetWeaponCount(UnitGetByPID('PID_CHIGU')) <= 1) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0.

### Scene 13: function_13

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [2, 2, 2], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 2}}`. Local trace: all explored local paths returned


### Scene 14: function_14

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2477, 1893, 0, 486], 'conversation_event': {'actor': 'PID_JILL', 'target': 'PID_IKE', 'reversible': False, 'key': 'ジル仲間会話'}}`. Local trace: all explored local paths returned

- `0x2239 UnitTransferToForceByPID('PID_JILL', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 15: function_15

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 1], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 16: function_16

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 1], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 17: function_17

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 1], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 18: function_18

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 1], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 19: function_19

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [11, 11, 1], 'inferred_turn_trigger': {'first_turn': 11, 'last_turn': 11, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 20: function_20

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [13, 13, 1], 'inferred_turn_trigger': {'first_turn': 13, 'last_turn': 13, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 21: function_21

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 1], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 28: function_28

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x25F7 set('gf_complete')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.

### Scene 29: function_29

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [3220]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2656 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x2673 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x2724 UnitEscapeByPID('PID_WAYU')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0.
- `0x2731 UnitEscapeByPID('PID_ELAICE')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0.
- `0x273E UnitEscapeByPID('PID_MARCIA')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x274B UnitEscapeByPID('PID_VOKE')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2758 UnitEscapeByPID('PID_ZIHARK')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2765 UnitEscapeByPID('PID_SOTHE')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x29D0 UnitEscapeByPID('PID_NASIR')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2CA4 UnitEscapeByPID('PID_G_ZAKO_EV1')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2CAC UnitEscapeByPID('PID_G_ZAKO_EV2')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2CB4 UnitEscapeByPID('PID_G_ZAKO_EV3')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x2E6C AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !((GCST() & 1)) != 0.
- `0x2E76 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !((GCST() & 1)) != 0.

## Ch.13: A Guiding Wind — Scripts/C14.cmb

### Scene 5: function_5

Trigger metadata: `{'kind': 4, 'argc': 0, 'parameters': [31, 29, 31, 29, 1, 276]}`. Local trace: all explored local paths returned

- `0x12D7 set('gf_gameover')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [29, 28, 12, 298], 'tile_event': {'x': 29, 'y': 28, 'action_code': 12, 'key_pool_offset': 298, 'key': '宝箱１'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [29, 30, 12, 359], 'tile_event': {'x': 29, 'y': 30, 'action_code': 12, 'key_pool_offset': 359, 'key': '宝箱２'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [28, 21, 12, 380], 'tile_event': {'x': 28, 'y': 21, 'action_code': 12, 'key_pool_offset': 380, 'key': '宝箱３'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [32, 22, 12, 400], 'tile_event': {'x': 32, 'y': 22, 'action_code': 12, 'key_pool_offset': 400, 'key': '宝箱４'}}`. Local trace: all explored local paths returned


### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [36, 22, 12, 421], 'tile_event': {'x': 36, 'y': 22, 'action_code': 12, 'key_pool_offset': 421, 'key': '宝箱５'}}`. Local trace: all explored local paths returned


### Scene 11: function_11

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [39, 28, 12, 442], 'tile_event': {'x': 39, 'y': 28, 'action_code': 12, 'key_pool_offset': 442, 'key': '宝箱６'}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [39, 30, 12, 465], 'tile_event': {'x': 39, 'y': 30, 'action_code': 12, 'key_pool_offset': 465, 'key': '宝箱７'}}`. Local trace: all explored local paths returned


### Scene 13: function_13

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [20, 20, 44, 483], 'tile_event': {'x': 20, 'y': 20, 'action_code': 44, 'key_pool_offset': 483, 'key': ''}}`. Local trace: all explored local paths returned

- `0x14F2 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: MindGetMe() != 0.

### Scene 14: function_14

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [21, 20, 44, 483], 'tile_event': {'x': 21, 'y': 20, 'action_code': 44, 'key_pool_offset': 483, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1546 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: MindGetMe() != 0.

### Scene 20: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x17BE AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x17D3 Join('always_dbg_mik_04g')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17E4 UnitTransferToForceByPID('PID_GATRIE', 7)`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 21: function_21

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1AD3 UnitEscapeByPID('PID_OSCAR')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0.
- `0x1AE0 UnitEscapeByPID('PID_BOLE')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0.
- `0x1AED UnitEscapeByPID('PID_KILROY')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1AFA UnitEscapeByPID('PID_WAYU')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B07 UnitEscapeByPID('PID_ELAICE')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B14 UnitEscapeByPID('PID_MARCIA')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B21 UnitEscapeByPID('PID_LOFA')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B2E UnitEscapeByPID('PID_LETHE')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B3B UnitEscapeByPID('PID_MORDY')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B48 UnitEscapeByPID('PID_CHAP')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B55 UnitEscapeByPID('PID_NEPENEE')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B62 UnitEscapeByPID('PID_KEVIN')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B6F UnitEscapeByPID('PID_VOKE')`: 5 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B7C UnitEscapeByPID('PID_JILL')`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1B89 UnitEscapeByPID('PID_SOTHE')`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1D47 AllUnitEscape()`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x1D51 AllUnitEscape()`: 4 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(1) != 0 AND UnitQueryJIDByPID('PID_SENERIO', 'JID_MAGE') != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.

### Scene 24: function_24

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 6, 1], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 6, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 1], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 1}}`. Local trace: all explored local paths returned

- `0x25F0 UnitEscapeByPID('PID_TIBARN')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x25F8 UnitEscapeByPID('PID_VULCI')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x2600 UnitEscapeByPID('PID_JANAFF')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 28: function_28

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 30: function_30

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 0], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 31: function_31

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [8, 8, 1], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 32: function_32

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 4, 1], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 33: function_33

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 1], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 34: function_34

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 1], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 35: function_35

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 1], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 36: function_36

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1970, 2166, 0, 570], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_STELLA', 'reversible': False, 'key': 'ステラ仲間'}}`. Local trace: all explored local paths returned

- `0x2B65 UnitTransferToForceByPID('PID_STELLA', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 37: function_37

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2166, 774, 0, 619], 'conversation_event': {'actor': 'PID_STELLA', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー仲間'}}`. Local trace: all explored local paths returned

- `0x2C15 UnitTransferToForceByPID('PID_GATRIE', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 38: function_38

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1970, 774, 0, 581], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話アイク'}}`. Local trace: all explored local paths returned


### Scene 39: function_39

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [3489, 774, 0, 600], 'conversation_event': {'actor': 'PID_TIAMAT', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話傭兵団'}}`. Local trace: all explored local paths returned


### Scene 40: function_40

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1415, 774, 0, 600], 'conversation_event': {'actor': 'PID_SENERIO', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話傭兵団'}}`. Local trace: all explored local paths returned


### Scene 41: function_41

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [3526, 774, 0, 600], 'conversation_event': {'actor': 'PID_MIST', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話傭兵団'}}`. Local trace: all explored local paths returned


### Scene 42: function_42

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [196, 774, 0, 600], 'conversation_event': {'actor': 'PID_OSCAR', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話傭兵団'}}`. Local trace: all explored local paths returned


### Scene 43: function_43

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [206, 774, 0, 600], 'conversation_event': {'actor': 'PID_BOLE', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話傭兵団'}}`. Local trace: all explored local paths returned


### Scene 44: function_44

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [215, 774, 0, 600], 'conversation_event': {'actor': 'PID_LOFA', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話傭兵団'}}`. Local trace: all explored local paths returned


### Scene 45: function_45

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1303, 774, 0, 600], 'conversation_event': {'actor': 'PID_KILROY', 'target': 'PID_GATRIE', 'reversible': False, 'key': 'ガトリー会話傭兵団'}}`. Local trace: all explored local paths returned


### Scene 53: function_53

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 2], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 2}}`. Local trace: all explored local paths returned

- `0x309D set('gf_complete')`: 1 explored alternative(s). Example local guards: (BMGetTurn() == 10) != 0.
- `0x30BE set('gf_complete')`: 1 explored alternative(s). Example local guards: (BMGetTurn() == 10) == 0 AND (BMGetTurn() >= 7) != 0 AND (ForceGetCount(1) == 0) != 0.

### Scene 54: function_54

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [3790]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x319D UnitTransferToForceByPID('PID_NAESALA', 3)`: 1 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0.
- `0x31A7 UnitTransferToForceByPID('PID_NEALUCHI', 3)`: 1 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0.
- `0x31CE UnitEscape(ForceGetFirst(2), 0)`: 2 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0 AND ForceGetCount(2) != 0 AND ForceGetFirst(2) != 0.
- `0x3275 UnitEscape(ForceGetFirst(1), 0)`: 2 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0 AND ForceGetCount(2) != 0 AND ForceGetFirst(2) != 0 AND (ForceGetCount(2) - 1) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (ForceGetCount(1) >= 1) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) != 0) != 0.
- `0x3372 AllUnitEscape()`: 5 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0 AND ForceGetCount(2) != 0 AND ForceGetFirst(2) != 0 AND (ForceGetCount(2) - 1) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (ForceGetCount(1) >= 1) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) != 0) != 0 AND (ForceGetCount(1) - 1) == 0 AND !(get('ボス死亡')) != 0.
- `0x3436 AllUnitEscape()`: 5 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0 AND ForceGetCount(2) != 0 AND ForceGetFirst(2) != 0 AND (ForceGetCount(2) - 1) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (ForceGetCount(1) >= 1) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) != 0) != 0 AND (ForceGetCount(1) - 1) == 0 AND !(get('ボス死亡')) != 0.
- `0x3440 AllUnitEscape()`: 5 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0 AND ForceGetCount(2) != 0 AND ForceGetFirst(2) != 0 AND (ForceGetCount(2) - 1) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (ForceGetCount(1) >= 1) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) != 0) != 0 AND (ForceGetCount(1) - 1) == 0 AND !(get('ボス死亡')) != 0.
- `0x3228 UnitEscape(ForceGetFirst(1), 0)`: 1 explored alternative(s). Example local guards: UnitGetByPID('PID_GATRIE') != 0 AND ForceGetCount(2) != 0 AND ForceGetFirst(2) != 0 AND (ForceGetCount(2) - 1) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) == 0 AND UnitQueryJID(ForceGetFirst(1), 'JID_CROW') == 0 AND UnitQueryJID(ForceGetFirst(1), 'JID_BIRD_C') != 0.

## Ch.14: Training — Scripts/C15.cmb

### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [5, 4, 37, 249], 'tile_event': {'x': 5, 'y': 4, 'action_code': 37, 'key_pool_offset': 249, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [2, 3, 37, 273], 'tile_event': {'x': 2, 'y': 3, 'action_code': 37, 'key_pool_offset': 273, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [7, 23, 37, 280], 'tile_event': {'x': 7, 'y': 23, 'action_code': 37, 'key_pool_offset': 280, 'key': '訪問３'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [5, 4, 9, 249], 'tile_event': {'x': 5, 'y': 4, 'action_code': 9, 'key_pool_offset': 249, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [2, 3, 9, 273], 'tile_event': {'x': 2, 'y': 3, 'action_code': 9, 'key_pool_offset': 273, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [7, 23, 9, 280], 'tile_event': {'x': 7, 'y': 23, 'action_code': 9, 'key_pool_offset': 280, 'key': '訪問３'}}`. Local trace: all explored local paths returned


### Scene 19: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x162E AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 22: function_22

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 23: function_23

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [224, 2064, 0, 575], 'conversation_event': {'actor': 'PID_MARCIA', 'target': 'PID_MAKAROV', 'reversible': False, 'key': 'マカロフ仲間'}}`. Local trace: all explored local paths returned

- `0x1FC5 UnitTransferToForceByPID('PID_MAKAROV', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 36: function_36

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [2144]}`. Local trace: all explored local paths returned

- `0x2435 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 37: function_37

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [2896]}`. Local trace: all explored local paths returned

- `0x2507 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.

## Ch.15: The Feral Frontier — Scripts/C16.cmb

### Scene 20: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x179A AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x17AF Join('always_dbg_mik_08')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17B7 Join('always_dbg_mik_09')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17BF Join('always_dbg_mik_10')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17C7 Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17CF Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17D7 Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17DF Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x17E7 Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 21: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1AA2 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x1CE7 UnitEscapeByPID('PID_TOPUCK_EV')`: 2 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_SENERIO')) != 0.
- `0x1E45 UnitEscapeByPID('PID_SENERIO_EV')`: 2 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.

### Scene 23: function_23

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x202B UnitEscapeByPID('PID_SOANVALCKE')`: 3 explored alternative(s). Example local guards: !(get('ソーンバルケ登場トリガ')) == 0 AND get('ソーンバルケイベント') == 0 AND (MindGetMe() == UnitGetByPID('PID_LETHE')) == 0 AND (MindGetMe() == UnitGetByPID('PID_MORDY')) != 0 AND (MindGetMe() == UnitGetByPID('PID_MORDY')) != 0.
- `0x2144 UnitTransferToForceByPID('PID_SOANVALCKE', 0)`: 9 explored alternative(s). Example local guards: !(get('ソーンバルケ登場トリガ')) == 0 AND get('ソーンバルケイベント') == 0 AND (MindGetMe() == UnitGetByPID('PID_LETHE')) == 0 AND (MindGetMe() == UnitGetByPID('PID_MORDY')) != 0 AND (MindGetMe() == UnitGetByPID('PID_MORDY')) != 0 AND (UnitGetByPos(28, 3) == 0) != 0.
- `0x2243 UnitEscapeByPID('PID_SOANVALCKE')`: 4 explored alternative(s). Example local guards: !(get('ソーンバルケ登場トリガ')) == 0 AND get('ソーンバルケイベント') == 0 AND (MindGetMe() == UnitGetByPID('PID_LETHE')) == 0 AND (MindGetMe() == UnitGetByPID('PID_MORDY')) == 0 AND (UnitGetByPos(28, 3) == 0) != 0 AND (MindGetMe() == UnitGetByPID('PID_SENERIO')) != 0.

### Scene 33: function_33

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [849]}`. Local trace: all explored local paths returned

- `0x2539 set('gf_complete')`: 8 explored alternative(s). Example local guards: (BMGetPhase() == 1) != 0 AND (MindGetTarget() == UnitGetByPID('PID_IKE')) != 0 AND (GetBattleType() & -2147483648) != 0.

### Scene 34: function_34

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [3071]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x25F7 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x2C2E AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !((GCST() & 1)) != 0.

### Scene 39: function_39

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.16: The Atonement — Scripts/C17.cmb

### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [14, 18, 12, 491], 'tile_event': {'x': 14, 'y': 18, 'action_code': 12, 'key_pool_offset': 491, 'key': '宝箱１'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [13, 19, 12, 556], 'tile_event': {'x': 13, 'y': 19, 'action_code': 12, 'key_pool_offset': 556, 'key': '宝箱２'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [23, 8, 12, 575], 'tile_event': {'x': 23, 'y': 8, 'action_code': 12, 'key_pool_offset': 575, 'key': '宝箱３'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [5, 7, 12, 598], 'tile_event': {'x': 5, 'y': 7, 'action_code': 12, 'key_pool_offset': 598, 'key': '宝箱４'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [22, 8, 12, 622], 'tile_event': {'x': 22, 'y': 8, 'action_code': 12, 'key_pool_offset': 622, 'key': '宝箱５'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 7, 12, 642], 'tile_event': {'x': 6, 'y': 7, 'action_code': 12, 'key_pool_offset': 642, 'key': '宝箱６'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [14, 6, 13, 660], 'tile_event': {'x': 14, 'y': 6, 'action_code': 13, 'key_pool_offset': 660, 'key': ''}}`. Local trace: all explored local paths returned

- `0x102B set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [12, 17, 11, 673], 'tile_event': {'x': 12, 'y': 17, 'action_code': 11, 'key_pool_offset': 673, 'key': 'F1217'}}`. Local trace: all explored local paths returned


### Scene 11: function_11

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [24, 10, 11, 688], 'tile_event': {'x': 24, 'y': 10, 'action_code': 11, 'key_pool_offset': 688, 'key': 'F2410'}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [3, 9, 11, 694], 'tile_event': {'x': 3, 'y': 9, 'action_code': 11, 'key_pool_offset': 694, 'key': 'F0309'}}`. Local trace: all explored local paths returned


### Scene 13: function_13

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [2, 17, 44, 660], 'tile_event': {'x': 2, 'y': 17, 'action_code': 44, 'key_pool_offset': 660, 'key': ''}}`. Local trace: all explored local paths returned

- `0x112A UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 14: function_14

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [2, 16, 44, 660], 'tile_event': {'x': 2, 'y': 16, 'action_code': 44, 'key_pool_offset': 660, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1182 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 20: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x13CE AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1596 Join('always_c16')`: 9 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND IsE3Version() != 0 AND !((GCST() & 3)) != 0.

### Scene 21: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1626 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x1991 UnitEscapeByPID('PID_OLIVER')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 23: function_23

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 9, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 9, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 6, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [2, 4, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 27: function_27

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 8, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 28: function_28

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 0], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 0, 'argc': 1, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1BB4 UnitTransferToForceByPID('PID_DALAHOWE', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 30: function_30

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2459, 2003, 0, 902], 'conversation_event': {'actor': 'PID_MIST', 'target': 'PID_DALAHOWE', 'reversible': False, 'key': 'ダラハウ仲間'}}`. Local trace: all explored local paths returned


### Scene 31: function_31

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2480, 2003, 0, 902], 'conversation_event': {'actor': 'PID_LOFA', 'target': 'PID_DALAHOWE', 'reversible': False, 'key': 'ダラハウ仲間'}}`. Local trace: all explored local paths returned


### Scene 32: function_32

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2501, 2003, 0, 902], 'conversation_event': {'actor': 'PID_SENERIO', 'target': 'PID_DALAHOWE', 'reversible': False, 'key': 'ダラハウ仲間'}}`. Local trace: all explored local paths returned


### Scene 33: function_33

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [120, 2003, 0, 902], 'conversation_event': {'actor': 'PID_TOPUCK', 'target': 'PID_DALAHOWE', 'reversible': False, 'key': 'ダラハウ仲間'}}`. Local trace: all explored local paths returned


### Scene 34: function_34

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2537, 2003, 0, 902], 'conversation_event': {'actor': 'PID_SOTHE', 'target': 'PID_DALAHOWE', 'reversible': False, 'key': 'ダラハウ仲間'}}`. Local trace: all explored local paths returned


### Scene 48: function_48

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [661]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x21EF AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

## Ch.17: Day Breaks — Scripts/C18.cmb

### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [27, 9, 41, 247], 'tile_event': {'x': 27, 'y': 9, 'action_code': 41, 'key_pool_offset': 247, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 36: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2E21 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x2E36 Join('always_dbg_mik_04c')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E3E Join('always_dbg_mik_08')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E46 Join('always_dbg_mik_09')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E4E Join('always_dbg_mik_10')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E56 Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E5E Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E66 Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E6E Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E76 Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E7E Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E86 Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2E97 UnitTransferToForceByPID('PID_CHINON', 7)`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 37: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x333E AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x3394 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x37BC UnitEscapeByPID('PID_OLIVER')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37C4 UnitEscapeByPID('PID_ZAKO_EV1')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37CC UnitEscapeByPID('PID_ZAKO_EV2')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37D4 UnitEscapeByPID('PID_ZAKO_EV3')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37DC UnitEscapeByPID('PID_ZAKO_EV4')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37E4 UnitEscapeByPID('PID_ZAKO_EV5')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37EC UnitEscapeByPID('PID_ZAKO_EV6')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37F4 UnitEscapeByPID('PID_ZAKO_EV7')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x37FC UnitEscapeByPID('PID_ZAKO_EV8')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.
- `0x3804 UnitEscapeByPID('PID_ZAKO_EV9')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND Comeback() != 0.

### Scene 39: function_39

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 40: function_40

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 41: function_41

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 42: function_42

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 43: function_43

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 44: function_44

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 45: function_45

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 46: function_46

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 47: function_47

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 48: function_48

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 0], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 49: function_49

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 0], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 50: function_50

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 51: function_51

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 52: function_52

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 53: function_53

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 54: function_54

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 1], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 55: function_55

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 1], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 56: function_56

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 57: function_57

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 60: function_60

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 62: function_62

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 2], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 2}}`. Local trace: all explored local paths returned


### Scene 63: function_63

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 64: function_64

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 1], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 65: function_65

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 4, 1], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 66: function_66

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 1], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 67: function_67

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 1], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 68: function_68

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 1], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 69: function_69

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 1], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 80: function_80

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [2590]}`. Local trace: all explored local paths returned

- `0x5539 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 82: function_82

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [572]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x57C4 Complete18(1)`: 10 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND 1 != 0 AND (ForceGetFirst(1) == 0) != 0 AND (ForceGetCount(5) > 0) != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0.
- `0x5729 UnitEscape(ForceGetFirst(1), 0)`: 4 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND 1 != 0 AND (ForceGetFirst(1) == 0) == 0.

### Scene 83: Opening18_2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x57F2 BMSetTurn(1)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x595D UnitEscapeByPID('PID_TIBARN')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x5965 UnitEscapeByPID('PID_VULCI')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x596D UnitEscapeByPID('PID_JANAFF')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x5B58 UnitEscapeByPID('PID_RIEUSION')`: 1 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_MIST') != 0 AND UnitCheckExistsByPID('PID_LETHE') != 0 AND UnitCheckExistsByPID('PID_MORDY') != 0.

### Scene 85: function_85

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [248]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x5F00 Complete18(2)`: 3 explored alternative(s). Example local guards: 1 != 0 AND (ForceGetFirst(1) == 0) != 0 AND (ForceGetCount(5) > 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0.
- `0x5EA8 UnitEscape(ForceGetFirst(1), 0)`: 2 explored alternative(s). Example local guards: 1 != 0 AND (ForceGetFirst(1) == 0) == 0.

### Scene 86: Opening18_3

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x5F2E BMSetTurn(1)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6678 UnitEscapeByPID('PID_LEARNE_EV')`: 1 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0.
- `0x6680 UnitEscapeByPID('PID_NASIR')`: 1 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0.
- `0x6688 UnitEscapeByPID('PID_OLIVER')`: 1 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0.

### Scene 88: function_88

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [585]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x6DA7 UnitEscapeByPID('PID_OLIVER')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x7100 UnitEscapeByPID('PID_NASIR')`: 15 explored alternative(s). Example local guards: 1 != 0 AND (ForceGetFirst(1) == 0) != 0 AND !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !((GCST() & 1)) != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND UnitCheckExistsByPID('PID_MIST') != 0 AND (ForceGetCount(5) > 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0.
- `0x713A Complete18(3)`: 15 explored alternative(s). Example local guards: 1 != 0 AND (ForceGetFirst(1) == 0) != 0 AND !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !((GCST() & 1)) != 0 AND UnitCheckExistsByPID('PID_SENERIO') != 0 AND UnitCheckExistsByPID('PID_BOLE') != 0 AND UnitCheckExistsByPID('PID_MIST') != 0 AND (ForceGetCount(5) > 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT') != 0.

### Scene 89: Opening18_4

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x7166 BMSetTurn(1)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x7526 UnitEscapeByPID('PID_RIEUSION')`: 1 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0.
- `0x752E UnitEscapeByPID('PID_TIBARN')`: 1 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0.
- `0x7536 UnitEscapeByPID('PID_VULCI')`: 1 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0.
- `0x753E UnitEscapeByPID('PID_JANAFF')`: 1 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0.
- `0x77A0 UnitEscape(UnitGetByPos(5, 50), 0)`: 2 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND UnitGetByPID('PID_IKE') != 0 AND UnitGetByPID('PID_LEARNE') != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0 AND UnitCheckExistsByPID('PID_MIST') != 0 AND !((GCST() & 1)) != 0 AND !((GCST() & 1)) != 0 AND 1 != 0 AND (UnitGetByPos(5, 50) == 0) == 0.

### Scene 90: function_90

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 92: function_92

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 2], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 2}}`. Local trace: all explored local paths returned


### Scene 94: function_94

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [4517]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x7FD6 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND 1 != 0 AND (ForceGetFirst(1) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND !(UnitCheckExistsByPID('PID_RIEUSION')) != 0 AND !(UnitCheckExistsByPID('PID_TIBARN')) != 0 AND !(UnitCheckExistsByPID('PID_VULCI')) != 0 AND !(UnitCheckExistsByPID('PID_JANAFF')) != 0 AND UnitGetByPID('PID_RIEUSION') != 0 AND UnitGetByPID('PID_TIBARN') != 0 AND UnitGetByPID('PID_VULCI') != 0 AND UnitGetByPID('PID_JANAFF') != 0.
- `0x836A AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND 1 != 0 AND (ForceGetFirst(1) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND !(UnitCheckExistsByPID('PID_RIEUSION')) != 0 AND !(UnitCheckExistsByPID('PID_TIBARN')) != 0 AND !(UnitCheckExistsByPID('PID_VULCI')) != 0 AND !(UnitCheckExistsByPID('PID_JANAFF')) != 0 AND UnitGetByPID('PID_RIEUSION') != 0 AND UnitGetByPID('PID_TIBARN') != 0 AND UnitGetByPID('PID_VULCI') != 0 AND UnitGetByPID('PID_JANAFF') != 0.

## Ch.18: Crimea Marches — Scripts/C19.cmb

### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [10, 18, 12, 211], 'tile_event': {'x': 10, 'y': 18, 'action_code': 12, 'key_pool_offset': 211, 'key': '宝箱１'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [30, 19, 12, 271], 'tile_event': {'x': 30, 'y': 19, 'action_code': 12, 'key_pool_offset': 271, 'key': '宝箱２'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [31, 19, 12, 290], 'tile_event': {'x': 31, 'y': 19, 'action_code': 12, 'key_pool_offset': 290, 'key': '宝箱３'}}`. Local trace: all explored local paths returned


### Scene 18: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1E87 UnitTransferToForceByPID('PID_CHINON', 7)`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1E8C AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 19: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x21D4 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x2656 UnitTransferToForceByPID('PID_RIEUSION', 0)`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) != 0.
- `0x2660 UnitTransferToForceByPID('PID_JANAFF', 0)`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) != 0.
- `0x266A UnitTransferToForceByPID('PID_VULCI', 0)`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) != 0.
- `0x2756 UnitEscapeByPID('PID_TIBARN')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) != 0 AND 1 != 0.
- `0x275E UnitEscapeByPID('PID_LEARNE')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) != 0 AND 1 != 0.
- `0x2952 UnitEscapeByPID('PID_DUMMY1')`: 4 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) != 0 AND 1 != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0.
- `0x2843 UnitEscapeByPID('PID_RIEUSION')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) == 0 AND 1 != 0 AND Comeback() != 0.
- `0x284B UnitEscapeByPID('PID_JANAFF')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) == 0 AND 1 != 0 AND Comeback() != 0.
- `0x2853 UnitEscapeByPID('PID_VULCI')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) == 0 AND 1 != 0 AND Comeback() != 0.
- `0x285B UnitEscapeByPID('PID_TIBARN')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) == 0 AND 1 != 0 AND Comeback() != 0.
- `0x2863 UnitEscapeByPID('PID_LEARNE')`: 2 explored alternative(s). Example local guards: ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND (GCST() & 3) != 0 AND 1 != 0 AND Comeback() != 0 AND (DialogGetRes() == 0) == 0 AND 1 != 0 AND Comeback() != 0.

### Scene 20: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2CD1 UnitEscapeByPID('PID_NAESALA')`: 4 explored alternative(s). Example local guards: UnitGetByPos(25, 9) != 0 AND UnitCheckExistsByPID('PID_CHINON') != 0 AND UnitCheckExistsByPID('PID_CHINON') != 0 AND UnitCheckExistsByPID('PID_CHINON') != 0 AND UnitCheckExistsByPID('PID_CHINON') != 0 AND UnitGetByPos(25, 9) != 0.

### Scene 21: function_21

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [802, 3449, 1, 605], 'conversation_event': {'actor': 'PID_CHINON', 'target': 'PID_MIST', 'reversible': True, 'key': 'シノン会話ミスト'}}`. Local trace: all explored local paths returned


### Scene 22: function_22

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [802, 3502, 1, 569], 'conversation_event': {'actor': 'PID_CHINON', 'target': 'PID_LOFA', 'reversible': True, 'key': 'シノン会話ヨファ'}}`. Local trace: all explored local paths returned


### Scene 23: function_23

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [802, 3532, 1, 586], 'conversation_event': {'actor': 'PID_CHINON', 'target': 'PID_KILROY', 'reversible': True, 'key': 'シノン会話キルロイ'}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 0], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 27: function_27

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 48: function_48

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x380B set('gf_complete')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.

### Scene 49: function_49

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [4248]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x38A7 UnitTransferToForceByPID('PID_CHINON', 0)`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND UnitGetByPID('PID_CHINON') != 0 AND get('シノンを倒したのがアイク') != 0 AND get('シノン会話ヨファ') != 0.
- `0x38BF UnitTransferToForce(UnitGetByPID('PID_CHINON'), 0)`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND UnitGetByPID('PID_CHINON') != 0 AND get('シノンを倒したのがアイク') != 0 AND get('シノン会話ヨファ') != 0 AND UnitGetByPID('PID_CHINON') != 0.
- `0x390E AllUnitEscape()`: 11 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND UnitGetByPID('PID_CHINON') != 0 AND get('シノンを倒したのがアイク') != 0 AND get('シノン会話ヨファ') != 0 AND UnitGetByPID('PID_CHINON') != 0 AND (UnitSearchItem(UnitGetByPID('PID_CHINON'), 'IID_BRAVEBOW') >= 0) != 0.
- `0x3909 UnitTransferToForceByPID('PID_CHINON', 1)`: 8 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND UnitGetByPID('PID_CHINON') != 0 AND get('シノンを倒したのがアイク') != 0 AND get('シノン会話ヨファ') == 0 AND !(UnitCheckExistsByPID('PID_CHINON')) != 0.

### Scene 52: function_52

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


## Ch.19: Entrusted — Scripts/C20.cmb

### Scene 5: function_5

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x17EF UnitEscape(MindGetMe(), 0)`: 4 explored alternative(s). Example local guards: (UnitGetForce(MindGetMe()) == 2) != 0 AND MindGetMe() != 0 AND (UnitGetX(MindGetMe()) <= 13) != 0.

### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 14, 44, 654], 'tile_event': {'x': 6, 'y': 14, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 6, 44, 654], 'tile_event': {'x': 6, 'y': 6, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 13: function_13

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 8, 44, 654], 'tile_event': {'x': 6, 'y': 8, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 14: function_14

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 9, 44, 654], 'tile_event': {'x': 6, 'y': 9, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 15: function_15

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 10, 44, 654], 'tile_event': {'x': 6, 'y': 10, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 16: function_16

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 11, 44, 654], 'tile_event': {'x': 6, 'y': 11, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 17: function_17

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 12, 44, 654], 'tile_event': {'x': 6, 'y': 12, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 18: function_18

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 13, 44, 654], 'tile_event': {'x': 6, 'y': 13, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 19: function_19

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 15, 44, 654], 'tile_event': {'x': 6, 'y': 15, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 20: function_20

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 16, 44, 654], 'tile_event': {'x': 6, 'y': 16, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 21: function_21

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 17, 44, 654], 'tile_event': {'x': 6, 'y': 17, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 22: function_22

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 18, 44, 654], 'tile_event': {'x': 6, 'y': 18, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 23: function_23

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 19, 44, 654], 'tile_event': {'x': 6, 'y': 19, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 20, 44, 654], 'tile_event': {'x': 6, 'y': 20, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 21, 44, 654], 'tile_event': {'x': 6, 'y': 21, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 22, 44, 654], 'tile_event': {'x': 6, 'y': 22, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 27: function_27

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 23, 44, 654], 'tile_event': {'x': 6, 'y': 23, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 28: function_28

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 24, 44, 654], 'tile_event': {'x': 6, 'y': 24, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 25, 44, 654], 'tile_event': {'x': 6, 'y': 25, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 30: function_30

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 26, 44, 654], 'tile_event': {'x': 6, 'y': 26, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 31: function_31

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 28, 44, 654], 'tile_event': {'x': 6, 'y': 28, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 32: function_32

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 29, 44, 654], 'tile_event': {'x': 6, 'y': 29, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 33: function_33

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 31, 44, 654], 'tile_event': {'x': 6, 'y': 31, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 34: function_34

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 32, 44, 654], 'tile_event': {'x': 6, 'y': 32, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 35: function_35

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 34, 44, 654], 'tile_event': {'x': 6, 'y': 34, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 36: function_36

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 35, 44, 654], 'tile_event': {'x': 6, 'y': 35, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 37: function_37

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 6, 44, 654], 'tile_event': {'x': 25, 'y': 6, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 38: function_38

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 7, 44, 654], 'tile_event': {'x': 25, 'y': 7, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 39: function_39

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 8, 44, 654], 'tile_event': {'x': 25, 'y': 8, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 40: function_40

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 9, 44, 654], 'tile_event': {'x': 25, 'y': 9, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 41: function_41

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 10, 44, 654], 'tile_event': {'x': 25, 'y': 10, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 42: function_42

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 11, 44, 654], 'tile_event': {'x': 25, 'y': 11, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 43: function_43

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 12, 44, 654], 'tile_event': {'x': 25, 'y': 12, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 44: function_44

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 13, 44, 654], 'tile_event': {'x': 25, 'y': 13, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 45: function_45

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 14, 44, 654], 'tile_event': {'x': 25, 'y': 14, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 46: function_46

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 15, 44, 654], 'tile_event': {'x': 25, 'y': 15, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 47: function_47

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 16, 44, 654], 'tile_event': {'x': 25, 'y': 16, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 48: function_48

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 17, 44, 654], 'tile_event': {'x': 25, 'y': 17, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 49: function_49

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 18, 44, 654], 'tile_event': {'x': 25, 'y': 18, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 50: function_50

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 19, 44, 654], 'tile_event': {'x': 25, 'y': 19, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 51: function_51

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 20, 44, 654], 'tile_event': {'x': 25, 'y': 20, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 52: function_52

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 21, 44, 654], 'tile_event': {'x': 25, 'y': 21, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 53: function_53

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 22, 44, 654], 'tile_event': {'x': 25, 'y': 22, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 54: function_54

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 23, 44, 654], 'tile_event': {'x': 25, 'y': 23, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 55: function_55

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 24, 44, 654], 'tile_event': {'x': 25, 'y': 24, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 56: function_56

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 25, 44, 654], 'tile_event': {'x': 25, 'y': 25, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 57: function_57

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 26, 44, 654], 'tile_event': {'x': 25, 'y': 26, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 58: function_58

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 27, 44, 654], 'tile_event': {'x': 25, 'y': 27, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 59: function_59

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 28, 44, 654], 'tile_event': {'x': 25, 'y': 28, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 60: function_60

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 29, 44, 654], 'tile_event': {'x': 25, 'y': 29, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 61: function_61

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 30, 44, 654], 'tile_event': {'x': 25, 'y': 30, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 62: function_62

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 31, 44, 654], 'tile_event': {'x': 25, 'y': 31, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 63: function_63

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 32, 44, 654], 'tile_event': {'x': 25, 'y': 32, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 64: function_64

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 33, 44, 654], 'tile_event': {'x': 25, 'y': 33, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 65: function_65

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 34, 44, 654], 'tile_event': {'x': 25, 'y': 34, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 66: function_66

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [25, 35, 44, 654], 'tile_event': {'x': 25, 'y': 35, 'action_code': 44, 'key_pool_offset': 654, 'key': ''}}`. Local trace: all explored local paths returned


### Scene 75: function_75

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x26A7 AllUnitEscape()`: 2 explored alternative(s). Example local guards: Comeback() != 0.
- `0x28F2 AllUnitEscape()`: 2 explored alternative(s). Example local guards: Comeback() != 0.

### Scene 76: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2962 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x2977 Join('always_dbg_mik_02')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x297F Join('always_dbg_mik_03')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2987 Join('always_dbg_mik_05')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x298F Join('always_dbg_mik_08')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x2997 Join('always_dbg_mik_09')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x299F Join('always_dbg_mik_10')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29A7 Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29AF Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29B7 Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29BF Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29C7 Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29CF Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29D7 Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x29DF Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 77: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2C78 UnitEscapeByPID('PID_TIAMAT_EV')`: 1 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0.
- `0x2C80 UnitEscapeByPID('PID_SENERIO_EV')`: 1 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0.

### Scene 78: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x3144 UnitEscapeByPID('PID_NASIR')`: 18 explored alternative(s). Example local guards: Normal() != 0 AND Normal() != 0 AND Hard() == 0 AND Maniac() != 0 AND (UnitSearchItem(UnitGetByPID('PID_NAESALA'), 'IID_CHANGERING2') >= 0) != 0 AND UnitCheckLiveByPID('PID_RIEUSION') != 0 AND UnitCheckLiveByPID('PID_JANAFF') == 0 AND UnitCheckLiveByPID('PID_VULCI') != 0.

### Scene 79: function_79

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 80: function_80

Trigger metadata: `{'kind': 0, 'argc': 1, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x32E6 UnitTransferToForce(ForceGetFirst(1), 2)`: 5 explored alternative(s). Example local guards: (UnitGetXByPID('PID_NAESALA') <= 15) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) == 0 AND UnitQueryPID(ForceGetFirst(1), 'PID_K_ZAKO') != 0.

### Scene 81: function_81

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x33E6 UnitEscapeByPID('PID_NAESALA')`: 2 explored alternative(s). Example local guards: get('ネサラ死亡') != 0 AND !(get('ネサラ退却')) != 0 AND get('ネサラ死亡オンバト') != 0.

### Scene 82: function_82

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [437, 1249, 1, 807], 'conversation_event': {'actor': 'PID_JANAFF', 'target': 'PID_NAESALA', 'reversible': True, 'key': 'ネサラ会話'}}`. Local trace: all explored local paths returned


### Scene 83: function_83

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [473, 1249, 1, 807], 'conversation_event': {'actor': 'PID_VULCI', 'target': 'PID_NAESALA', 'reversible': True, 'key': 'ネサラ会話'}}`. Local trace: all explored local paths returned


### Scene 84: function_84

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [1249, 3012, 0, 818], 'conversation_event': {'actor': 'PID_NAESALA', 'target': 'PID_RIEUSION', 'reversible': False, 'key': 'ネサラ会話リュシオン'}}`. Local trace: all explored local paths returned

- `0x3559 UnitTransferToForceByPID('PID_NAESALA', 2)`: 3 explored alternative(s). Example local guards: get('カラス兵死亡') != 0.

### Scene 104: function_104

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [1956]}`. Local trace: all explored local paths returned

- `0x3CE9 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 105: function_105

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [4262]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x3DFC AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND !(get('ネサラ退却')) != 0 AND UnitCheckExistsByPID('PID_NAESALA') != 0.

## Ch.20: Defending Talrega — Scripts/C21.cmb

### Scene 1: function_1

Trigger metadata: `{'kind': 14, 'argc': 0, 'parameters': [20, 83, 3]}`. Local trace: all explored local paths returned

- `0x1109 Join('always_kariru')`: 1 explored alternative(s). Example local guards: Check() == 0 AND (DialogGetRes() == 0) != 0.

### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [11, 5, 37, 400], 'tile_event': {'x': 11, 'y': 5, 'action_code': 37, 'key_pool_offset': 400, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [11, 5, 9, 400], 'tile_event': {'x': 11, 'y': 5, 'action_code': 9, 'key_pool_offset': 400, 'key': '訪問１'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [17, 17, 37, 560], 'tile_event': {'x': 17, 'y': 17, 'action_code': 37, 'key_pool_offset': 560, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [17, 17, 9, 560], 'tile_event': {'x': 17, 'y': 17, 'action_code': 9, 'key_pool_offset': 560, 'key': '訪問２'}}`. Local trace: all explored local paths returned


### Scene 11: function_11

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [24, 7, 41, 687], 'tile_event': {'x': 24, 'y': 7, 'action_code': 41, 'key_pool_offset': 687, 'key': ''}}`. Local trace: all explored local paths returned

- `0x13BB set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 21: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1999 Join('always_dbg_mik_10')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19A1 Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19A9 Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19B1 Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19B9 Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19C1 Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19C9 Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19D1 Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19D9 Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19DE AllUnitEscape()`: 2 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 24: function_24

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [1, 1, 1], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 1}}`. Local trace: all explored local paths returned

- `0x20C9 UnitEscapeByPID('PID_HAAR')`: 3 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_JILL') != 0 AND !(get('会話ジル−シハラム終了')) != 0.

### Scene 26: function_26

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2485, 2266, 0, 891], 'conversation_event': {'actor': 'PID_JILL', 'target': 'PID_SIHARAMU', 'reversible': False, 'key': '会話ジル−シハラム'}}`. Local trace: all explored local paths returned

- `0x21B1 UnitTransferToForceByPID('PID_JILL', 1)`: 1 explored alternative(s). Example local guards: (PersonGetYellLevel('PID_JILL', 'PID_MIST') == 3) == 0 AND (PersonGetYellLevel('PID_JILL', 'PID_LETHE') == 3) == 0.

### Scene 27: function_27

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2266, 2485, 0, 891], 'conversation_event': {'actor': 'PID_SIHARAMU', 'target': 'PID_JILL', 'reversible': False, 'key': '会話ジル−シハラム'}}`. Local trace: all explored local paths returned

- `0x22BD UnitTransferToForceByPID('PID_JILL', 1)`: 1 explored alternative(s). Example local guards: (PersonGetYellLevel('PID_JILL', 'PID_MIST') == 3) == 0 AND (PersonGetYellLevel('PID_JILL', 'PID_LETHE') == 3) == 0.

### Scene 28: function_28

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 30: function_30

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 0], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 31: function_31

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [10, 10, 0], 'inferred_turn_trigger': {'first_turn': 10, 'last_turn': 10, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 32: function_32

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 33: function_33

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 34: function_34

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 35: function_35

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 51: function_51

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [688]}`. Local trace: all explored local paths returned

- `0x2B07 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 52: function_52

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned

- `0x2D0E set('gf_gameover')`: 4 explored alternative(s). Example local guards: Normal() != 0 AND (BMGetTurn() == 15) != 0.

## Ch.21: Without a King — Scripts/C22.cmb

### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [7, 6, 12, 205], 'tile_event': {'x': 7, 'y': 6, 'action_code': 12, 'key_pool_offset': 205, 'key': '宝箱１'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [9, 6, 12, 264], 'tile_event': {'x': 9, 'y': 6, 'action_code': 12, 'key_pool_offset': 264, 'key': '宝箱２'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [14, 3, 12, 289], 'tile_event': {'x': 14, 'y': 3, 'action_code': 12, 'key_pool_offset': 289, 'key': '宝箱３'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [24, 3, 12, 307], 'tile_event': {'x': 24, 'y': 3, 'action_code': 12, 'key_pool_offset': 307, 'key': '宝箱４'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [30, 14, 12, 328], 'tile_event': {'x': 30, 'y': 14, 'action_code': 12, 'key_pool_offset': 328, 'key': '宝箱５'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [30, 15, 12, 348], 'tile_event': {'x': 30, 'y': 15, 'action_code': 12, 'key_pool_offset': 348, 'key': '宝箱６'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [16, 28, 12, 368], 'tile_event': {'x': 16, 'y': 28, 'action_code': 12, 'key_pool_offset': 368, 'key': '宝箱７'}}`. Local trace: all explored local paths returned


### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [18, 28, 12, 390], 'tile_event': {'x': 18, 'y': 28, 'action_code': 12, 'key_pool_offset': 390, 'key': '宝箱８'}}`. Local trace: all explored local paths returned


### Scene 11: function_11

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [29, 17, 11, 413], 'tile_event': {'x': 29, 'y': 17, 'action_code': 11, 'key_pool_offset': 413, 'key': 'F2917'}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [24, 6, 11, 440], 'tile_event': {'x': 24, 'y': 6, 'action_code': 11, 'key_pool_offset': 440, 'key': 'F2406'}}`. Local trace: all explored local paths returned


### Scene 13: function_13

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [14, 6, 11, 446], 'tile_event': {'x': 14, 'y': 6, 'action_code': 11, 'key_pool_offset': 446, 'key': 'F1406'}}`. Local trace: all explored local paths returned


### Scene 14: function_14

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [8, 9, 11, 452], 'tile_event': {'x': 8, 'y': 9, 'action_code': 11, 'key_pool_offset': 452, 'key': 'F0809'}}`. Local trace: all explored local paths returned


### Scene 15: function_15

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [17, 26, 11, 458], 'tile_event': {'x': 17, 'y': 26, 'action_code': 11, 'key_pool_offset': 458, 'key': 'F1726'}}`. Local trace: all explored local paths returned


### Scene 19: function_19

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [10, 16, 13, 533], 'tile_event': {'x': 10, 'y': 16, 'action_code': 13, 'key_pool_offset': 533, 'key': ''}}`. Local trace: all explored local paths returned

- `0x16D7 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 22: function_22

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [16, 23, 44, 533], 'tile_event': {'x': 16, 'y': 23, 'action_code': 44, 'key_pool_offset': 533, 'key': ''}}`. Local trace: all explored local paths returned

- `0x18D6 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 30: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1D76 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1D8B Join('always_dbg_mik_02')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1D93 Join('always_dbg_mik_03')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1D9B Join('always_dbg_mik_05')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DA3 Join('always_dbg_mik_08')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DAB Join('always_dbg_mik_09')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DB3 Join('always_dbg_mik_10')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DBB Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DC3 Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DCB Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DD3 Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DDB Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DE3 Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DEB Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DF3 Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1DFB Join('always_dbg_mik_21')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 31: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x237A UnitEscapeByPID('PID_ENA_EV2')`: 2 explored alternative(s). Example local guards: ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0.

### Scene 36: function_36

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2577, 2846, 0, 865], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_TAURONEO', 'reversible': False, 'key': 'タウロニオ仲間'}}`. Local trace: all explored local paths returned

- `0x28CD UnitTransferToForceByPID('PID_TAURONEO', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 37: function_37

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 38: function_38

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 39: function_39

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 40: function_40

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 41: function_41

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 8, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 42: function_42

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 43: function_43

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [19, 19, 0], 'inferred_turn_trigger': {'first_turn': 19, 'last_turn': 19, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 64: function_64

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [534]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x328A UnitEscape(ForceGetFirst(1), 0)`: 2 explored alternative(s). Example local guards: ForceGetFirst(1) != 0.
- `0x32A2 UnitEscape(ForceGetFirst(3), 0)`: 2 explored alternative(s). Example local guards: ForceGetFirst(1) == 0 AND ForceGetFirst(3) != 0.
- `0x32AD UnitEscapeByPID('PID_TIAMAT')`: 1 explored alternative(s). Example local guards: ForceGetFirst(1) == 0 AND ForceGetFirst(3) == 0.
- `0x32B5 UnitEscapeByPID('PID_SENERIO')`: 1 explored alternative(s). Example local guards: ForceGetFirst(1) == 0 AND ForceGetFirst(3) == 0.
- `0x35F5 UnitEscapeByPID('PID_ENA')`: 2 explored alternative(s). Example local guards: ForceGetFirst(1) == 0 AND ForceGetFirst(3) == 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) != 0) != 0 AND (ForceGetFirst(0) != UnitGetByPID('PID_IKE')) != 0 AND (ForceGetCount(0) - 1) == 0.
- `0x3714 AllUnitEscape()`: 2 explored alternative(s). Example local guards: ForceGetFirst(1) == 0 AND ForceGetFirst(3) == 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) != 0) != 0 AND (ForceGetFirst(0) != UnitGetByPID('PID_IKE')) != 0 AND (ForceGetCount(0) - 1) == 0.

## Ch.22: Solo — Scripts/C23.cmb

### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 9, 12, 170], 'tile_event': {'x': 6, 'y': 9, 'action_code': 12, 'key_pool_offset': 170, 'key': 'F0306'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 11, 12, 231], 'tile_event': {'x': 6, 'y': 11, 'action_code': 12, 'key_pool_offset': 231, 'key': 'F0308'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 13, 12, 248], 'tile_event': {'x': 6, 'y': 13, 'action_code': 12, 'key_pool_offset': 248, 'key': 'F0310'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [16, 9, 12, 264], 'tile_event': {'x': 16, 'y': 9, 'action_code': 12, 'key_pool_offset': 264, 'key': 'F2306'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [16, 11, 12, 284], 'tile_event': {'x': 16, 'y': 11, 'action_code': 12, 'key_pool_offset': 284, 'key': 'F2308'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [16, 13, 12, 303], 'tile_event': {'x': 16, 'y': 13, 'action_code': 12, 'key_pool_offset': 303, 'key': 'F2310'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [3, 9, 44, 323], 'tile_event': {'x': 3, 'y': 9, 'action_code': 44, 'key_pool_offset': 323, 'key': ''}}`. Local trace: all explored local paths returned

- `0x123E UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [3, 10, 44, 323], 'tile_event': {'x': 3, 'y': 10, 'action_code': 44, 'key_pool_offset': 323, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1296 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 11: function_11

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [19, 9, 44, 323], 'tile_event': {'x': 19, 'y': 9, 'action_code': 44, 'key_pool_offset': 323, 'key': ''}}`. Local trace: all explored local paths returned

- `0x12EE UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 12: function_12

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [19, 10, 44, 323], 'tile_event': {'x': 19, 'y': 10, 'action_code': 44, 'key_pool_offset': 323, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1346 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 25: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x18C2 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x18D7 Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x18DF Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x18E7 Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x18EF Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x18F7 Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x18FF Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1910 UnitTransferToForceByPID('PID_RIEUSION', 6)`: 2 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0 AND Normal() != 0.

### Scene 26: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1CDB AllUnitEscape()`: 1 explored alternative(s). Example local guards: UnitGetByPID('PID_RIEUSION') != 0 AND UnitGetByPID('PID_RIEUSION') != 0 AND (UnitGetForce(UnitGetByPID('PID_RIEUSION')) == 6) != 0 AND !((GCST() & 2)) != 0.

### Scene 28: function_28

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 30: function_30

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [10, 10, 0], 'inferred_turn_trigger': {'first_turn': 10, 'last_turn': 10, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 31: function_31

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 32: function_32

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 45: function_45

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [2149]}`. Local trace: all explored local paths returned

- `0x2BCD set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 46: function_46

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [3115]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2CA0 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0.

## Ch.23: The Great Bridge — Scripts/C24.cmb

### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [15, 7, 13, 253], 'tile_event': {'x': 15, 'y': 7, 'action_code': 13, 'key_pool_offset': 253, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1137 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 33: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1992 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x19A7 Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19AF Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19B7 Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19BF Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19C7 Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19CF Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x19D7 Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 35: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x20AB UnitEscapeByPID('PID_HAAR')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x20B3 UnitEscapeByPID('PID_DAYNE_DKN_1')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x20BB UnitEscapeByPID('PID_DAYNE_DKN_2')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x20C3 UnitEscapeByPID('PID_DAYNE_DKN_3')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 36: function_36

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x21EA UnitEscapeByPID('PID_DAYNE_DKN_1')`: 1 explored alternative(s). Example local guards: !(get('ハール退場イベント')) == 0 AND !(get('ハール再登場トリガ')) == 0 AND get('ハール再登場イベント') == 0 AND get('ハール死亡') == 0 AND get('ドラゴンナイト１死亡') != 0.
- `0x21FC UnitEscapeByPID('PID_DAYNE_DKN_2')`: 2 explored alternative(s). Example local guards: !(get('ハール退場イベント')) == 0 AND !(get('ハール再登場トリガ')) == 0 AND get('ハール再登場イベント') == 0 AND get('ハール死亡') == 0 AND get('ドラゴンナイト１死亡') != 0 AND get('ドラゴンナイト２死亡') != 0.
- `0x220E UnitEscapeByPID('PID_DAYNE_DKN_3')`: 4 explored alternative(s). Example local guards: !(get('ハール退場イベント')) == 0 AND !(get('ハール再登場トリガ')) == 0 AND get('ハール再登場イベント') == 0 AND get('ハール死亡') == 0 AND get('ドラゴンナイト１死亡') != 0 AND get('ドラゴンナイト２死亡') != 0 AND get('ドラゴンナイト３死亡') != 0.

### Scene 37: function_37

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 2], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 2}}`. Local trace: all explored local paths returned

- `0x24E7 UnitEscapeByPID('PID_ULYSSES')`: 1 explored alternative(s). Example local guards: get('クリミア増援トリガ') != 0 AND !(get('クリミア増援イベント１')) != 0.

### Scene 38: function_38

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2942, 1875, 0, 657], 'conversation_event': {'actor': 'PID_JILL', 'target': 'PID_HAAR', 'reversible': False, 'key': 'ハール会話'}}`. Local trace: all explored local paths returned

- `0x26B5 UnitTransferToForceByPID('PID_HAAR', 0)`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 39: function_39

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 40: function_40

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 41: function_41

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 62: function_62

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [254]}`. Local trace: all explored local paths returned

- `0x2ED8 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

## Ch.24: Battle Reunion — Scripts/C25.cmb

### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [12, 31, 9, 173], 'tile_event': {'x': 12, 'y': 31, 'action_code': 9, 'key_pool_offset': 173, 'key': 'F1237'}}`. Local trace: all explored local paths returned


### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [12, 31, 37, 173], 'tile_event': {'x': 12, 'y': 31, 'action_code': 37, 'key_pool_offset': 173, 'key': 'F1237'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [34, 12, 9, 339], 'tile_event': {'x': 34, 'y': 12, 'action_code': 9, 'key_pool_offset': 339, 'key': 'F3412'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [34, 12, 37, 339], 'tile_event': {'x': 34, 'y': 12, 'action_code': 37, 'key_pool_offset': 339, 'key': 'F3412'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [13, 10, 41, 393], 'tile_event': {'x': 13, 'y': 10, 'action_code': 41, 'key_pool_offset': 393, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1407 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 24: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x1F76 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1F8B Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1F93 Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1F9B Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1FA3 Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x20C1 AllUnitEscape()`: 8 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0 AND Comeback() != 0.

### Scene 25: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2523 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x2530 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 27: function_27

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: all explored local paths returned

- `0x2AF9 UnitEscapeByPID('PID_DUMMY1')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 28: function_28

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 29: function_29

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2D8D UnitEscapeByPID('PID_BLACKKNIGHT')`: 4 explored alternative(s). Example local guards: get('漆黒の騎士戦闘アイク') != 0 AND !(get('漆黒のとの戦闘後会話')) != 0 AND get('gf_gameover') == 0 AND get('漆黒の騎士戦闘アイクオンマップ') != 0 AND UnitGetByPID('PID_BLACKKNIGHT') != 0.

### Scene 30: function_30

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2286, 2395, 0, 869], 'conversation_event': {'actor': 'PID_ULYSSES', 'target': 'PID_IKE', 'reversible': False, 'key': '会話ユリシーズ⇒アイク'}}`. Local trace: all explored local paths returned


### Scene 31: function_31

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2766, 2395, 0, 892], 'conversation_event': {'actor': 'PID_LUCHINO', 'target': 'PID_IKE', 'reversible': False, 'key': '会話ルキノ⇒アイク'}}`. Local trace: all explored local paths returned


### Scene 32: function_32

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2395, 2192, 0, 911], 'conversation_event': {'actor': 'PID_IKE', 'target': 'PID_GEOFFRAY', 'reversible': False, 'key': '会話アイク⇒ジョフレ'}}`. Local trace: all explored local paths returned


### Scene 33: function_33

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2192, 2286, 1, 932], 'conversation_event': {'actor': 'PID_GEOFFRAY', 'target': 'PID_ULYSSES', 'reversible': True, 'key': '会話ジョフレ⇔ユリシーズ'}}`. Local trace: all explored local paths returned


### Scene 34: function_34

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2192, 2766, 1, 957], 'conversation_event': {'actor': 'PID_GEOFFRAY', 'target': 'PID_LUCHINO', 'reversible': True, 'key': '会話ジョフレ⇔ルキノ'}}`. Local trace: all explored local paths returned


### Scene 35: function_35

Trigger metadata: `{'kind': 8, 'argc': 0, 'parameters': [2192, 3050, 1, 978], 'conversation_event': {'actor': 'PID_GEOFFRAY', 'target': 'PID_KEVIN', 'reversible': True, 'key': '会話ジョフレ⇔ケビン'}}`. Local trace: all explored local paths returned


### Scene 36: function_36

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 37: function_37

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 38: function_38

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 39: function_39

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 40: function_40

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 0], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 41: function_41

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [2395]}`. Local trace: all explored local paths returned

- `0x3104 set('gf_gameover')`: 4 explored alternative(s). Example local guards: (BMGetPhase() == 0) != 0 AND (MindGetTarget() == UnitGetByPID('PID_BLACKKNIGHT')) != 0.

### Scene 56: function_56

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [394]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x372A UnitTransferToForce(UnitCheckExistsByPID2('PID_GEOFFRAY'), 0)`: 1 explored alternative(s). Example local guards: !(get('漆黒の騎士戦闘アイク')) != 0 AND UnitCheckExistsByPID('PID_BLACKKNIGHT') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0.
- `0x372F AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('漆黒の騎士戦闘アイク')) != 0 AND UnitCheckExistsByPID('PID_BLACKKNIGHT') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0.
- `0x3C7C UnitEscapeByPID('PID_BLACKKNIGHT_EV2')`: 8 explored alternative(s). Example local guards: !(get('漆黒の騎士戦闘アイク')) != 0 AND UnitCheckExistsByPID('PID_BLACKKNIGHT') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND !(get('漆黒の騎士戦闘アイク')) != 0 AND (get('gf_canceled') == 0) != 0 AND UnitGetByPID('PID_BLACKKNIGHT_EV2') != 0.
- `0x3C9F AllUnitEscape()`: 8 explored alternative(s). Example local guards: !(get('漆黒の騎士戦闘アイク')) != 0 AND UnitCheckExistsByPID('PID_BLACKKNIGHT') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND !(get('漆黒の騎士戦闘アイク')) != 0 AND (get('gf_canceled') == 0) != 0 AND UnitGetByPID('PID_BLACKKNIGHT_EV2') != 0.

### Scene 57: function_57

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned

- `0x3D13 set('gf_gameover')`: 4 explored alternative(s). Example local guards: Normal() != 0 AND (BMGetTurn() == 15) != 0.

## Ch.25: Strange Lands — Scripts/C26.cmb

### Scene 3: function_3

Trigger metadata: `{'kind': 14, 'argc': 0, 'parameters': [59, 184, 3]}`. Local trace: all explored local paths returned

- `0x13E8 Join('always_rarugo')`: 1 explored alternative(s). Example local guards: Check() == 0 AND UnitCheckLiveByPID('PID_CALILL') != 0 AND (DialogGetRes() == 0) != 0.

### Scene 38: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1E4E AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1E63 Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1E6B Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1E73 Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1E7B Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1E83 Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1E8B Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1E93 Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1E9B Join('always_dbg_mik_21')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1EA3 Join('always_dbg_mik_22')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1EAB Join('always_dbg_mik_24')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 39: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2613 UnitEscapeByPID('PID_TIAMAT_EV')`: 12 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0 AND !((GCST() & 1)) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') == 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') == 0 AND UnitCheckExistsByPID('PID_LAY_EV3') != 0.
- `0x261B UnitEscapeByPID('PID_SENERIO_EV')`: 12 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0 AND !((GCST() & 1)) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') == 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') == 0 AND UnitCheckExistsByPID('PID_LAY_EV3') != 0.
- `0x2623 UnitEscapeByPID('PID_LAY_EV3')`: 12 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0 AND !((GCST() & 1)) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') == 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') == 0 AND UnitCheckExistsByPID('PID_LAY_EV3') != 0.

### Scene 41: function_41

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 42: function_42

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 43: function_43

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 44: function_44

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 45: function_45

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 46: function_46

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 47: function_47

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 48: function_48

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 49: function_49

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 50: function_50

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 51: function_51

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 52: function_52

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 53: function_53

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [0, 0, 1], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 68: function_68

Trigger metadata: `{'kind': 7, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x2FD7 set('gf_complete')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.

### Scene 69: function_69

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [3744]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x303E AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x3565 UnitEscapeByPID('PID_DAYNE_SOL_1')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x356D UnitEscapeByPID('PID_DAYNE_SOL_2')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x3575 UnitEscapeByPID('PID_DAYNE_SOL_3')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x357D UnitEscapeByPID('PID_DAYNE_SOL_4')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x3585 UnitEscapeByPID('PID_DAYNE_SOL_5')`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.
- `0x3689 AllUnitEscape()`: 2 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0.

## Ch.26: Clash! — Scripts/C27.cmb

### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [11, 10, 13, 177], 'tile_event': {'x': 11, 'y': 10, 'action_code': 13, 'key_pool_offset': 177, 'key': ''}}`. Local trace: all explored local paths returned

- `0xD2F set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 11: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x126A AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 12: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x184B UnitEscapeByPID('PID_TIAMAT_EV')`: 12 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND get('G_クリミア忠臣イベント') != 0 AND !((GCST() & 1)) != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.
- `0x1853 UnitEscapeByPID('PID_SENERIO_EV')`: 11 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND get('G_クリミア忠臣イベント') != 0 AND !((GCST() & 1)) != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.

### Scene 13: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1AB6 UnitEscapeByPID('PID_TIAMAT_EV')`: 12 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.
- `0x1ABE UnitEscapeByPID('PID_SENERIO_EV')`: 12 explored alternative(s). Example local guards: !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0 AND UnitCheckExistsByPID('PID_TIAMAT_EV') != 0 AND UnitCheckExistsByPID('PID_SENERIO_EV') != 0.

### Scene 14: function_14

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [4, 4, 0], 'inferred_turn_trigger': {'first_turn': 4, 'last_turn': 4, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 15: function_15

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 16: function_16

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [7, 7, 0], 'inferred_turn_trigger': {'first_turn': 7, 'last_turn': 7, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 17: function_17

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 0], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 18: function_18

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [10, 10, 0], 'inferred_turn_trigger': {'first_turn': 10, 'last_turn': 10, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 19: function_19

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [13, 13, 0], 'inferred_turn_trigger': {'first_turn': 13, 'last_turn': 13, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 20: function_20

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [16, 16, 0], 'inferred_turn_trigger': {'first_turn': 16, 'last_turn': 16, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 35: function_35

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [178]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x22FF AllUnitEscape()`: 1 explored alternative(s). Example local guards: 1 != 0 AND (ForceGetFirst(1) == 0) != 0.
- `0x2203 UnitEscape(ForceGetFirst(1), 0)`: 2 explored alternative(s). Example local guards: 1 != 0 AND (ForceGetFirst(1) == 0) == 0.

## Ch.27: Moment of Fate — Scripts/C28.cmb

### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [16, 3, 41, 168], 'tile_event': {'x': 16, 'y': 3, 'action_code': 41, 'key_pool_offset': 168, 'key': ''}}`. Local trace: all explored local paths returned

- `0xE03 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [4, 7, 12, 181], 'tile_event': {'x': 4, 'y': 7, 'action_code': 12, 'key_pool_offset': 181, 'key': '宝箱１'}}`. Local trace: all explored local paths returned


### Scene 4: function_4

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 7, 12, 243], 'tile_event': {'x': 6, 'y': 7, 'action_code': 12, 'key_pool_offset': 243, 'key': '宝箱２'}}`. Local trace: all explored local paths returned


### Scene 5: function_5

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [11, 12, 12, 263], 'tile_event': {'x': 11, 'y': 12, 'action_code': 12, 'key_pool_offset': 263, 'key': '宝箱３'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [28, 7, 12, 286], 'tile_event': {'x': 28, 'y': 7, 'action_code': 12, 'key_pool_offset': 286, 'key': '宝箱４'}}`. Local trace: all explored local paths returned


### Scene 7: function_7

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [26, 7, 12, 310], 'tile_event': {'x': 26, 'y': 7, 'action_code': 12, 'key_pool_offset': 310, 'key': '宝箱５'}}`. Local trace: all explored local paths returned


### Scene 8: function_8

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [21, 12, 12, 329], 'tile_event': {'x': 21, 'y': 12, 'action_code': 12, 'key_pool_offset': 329, 'key': '宝箱６'}}`. Local trace: all explored local paths returned


### Scene 9: function_9

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [5, 6, 12, 347], 'tile_event': {'x': 5, 'y': 6, 'action_code': 12, 'key_pool_offset': 347, 'key': '宝箱７'}}`. Local trace: all explored local paths returned


### Scene 10: function_10

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [21, 18, 11, 364], 'tile_event': {'x': 21, 'y': 18, 'action_code': 11, 'key_pool_offset': 364, 'key': 'F2118'}}`. Local trace: all explored local paths returned


### Scene 11: function_11

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [11, 18, 11, 379], 'tile_event': {'x': 11, 'y': 18, 'action_code': 11, 'key_pool_offset': 379, 'key': 'F1118'}}`. Local trace: all explored local paths returned


### Scene 12: function_12

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [5, 14, 11, 385], 'tile_event': {'x': 5, 'y': 14, 'action_code': 11, 'key_pool_offset': 385, 'key': 'F0514'}}`. Local trace: all explored local paths returned


### Scene 13: function_13

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [27, 14, 11, 391], 'tile_event': {'x': 27, 'y': 14, 'action_code': 11, 'key_pool_offset': 391, 'key': 'F2714'}}`. Local trace: all explored local paths returned


### Scene 14: function_14

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [16, 11, 11, 397], 'tile_event': {'x': 16, 'y': 11, 'action_code': 11, 'key_pool_offset': 397, 'key': 'F1611'}}`. Local trace: all explored local paths returned


### Scene 15: function_15

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [6, 11, 44, 168], 'tile_event': {'x': 6, 'y': 11, 'action_code': 44, 'key_pool_offset': 168, 'key': ''}}`. Local trace: all explored local paths returned

- `0x1132 UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 16: function_16

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [26, 11, 44, 168], 'tile_event': {'x': 26, 'y': 11, 'action_code': 44, 'key_pool_offset': 168, 'key': ''}}`. Local trace: all explored local paths returned

- `0x118A UnitEscape(MindGetMe(), 0)`: 1 explored alternative(s). Example local guards: !(MindGetMe()) == 0.

### Scene 26: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x16AE AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x16C3 Join('always_dbg_mik_02')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16CB Join('always_dbg_mik_03')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16D3 Join('always_dbg_mik_05')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16DB Join('always_dbg_mik_08')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16E3 Join('always_dbg_mik_09')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16EB Join('always_dbg_mik_10')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16F3 Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16FB Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1703 Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x170B Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1713 Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x171B Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1723 Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x172B Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1733 Join('always_dbg_mik_21')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x173B Join('always_dbg_mik_22')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1743 Join('always_dbg_mik_24')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x174B Join('always_dbg_mik_25')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1753 Join('always_dbg_mik_27')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 27: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x19BA AllUnitEscape()`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0.
- `0x1B8B UnitEscapeByPID('PID_BLACKKNIGHT')`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0.
- `0x1BDA AllUnitEscape()`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_ULYSSES') != 0.

### Scene 40: function_40

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [169]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x257B UnitEscape(ForceGetFirst(1), 0)`: 2 explored alternative(s). Example local guards: ForceGetFirst(1) != 0.
- `0x2593 UnitEscape(ForceGetFirst(3), 0)`: 2 explored alternative(s). Example local guards: ForceGetFirst(1) == 0 AND ForceGetFirst(3) != 0.
- `0x292E AllUnitEscape()`: 5 explored alternative(s). Example local guards: ForceGetFirst(1) == 0 AND ForceGetFirst(3) == 0 AND !(UnitCheckExistsByPID('PID_TIAMAT')) != 0 AND !(UnitCheckExistsByPID('PID_SENERIO')) != 0 AND ForceGetCount(0) != 0 AND (ForceGetFirst(0) == 0) != 0.

## Ch.27-2: Moment of Fate — Scripts/C29.cmb

### Scene 0: function_0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0xC79 set('gf_complete')`: 1 explored alternative(s). Example local guards: (MindGetMe() == UnitGetByPID('PID_IKE')) != 0.
- `0xC92 set('gf_complete')`: 1 explored alternative(s). Example local guards: (MindGetMe() == UnitGetByPID('PID_IKE')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0.
- `0xD13 UnitEscape(MindGetMe(), 0)`: 5 explored alternative(s). Example local guards: (MindGetMe() == UnitGetByPID('PID_IKE')) == 0 AND (UnitGet(MindGetMe(), 4) == UnitGetByPID('PID_IKE')) != 0 AND (UnitGetX(UnitGet(MindGetMe(), 4)) == 8) == 0 AND (UnitGetX(UnitGet(MindGetMe(), 4)) == 9) != 0.

### Scene 1: function_1

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [8, 12, 14, 226], 'tile_event': {'x': 8, 'y': 12, 'action_code': 14, 'key_pool_offset': 226, 'key': '', 'action': 'Escape'}}`. Local trace: all explored local paths returned


### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [9, 12, 14, 226], 'tile_event': {'x': 9, 'y': 12, 'action_code': 14, 'key_pool_offset': 226, 'key': '', 'action': 'Escape'}}`. Local trace: all explored local paths returned


### Scene 3: function_3

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [10, 12, 14, 226], 'tile_event': {'x': 10, 'y': 12, 'action_code': 14, 'key_pool_offset': 226, 'key': '', 'action': 'Escape'}}`. Local trace: all explored local paths returned


### Scene 6: function_6

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0xE74 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x12B2 UnitEscapeByPID('PID_ENA')`: 2 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_MIST') != 0.

### Scene 7: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x136A AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.

### Scene 8: function_8

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 9: function_9

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [10]}`. Local trace: all explored local paths returned

- `0x1622 set('gf_gameover')`: 4 explored alternative(s). Example local guards: (BMGetPhase() == 0) != 0 AND (MindGetTarget() == UnitGetByPID('PID_BLACKKNIGHT')) != 0.

### Scene 12: function_12

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [528]}`. Local trace: all explored local paths returned

- `0x1702 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 13: function_13

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 2], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 2}}`. Local trace: all explored local paths returned

- `0x172A set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 15: function_15

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x204D UnitEscapeByPID('PID_ZAKO_EV1')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.
- `0x2055 UnitEscapeByPID('PID_ZAKO_EV2')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.
- `0x205D UnitEscapeByPID('PID_ZAKO_EV3')`: 1 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0.
- `0x245B UnitEscapeByPID('PID_IKE')`: 17 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0 AND (UnitGetXByPID('PID_IKE') != 9) != 0 AND (UnitGetXByPID('PID_IKE') >= 0) != 0 AND (UnitGetXByPID('PID_IKE') <= 8) != 0 AND (UnitGetXByPID('PID_MIST') >= 0) != 0 AND (UnitGetXByPID('PID_MIST') <= 8) != 0.
- `0x2463 UnitEscapeByPID('PID_MIST')`: 17 explored alternative(s). Example local guards: (ForceGetCount(1) == 0) != 0 AND (UnitGetXByPID('PID_IKE') != 9) != 0 AND (UnitGetXByPID('PID_IKE') >= 0) != 0 AND (UnitGetXByPID('PID_IKE') <= 8) != 0 AND (UnitGetXByPID('PID_MIST') >= 0) != 0 AND (UnitGetXByPID('PID_MIST') <= 8) != 0.

### Scene 17: function_17

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [65]}`. Local trace: all explored local paths returned

- `0x2980 AllUnitEscape()`: 2 explored alternative(s). Example local guards: get('G_漆黒の騎士倒した') != 0.

## Ch.28: Twisted Tower — Scripts/C30.cmb

### Scene 2: function_2

Trigger metadata: `{'kind': 5, 'argc': 0, 'parameters': [8, 7, 13, 274], 'tile_event': {'x': 8, 'y': 7, 'action_code': 13, 'key_pool_offset': 274, 'key': ''}}`. Local trace: all explored local paths returned

- `0x105B set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 18: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x161E AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x1648 Join('always_dbg_mik_10')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1650 Join('always_dbg_mik_11')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1658 Join('always_dbg_mik_12')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1660 Join('always_dbg_mik_13')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1668 Join('always_dbg_mik_14')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1670 Join('always_dbg_mik_15')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1678 Join('always_dbg_mik_16')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1680 Join('always_dbg_mik_17')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1688 Join('always_dbg_mik_19')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1690 Join('always_dbg_mik_21')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x1698 Join('always_dbg_mik_22')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16A0 Join('always_dbg_mik_24')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16A8 Join('always_dbg_mik_25')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16B0 Join('always_dbg_mik_26')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.
- `0x16B8 Join('always_dbg_mik_27')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND !(Maniac()) != 0.

### Scene 19: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x1780 UnitTransferToForceByPID('PID_ERINCIA_QUEEN', 7)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x18CE AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x1A94 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('G_漆黒の騎士倒した')) != 0 AND get('G_漆黒の騎士倒した') != 0 AND !(UnitCheckExistsByPID('PID_RIEUSION')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0.
- `0x1DDB UnitEscapeByPID('PID_RIEUSION_EV')`: 9 explored alternative(s). Example local guards: !(get('G_漆黒の騎士倒した')) != 0 AND get('G_漆黒の騎士倒した') != 0 AND !(UnitCheckExistsByPID('PID_RIEUSION')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0 AND Normal() != 0 AND Normal() != 0 AND get('G_漆黒の騎士倒した') != 0 AND !(UnitCheckExistsByPID('PID_RIEUSION')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0 AND UnitCheckLiveByPID('PID_RIEUSION') != 0 AND UnitCheckLiveByPID('PID_LAY') != 0.
- `0x1DE3 UnitEscapeByPID('PID_LAY_EV3')`: 9 explored alternative(s). Example local guards: !(get('G_漆黒の騎士倒した')) != 0 AND get('G_漆黒の騎士倒した') != 0 AND !(UnitCheckExistsByPID('PID_RIEUSION')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0 AND Normal() != 0 AND Normal() != 0 AND get('G_漆黒の騎士倒した') != 0 AND !(UnitCheckExistsByPID('PID_RIEUSION')) != 0 AND !(UnitCheckExistsByPID('PID_LAY')) != 0 AND UnitCheckLiveByPID('PID_RIEUSION') != 0 AND UnitCheckLiveByPID('PID_LAY') != 0.

### Scene 21: function_21

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [2, 2, 2], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 2}}`. Local trace: all explored local paths returned

- `0x2158 UnitEscapeByPID('PID_DAYNE_SOL_1')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 22: function_22

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 2], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 2}}`. Local trace: all explored local paths returned

- `0x249B UnitEscapeByPID('PID_NAESALA')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x24A3 UnitEscapeByPID('PID_LEARNE')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x24AB UnitEscapeByPID('PID_NEALUCHI')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x24B3 UnitEscapeByPID('PID_K_ZAKO_EV1')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x24BB UnitEscapeByPID('PID_K_ZAKO_EV2')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 23: function_23

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [5, 5, 0], 'inferred_turn_trigger': {'first_turn': 5, 'last_turn': 5, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 24: function_24

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [6, 6, 0], 'inferred_turn_trigger': {'first_turn': 6, 'last_turn': 6, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 25: function_25

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [8, 8, 0], 'inferred_turn_trigger': {'first_turn': 8, 'last_turn': 8, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 26: function_26

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 0], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 27: function_27

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 41: function_41

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [275]}`. Local trace: all explored local paths returned

- `0x2ACD UnitTransferToForceByPID('PID_ERINCIA_QUEEN', 0)`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x2AE2 AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x2B8A AllUnitEscape()`: 1 explored alternative(s). Example local guards: none in this scene.

## Endgame: Repatriation — Scripts/C31.cmb

### Scene 14: Opening0

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x29E2 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0.
- `0x29F6 Join('always_dbg_all_c')`: 1 explored alternative(s). Example local guards: !(get('DBG_最初からやってる')) != 0 AND (ForceGetCount(5) == 0) != 0 AND Normal() != 0.

### Scene 15: Opening1

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x2FAE AllUnitEscape()`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND !((GCST() & 2)) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0.
- `0x3676 UnitEscapeByPID('PID_IKE_EV')`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND !((GCST() & 2)) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0 AND (0 < 15) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (0 >= 15) != 0 AND get('G_漆黒の騎士倒した') != 0 AND get('G_漆黒の騎士倒した') != 0 AND UnitCheckLiveByPID('PID_NASIR') != 0 AND (0 < 0) == 0.
- `0x367E UnitEscapeByPID('PID_ERINCIA_QUEEN_EV')`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND !((GCST() & 2)) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0 AND (0 < 15) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (0 >= 15) != 0 AND get('G_漆黒の騎士倒した') != 0 AND get('G_漆黒の騎士倒した') != 0 AND UnitCheckLiveByPID('PID_NASIR') != 0 AND (0 < 0) == 0.
- `0x3686 UnitEscapeByPID('PID_SENERIO_EV')`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND !((GCST() & 2)) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0 AND (0 < 15) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (0 >= 15) != 0 AND get('G_漆黒の騎士倒した') != 0 AND get('G_漆黒の騎士倒した') != 0 AND UnitCheckLiveByPID('PID_NASIR') != 0 AND (0 < 0) == 0.
- `0x368E UnitEscapeByPID('PID_TIAMAT_EV')`: 1 explored alternative(s). Example local guards: UnitCheckLiveByPID('PID_ULYSSES') != 0 AND UnitCheckLiveByPID('PID_GEOFFRAY') != 0 AND UnitCheckLiveByPID('PID_LUCHINO') != 0 AND !((GCST() & 2)) != 0 AND (GCST() & 3) != 0 AND Comeback() != 0 AND 1 != 0 AND (DialogGetRes() == 0) != 0 AND (0 < 15) == 0 AND ForceGetCount(1) != 0 AND (ForceGetFirst(1) == 0) != 0 AND (0 >= 15) != 0 AND get('G_漆黒の騎士倒した') != 0 AND get('G_漆黒の騎士倒した') != 0 AND UnitCheckLiveByPID('PID_NASIR') != 0 AND (0 < 0) == 0.

### Scene 16: Opening2

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x3AD1 UnitEscapeByPID('PID_ERINCIA_QUEEN_EV')`: 2 explored alternative(s). Example local guards: UnitCheckExistsByPID('PID_ERINCIA_QUEEN') != 0 AND UnitCheckExistsByPID('PID_ERINCIA_QUEEN') != 0 AND UnitCheckExistsByPID('PID_ERINCIA_QUEEN') != 0 AND UnitCheckExistsByPID('PID_ERINCIA_QUEEN_EV') != 0.

### Scene 17: function_17

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [1, 1, 0], 'inferred_turn_trigger': {'first_turn': 1, 'last_turn': 1, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 18: function_18

Trigger metadata: `{'kind': 6, 'argc': 0, 'parameters': [2, 2, 0], 'inferred_turn_trigger': {'first_turn': 2, 'last_turn': 2, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 19: function_19

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [3, 3, 0], 'inferred_turn_trigger': {'first_turn': 3, 'last_turn': 3, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 20: function_20

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [10, 10, 0], 'inferred_turn_trigger': {'first_turn': 10, 'last_turn': 10, 'phase': 0}}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound


### Scene 21: function_21

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [9, 9, 1], 'inferred_turn_trigger': {'first_turn': 9, 'last_turn': 9, 'phase': 1}}`. Local trace: all explored local paths returned


### Scene 23: function_23

Trigger metadata: `{'kind': 3, 'argc': 0, 'parameters': [0, 0, 0], 'inferred_turn_trigger': {'first_turn': 0, 'last_turn': 0, 'phase': 0}}`. Local trace: all explored local paths returned


### Scene 51: function_51

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [418]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x5267 set('gf_complete')`: 1 explored alternative(s). Example local guards: Normal() != 0.

### Scene 57: function_57

Trigger metadata: `{'kind': 11, 'argc': 0, 'parameters': [3959]}`. Local trace: all explored local paths returned

- `0x5459 set('gf_complete')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 58: function_58

Trigger metadata: `{'kind': 1, 'argc': 0, 'parameters': [5222]}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x55B5 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0.
- `0x56CC UnitEscapeByPID('PID_OSCAR')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0.
- `0x56D9 UnitEscapeByPID('PID_BOLE')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0.
- `0x56E6 UnitEscapeByPID('PID_LOFA')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x56F3 UnitEscapeByPID('PID_VULCI')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x5700 UnitEscapeByPID('PID_JANAFF')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x570D UnitEscapeByPID('PID_HAAR')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x571A UnitEscapeByPID('PID_LUCHINO')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x5727 UnitEscapeByPID('PID_ULYSSES')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x5734 UnitEscapeByPID('PID_GEOFFRAY')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x5747 UnitEscapeByPID('PID_NASIR_EV')`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !(get('G_漆黒の騎士倒した')) != 0.
- `0x5B4F AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !(get('G_漆黒の騎士倒した')) != 0.
- `0x5B59 AllUnitEscape()`: 1 explored alternative(s). Example local guards: !((GetBattleType() & -2147483648)) != 0 AND Normal() != 0 AND !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND !(get('G_漆黒の騎士倒した')) != 0.

### Scene 62: function_62

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x63B1 UnitEscapeByPID('PID_TIAMAT_EV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63B9 UnitEscapeByPID('PID_SENERIO')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63C1 UnitEscapeByPID('PID_BOLE')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63C9 UnitEscapeByPID('PID_LOFA')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63D1 UnitEscapeByPID('PID_OSCAR')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63D9 UnitEscapeByPID('PID_KILROY')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63E1 UnitEscapeByPID('PID_WAYU')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63E9 UnitEscapeByPID('PID_CHINON')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63F1 UnitEscapeByPID('PID_GATRIE')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x63F9 UnitEscapeByPID('PID_VOKE')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 63: function_63

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x65C9 UnitEscapeByPID('PID_DUMMY1')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x65D1 UnitEscapeByPID('PID_GEOFFRAY')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x65D9 UnitEscapeByPID('PID_ULYSSES')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x65E1 UnitEscapeByPID('PID_LUCHINO')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x65E9 UnitEscapeByPID('PID_KEVIN')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x65F1 UnitEscapeByPID('PID_CHAP')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x65F9 UnitEscapeByPID('PID_NEPENEE')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6601 UnitEscapeByPID('PID_LARGO')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6609 UnitEscapeByPID('PID_CALILL')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 64: function_64

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x679B UnitEscapeByPID('PID_TANIS')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67A3 UnitEscapeByPID('PID_ZELGIUS')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67AB UnitEscapeByPID('PID_MARCIA')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67B3 UnitEscapeByPID('PID_STELLA')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67BB UnitEscapeByPID('PID_MAKAROV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67C3 UnitEscapeByPID('PID_MWARIM')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67CB UnitEscapeByPID('PID_TOPUCK')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67D3 UnitEscapeByPID('PID_SOANVALCKE')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x67DB UnitEscapeByPID('PID_DALAHOWE')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 65: function_65

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: all explored local paths returned

- `0x686B UnitEscapeByPID('PID_LAY_EV3')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6873 UnitEscapeByPID('PID_GIFFCA_EV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x687B UnitEscapeByPID('PID_LETHE')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6883 UnitEscapeByPID('PID_MORDY')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x688B UnitEscapeByPID('PID_RIEUSION_EV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6893 UnitEscapeByPID('PID_LEARNE')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 66: function_66

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x6909 UnitEscapeByPID('PID_TIBARN_EV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6911 UnitEscapeByPID('PID_NAESALA_EV')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6919 UnitEscapeByPID('PID_NEALUCHI')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6921 UnitEscapeByPID('PID_JANAFF')`: 1 explored alternative(s). Example local guards: none in this scene.
- `0x6929 UnitEscapeByPID('PID_VULCI')`: 1 explored alternative(s). Example local guards: none in this scene.

### Scene 67: GrandFinale

Trigger metadata: `{'kind': 0, 'argc': 0, 'parameters': []}`. Local trace: INCONCLUSIVE: unsupported operation or exploration bound

- `0x6DBF UnitEscapeByPID('PID_ZELGIUS')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0.
- `0x6DD3 UnitEscapeByPID('PID_OSCAR')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0.
- `0x6DE0 UnitEscapeByPID('PID_BOLE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0.
- `0x6DED UnitEscapeByPID('PID_KILROY')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6DFA UnitEscapeByPID('PID_GATRIE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E07 UnitEscapeByPID('PID_CHINON')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E14 UnitEscapeByPID('PID_WAYU')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E21 UnitEscapeByPID('PID_ELAICE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E2E UnitEscapeByPID('PID_LOFA')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E3B UnitEscapeByPID('PID_MARCIA')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E48 UnitEscapeByPID('PID_LETHE_EV')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E55 UnitEscapeByPID('PID_MORDY_EV')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E62 UnitEscapeByPID('PID_CHAP')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E6F UnitEscapeByPID('PID_NEPENEE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E7C UnitEscapeByPID('PID_KEVIN')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E89 UnitEscapeByPID('PID_VOKE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6E96 UnitEscapeByPID('PID_ZIHARK')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6EA3 UnitEscapeByPID('PID_SOTHE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6EB0 UnitEscapeByPID('PID_JILL')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6EBD UnitEscapeByPID('PID_STELLA')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6ECA UnitEscapeByPID('PID_MAKAROV')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6ED7 UnitEscapeByPID('PID_MWARIM')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6EE4 UnitEscapeByPID('PID_TOPUCK')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6EF1 UnitEscapeByPID('PID_SOANVALCKE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6EFE UnitEscapeByPID('PID_DALAHOWE')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F0B UnitEscapeByPID('PID_VULCI')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F18 UnitEscapeByPID('PID_JANAFF')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F25 UnitEscapeByPID('PID_TANIS')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F32 UnitEscapeByPID('PID_CALILL')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F3F UnitEscapeByPID('PID_TAURONEO')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F4C UnitEscapeByPID('PID_HAAR')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F59 UnitEscapeByPID('PID_LUCHINO')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F66 UnitEscapeByPID('PID_ULYSSES')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F73 UnitEscapeByPID('PID_GEOFFRAY')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
- `0x6F80 UnitEscapeByPID('PID_LARGO')`: 1 explored alternative(s). Example local guards: !(UnitCheckLiveByPID('PID_OSCAR')) != 0 AND !(UnitCheckLiveByPID('PID_BOLE')) != 0 AND !(UnitCheckLiveByPID('PID_KILROY')) != 0 AND !(UnitCheckLiveByPID('PID_GATRIE')) != 0 AND !(UnitCheckLiveByPID('PID_CHINON')) != 0 AND !(UnitCheckLiveByPID('PID_WAYU')) != 0 AND !(UnitCheckLiveByPID('PID_ELAICE')) != 0 AND !(UnitCheckLiveByPID('PID_LOFA')) != 0 AND !(UnitCheckLiveByPID('PID_MARCIA')) != 0 AND !(UnitCheckLiveByPID('PID_LETHE')) != 0 AND !(UnitCheckLiveByPID('PID_MORDY')) != 0 AND !(UnitCheckLiveByPID('PID_CHAP')) != 0 AND !(UnitCheckLiveByPID('PID_NEPENEE')) != 0 AND !(UnitCheckLiveByPID('PID_KEVIN')) != 0 AND !(UnitCheckLiveByPID('PID_VOKE')) != 0 AND !(UnitCheckLiveByPID('PID_ZIHARK')) != 0 AND !(UnitCheckLiveByPID('PID_SOTHE')) != 0 AND !(UnitCheckLiveByPID('PID_JILL')) != 0 AND !(UnitCheckLiveByPID('PID_STELLA')) != 0 AND !(UnitCheckLiveByPID('PID_MAKAROV')) != 0 AND !(UnitCheckLiveByPID('PID_MWARIM')) != 0 AND !(UnitCheckLiveByPID('PID_TOPUCK')) != 0 AND !(UnitCheckLiveByPID('PID_SOANVALCKE')) != 0 AND !(UnitCheckLiveByPID('PID_DALAHOWE')) != 0 AND !(UnitCheckLiveByPID('PID_VULCI')) != 0 AND !(UnitCheckLiveByPID('PID_JANAFF')) != 0 AND !(UnitCheckLiveByPID('PID_TANIS')) != 0 AND !(UnitCheckLiveByPID('PID_CALILL')) != 0 AND !(UnitCheckLiveByPID('PID_TAURONEO')) != 0 AND !(UnitCheckLiveByPID('PID_HAAR')) != 0 AND !(UnitCheckLiveByPID('PID_LUCHINO')) != 0 AND !(UnitCheckLiveByPID('PID_ULYSSES')) != 0 AND !(UnitCheckLiveByPID('PID_GEOFFRAY')) != 0 AND !(UnitCheckLiveByPID('PID_LARGO')) != 0 AND !(1) != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0 AND 1 != 0.
