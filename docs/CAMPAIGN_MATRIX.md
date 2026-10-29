# Campaign compatibility matrix

Baseline: 10d2496 (draft research); stable main 6a81522.

Generated from the user's GFEE01 rev 0 image. Static inventory and local instruction CFGs cover discovered containers; event interpretation is incomplete. Current evidence columns come from campaign/verification.json. PASS* covers only the named run/event there, never whole-chapter compatibility. Historical reports are retained separately and must not be promoted to current acceptance. Predicate/tile/conversation records are generated in CAMPAIGN_EVENTS.md.

| Chapter | ID | Maps | Static research | Automated | Original event | Cleared | Transition | Netplay two PCs |
|---|---|---|---|---|---|---|---|---|
| Prologue: Mercenaries | 1 | bmap01 | inventory; conditions open | see ledger | PASS* | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.1: The Battle Begins | 2 | bmap02 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.2: Rescue | 3 | bmap03 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.3: Pirates Aground | 4 | bmap04 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.4: Roadside Battle | 5 | bmap05 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.5: Flight! | 6 | bmap06, bmap06_2 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.6: A Brief Diversion | 7 | bmap07 | inventory; conditions open | see ledger | PASS* | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.7: Shades of Evil | 8 | bmap08, bmap08_2 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.8: Despair and Hope | 9 | bmap09, bmap09_2, bmap09_3, bmap09_4, bmap09_5 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.9: Gallia | 10 | bmap10 | inventory; conditions open | see ledger | PASS* | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.10: Prisoner Release | 11 | bmap11 | inventory; conditions open | see ledger | PASS* | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.11: Blood Runs Red | 12 | bmap12, bmap12_2 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.12: A Strange Land | 13 | bmap13 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.13: A Guiding Wind | 14 | bmap14, bmap14_2 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.14: Training | 15 | bmap15 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.15: The Feral Frontier | 16 | bmap16 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.16: The Atonement | 17 | bmap17 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.17: Day Breaks | 18 | bmap18, bmap18_3 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.18: Crimea Marches | 19 | bmap19 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.19: Entrusted | 20 | bmap20 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.20: Defending Talrega | 21 | bmap21 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.21: Without a King | 22 | bmap22 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.22: Solo | 23 | bmap23 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.23: The Great Bridge | 24 | bmap24 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.24: Battle Reunion | 25 | bmap25, bmap25_2 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.25: Strange Lands | 26 | bmap26, bmap26_2 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.26: Clash! | 27 | bmap27 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.27: Moment of Fate | 28 | bmap28 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.27-2: Moment of Fate | 29 | bmap29 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Ch.28: Twisted Tower | 30 | bmap30 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |
| Endgame: Repatriation | 31 | bmap31, bmap31_2, bmap31_3 | inventory; conditions open | see ledger | NOT TESTED | NOT TESTED | NOT TESTED | NOT TESTED |

## Multipart and special encounters

Internal 18 is Chapter 17, Day Breaks. Both bmap18 and bmap18_3 are inventoried. The four gameplay stages need separate acceptance: 17-1 untested; 17-2 untested; 17-3 untested; 17-4 untested. Do not assign stage transitions to SetChapter without tracing C18's local Complete18/BMSetTurn flow.

Internal 29 is Ch.27-2, Moment of Fate (separate special encounter), not Chapter 28. Internal 30 is Chapter 28; internal 31 is Endgame. Names come directly from Mess/common.m MCTxx.

## Prologue: Mercenaries — internal 1

Historical evidence: Prologue played with COOP-P3 (no yellow phase when force 3 is empty, F-37).

Slot-group counts by file suffix: `{'c': 1}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap01/dispos_c.bin:bmap01_ending_c`: F2: PID_GREIL_MAP1
- `bmap01/dispos_c.bin:bmap01_event_bole_c`: F2: PID_BOLE_MAP1
- `bmap01/dispos_c.bin:bmap01_first_c`: F2: PID_MIST
- `bmap01/dispos_c.bin:bmap01_mikata_c`: F0: PID_IKE
- `bmap01/dispos_h.bin:bmap01_first_g_h`: F2: PID_GREIL_MAP1
- `bmap01/dispos_h.bin:bmap01_first_h`: F1: PID_BOLE_MAP1
- `bmap01/dispos_m.bin:bmap01_first_g_m`: F2: PID_GREIL_MAP1
- `bmap01/dispos_m.bin:bmap01_first_m`: F1: PID_BOLE_MAP1
- `bmap01/dispos_n.bin:bmap01_first_g_n`: F2: PID_GREIL_MAP1
- `bmap01/dispos_n.bin:bmap01_first_n`: F1: PID_BOLE_MAP1

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| AFE | 1 | regist | 木刀捨てイベント起きたターン |
| B05 | 1 | regist | そっちじゃない１ |
| B0C | 1 | regist | そっちじゃない２ |
| B13 | 1 | regist | 早くかかってこいよ１ |
| B1A | 1 | regist | 早くかかってこいよ２ |
| B21 | 1 | regist | へへ、まだまだ |
| B28 | 1 | regist | ボーレ戦闘 |
| B30 | 1 | regist | ボーレ死亡 |
| B38 | 1 | regist | グレイル参戦 |
| B40 | 1 | regist | グレイル行動開始 |
| B48 | 1 | regist | グレイル頑張るではないか |
| B50 | 1 | regist | 傷薬使って |
| B58 | 1 | regist | 傷薬使え |
| B60 | 1 | regist | ボス戦闘会話 |
| B68 | 1 | regist | スキルデモ |
| B70 | 1 | regist | 持ち物デモ |
| B78 | 1 | regist | ボーレ死亡オンバト |
| B80 | 1 | regist | グレイル死亡オンバト |
| C38 | 3 | ChapterMoviePlay | 1 |
| C8C | 4 | MapLoad | bmap01 |
| CC3 | 4 | SallySetByGroup | bmap01_mikata_c |
| CCB | 4 | InstantDisposFirst | bmap01_mikata_c |
| CD3 | 4 | InstantDisposFirst | bmap01_first_c |
| CE1 | 4 | InstantDisposFirstSetMode | bmap01_first_g_n, bmap01_first_g_h, bmap01_first_g_m |
| CEF | 4 | InstantDisposFirstSetMode | bmap01_first_n, bmap01_first_h, bmap01_first_m |
| DAD | 4 | TalkEvent | MS_01_OP_01 |
| DEF | 4 | TalkEvent | MS_01_OP_02 |
| DFE | 4 | TalkResume |  |
| E8A | 4 | TalkEvent | MS_01_OP_03_01 |
| ECB | 4 | TalkEvent | MS_01_OP_03_02 |
| F81 | 4 | DisposContinueSetMode | bmap01_first_n, bmap01_first_h, bmap01_first_m |
| FCE | 4 | TalkEvent | MS_01_OP_04 |
| 10D3 | 6 | BMGetTurn |  |
| 1132 | 6 | TalkEvent | MS_01_EV_02 |
| 1174 | 6 | TalkEvent | MS_01_EV_07_02 |
| 11EE | 6 | TalkEvent | MS_01_EV_07_01_01 |
| 122C | 6 | TalkEvent | MS_01_EV_07_01_02 |
| 123E | 6 | TalkEvent | MS_01_EV_07_01_03 |
| 1249 | 6 | TalkEvent | MS_01_EV_07_02 |
| 12F5 | 7 | TalkEvent | MS_01_EV_08_01 |
| 132F | 7 | TalkEvent | MS_01_EV_08_02 |
| 1452 | 8 | TalkEvent | MS_01_EV_01_01 |
| 146E | 8 | TalkEvent | MS_01_EV_01_02 |
| 1480 | 8 | TalkEvent | MS_01_EV_01_03 |
| 15C9 | 10 | TalkEvent | MS_01_EV_07_03 |
| 161B | 11 | TalkEvent | MS_01_EV_05 |
| 16D7 | 12 | UnitTransferToForceByPID | PID_BOLE_MAP1, 2 |
| 1717 | 12 | TalkEvent | MDIE_BOLE_MAP1 |
| 1770 | 12 | TalkEvent | MS_01_EV_03_01 |
| 17D9 | 12 | TalkEvent | MS_01_EV_03_02 |
| 1813 | 12 | TalkEvent | MS_01_EV_03_03 |
| 1850 | 12 | UnitTransferToForceByPID | PID_GREIL_MAP1, 1 |
| 1932 | 13 | TalkEvent | MS_01_EV_03_04 |
| 195F | 13 | TalkEvent | MS_01_EV_04 |
| 19E9 | 14 | TalkEvent | MDIE_IKE_MAP1 |
| 1A24 | 15 | TalkEvent | MS_01_BT_BOlE |
| 1AB8 | 17 | TalkEvent | MS_01_BT |
| 1AF0 | 18 | TalkEvent | MDIE_GREIL_MAP1 |
| 1C13 | 19 | TalkEvent | MS_01_ED_01 |
| 1C3F | 19 | TalkEvent | MS_01_ED_02 |
| 1C70 | 19 | AllUnitEscape |  |
| 1DBD | 21 | TalkEvent | MS_01_OP_04 |
| 1E42 | 22 | TalkEvent | MS_01_EV_07_01_01 |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.1: The Battle Begins — internal 2

Historical evidence: Ch1 cleared with two armies (EXP-15 v3).

Slot-group counts by file suffix: `{'h': 4, 'n': 4, 'c': 4, 'm': 4}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap02/dispos_h.bin:bmap02_first_h`: F1: PID_BANDIT_MOU, PID_BANDIT_MOU_EV1, PID_ZAWANAR
- `bmap02/dispos_h.bin:bmap02_mikata_h`: F0: PID_BOLE, PID_IKE, PID_OSCAR, PID_TIAMAT
- `bmap02/dispos_h.bin:bmap02_z01_h`: F1: PID_BANDIT_MOU
- `bmap02/dispos_n.bin:bmap02_first_n`: F1: PID_BANDIT_MOU, PID_BANDIT_MOU_EV1, PID_ZAWANAR
- `bmap02/dispos_n.bin:bmap02_mikata_n`: F0: PID_BOLE, PID_IKE, PID_OSCAR, PID_TIAMAT
- `bmap02/dispos_c.bin:bmap02_mikata_c`: F0: PID_BOLE, PID_IKE, PID_OSCAR, PID_TIAMAT
- `bmap02/dispos_m.bin:bmap02_first_m`: F1: PID_BANDIT_MOU, PID_BANDIT_MOU_EV1, PID_ZAWANAR
- `bmap02/dispos_m.bin:bmap02_mikata_m`: F0: PID_BOLE, PID_IKE, PID_OSCAR, PID_TIAMAT

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| C21 | 1 | TalkEvent | MS_02_VIL_02 |
| CCE | 3 | TalkEvent | MS_02_VIL_03 |
| D76 | 5 | regist | 訪問１ |
| D7E | 5 | regist | 訪問２ |
| E1F | 8 | regist | アイクボーレ |
| E27 | 8 | regist | アイクオスカー |
| E2F | 8 | regist | アイクティアマト |
| E37 | 8 | regist | 敵ＣＰ変更 |
| E3F | 8 | regist | ボス戦闘会話 |
| E47 | 8 | regist | ボス戦闘会話アイク |
| E4F | 8 | regist | ボス死亡 |
| E57 | 8 | regist | 制圧デモ |
| E5F | 8 | regist | 騎乗デモ |
| E67 | 8 | regist | 救出デモ |
| E6F | 8 | regist | 持ち物デモ |
| EAF | 9 | ChapterMoviePlay | 2 |
| F04 | 10 | MapLoad | bmap06_2 |
| F24 | 10 | InstantDispos | bmap06_2_event00_c |
| F2C | 10 | UnitEscapeByPID | PID_GREIL_EV |
| F34 | 10 | UnitEscapeByPID | PID_KILROY |
| F3C | 10 | UnitEscapeByPID | PID_SENERIO |
| 110E | 10 | TalkEvent | MS_02_OP_01 |
| 1127 | 10 | TalkResume |  |
| 11C6 | 10 | TalkEvent | MS_02_OP_01_02 |
| 1263 | 10 | AllUnitEscape |  |
| 126D | 10 | AllUnitEscape |  |
| 12B0 | 11 | MapLoad | bmap02 |
| 1315 | 11 | SallySetByGroup | bmap02_mikata_c |
| 131D | 11 | InstantDispos | bmap02_mikata_c |
| 1322 | 11 | AllUnitEscape |  |
| 132A | 11 | InstantDisposRank | bmap02_first |
| 13AC | 11 | InstantDisposFirst | bmap02_mikata_c |
| 1466 | 11 | TalkEvent | MS_02_OP_02_01 |
| 14BF | 11 | TalkEvent | MS_02_OP_02_01_2 |
| 14D4 | 11 | TalkResume |  |
| 14D9 | 11 | TalkResume |  |
| 14EE | 11 | TalkResume |  |
| 14F3 | 11 | TalkResume |  |
| 1573 | 11 | TalkEvent | MS_02_OP_02_04 |
| 159C | 11 | TalkEvent | MS_02_OP_02_00 |
| 160A | 11 | TalkEvent | MS_02_OP_03_01 |
| 1631 | 11 | TalkEvent | MS_02_OP_03_02 |
| 16F7 | 12 | ForceGetCount | 5 |
| 171E | 12 | MapLoad | bmap02 |
| 172C | 12 | InstantDisposSetMode | bmap02_mikata_n, bmap02_mikata_h, bmap02_mikata_m |
| 1731 | 12 | AllUnitEscape |  |
| 17DE | 13 | TalkEvent | MS_02_EV_00 |
| 1845 | 13 | TalkEvent | MS_02_EV_000 |
| 1950 | 14 | TalkEvent | MS_02_EV_01 |
| 19A5 | 15 | TalkEvent | MS_02_EV_01_02 |
| 1A81 | 16 | TalkEvent | MS_02_EV_03 |
| 1ABC | 17 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1AC4 | 17 | TalkEvent | MS_02_BT_IKE |
| 1AD1 | 17 | SoundBossTalkEnd |  |
| 1B06 | 18 | BMGetPhase |  |
| 1B36 | 18 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1B3E | 18 | TalkEvent | MS_02_BT |
| 1B4B | 18 | SoundBossTalkEnd |  |
| 1B7C | 19 | TalkEvent | MS_02_DIE |
| 1BD7 | 20 | AllUnitEscape |  |
| 1C21 | 20 | TalkEvent | MS_02_ED_01_01 |
| 1C47 | 20 | TalkEvent | MS_02_ED_01_03 |
| 1C4F | 20 | TalkEvent | MS_02_ED_01_04_A |
| 1C7B | 20 | TalkEvent | MS_02_ED_01_02_DIE |
| 1C83 | 20 | TalkEvent | MS_02_ED_01_03_DIE |
| 1CAD | 20 | TalkEvent | MS_02_ED_01_02_DIE |
| 1CB5 | 20 | TalkEvent | MS_02_ED_01_04_B |
| 1CC0 | 20 | TalkEvent | MS_02_ED_01_02_DIE |
| 1CC8 | 20 | TalkEvent | MS_02_ED_01_03_DIE_B |
| 1CE9 | 20 | TalkEvent | MS_02_ED_01_01_OB_OIE |
| 1CFF | 20 | TalkEvent | MS_02_ED_01_03_2 |
| 1D07 | 20 | TalkEvent | MS_02_ED_01_04_C |
| 1D12 | 20 | TalkEvent | MS_02_ED_01_03_3 |
| 1D1A | 20 | TalkEvent | MS_02_ED_01_04_D |
| 1D5A | 21 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.2: Rescue — internal 3

Historical evidence: Ch2 cleared, yellow Oscar/Boyd automatic (EXP-16).

Slot-group counts by file suffix: `{'c': 4, 'h': 4, 'm': 4, 'n': 4}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap03/dispos_c.bin:bmap03_event00_c`: F1: PID_ZAKO_EV1; F2: PID_LOFA_EV, PID_MIST
- `bmap03/dispos_c.bin:bmap03_event01_c`: F2: PID_CHINON, PID_GATRIE
- `bmap03/dispos_c.bin:bmap03_event02_c`: F2: PID_TIAMAT_EV
- `bmap03/dispos_c.bin:bmap03_m01_c`: F0: PID_TIAMAT
- `bmap03/dispos_c.bin:bmap03_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR
- `bmap03/dispos_h.bin:bmap03_first_boss_h`: F1: PID_IKANAU
- `bmap03/dispos_h.bin:bmap03_first_h`: F1: PID_BANDIT_MOU, PID_BANDIT_MOU_EV1
- `bmap03/dispos_h.bin:bmap03_mikata_h`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR
- `bmap03/dispos_m.bin:bmap03_first_boss_m`: F1: PID_IKANAU
- `bmap03/dispos_m.bin:bmap03_first_m`: F1: PID_BANDIT_MOU, PID_BANDIT_MOU_EV1
- `bmap03/dispos_m.bin:bmap03_mikata_m`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR
- `bmap03/dispos_n.bin:bmap03_first_boss_n`: F1: PID_IKANAU
- `bmap03/dispos_n.bin:bmap03_first_n`: F1: PID_BANDIT_MOU, PID_BANDIT_MOU_EV1
- `bmap03/dispos_n.bin:bmap03_mikata_n`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| E2A | 1 | regist | 地形効果デモ起動 |
| EBA | 4 | regist | アイクティアマト |
| EC1 | 4 | regist | シノンガトリー配置 |
| EC8 | 4 | regist | ボス戦闘会話アイク |
| ECF | 4 | regist | ボス戦闘会話ティアマト |
| ED6 | 4 | regist | ボス戦闘会話 |
| EDD | 4 | regist | 地形効果デモ |
| F1F | 5 | ChapterMoviePlay | 3 |
| FA0 | 6 | MapLoad | bmap06_2 |
| FC0 | 6 | InstantDispos | bmap06_2_event00_c |
| FE1 | 6 | UnitEscapeByPID | PID_OSCAR |
| FEE | 6 | UnitEscapeByPID | PID_BOLE |
| FF6 | 6 | UnitEscapeByPID | PID_GREIL_EV |
| FFE | 6 | UnitEscapeByPID | PID_MIST_EV |
| 1006 | 6 | UnitEscapeByPID | PID_LOFA_EV |
| 100E | 6 | UnitEscapeByPID | PID_CHINON_EV |
| 1016 | 6 | UnitEscapeByPID | PID_GATRIE |
| 101E | 6 | UnitEscapeByPID | PID_SENERIO |
| 1171 | 6 | TalkEvent | MS_03_OP_01 |
| 11FE | 6 | TalkEvent | MS_03_OP_02_A |
| 1209 | 6 | TalkEvent | MS_03_OP_02_B |
| 1315 | 6 | TalkEvent | MS_03_OP_03_A |
| 1336 | 6 | TalkEvent | MS_03_OP_03_B |
| 1356 | 6 | TalkEvent | MS_03_OP_03_C |
| 1361 | 6 | TalkEvent | MS_03_OP_03_D |
| 13D1 | 6 | AllUnitEscape |  |
| 13DB | 6 | AllUnitEscape |  |
| 1438 | 7 | TalkEvent | MS_03_OP_04 |
| 1490 | 8 | MapLoad | bmap03 |
| 14A4 | 8 | InstantDisposRank | bmap03_first |
| 14A9 | 8 | AllUnitEscape |  |
| 14B7 | 8 | InstantDisposFirstSetMode | bmap03_first_boss_n, bmap03_first_boss_h, bmap03_first_boss_m |
| 14CD | 8 | SallySetByGroup | bmap03_mikata_c |
| 14D5 | 8 | InstantDisposFirst | bmap03_mikata_c |
| 16CB | 8 | TalkEvent | MS_03_OP_05 |
| 16D6 | 8 | TalkEvent | MS_03_OP_05_B |
| 1753 | 8 | DisposSetMode | bmap03_first_n, bmap03_first_h, bmap03_first_m |
| 1779 | 8 | TalkEvent | MS_03_OP_05_2_A |
| 179A | 8 | TalkEvent | MS_03_OP_05_2_B |
| 17BA | 8 | TalkEvent | MS_03_OP_05_2_C |
| 17DA | 8 | TalkEvent | MS_03_OP_05_2_D |
| 18C3 | 9 | ForceGetCount | 5 |
| 18EA | 9 | MapLoad | bmap03 |
| 18F8 | 9 | InstantDisposSetMode | bmap03_mikata_n, bmap03_mikata_h, bmap03_mikata_m |
| 1900 | 9 | InstantDispos | bmap03_m01_c |
| 1905 | 9 | AllUnitEscape |  |
| 1949 | 9 | UnitTransferToForceByPID | PID_TIAMAT, 7 |
| 1A4D | 10 | TalkEvent | MS_03_EV_01_A |
| 1A6E | 10 | TalkEvent | MS_03_EV_01_C |
| 1A79 | 10 | TalkEvent | MS_03_EV_01_B |
| 1ACF | 11 | UnitTransferToForceByPID | PID_TIAMAT, 5 |
| 1B1B | 11 | InstantDispos | bmap03_m01_c |
| 1B5F | 11 | TalkEvent | MS_03_EV_02 |
| 1B75 | 11 | DisposContinue | bmap03_m01_c |
| 1BD8 | 12 | ForceGetCount | 1 |
| 1BEA | 12 | InstantDispos | bmap03_event01_c |
| 1C22 | 13 | TalkEvent | MS_03_TK_01 |
| 1C60 | 14 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1C68 | 14 | TalkEvent | MS_03_BT_IKE |
| 1C74 | 14 | SoundBossTalkEnd |  |
| 1CA8 | 15 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1CB0 | 15 | TalkEvent | MS_03_BT_TIAMAT |
| 1CBC | 15 | SoundBossTalkEnd |  |
| 1CFC | 16 | BMGetPhase |  |
| 1D34 | 16 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1D3C | 16 | TalkEvent | MS_03_BT |
| 1D48 | 16 | SoundBossTalkEnd |  |
| 1D78 | 17 | TalkEvent | MS_03_DIE |
| 1D9E | 18 | ForceGetCount | 1 |
| 1E2E | 19 | InstantDispos | bmap03_event00_c |
| 1E41 | 19 | InstantDispos | bmap03_event02_c |
| 1E53 | 19 | InstantDispos | bmap03_event01_c |
| 1F19 | 19 | UnitCheckDeadHereByPID | PID_TIAMAT |
| 1F20 | 19 | ForceGetCount | 6 |
| 1F2D | 19 | TalkEvent | MS_03_ED_01 |
| 1F3C | 19 | TalkResume |  |
| 1F4E | 19 | TalkResume |  |
| 1F68 | 19 | TalkEvent | MS_03_ED_00_td |
| 1F73 | 19 | TalkEvent | MS_03_ED_00 |
| 1F83 | 19 | TalkEvent | MS_03_ED_00_tdbd |
| 1F8E | 19 | TalkEvent | MS_03_ED_00_bd |
| 1F9D | 19 | TalkResume |  |
| 1FAF | 19 | TalkResume |  |
| 1FCC | 19 | TalkEvent | MS_03_ED_01_A |
| 1FE1 | 19 | TalkEvent | MS_03_ED_01_B |
| 1FEC | 19 | TalkEvent | MS_03_ED_01_C |
| 20D5 | 19 | TalkEvent | MS_03_ED_02_A |
| 20F6 | 19 | TalkEvent | MS_03_ED_02_B |
| 2116 | 19 | TalkEvent | MS_03_ED_02_C |
| 2121 | 19 | TalkEvent | MS_03_ED_02_D |
| 2172 | 19 | TalkResume |  |
| 219F | 19 | TalkResume |  |
| 21D6 | 19 | TalkResume |  |
| 2203 | 19 | TalkResume |  |
| 223A | 19 | TalkResume |  |
| 2322 | 19 | TalkEvent | MS_03_ED_03 |
| 2338 | 19 | UnitDead | ? |
| 2346 | 19 | UnitEscape | ?, 0 |
| 2382 | 19 | TalkEvent | MS_03_ED_04 |
| 240F | 19 | TalkEvent | MS_03_ED_04_A |
| 2430 | 19 | TalkEvent | MS_03_ED_04_B |
| 2450 | 19 | TalkEvent | MS_03_ED_04_C |
| 245B | 19 | TalkEvent | MS_03_ED_04_D |
| 246A | 19 | TalkResume |  |
| 2552 | 19 | AllUnitEscape |  |
| 255E | 19 | ForceGetCount | 6 |
| 256B | 19 | TalkEvent | MS_03_ED_05_A |
| 2594 | 19 | TalkEvent | MS_03_ED_05_B |
| 259F | 19 | TalkEvent | MS_03_ED_05_C |
| 25BE | 19 | TalkEvent | MS_03_ED_05_D |
| 25C9 | 19 | TalkEvent | MS_03_ED_05_E |
| 25EA | 19 | UnitCheckDeadHereByPID | PID_KILROY |
| 25F4 | 19 | UnitCheckDeadHereByPID | PID_OSCAR |
| 25FE | 19 | UnitCheckDeadHereByPID | PID_BOLE |
| 263E | 19 | TalkEvent | MS_03_ED_06_D |
| 264E | 19 | TalkEvent | MS_03_ED_06_F |
| 265E | 19 | TalkEvent | MS_03_ED_06_G |
| 2669 | 19 | TalkEvent | MS_03_ED_06_A |
| 267E | 19 | TalkEvent | MS_03_ED_06_E |
| 268E | 19 | TalkEvent | MS_03_ED_06_B |
| 269E | 19 | TalkEvent | MS_03_ED_06_C |
| 26DE | 20 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.3: Pirates Aground — internal 4

Historical evidence: Ch3 cleared, yellow Shinon/Gatrie (EXP-16 run 2).

Slot-group counts by file suffix: `{'c': 4, 'h': 7, 'm': 7, 'n': 7}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap04/dispos_c.bin:bmap04_event1_c`: F2: PID_OLDMAN_1
- `bmap04/dispos_c.bin:bmap04_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap04/dispos_c.bin:bmap04_m01_c`: F2: PID_MARCIA
- `bmap04/dispos_c.bin:bmap04_mikata_c`: F0: PID_CHINON, PID_GATRIE, PID_IKE, PID_TIAMAT
- `bmap04/dispos_h.bin:bmap04_first_h`: F1: PID_BANDIT_SEA, PID_BANDIT_SEA_EV1, PID_HIBUCCHI
- `bmap04/dispos_h.bin:bmap04_mikata_h`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_TIAMAT
- `bmap04/dispos_h.bin:bmap04_zoen1_h`: F1: PID_BANDIT_SEA
- `bmap04/dispos_h.bin:bmap04_zoen2_h`: F1: PID_BANDIT_SEA
- `bmap04/dispos_m.bin:bmap04_first_m`: F1: PID_BANDIT_SEA, PID_BANDIT_SEA_EV1, PID_HIBUCCHI
- `bmap04/dispos_m.bin:bmap04_mikata_m`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_TIAMAT
- `bmap04/dispos_n.bin:bmap04_first_n`: F1: PID_BANDIT_SEA, PID_BANDIT_SEA_EV1, PID_HIBUCCHI
- `bmap04/dispos_n.bin:bmap04_mikata_n`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_TIAMAT

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| C24 | 0 | TalkEvent | MS_04_VIL_03_A |
| C2E | 0 | TalkEvent | MS_04_VIL_03_B |
| D19 | 3 | UnitEscape | ?, 0 |
| D69 | 4 | UnitEscape | ?, 0 |
| D9E | 5 | regist | 訪問１ |
| DA6 | 5 | regist | マーシャのイベントトリガ |
| E37 | 8 | regist | マーシャのイベント |
| E3F | 8 | regist | マーシャ会話アイク |
| E47 | 8 | regist | マーシャ会話ティアマト |
| E4F | 8 | regist | マーシャ会話シノン |
| E57 | 8 | regist | マーシャ会話ガトリー |
| E5F | 8 | regist | ボス戦闘会話アイク |
| E67 | 8 | regist | ボス戦闘会話 |
| EA6 | 9 | InstantDisposRank | bmap04_first |
| EE7 | 10 | SallySetByGroup | bmap04_mikata_c |
| F23 | 11 | ChapterMoviePlay | 4 |
| F81 | 12 | MapLoad | bmap06_2 |
| 104F | 12 | TalkEvent | MS_04_OP_01_01_A |
| 105A | 12 | TalkEvent | MS_04_OP_01_01_B |
| 1067 | 12 | TalkEvent | MS_04_OP_01_02_A |
| 1074 | 12 | TalkEvent | MS_04_OP_01_03_A |
| 1081 | 12 | TalkEvent | MS_04_OP_01_04_A |
| 1091 | 12 | TalkEvent | MS_04_OP_01_05_S |
| 109E | 12 | TalkEvent | MS_04_OP_01_05_A |
| 10A9 | 12 | TalkEvent | MS_04_OP_01_05_B |
| 10C0 | 12 | TalkEvent | MS_04_OP_01_06_A2 |
| 10DB | 12 | TalkEvent | MS_04_OP_01_06_B |
| 10F6 | 12 | TalkEvent | MS_04_OP_01_06_C |
| 1111 | 12 | TalkEvent | MS_04_OP_01_06_D |
| 112D | 12 | TalkEvent | MS_04_OP_01_06_E |
| 1149 | 12 | TalkEvent | MS_04_OP_01_06_F |
| 1165 | 12 | TalkEvent | MS_04_OP_01_06_G |
| 1182 | 12 | TalkEvent | MS_04_OP_01_06_H |
| 11D4 | 13 | MapLoad | bmap04 |
| 11F1 | 13 | SallySetByGroup | bmap04_mikata_c |
| 11F9 | 13 | InstantDisposFirst | bmap04_mikata_c |
| 120C | 13 | InstantDispos | bmap04_event_tiamat_c |
| 1211 | 13 | AllUnitEscape |  |
| 1228 | 13 | InstantDispos | bmap04_event1_c |
| 12DB | 13 | TalkEvent | MS_04_OP_02_00 |
| 13BD | 13 | InstantDispos | bmap04_mikata_c |
| 13D0 | 13 | InstantDispos | bmap04_event_tiamat_c |
| 14F0 | 13 | TalkEvent | MS_04_OP_02_A |
| 14FB | 13 | TalkEvent | MS_04_OP_02_B |
| 1511 | 13 | TalkResume |  |
| 1552 | 13 | UnitEscapeByPID | PID_OLDMAN_1 |
| 157F | 13 | UnitEscapeByPID | PID_TIAMAT_EV |
| 163F | 13 | TalkEvent | MS_04_OP_02_01 |
| 1661 | 13 | TalkEvent | MS_04_OP_02_02 |
| 16E7 | 14 | ForceGetCount | 5 |
| 1713 | 14 | MapLoad | bmap04 |
| 1721 | 14 | InstantDisposSetMode | bmap04_mikata_n, bmap04_mikata_h, bmap04_mikata_m |
| 1726 | 14 | AllUnitEscape |  |
| 1752 | 14 | UnitTransferToForceByPID | PID_OSCAR, 7 |
| 175C | 14 | UnitTransferToForceByPID | PID_BOLE, 7 |
| 1766 | 14 | UnitTransferToForceByPID | PID_KILROY, 7 |
| 1779 | 14 | UnitTransferToForceByPID | PID_OSCAR, 5 |
| 1783 | 14 | UnitTransferToForceByPID | PID_BOLE, 5 |
| 178D | 14 | UnitTransferToForceByPID | PID_KILROY, 5 |
| 17C7 | 14 | UnitForcedSallyByPID | PID_IKE |
| 17CF | 14 | UnitForcedSallyByPID | PID_TIAMAT |
| 17D7 | 14 | UnitForcedSallyByPID | PID_CHINON |
| 17DF | 14 | UnitForcedSallyByPID | PID_GATRIE |
| 17E6 | 14 | UnitDontMoveSallyByPID | PID_IKE |
| 1863 | 14 | SallySetByGroup | bmap04_mikata_c |
| 18A4 | 15 | InstantDispos | bmap04_m01_c |
| 18BA | 15 | UnitEscapeByPID | PID_MARCIA |
| 18F7 | 15 | UnitTransferToForceByPID | PID_OSCAR, 7 |
| 1901 | 15 | UnitTransferToForceByPID | PID_BOLE, 7 |
| 190B | 15 | UnitTransferToForceByPID | PID_KILROY, 7 |
| 19F1 | 16 | InstantDispos | bmap04_m01_c |
| 1A5F | 16 | TalkEvent | MS_04_EV_01 |
| 1B62 | 17 | TalkEvent | MS_04_TK_01 |
| 1BBA | 17 | UnitEscapeByPID | PID_MARCIA |
| 1BF2 | 18 | LocalDieTalkWithBgmChange | , MS_04_DIE_MARCIA |
| 1C28 | 19 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1C30 | 19 | TalkEvent | MS_04_BT_IKE |
| 1C3D | 19 | SoundBossTalkEnd |  |
| 1C71 | 20 | BMGetPhase |  |
| 1CA1 | 20 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1CA9 | 20 | TalkEvent | MS_04_BT |
| 1CB6 | 20 | SoundBossTalkEnd |  |
| 1CE4 | 21 | TalkEvent | MS_04_DIE |
| 1D5D | 22 | AllUnitEscape |  |
| 1D7C | 22 | UnitCheckDeadHereByPID | PID_TIAMAT |
| 1D86 | 22 | TalkEvent | MS_04_ED_00_DIE |
| 1DB9 | 22 | TalkEvent | MS_04_ED_02_A |
| 1DD4 | 22 | TalkEvent | MS_04_ED_02_B |
| 1E00 | 22 | TalkEvent | MS_04_ED_02_B_02 |
| 1E1B | 22 | TalkEvent | MS_04_ED_02_C |
| 1E47 | 22 | TalkEvent | MS_04_ED_02_C_02 |
| 1E57 | 22 | TalkEvent | MS_04_ED_02_D |
| 1E83 | 22 | TalkEvent | MS_04_ED_02_D_02 |
| 1ED2 | 23 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.4: Roadside Battle — internal 5

Historical evidence: Ch4 cleared, yellow Shinon/Gatrie (EXP-16 run 2).

Slot-group counts by file suffix: `{'c': 6, 'h': 8, 'm': 8, 'n': 8}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap05/dispos_c.bin:bmap05_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap05/dispos_c.bin:bmap05_mikata_c`: F0: PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_SENERIO, PID_TIAMAT
- `bmap05/dispos_h.bin:bmap05_first_boss2_h`: F1: PID_DAYNE_ARC_1, PID_DAYNE_SOL_1, PID_DAYNE_SOL_2, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4, PID_DAYNE_SOL_5
- `bmap05/dispos_h.bin:bmap05_first_boss_h`: F1: PID_MAIZIN
- `bmap05/dispos_h.bin:bmap05_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL, PID_ZAKO
- `bmap05/dispos_h.bin:bmap05_mikata_h`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap05/dispos_m.bin:bmap05_first_boss2_m`: F1: PID_DAYNE_ARC_1, PID_DAYNE_SOL_1, PID_DAYNE_SOL_2, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4, PID_DAYNE_SOL_5
- `bmap05/dispos_m.bin:bmap05_first_boss_m`: F1: PID_MAIZIN
- `bmap05/dispos_m.bin:bmap05_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL, PID_ZAKO
- `bmap05/dispos_m.bin:bmap05_mikata_m`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap05/dispos_n.bin:bmap05_first_boss2_n`: F1: PID_DAYNE_ARC_1, PID_DAYNE_SOL_1, PID_DAYNE_SOL_2, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4, PID_DAYNE_SOL_5
- `bmap05/dispos_n.bin:bmap05_first_boss_n`: F1: PID_MAIZIN
- `bmap05/dispos_n.bin:bmap05_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL, PID_ZAKO
- `bmap05/dispos_n.bin:bmap05_mikata_n`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 13D6 | 5 | regist | F04040910 |
| 13DD | 5 | regist | F10041009 |
| 13E4 | 5 | regist | F07110811 |
| 13EB | 5 | regist | F11061106 |
| 13F3 | 5 | regist | F11051206 |
| 147B | 8 | regist | ボス戦闘会話アイク |
| 1483 | 8 | regist | ボス戦闘会話ティアマト |
| 148B | 8 | regist | ボス戦闘会話セネリオ |
| 1493 | 8 | regist | ボス戦闘会話 |
| 14D2 | 9 | InstantDisposRank | bmap05_first_boss |
| 14DA | 9 | InstantDisposRank | bmap05_first_boss2 |
| 14E2 | 9 | InstantDisposRank | bmap05_first |
| 1523 | 10 | SallySetByGroup | bmap05_mikata_c |
| 155F | 11 | ChapterMoviePlay | 5 |
| 1646 | 12 | TalkEvent | MS_05_GMAP_02 |
| 1662 | 12 | TalkResume |  |
| 1686 | 12 | TalkResume |  |
| 1696 | 12 | TalkEvent | MS_05_GMAP_04_01 |
| 16A5 | 12 | TalkResume |  |
| 16FC | 12 | TalkEvent | MS_05_GMAP_04_02 |
| 1751 | 12 | TalkEvent | MS_05_GMAP_04_03 |
| 17DD | 12 | TalkEvent | MS_05_GMAP_04_04 |
| 187B | 12 | TalkEvent | MS_05_GMAP_04_05 |
| 18A1 | 12 | TalkResume |  |
| 1982 | 13 | MapLoad | bmap06_2 |
| 19A9 | 13 | InstantDispos | bmap06_2_event00_c |
| 19CB | 13 | UnitEscapeByPID | PID_OSCAR |
| 19D8 | 13 | UnitEscapeByPID | PID_BOLE |
| 19E5 | 13 | UnitEscapeByPID | PID_KILROY |
| 19F2 | 13 | UnitEscapeByPID | PID_CHINON_EV |
| 19FF | 13 | UnitEscapeByPID | PID_GATRIE |
| 1C78 | 13 | AllUnitEscape |  |
| 1C82 | 13 | AllUnitEscape |  |
| 1C9C | 13 | TalkEvent | MS_05_OP_01 |
| 1CB1 | 13 | TalkEvent | MS_05_OP_02 |
| 1CE5 | 13 | TalkEvent | MS_05_OP_03_00 |
| 1D0C | 13 | TalkEvent | MS_05_GMAP_05 |
| 1D4B | 13 | TalkEvent | MS_05_OP_03_02_A |
| 1D76 | 13 | TalkEvent | MS_05_OP_03_02_B |
| 1DA1 | 13 | TalkEvent | MS_05_OP_03_02_C |
| 1DCC | 13 | TalkEvent | MS_05_OP_03_02_D |
| 1DF6 | 13 | TalkEvent | MS_05_OP_03_02_E |
| 1E20 | 13 | TalkEvent | MS_05_OP_03_02_F |
| 1E4C | 13 | TalkEvent | MS_05_OP_03_02_G |
| 1E57 | 13 | TalkEvent | MS_05_OP_03_02_H |
| 1E86 | 13 | TalkEvent | MS_05_OP_03_03 |
| 1EBA | 13 | TalkEvent | MS_05_OP_03_03_DEL |
| 1EE6 | 13 | TalkEvent | MS_05_OP_03_03_DISP |
| 1EEE | 13 | TalkEvent | MS_05_OP_03_04 |
| 1F7C | 14 | MapLoad | bmap05 |
| 1F9E | 14 | InstantDisposRank | bmap05_first_boss |
| 1FA6 | 14 | InstantDisposRank | bmap05_first_boss2 |
| 1FAE | 14 | InstantDisposRank | bmap05_first |
| 2046 | 14 | AllUnitEscape |  |
| 204E | 14 | SallySetByGroup | bmap05_mikata_c |
| 2056 | 14 | InstantDisposFirst | bmap05_mikata_c |
| 2069 | 14 | InstantDisposFirst | bmap05_event_tiamat_c |
| 2258 | 14 | TalkEvent | MS_05_OP_04_A |
| 2338 | 14 | TalkEvent | MS_05_OP_04_B |
| 2351 | 14 | TalkResume |  |
| 249F | 14 | TalkEvent | MS_05_OP_05_A |
| 24BF | 14 | TalkEvent | MS_05_OP_05_B |
| 24DF | 14 | TalkEvent | MS_05_OP_05_C |
| 24EA | 14 | TalkEvent | MS_05_OP_05_D |
| 25A5 | 14 | InstantDisposFirstSetMode | bmap05_first_boss2_n, bmap05_first_boss2_h, bmap05_first_boss2_m |
| 2662 | 14 | InstantDisposFirstSetMode | bmap05_first_boss_n, bmap05_first_boss_h, bmap05_first_boss_m |
| 273B | 14 | TalkEvent | MS_05_OP_06_A2 |
| 2746 | 14 | TalkEvent | MS_05_OP_06_B2 |
| 274E | 14 | TalkEvent | MS_05_OP_06_C |
| 2824 | 14 | DisposAsynchronous | bmap05_first_n |
| 2836 | 14 | DisposAsynchronous | bmap05_first_h |
| 2841 | 14 | DisposAsynchronous | bmap05_first_m |
| 28E0 | 14 | TalkEvent | MS_05_OP_06_02 |
| 29AC | 14 | UnitEscapeByPID | PID_TIAMAT_EV |
| 2A07 | 14 | TalkEvent | MS_05_OP_07_NORMAL |
| 2A12 | 14 | TalkEvent | MS_05_OP_07_NORMAL_2 |
| 2A1D | 14 | TalkEvent | MS_05_OP_07 |
| 2A69 | 14 | TalkEvent | MS_05_OP_07B |
| 2A9D | 14 | TalkEvent | MS_05_OP_07C |
| 2B4F | 15 | ForceGetCount | 5 |
| 2B76 | 15 | MapLoad | bmap05 |
| 2B84 | 15 | InstantDisposSetMode | bmap05_mikata_n, bmap05_mikata_h, bmap05_mikata_m |
| 2B89 | 15 | AllUnitEscape |  |
| 2B98 | 15 | UnitTransferToForceByPID | PID_OSCAR, 7 |
| 2BA2 | 15 | UnitTransferToForceByPID | PID_BOLE, 7 |
| 2BA7 | 15 | AllUnitEscape |  |
| 2BDA | 15 | UnitForcedSallyByPID | PID_IKE |
| 2BE2 | 15 | UnitForcedSallyByPID | PID_TIAMAT |
| 2BEA | 15 | UnitForcedSallyByPID | PID_CHINON |
| 2BF2 | 15 | UnitForcedSallyByPID | PID_GATRIE |
| 2BFA | 15 | UnitForcedSallyByPID | PID_KILROY |
| 2C02 | 15 | UnitForcedSallyByPID | PID_SENERIO |
| 2C0A | 15 | UnitDontMoveSallyByPID | PID_IKE |
| 2C14 | 15 | UnitTransferToForceByPID | PID_OSCAR, 5 |
| 2C1E | 15 | UnitTransferToForceByPID | PID_BOLE, 5 |
| 2CB0 | 16 | UnitTransferToForceByPID | PID_OSCAR, 7 |
| 2CBA | 16 | UnitTransferToForceByPID | PID_BOLE, 7 |
| 2D08 | 17 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D10 | 17 | TalkEvent | MS_05_BT_IKE |
| 2D1D | 17 | SoundBossTalkEnd |  |
| 2D50 | 18 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D58 | 18 | TalkEvent | MS_05_BT_TI |
| 2D65 | 18 | SoundBossTalkEnd |  |
| 2D98 | 19 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2DA0 | 19 | TalkEvent | MS_05_BT_SE |
| 2DAD | 19 | SoundBossTalkEnd |  |
| 2DF6 | 20 | BMGetPhase |  |
| 2E36 | 20 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2E3E | 20 | TalkEvent | MS_05_BT |
| 2E4B | 20 | SoundBossTalkEnd |  |
| 2E7C | 21 | TalkEvent | MS_05_DIE |
| 2EF5 | 22 | AllUnitEscape |  |
| 2F07 | 22 | ForceCheckAnyoneDead |  |
| 2F1C | 22 | TalkEvent | MS_05_ED_01_A |
| 2F36 | 22 | UnitCheckDeadHereByPID | PID_TIAMAT |
| 2F40 | 22 | TalkEvent | MS_05_ED_01_B |
| 2F54 | 22 | UnitCheckDeadHereByPID | PID_SENERIO |
| 2F5E | 22 | TalkEvent | MS_05_ED_01_B2 |
| 2F74 | 22 | UnitCheckDeadHereByPID | PID_CHINON |
| 2F7E | 22 | UnitCheckDeadHereByPID | PID_GATRIE |
| 2F88 | 22 | UnitCheckDeadHereByPID | PID_KILROY |
| 2F9F | 22 | TalkEvent | MS_05_ED_01_C1 |
| 2FBB | 22 | TalkEvent | MS_05_ED_01_C2 |
| 2FD7 | 22 | TalkEvent | MS_05_ED_01_C3 |
| 2FF3 | 22 | TalkEvent | MS_05_ED_01_C4 |
| 300E | 22 | TalkEvent | MS_05_ED_01_C5 |
| 3029 | 22 | TalkEvent | MS_05_ED_01_C6 |
| 3044 | 22 | TalkEvent | MS_05_ED_01_C7 |
| 3065 | 22 | TalkEvent | MS_05_ED_02_S |
| 307C | 22 | TalkEvent | MS_05_ED_03_A |
| 3087 | 22 | TalkEvent | MS_05_ED_03_B |
| 30AD | 22 | TalkResume |  |
| 30D9 | 22 | TalkEvent | MS_05_ED_04_A |
| 30E4 | 22 | TalkEvent | MS_05_ED_04_B |
| 311E | 23 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.5: Flight! — internal 6

Historical evidence: Ch5 cleared with 4 yellow units; suspend/resume; yellow death (EXP-18 session).

Slot-group counts by file suffix: `{'c': 8, 'h': 8, 'm': 8, 'n': 8}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap06/dispos_c.bin:bmap06_event01_c`: F1: PID_DAKKOWA, PID_DAYNE_ARC_1, PID_DAYNE_ARC_2, PID_DAYNE_ARC_3, PID_DAYNE_ARC_4, PID_DAYNE_SKN_1, PID_DAYNE_SKN_2, PID_DAYNE_SOL_1, PID_DAYNE_SOL_2, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4, PID_DAYNE_SOL_5, PID_DAYNE_SOL_6, PID_DAYNE_SOL_7, PID_DAYNE_SOL_8
- `bmap06/dispos_c.bin:bmap06_event_greil_c`: F2: PID_GREIL_EV
- `bmap06/dispos_c.bin:bmap06_mikata_c`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap06/dispos_h.bin:bmap06_first_h`: F1: PID_DAKKOWA, PID_DAYNE_ARC, PID_DAYNE_FIG, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_ZAKO, PID_ZAKO_2
- `bmap06/dispos_h.bin:bmap06_mikata_h`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap06/dispos_h.bin:bmap06_zoen_h`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap06/dispos_m.bin:bmap06_first_m`: F1: PID_DAKKOWA, PID_DAYNE_ARC, PID_DAYNE_FIG, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_ZAKO, PID_ZAKO_2
- `bmap06/dispos_m.bin:bmap06_mikata_m`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap06/dispos_m.bin:bmap06_zoen_m`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap06/dispos_n.bin:bmap06_first_n`: F1: PID_DAKKOWA, PID_DAYNE_ARC, PID_DAYNE_FIG, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_ZAKO, PID_ZAKO_2
- `bmap06/dispos_n.bin:bmap06_mikata_n`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap06/dispos_n.bin:bmap06_zoen_n`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap06_2/dispos_c.bin:bmap06_2_event00_c`: F0: PID_BOLE, PID_GATRIE, PID_KILROY, PID_OSCAR, PID_SENERIO; F2: PID_CHINON_EV, PID_GREIL_EV, PID_IKE_EV, PID_LOFA_EV, PID_MIST_EV, PID_TIAMAT_EV
- `bmap06_2/dispos_c.bin:bmap06_2_event_ged_c`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_KILROY, PID_LOFA, PID_OSCAR, PID_SENERIO, PID_WAYU; F2: PID_IKE_EV, PID_MIST_EV, PID_TIAMAT_EV

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| E7E | 3 | regist | F16101610 |
| E85 | 3 | regist | F15161819 |
| E8C | 3 | regist | F15192322 |
| F1B | 6 | regist | ボス戦闘会話 |
| F23 | 6 | regist | ボス戦闘会話アイク |
| F2B | 6 | regist | ボス倒した |
| F63 | 7 | InstantDisposRank | bmap06_first |
| F6C | 7 | ForceGetCount | 1 |
| F75 | 7 | ForceGetFirst | 1 |
| FDF | 8 | SallySetByGroup | bmap06_mikata_c |
| 101B | 9 | ChapterMoviePlay | 6 |
| 10F4 | 10 | MapLoad | bmap06_2 |
| 1128 | 10 | InstantDispos | bmap06_2_event00_c |
| 1135 | 10 | UnitEscapeByPID | PID_OSCAR |
| 1142 | 10 | UnitEscapeByPID | PID_BOLE |
| 114F | 10 | UnitEscapeByPID | PID_KILROY |
| 115C | 10 | UnitEscapeByPID | PID_CHINON_EV |
| 1169 | 10 | UnitEscapeByPID | PID_GATRIE |
| 1176 | 10 | UnitEscapeByPID | PID_SENERIO |
| 12F6 | 10 | AllUnitEscape |  |
| 1300 | 10 | AllUnitEscape |  |
| 130D | 10 | TalkEvent | MS_06_OP_01 |
| 132E | 10 | TalkEvent | MS_06_OP_02 |
| 133D | 10 | TalkResume |  |
| 134C | 10 | TalkResume |  |
| 135D | 10 | TalkResume |  |
| 13B4 | 11 | MapLoad | bmap06 |
| 1451 | 11 | InstantDispos | bmap06_event01_c |
| 14A8 | 11 | TalkEvent | MS_06_OP_05 |
| 14C1 | 11 | TalkResume |  |
| 1510 | 11 | AllUnitEscape |  |
| 1518 | 11 | SallySetByGroup | bmap06_mikata_c |
| 1520 | 11 | InstantDispos | bmap06_mikata_c |
| 1528 | 11 | InstantDispos | bmap06_event_greil_c |
| 152D | 11 | AllUnitEscape |  |
| 1565 | 11 | InstantDispos | bmap06_mikata_c |
| 15F9 | 11 | TalkEvent | MS_06_OP_05_01 |
| 160B | 11 | TalkEvent | MS_06_OP_05_02_A |
| 1616 | 11 | TalkEvent | MS_06_OP_05_02_B |
| 1628 | 11 | TalkEvent | MS_06_OP_05_03_A |
| 1633 | 11 | TalkEvent | MS_06_OP_05_03_B |
| 163B | 11 | TalkEvent | MS_06_OP_05_04 |
| 1657 | 11 | TalkEvent | MS_06_OP_05_05_A |
| 1677 | 11 | TalkEvent | MS_06_OP_05_05_B |
| 1697 | 11 | TalkEvent | MS_06_OP_05_05_C |
| 16B3 | 11 | TalkEvent | MS_06_OP_05_06_A |
| 16D3 | 11 | TalkEvent | MS_06_OP_05_06_B |
| 16F3 | 11 | TalkEvent | MS_06_OP_05_06_C |
| 1705 | 11 | TalkEvent | MS_06_OP_05_06_D |
| 1710 | 11 | TalkEvent | MS_06_OP_05_06_E |
| 1718 | 11 | TalkEvent | MS_06_OP_05_07 |
| 172A | 11 | TalkEvent | MS_06_OP_05_08_A |
| 1732 | 11 | TalkEvent | MS_06_OP_05_09 |
| 175A | 11 | TalkEvent | MS_06_OP_05_10_A |
| 1765 | 11 | TalkEvent | MS_06_OP_05_10_B |
| 1777 | 11 | TalkEvent | MS_06_OP_05_11_A |
| 1782 | 11 | TalkEvent | MS_06_OP_05_11_B |
| 1794 | 11 | TalkEvent | MS_06_OP_05_12_A |
| 17A6 | 11 | TalkEvent | MS_06_OP_05_13_A |
| 17B1 | 11 | TalkEvent | MS_06_OP_05_13_B |
| 17B9 | 11 | TalkEvent | MS_06_OP_05_14 |
| 17CA | 11 | TalkResume |  |
| 183A | 11 | Dispos | bmap06_event_greil_c |
| 1842 | 11 | Dispos | bmap06_mikata_c |
| 186D | 11 | Dispos | bmap06_event_greil_c |
| 19ED | 11 | TalkEvent | MS_06_OP_05_15 |
| 1A11 | 11 | UnitTransferToForceByPID | PID_GREIL_EV, 1 |
| 1A2E | 11 | UnitEscapeByPID | PID_GREIL_EV |
| 1AA8 | 11 | TalkEvent | MS_06_OP_05_15_0 |
| 1B3B | 12 | ForceGetCount | 5 |
| 1B62 | 12 | MapLoad | bmap06 |
| 1B70 | 12 | InstantDisposSetMode | bmap06_mikata_n, bmap06_mikata_h, bmap06_mikata_m |
| 1B75 | 12 | AllUnitEscape |  |
| 1BA1 | 12 | UnitTransferToForceByPID | PID_OSCAR, 5 |
| 1BAB | 12 | UnitTransferToForceByPID | PID_BOLE, 5 |
| 1BB5 | 12 | UnitTransferToForceByPID | PID_KILROY, 5 |
| 1BC6 | 12 | UnitForcedSallyByPID | PID_IKE |
| 1BCE | 12 | UnitForcedSallyByPID | PID_GREIL |
| 1BD6 | 12 | UnitForcedSallyByPID | PID_TIAMAT |
| 1BDE | 12 | UnitForcedSallyByPID | PID_OSCAR |
| 1BE6 | 12 | UnitForcedSallyByPID | PID_BOLE |
| 1BEE | 12 | UnitForcedSallyByPID | PID_CHINON |
| 1BF6 | 12 | UnitForcedSallyByPID | PID_GATRIE |
| 1BFE | 12 | UnitForcedSallyByPID | PID_KILROY |
| 1C06 | 12 | UnitForcedSallyByPID | PID_SENERIO |
| 1C0E | 12 | UnitDontMoveSallyByPID | PID_IKE |
| 1CA1 | 14 | DisposSetMode | bmap06_zoen_n, bmap06_zoen_h, bmap06_zoen_m |
| 1CDD | 15 | DisposSetMode | bmap06_zoen_n, bmap06_zoen_h, bmap06_zoen_m |
| 1D0C | 16 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1D14 | 16 | TalkEvent | MS_06_BT_IKE |
| 1D21 | 16 | SoundBossTalkEnd |  |
| 1D56 | 17 | BMGetPhase |  |
| 1D86 | 17 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1D8E | 17 | TalkEvent | MS_06_BT |
| 1D9B | 17 | SoundBossTalkEnd |  |
| 1DCC | 18 | TalkEvent | MS_06_DIE |
| 1DDC | 18 | TalkEvent | MS_06_EV_ENEMY_01 |
| 1EAC | 20 | TalkEvent | MS_06_ED_ENEMY |
| 1F27 | 20 | TalkEvent | MS_06_ED_ENEMY_BOSS |
| 1F57 | 20 | AllUnitEscape |  |
| 1F92 | 20 | TalkEvent | MS_06_ED_01_01_A |
| 1F9D | 20 | TalkEvent | MS_06_ED_01_01_B |
| 1FB9 | 20 | TalkEvent | MS_06_ED_01_02_A |
| 1FCE | 20 | TalkEvent | MS_06_ED_01_02_A_a |
| 1FE3 | 20 | TalkEvent | MS_06_ED_01_02_A_b |
| 1FEE | 20 | TalkEvent | MS_06_ED_01_02_B |
| 2000 | 20 | TalkEvent | MS_06_ED_01_03_A |
| 200B | 20 | TalkEvent | MS_06_ED_01_03_B |
| 2046 | 20 | TalkEvent | MS_06_ED_02 |
| 2097 | 20 | TalkEvent | MS_06_ED_03 |
| 20CD | 20 | TalkEvent | MS_06_ED_04 |
| 20D8 | 20 | TalkEvent | MS_06_ED_04_BOSS |
| 215C | 21 | TalkEvent | MS_06_GAMEOVER |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.6: A Brief Diversion — internal 7

Historical evidence: Ch6 started; yellow death record verified (EXP-19); escape not yet played.

Slot-group counts by file suffix: `{'c': 6, 'h': 6, 'm': 6, 'n': 6}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap07/dispos_c.bin:bmap07_event00_c`: F1: PID_DAYNE_SOL_1
- `bmap07/dispos_c.bin:bmap07_event01_c`: F2: PID_DUMMY1, PID_LOFA_EV, PID_MIST
- `bmap07/dispos_c.bin:bmap07_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap07/dispos_c.bin:bmap07_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap07/dispos_c.bin:bmap07_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap07/dispos_c.bin:bmap07_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap07/dispos_h.bin:bmap07_dispos_z01_h`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap07/dispos_h.bin:bmap07_dispos_z02_h`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap07/dispos_h.bin:bmap07_dispos_z03_h`: F1: PID_DAYNE_SOL
- `bmap07/dispos_h.bin:bmap07_dispos_z04_h`: F1: PID_DAYNE_MAG
- `bmap07/dispos_h.bin:bmap07_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_EMAKOU
- `bmap07/dispos_h.bin:bmap07_mikata_h`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap07/dispos_m.bin:bmap07_dispos_z02_m`: F1: PID_DAYNE_SOL
- `bmap07/dispos_m.bin:bmap07_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_EMAKOU
- `bmap07/dispos_m.bin:bmap07_mikata_m`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap07/dispos_n.bin:bmap07_dispos_z02_n`: F1: PID_DAYNE_SOL
- `bmap07/dispos_n.bin:bmap07_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_EMAKOU
- `bmap07/dispos_n.bin:bmap07_mikata_n`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| E38 | 1 | TalkEvent | MESC_IKE |
| E40 | 1 | DefaultEscapeTalk |  |
| E66 | 1 | UnitEscape | ?, 0 |
| F17 | 4 | regist | F08201826 |
| F6B | 6 | regist | 見つかるトリガ |
| F73 | 6 | regist | 見つかるイベント |
| F7B | 6 | regist | ＣＰ変更トリガ |
| F83 | 6 | regist | ＣＰ変更 |
| F8B | 6 | regist | 増援イベント |
| F93 | 6 | regist | ボス戦闘会話 |
| F9B | 6 | regist | ボス戦闘会話アイク |
| FDA | 7 | InstantDisposRank | bmap07_first |
| FE2 | 7 | InstantDispos | bmap07_event00_c |
| FF2 | 7 | ForceGetCount | 1 |
| FFB | 7 | ForceGetFirst | 1 |
| 1077 | 8 | SallySetByGroup | bmap07_mikata_c |
| 1127 | 9 | MapLoad | gmap |
| 11FF | 9 | TalkEvent | MS_07_GMAP_01 |
| 12A9 | 9 | TalkEvent | MS_07_GMAP_02 |
| 1413 | 9 | TalkEvent | MS_07_GMAP_03 |
| 149C | 9 | TalkEvent | MS_07_GMAP_04 |
| 157A | 9 | TalkEvent | MS_07_GMAP_06 |
| 1640 | 9 | TalkEvent | MS_07_GMAP_07 |
| 16E6 | 9 | TalkEvent | MS_07_GMAP_08 |
| 17FA | 10 | ChapterMoviePlay | 7 |
| 185D | 11 | TalkEvent | MS_07_OP_01_A |
| 1868 | 11 | TalkEvent | MS_07_OP_01_B |
| 1899 | 11 | TalkEvent | MS_07_OP_02 |
| 18D4 | 11 | TalkEvent | MS_07_OP_03_01_A |
| 18DF | 11 | TalkEvent | MS_07_OP_03_01_B |
| 18FB | 11 | TalkEvent | MS_07_OP_03_02_A |
| 191B | 11 | TalkEvent | MS_07_OP_03_02_B |
| 193B | 11 | TalkEvent | MS_07_OP_03_02_C |
| 1946 | 11 | TalkEvent | MS_07_OP_03_02_D |
| 197B | 12 | MapLoad | bmap07 |
| 199F | 12 | SallySetByGroup | bmap07_mikata_c |
| 19A7 | 12 | InstantDispos | bmap07_mikata_c |
| 19AF | 12 | InstantDispos | bmap07_event01_c |
| 19CB | 12 | Dispos_ForEventTiamat | bmap07_event_tiamat_c, 1 |
| 19E3 | 12 | Dispos_ForEventSenerio | bmap07_event_senerio_c, bmap07_event_senerio2_c, 1 |
| 1D60 | 12 | TalkEvent | MS_07_OP_04 |
| 1DED | 12 | TalkEvent | MS_07_OP_05_01 |
| 1E00 | 12 | TalkEvent | MS_07_OP_05_02 |
| 1EB9 | 12 | UnitEscapeByPID | PID_LOFA_EV |
| 1EC1 | 12 | UnitEscapeByPID | PID_MIST |
| 1EC9 | 12 | UnitEscapeByPID | PID_DUMMY1 |
| 1ED1 | 12 | UnitEscapeByPID | PID_TIAMAT_EV |
| 1ED9 | 12 | UnitEscapeByPID | PID_SENERIO_EV |
| 1EE1 | 12 | TalkEvent | MS_07_OP_04_x |
| 1F33 | 13 | ForceGetCount | 5 |
| 1F5A | 13 | MapLoad | bmap07 |
| 1F68 | 13 | InstantDisposSetMode | bmap07_mikata_n, bmap07_mikata_h, bmap07_mikata_m |
| 1F6D | 13 | AllUnitEscape |  |
| 1F7A | 13 | MapLoad | bmap04 |
| 1F88 | 13 | InstantDisposSetMode | bmap04_mikata_n, bmap04_mikata_h, bmap04_mikata_m |
| 1F8D | 13 | AllUnitEscape |  |
| 1FB9 | 13 | UnitTransferToForceByPID | PID_GREIL, 7 |
| 1FC3 | 13 | UnitTransferToForceByPID | PID_CHINON, 7 |
| 1FCD | 13 | UnitTransferToForceByPID | PID_GATRIE, 7 |
| 1FE0 | 13 | UnitForcedSallyByPID | PID_IKE |
| 1FE8 | 13 | UnitForcedSallyByPID | PID_TIAMAT |
| 1FF0 | 13 | UnitForcedSallyByPID | PID_OSCAR |
| 1FF8 | 13 | UnitForcedSallyByPID | PID_BOLE |
| 2000 | 13 | UnitForcedSallyByPID | PID_KILROY |
| 2008 | 13 | UnitForcedSallyByPID | PID_SENERIO |
| 200F | 13 | UnitDontMoveSallyByPID | PID_IKE |
| 20D3 | 15 | ForceGetCount | 0 |
| 20DC | 15 | ForceGetFirst | 0 |
| 21E8 | 15 | TalkEvent | MS_07_EV_01 |
| 2216 | 15 | UnitEscapeByPID | PID_DAYNE_SOL_1 |
| 221F | 15 | ForceGetCount | 1 |
| 2228 | 15 | ForceGetFirst | 1 |
| 232A | 16 | TalkEvent | MS_07_EV_02 |
| 233F | 16 | ForceGetCount | 1 |
| 2352 | 16 | ForceGetFirst | 1 |
| 23DC | 17 | BMGetPhase |  |
| 2434 | 18 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 243C | 18 | TalkEvent | MS_07_BT_IKE |
| 2449 | 18 | SoundBossTalkEnd |  |
| 247D | 19 | BMGetPhase |  |
| 24AD | 19 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 24B5 | 19 | TalkEvent | MS_07_BT |
| 24C2 | 19 | SoundBossTalkEnd |  |
| 24F0 | 20 | TalkEvent | MS_07_DIE |
| 2543 | 21 | AllUnitEscape |  |
| 2576 | 21 | TalkEvent | MS_07_ED_01_A |
| 2595 | 21 | TalkEvent | MS_07_ED_01_B |
| 25A0 | 21 | TalkEvent | MS_07_ED_01_C |
| 25C9 | 21 | TalkEvent | MS_07_ED_02_A |
| 2602 | 21 | TalkEvent | MS_07_ED_02_B |
| 262C | 21 | TalkEvent | MS_07_ED_02_B_DEL |
| 2658 | 21 | TalkEvent | MS_07_ED_02_B_DISP |
| 2660 | 21 | TalkEvent | MS_07_ED_02_B_2 |
| 26AC | 21 | TalkEvent | MS_07_ED_03 |
| 271E | 22 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.7: Shades of Evil — internal 8

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 6, 'h': 6, 'm': 6, 'n': 6}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap08/dispos_c.bin:bmap08_event00_c`: F1: PID_PRAGUE; F2: PID_GREIL_EV
- `bmap08/dispos_c.bin:bmap08_event_ike_c`: F0: PID_IKE_EV
- `bmap08/dispos_c.bin:bmap08_event_pra_c`: F1: PID_PRAGUE
- `bmap08/dispos_c.bin:bmap08_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap08/dispos_c.bin:bmap08_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap08/dispos_c.bin:bmap08_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap08/dispos_c.bin:bmap08_event_zako_c`: F1: PID_DAYNE_SOL_1
- `bmap08/dispos_c.bin:bmap08_m01_c`: F0: PID_CHINON, PID_GATRIE; F2: PID_GREIL_EV
- `bmap08/dispos_c.bin:bmap08_m_zoen_c`: F2: PID_WAYU
- `bmap08/dispos_c.bin:bmap08_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap08/dispos_h.bin:bmap08_first01_h`: F1: PID_DAYNE_SOL_1, PID_DAYNE_SOL_2
- `bmap08/dispos_h.bin:bmap08_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_SOL, PID_ZAKO_8_H, PID_ZAKO_8_H_2
- `bmap08/dispos_h.bin:bmap08_mikata_h`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap08/dispos_h.bin:bmap08_z02_h`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap08/dispos_h.bin:bmap08_z03_h`: F1: PID_DAYNE_MAG, PID_DAYNE_SOL
- `bmap08/dispos_h.bin:bmap08_z04_h`: F1: PID_BARUMA, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SOL
- `bmap08/dispos_h.bin:bmap08_z05_h`: F1: PID_12_THIEF
- `bmap08/dispos_h.bin:bmap08_zoen_ev_h`: F1: PID_DAYNE_SOL, PID_ZAKO_8_H_2
- `bmap08/dispos_m.bin:bmap08_first01_m`: F1: PID_DAYNE_SOL_2
- `bmap08/dispos_m.bin:bmap08_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_SOL, PID_ZAKO_8_H
- `bmap08/dispos_m.bin:bmap08_mikata_m`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap08/dispos_m.bin:bmap08_z02_m`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap08/dispos_m.bin:bmap08_z03_m`: F1: PID_DAYNE_MAG, PID_DAYNE_SOL
- `bmap08/dispos_m.bin:bmap08_z04_m`: F1: PID_BARUMA, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SOL
- `bmap08/dispos_m.bin:bmap08_z05_m`: F1: PID_12_THIEF
- `bmap08/dispos_m.bin:bmap08_zoen_ev_m`: F1: PID_DAYNE_SOL, PID_ZAKO_8_H_2
- `bmap08/dispos_n.bin:bmap08_first01_n`: F1: PID_DAYNE_SOL_2
- `bmap08/dispos_n.bin:bmap08_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_SOL, PID_ZAKO_8_H
- `bmap08/dispos_n.bin:bmap08_mikata_n`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT
- `bmap08/dispos_n.bin:bmap08_z02_n`: F1: PID_DAYNE_ARC, PID_DAYNE_SOL
- `bmap08/dispos_n.bin:bmap08_z03_n`: F1: PID_DAYNE_MAG, PID_DAYNE_SOL
- `bmap08/dispos_n.bin:bmap08_z04_n`: F1: PID_BARUMA, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SOL
- `bmap08/dispos_n.bin:bmap08_z05_n`: F1: PID_12_THIEF
- `bmap08/dispos_n.bin:bmap08_zoen_ev_n`: F1: PID_DAYNE_SOL, PID_ZAKO_8_H_2
- `bmap08_2/dispos_c.bin:bmap08_2_event00_c`: F1: PID_PRAGUE; F2: PID_GREIL_EV
- `bmap08_2/dispos_c.bin:bmap08_2_event_garia2_c`: F2: PID_G_ZAKO
- `bmap08_2/dispos_c.bin:bmap08_2_event_garia_c`: F2: PID_LAY, PID_LETHE, PID_MORDY
- `bmap08_2/dispos_c.bin:bmap08_2_event_ike_c`: F0: PID_IKE
- `bmap08_2/dispos_c.bin:bmap08_2_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap08_2/dispos_c.bin:bmap08_2_event_senerio3_c`: F2: PID_SENERIO_EV
- `bmap08_2/dispos_c.bin:bmap08_2_event_senerio_c`: F0: PID_SENERIO
- `bmap08_2/dispos_c.bin:bmap08_2_event_sikkoku_c`: F1: PID_BLACKKNIGHT
- `bmap08_2/dispos_c.bin:bmap08_2_event_tiamat2_c`: F2: PID_TIAMAT_EV
- `bmap08_2/dispos_c.bin:bmap08_2_event_tiamat_c`: F0: PID_TIAMAT
- `bmap08_2/dispos_c.bin:bmap08_2_event_wayu_c`: F0: PID_WAYU
- `bmap08_2/dispos_c.bin:bmap08_2_event_youheidan_c`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_KILROY, PID_OSCAR
- `bmap08_2/dispos_c.bin:bmap08_2_event_zoen00_c`: F1: PID_DAYNE_SOL_2
- `bmap08_2/dispos_c.bin:bmap08_2_event_zoen01_c`: F1: PID_DAYNE_ARC_2, PID_DAYNE_SOL_2
- `bmap08_2/dispos_c.bin:bmap08_2_event_zoen02_c`: F1: PID_DAYNE_ARC_1, PID_DAYNE_SOL_1
- `bmap08_2/dispos_c.bin:bmap08_2_event_zoen03_c`: F1: PID_DAYNE_ARC_1, PID_DAYNE_SOL_1
- `bmap08_2/dispos_c.bin:bmap08_2_event_zoen04_c`: F1: PID_DAYNE_ARC_1, PID_DAYNE_SOL_1
- `bmap08_2/dispos_c.bin:bmap08_2_event_zoen05_c`: F1: PID_DAYNE_ARC_3, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4, PID_DAYNE_SOL_5

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 170A | 3 | UnitEscape | ?, 0 |
| 1762 | 4 | UnitEscape | ?, 0 |
| 18DE | 7 | regist | 宝箱２ |
| 18E5 | 7 | regist | 宝箱３ |
| 18EC | 7 | regist | 宝箱４ |
| 18F4 | 7 | regist | F03032011 |
| 18FC | 7 | regist | F21042205 |
| 1983 | 10 | regist | 増援予告 |
| 198B | 10 | regist | 増援トリガ |
| 1993 | 10 | regist | 増援 |
| 199B | 10 | regist | ターン増援 |
| 19A3 | 10 | regist | ターン増援トリガ |
| 19AB | 10 | regist | グレイルプラハ登場トリガ |
| 19B3 | 10 | regist | グレイルプラハ登場 |
| 19BB | 10 | regist | 会話アイクシノン |
| 19C3 | 10 | regist | 会話アイクガトリー |
| 19CB | 10 | regist | 会話アイクワユ |
| 19D3 | 10 | regist | ボス戦闘会話 |
| 19DB | 10 | regist | ボス戦闘会話アイク |
| 19E3 | 10 | regist | ボス死亡 |
| 1A22 | 11 | InstantDisposRank | bmap08_first |
| 1A2A | 11 | InstantDispos | bmap08_event_zako_c |
| 1A39 | 11 | InstantDisposRank | bmap08_first01 |
| 1A7B | 12 | SallySetByGroup | bmap08_mikata_c |
| 1AB7 | 13 | ChapterMoviePlay | 8 |
| 1B09 | 14 | TalkEvent | MS_08_OP_01 |
| 1B4B | 15 | MapLoad | bmap08 |
| 1B72 | 15 | InstantDisposRank | bmap08_first |
| 1B7A | 15 | InstantDisposRank | bmap08_first01 |
| 1B82 | 15 | InstantDispos | bmap08_event_zako_c |
| 1BAF | 15 | AllUnitEscape |  |
| 1BB7 | 15 | SallySetByGroup | bmap08_mikata_c |
| 1BBF | 15 | InstantDisposFirst | bmap08_mikata_c |
| 1BD4 | 15 | Dispos_ForEventTiamat | bmap08_event_tiamat_c, 1 |
| 1BEC | 15 | Dispos_ForEventSenerio | bmap08_event_senerio_c, bmap08_event_senerio2_c, 1 |
| 1E11 | 15 | TalkEvent | MS_08_OP_02_01 |
| 1E49 | 15 | TalkEvent | MS_08_OP_02_02 |
| 1E98 | 15 | InstantDisposFirstSetMode | bmap08_first01_n, bmap08_first01_h, bmap08_first01_m |
| 1FAE | 15 | TalkEvent | MS_08_OP_02_03 |
| 2037 | 15 | DisposAsynchronous | bmap08_event_zako_c |
| 2045 | 15 | DisposSetMode | bmap08_first_n, bmap08_first_h, bmap08_first_m |
| 205E | 15 | TalkEvent | MS_08_OP_02_04 |
| 2087 | 15 | TalkEvent | MS_08_OP_03_01 |
| 209A | 15 | TalkEvent | MS_08_OP_03_02 |
| 20E0 | 15 | UnitEscapeByPID | PID_SENERIO_EV |
| 20E8 | 15 | UnitEscapeByPID | PID_TIAMAT_EV |
| 21C7 | 15 | DisposContinueSetMode | bmap08_first01_n, bmap08_first01_h, bmap08_first01_m |
| 2241 | 15 | UnitForcedSallyByPID | PID_IKE |
| 2249 | 15 | UnitForcedSallyByPID | PID_TIAMAT |
| 2251 | 15 | UnitForcedSallyByPID | PID_OSCAR |
| 2259 | 15 | UnitForcedSallyByPID | PID_BOLE |
| 2261 | 15 | UnitForcedSallyByPID | PID_KILROY |
| 2269 | 15 | UnitForcedSallyByPID | PID_SENERIO |
| 2271 | 15 | UnitDontMoveSallyByPID | PID_IKE |
| 22CF | 16 | ForceGetCount | 5 |
| 22F6 | 16 | MapLoad | bmap08 |
| 2304 | 16 | InstantDisposSetMode | bmap08_mikata_n, bmap08_mikata_h, bmap08_mikata_m |
| 2309 | 16 | AllUnitEscape |  |
| 241A | 18 | Dispos | bmap08_m_zoen_c |
| 2459 | 18 | TalkEvent | MS_08_EV_04 |
| 256A | 19 | DisposSetMode | bmap08_zoen_ev_n, bmap08_zoen_ev_h, bmap08_zoen_ev_m |
| 2572 | 19 | Dispos | bmap08_event_pra_c |
| 25B0 | 19 | TalkEvent | MS_08_EV_01_A |
| 25BB | 19 | TalkEvent | MS_08_EV_01_B |
| 25CC | 19 | TalkResume |  |
| 25D4 | 19 | InstantDispos | bmap08_m01_c |
| 2769 | 19 | UnitEscape | ?, 0 |
| 2957 | 19 | TalkEvent | MS_08_EV_02_A |
| 2962 | 19 | TalkEvent | MS_08_EV_02_B |
| 29BD | 19 | UnitEscapeByPID | PID_PRAGUE |
| 29C5 | 19 | UnitEscapeByPID | PID_GREIL_EV |
| 29D4 | 19 | UnitEscapeByPID | PID_DAYNE_SOL_5 |
| 29DC | 19 | UnitEscapeByPID | PID_DAYNE_SOL_6 |
| 2A4F | 19 | TalkEvent | MS_08_EV_03_A |
| 2A5A | 19 | TalkEvent | MS_08_EV_03_B |
| 2ABD | 19 | DisposSetMode | bmap08_z04_n, bmap08_z04_h, bmap08_z04_m |
| 2B29 | 20 | DisposSetMode | bmap08_z05_n, bmap08_z05_h, bmap08_z05_m |
| 2B5A | 21 | Dispos | bmap08_z05_n |
| 2BE2 | 22 | TalkEvent | MS_08_TK_01_01 |
| 2BED | 22 | TalkEvent | MS_08_TK_01_02 |
| 2BF7 | 22 | UnitTransferToForceByPID | PID_WAYU, 0 |
| 2C52 | 23 | TalkEvent | MS_08_TK_02 |
| 2C92 | 24 | TalkEvent | MS_08_TK_03 |
| 2CCA | 25 | LocalDieTalkWithBgmChange | 会話アイクワユ, MS_08_DIE_WAYU |
| 2CF8 | 26 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D00 | 26 | TalkEvent | MS_08_BT_IKE |
| 2D0D | 26 | SoundBossTalkEnd |  |
| 2D42 | 27 | BMGetPhase |  |
| 2D72 | 27 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D7A | 27 | TalkEvent | MS_08_BT |
| 2D87 | 27 | SoundBossTalkEnd |  |
| 2DB8 | 28 | TalkEvent | MS_08_DIE |
| 2DDE | 29 | ForceGetCount | 1 |
| 2E0B | 30 | TalkEvent | MS_08_ED_01 |
| 2ED8 | 34 | ForceGetCount | 1 |
| 2EE2 | 34 | ForceGetFirst | 1 |
| 2F1C | 34 | UnitEscape | ?, 0 |
| 2F5F | 35 | MapLoad | bmap08_2 |
| 2F96 | 35 | InstantDispos | bmap08_2_event_zoen01_c |
| 2F9B | 35 | AllUnitEscape |  |
| 2FA3 | 35 | InstantDispos | bmap08_2_event00_c |
| 2FE8 | 35 | InstantDispos | bmap08_2_event_tiamat_c |
| 2FF3 | 35 | InstantDispos | bmap08_2_event_tiamat2_c |
| 3013 | 35 | InstantDisposFirst | bmap08_2_event_ike_c |
| 3025 | 35 | InstantDisposFirst | bmap08_2_event_senerio_c |
| 3035 | 35 | Dispos_ForEventSenerio | bmap08_2_event_senerio2_c, bmap08_2_event_senerio3_c, 1 |
| 303D | 35 | InstantDispos | bmap08_2_event_youheidan_c |
| 304F | 35 | InstantDispos | bmap08_2_event_wayu_c |
| 330F | 35 | TalkEvent | MS_08_ED_01_02 |
| 339A | 35 | TalkEvent | MS_08_ED_02_01 |
| 33A2 | 35 | Dispos | bmap08_2_event_zoen00_c |
| 33AF | 35 | TalkEvent | MS_08_ED_02_01_2 |
| 33DF | 35 | Dispos | bmap08_2_event_zoen01_c |
| 33EF | 35 | TalkEvent | MS_08_ED_02_01_3 |
| 3469 | 35 | DisposAsynchronous | bmap08_2_event_zoen02_c |
| 34F8 | 35 | DisposAsynchronous | bmap08_2_event_zoen03_c |
| 3517 | 35 | DisposAsynchronous | bmap08_2_event_zoen04_c |
| 354C | 35 | TalkEvent | MS_08_ED_02_02 |
| 35A8 | 35 | TalkEvent | MS_08_ED_03 |
| 385C | 35 | TalkEvent | MS_08_ED_04_01 |
| 3923 | 35 | TalkEvent | MS_08_ED_04_02 |
| 3BE9 | 35 | TalkEvent | MS_08_ED_05_01 |
| 3CA4 | 35 | TalkEvent | MS_08_ED_05_02 |
| 3F0F | 35 | TalkEvent | MS_08_ED_06 |
| 3FD5 | 35 | InstantDispos | bmap08_2_event_zoen05_c |
| 40C2 | 35 | TalkEvent | MS_08_ED_05_03 |
| 40D9 | 35 | Dispos | bmap08_2_event_garia_c |
| 4119 | 35 | Dispos | bmap08_2_event_garia2_c |
| 413C | 35 | TalkEvent | MS_08_ED_07 |
| 4177 | 35 | TalkEvent | MS_08_ED_08 |
| 417F | 35 | InstantDispos | bmap08_2_event_sikkoku_c |
| 4250 | 35 | TalkEvent | MS_08_ED_08_02 |
| 436C | 35 | UnitEscapeByPID | PID_PRAGUE |
| 438C | 35 | TalkEvent | MS_08_ED_09 |
| 43A4 | 35 | TalkEvent | MS_08_ED_09_02 |
| 4407 | 35 | UnitEscapeByPID | PID_BLACKKNIGHT |
| 440F | 35 | TalkEvent | MS_08_ED_10 |
| 4458 | 35 | AllUnitEscape |  |
| 4499 | 36 | TalkEvent | MS_08_ED_11 |
| 44AA | 36 | TalkResume |  |
| 44BB | 36 | TalkResume |  |
| 450C | 37 | MapLoad | bmap09_3 |
| 454B | 37 | InstantDispos | bmap09_3_event_ike_c |
| 4561 | 37 | InstantDispos | bmap09_3_event_greil_c |
| 4637 | 37 | TalkEvent | MS_08_ED_12 |
| 46A6 | 37 | TalkEvent | MS_08_ED_13 |
| 46B5 | 37 | TalkResume |  |
| 4767 | 37 | TalkEvent | MS_08_ED_14 |
| 485A | 37 | UnitEscapeByPID | PID_GREIL_EV |
| 48D8 | 37 | AllUnitEscape |  |
| 494C | 39 | MapLoad | bmap09_2 |
| 4975 | 39 | InstantDispos | bmap09_2_event1_c |
| 4A3C | 39 | TalkEvent | MS_08_ED_15 |
| 4B43 | 39 | TalkEvent | MS_08_ED_17_01 |
| 4C6E | 39 | TalkEvent | MS_08_ED_17_02 |
| 4CC4 | 39 | TalkEvent | MS_08_ED_18 |
| 4D10 | 39 | TalkEvent | MS_08_ED_19_01 |
| 4D4D | 39 | TalkEvent | MS_08_ED_19_02 |
| 4E07 | 39 | UnitEscapeByPID | PID_BLACKKNIGHT_EV1 |
| 4E96 | 39 | TalkEvent | MS_08_ED_20 |
| 4EB5 | 39 | TalkEvent | MS_08_ED_21 |
| 4F49 | 39 | AllUnitEscape |  |
| 5026 | 40 | MapLoad | bmap09_3 |
| 505D | 40 | InstantDispos | bmap09_3_event1_c |
| 5065 | 40 | InstantDispos | bmap09_3_event_tiamat_c |
| 5072 | 40 | Dispos_ForEventSenerio | bmap09_3_event_senerio_c, bmap09_3_event_senerio2_c, 1 |
| 507A | 40 | InstantDispos | bmap09_3_event_youheidan_c |
| 5087 | 40 | UnitEscapeByPID | PID_OSCAR |
| 5094 | 40 | UnitEscapeByPID | PID_BOLE |
| 50A1 | 40 | UnitEscapeByPID | PID_KILROY |
| 50AE | 40 | UnitEscapeByPID | PID_CHINON |
| 50BB | 40 | UnitEscapeByPID | PID_GATRIE |
| 50C8 | 40 | UnitEscapeByPID | PID_SENERIO |
| 5242 | 40 | TalkEvent | MS_08_ED_22_A |
| 52BB | 40 | TalkEvent | MS_08_ED_22_B |
| 5399 | 40 | AllUnitEscape |  |
| 53A3 | 40 | AllUnitEscape |  |
| 53C8 | 40 | TalkEvent | MS_08_ED_22_C |
| 549C | 41 | AllUnitEscape |  |
| 54DE | 42 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.8: Despair and Hope — internal 9

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 7, 'h': 7, 'm': 7, 'n': 7}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap09/dispos_c.bin:bmap09_elaice_c`: F1: PID_ELAICE
- `bmap09/dispos_c.bin:bmap09_enemy_common_c`: F1: PID_DAYNE_ARC, PID_DAYNE_ARC_1, PID_DAYNE_ARC_2, PID_DAYNE_SKN, PID_DAYNE_SKN_1, PID_DAYNE_SKN_2, PID_DAYNE_SKN_3, PID_DAYNE_SKN_4, PID_DAYNE_SOL, PID_DAYNE_SOL_1, PID_DAYNE_SOL_10, PID_DAYNE_SOL_2, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4, PID_DAYNE_SOL_5, PID_DAYNE_SOL_6, PID_DAYNE_SOL_7, PID_DAYNE_SOL_8, PID_DAYNE_SOL_9, PID_KAMURA
- `bmap09/dispos_c.bin:bmap09_event01_c`: F2: PID_IKE_EV
- `bmap09/dispos_c.bin:bmap09_event_boss_c`: F1: PID_DAYNE_ARM_1
- `bmap09/dispos_c.bin:bmap09_event_gria_c`: F2: PID_LETHE, PID_MORDY
- `bmap09/dispos_c.bin:bmap09_event_mist_c`: F2: PID_MIST_EV
- `bmap09/dispos_c.bin:bmap09_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap09/dispos_c.bin:bmap09_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap09/dispos_c.bin:bmap09_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap09/dispos_c.bin:bmap09_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap09/dispos_c.bin:bmap09_z01_1_c`: F1: PID_DAYNE_ARM
- `bmap09/dispos_c.bin:bmap09_z01_c`: F1: PID_DAYNE_SKN, PID_DAYNE_SOL
- `bmap09/dispos_c.bin:bmap09_z02_c`: F1: PID_DAYNE_MAG, PID_DAYNE_SOL
- `bmap09/dispos_c.bin:bmap09_z04_c`: F1: PID_DAYNE_SOL, PID_DAYNE_SRD
- `bmap09/dispos_h.bin:bmap09_elaice_h`: F1: PID_ELAICE
- `bmap09/dispos_h.bin:bmap09_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_FIG, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_KAMURA
- `bmap09/dispos_h.bin:bmap09_mikata_h`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap09/dispos_h.bin:bmap09_z01_1_h`: F1: PID_DAYNE_ARM
- `bmap09/dispos_h.bin:bmap09_z01_h`: F1: PID_DAYNE_SOL
- `bmap09/dispos_h.bin:bmap09_z02_1_h`: F1: PID_DAYNE_SOL
- `bmap09/dispos_h.bin:bmap09_z02_h`: F1: PID_DAYNE_SOL
- `bmap09/dispos_h.bin:bmap09_z03_h`: F1: PID_DAYNE_MAG, PID_DAYNE_SKN, PID_DAYNE_SOL
- `bmap09/dispos_h.bin:bmap09_z04_h`: F1: PID_DAYNE_SOL, PID_DAYNE_SRD
- `bmap09/dispos_h.bin:bmap09_z05_h`: F1: PID_DAYNE_MAG
- `bmap09/dispos_m.bin:bmap09_elaice_m`: F1: PID_ELAICE
- `bmap09/dispos_m.bin:bmap09_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_KAMURA, PID_ZAKO
- `bmap09/dispos_m.bin:bmap09_mikata_m`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap09/dispos_m.bin:bmap09_z01_1_m`: F1: PID_DAYNE_ARM
- `bmap09/dispos_m.bin:bmap09_z01_m`: F1: PID_DAYNE_SOL
- `bmap09/dispos_m.bin:bmap09_z02_1_m`: F1: PID_DAYNE_SOL
- `bmap09/dispos_m.bin:bmap09_z02_m`: F1: PID_DAYNE_SOL
- `bmap09/dispos_m.bin:bmap09_z03_2_m`: F1: PID_DAYNE_SOL
- `bmap09/dispos_m.bin:bmap09_z03_m`: F1: PID_DAYNE_SKN
- `bmap09/dispos_m.bin:bmap09_z04_m`: F1: PID_DAYNE_SOL, PID_ZAKO
- `bmap09/dispos_m.bin:bmap09_z05_m`: F1: PID_DAYNE_MAG
- `bmap09/dispos_n.bin:bmap09_elaice_n`: F1: PID_ELAICE
- `bmap09/dispos_n.bin:bmap09_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_KAMURA, PID_ZAKO
- `bmap09/dispos_n.bin:bmap09_mikata_n`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap09/dispos_n.bin:bmap09_z01_1_n`: F1: PID_DAYNE_ARM
- `bmap09/dispos_n.bin:bmap09_z01_n`: F1: PID_DAYNE_SOL
- `bmap09/dispos_n.bin:bmap09_z02_1_n`: F1: PID_DAYNE_SOL
- `bmap09/dispos_n.bin:bmap09_z02_n`: F1: PID_DAYNE_SOL
- `bmap09/dispos_n.bin:bmap09_z03_2_n`: F1: PID_DAYNE_SOL
- `bmap09/dispos_n.bin:bmap09_z03_n`: F1: PID_DAYNE_SKN
- `bmap09/dispos_n.bin:bmap09_z04_n`: F1: PID_DAYNE_SOL, PID_ZAKO
- `bmap09/dispos_n.bin:bmap09_z05_n`: F1: PID_DAYNE_MAG
- `bmap09_2/dispos_c.bin:bmap09_2_event1_c`: F1: PID_BLACKKNIGHT_EV1; F2: PID_GREIL_EV, PID_IKE_EV1
- `bmap09_3/dispos_c.bin:bmap09_3_event1_c`: F2: PID_GREIL_EV, PID_IKE_EV
- `bmap09_3/dispos_c.bin:bmap09_3_event_greil_c`: F2: PID_GREIL_EV
- `bmap09_3/dispos_c.bin:bmap09_3_event_ike_c`: F2: PID_IKE_EV
- `bmap09_3/dispos_c.bin:bmap09_3_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap09_3/dispos_c.bin:bmap09_3_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap09_3/dispos_c.bin:bmap09_3_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap09_3/dispos_c.bin:bmap09_3_event_youheidan_c`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_KILROY, PID_OSCAR, PID_WAYU
- `bmap09_4/dispos_c.bin:bmap09_4_event01_c`: F0: PID_BOLE, PID_ELAICE, PID_KILROY, PID_OSCAR; F2: PID_IKE_EV, PID_LETHE, PID_LOFA_EV, PID_MIST_EV, PID_MORDY, PID_TIAMAT_EV
- `bmap09_4/dispos_c.bin:bmap09_4_event01_wayu_c`: F0: PID_WAYU
- `bmap09_4/dispos_c.bin:bmap09_4_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap09_4/dispos_c.bin:bmap09_4_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap09_5/dispos_c.bin:bmap09_5_event00_c`: F2: PID_GREIL_SEPIA_EV, PID_IKE_CHILD_EV

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 14CE | 0 | regist | 情報１フラグ |
| 14D5 | 0 | regist | 情報２フラグ |
| 14DC | 0 | regist | 情報３フラグ |
| 14E3 | 0 | regist | 情報４フラグ |
| 14EA | 0 | regist | 情報５フラグ |
| 151F | 1 | TalkEvent | MS_09_INFO_01 |
| 1572 | 2 | TalkEvent | MS_09_INFO_02 |
| 157F | 2 | TalkEvent | MS_09_INFO_02_1 |
| 158C | 2 | TalkEvent | MS_09_INFO_02_2 |
| 15EC | 3 | TalkEvent | MS_09_INFO_03 |
| 1656 | 4 | TalkEvent | MS_09_INFO_04 |
| 16BE | 5 | TalkEvent | MS_09_INFO_05 |
| 1703 | 6 | regist | F12111211 |
| 1787 | 9 | regist | イレース仲間 |
| 178F | 9 | regist | イレース戦闘会話 |
| 1797 | 9 | regist | ボス戦闘会話 |
| 179F | 9 | regist | ボス戦闘会話アイク |
| 17A7 | 9 | regist | ボス死亡 |
| 17E3 | 10 | InstantDisposRank | bmap09_first |
| 17EB | 10 | InstantDisposRank | bmap09_elaice |
| 17F4 | 10 | ForceGetCount | 1 |
| 17FD | 10 | ForceGetFirst | 1 |
| 1877 | 11 | SallySetByGroup | bmap09_mikata_c |
| 18AF | 12 | ForceGetCount | 5 |
| 18DB | 12 | MapLoad | bmap09 |
| 18E9 | 12 | InstantDisposSetMode | bmap09_mikata_n, bmap09_mikata_h, bmap09_mikata_m |
| 18EE | 12 | AllUnitEscape |  |
| 1902 | 12 | MapLoad | bmap08 |
| 190A | 12 | InstantDispos | bmap08_m01_c |
| 190F | 12 | AllUnitEscape |  |
| 1949 | 12 | MapLoad | bmap09_5 |
| 1978 | 12 | InstantDispos | bmap09_5_event00_c |
| 1A3A | 12 | TalkEvent | MS_09_OP_01 |
| 1A66 | 12 | TalkEvent | MS_09_OP_02 |
| 1ABA | 12 | TalkEvent | MS_09_OP_03 |
| 1B24 | 12 | AllUnitEscape |  |
| 1BB6 | 12 | TalkEvent | MS_09_OP_05 |
| 1BC6 | 12 | TalkEvent | MS_09_OP_05_2 |
| 1BF6 | 12 | TalkEvent | MS_09_OP_05_3 |
| 1C50 | 12 | ChapterMoviePlay | 9 |
| 1CBD | 12 | TalkEvent | MS_09_OP_06_01_A |
| 1CC8 | 12 | TalkEvent | MS_09_OP_06_01_B |
| 1CF1 | 12 | TalkEvent | MS_09_OP_06_02_A |
| 1D01 | 12 | TalkEvent | MS_09_OP_06_02_A_1 |
| 1D11 | 12 | TalkEvent | MS_09_OP_06_02_A_2 |
| 1D1C | 12 | TalkEvent | MS_09_OP_06_02_3 |
| 1D36 | 12 | TalkEvent | MS_09_OP_06_02_B |
| 1D46 | 12 | TalkEvent | MS_09_OP_06_02_B_1 |
| 1D56 | 12 | TalkEvent | MS_09_OP_06_02_B_2 |
| 1D61 | 12 | TalkEvent | MS_09_OP_06_02_B_3 |
| 1D7B | 12 | TalkEvent | MS_09_OP_06_02_C |
| 1D8B | 12 | TalkEvent | MS_09_OP_06_02_C_1 |
| 1D9B | 12 | TalkEvent | MS_09_OP_06_02_C_2 |
| 1DA6 | 12 | TalkEvent | MS_09_OP_06_02_C_3 |
| 1DBB | 12 | TalkEvent | MS_09_OP_06_02_D |
| 1DCB | 12 | TalkEvent | MS_09_OP_06_02_D_1 |
| 1DDB | 12 | TalkEvent | MS_09_OP_06_02_D_2 |
| 1DEB | 12 | TalkEvent | MS_09_OP_06_02_D_3 |
| 1DF6 | 12 | TalkEvent | MS_09_OP_06_02_D_4 |
| 1E1F | 12 | TalkResume |  |
| 1E38 | 12 | TalkResume |  |
| 1E45 | 12 | TalkEvent | MS_09_OP_06_03_x |
| 1E4D | 12 | TalkEvent | MS_09_OP_06_03 |
| 1E6C | 12 | TalkEvent | MS_09_OP_06_BASE |
| 1ECF | 12 | UnitTransferToForceByPID | PID_CHINON, 7 |
| 1ED9 | 12 | UnitTransferToForceByPID | PID_GATRIE, 7 |
| 1F17 | 13 | MapLoad | bmap09 |
| 1F48 | 13 | InstantDisposFirstSetMode | bmap09_first_n, bmap09_first_h, bmap09_first_m |
| 1F61 | 13 | UnitEscape | ?, 0 |
| 1F71 | 13 | ForceGetCount | 1 |
| 1F7A | 13 | ForceGetFirst | 1 |
| 200C | 13 | TalkEvent | MS_09_OP_06_04X |
| 2084 | 13 | AllUnitEscape |  |
| 20D9 | 13 | TalkEvent | MS_09_OP_06_04A |
| 20F4 | 13 | TalkEvent | MS_09_OP_06_04B |
| 210F | 13 | TalkEvent | MS_09_OP_06_04C |
| 212B | 13 | TalkEvent | MS_09_OP_06_04D |
| 2146 | 13 | TalkEvent | MS_09_OP_06_04E |
| 2162 | 13 | TalkEvent | MS_09_OP_06_04F |
| 217E | 13 | TalkEvent | MS_09_OP_06_04G |
| 219B | 13 | TalkEvent | MS_09_OP_06_04H |
| 21A3 | 13 | TalkEvent | MS_09_OP_06_05 |
| 21C7 | 13 | TalkResume |  |
| 223F | 13 | MapLoad | bmap09 |
| 2262 | 13 | TalkEvent | MS_09_OP_06_05_2 |
| 22AC | 13 | SallySetByGroup | bmap09_mikata_c |
| 22B4 | 13 | InstantDispos | bmap09_mikata_c |
| 25D8 | 13 | TalkEvent | MS_09_OP_07 |
| 2628 | 13 | UnitForcedSallyByPID | PID_IKE |
| 2630 | 13 | UnitDontMoveSallyByPID | PID_IKE |
| 272B | 15 | TalkEvent | MS_09_EV_02 |
| 2740 | 15 | ForceGetCount | 1 |
| 2749 | 15 | ForceGetFirst | 1 |
| 27D9 | 16 | DisposSetMode | bmap09_z01_n, bmap09_z01_h, bmap09_z01_m |
| 27E7 | 16 | DisposSetMode | bmap09_z01_1_n, bmap09_z01_1_h, bmap09_z01_1_m |
| 2832 | 17 | DisposSetMode | bmap09_z02_n, bmap09_z02_h, bmap09_z02_m |
| 2840 | 17 | DisposSetMode | bmap09_z02_1_n, bmap09_z02_1_h, bmap09_z02_1_m |
| 2871 | 18 | DisposSetMode | bmap09_z03_n, bmap09_z03_h, bmap09_z03_m |
| 2880 | 18 | Dispos | bmap09_z03_2_n |
| 28B1 | 19 | DisposSetMode | bmap09_z04_n, bmap09_z04_h, bmap09_z04_m |
| 28E1 | 20 | DisposSetMode | bmap09_z05_n, bmap09_z05_h, bmap09_z05_m |
| 2961 | 21 | TalkEvent | MS_09_TK_ELAICE |
| 296B | 21 | UnitTransferToForceByPID | PID_ELAICE, 0 |
| 29C9 | 22 | BMGetPhase |  |
| 29D6 | 22 | SoundBossTalkStart | BGM_BTL_PL01 |
| 29E1 | 22 | SoundBossTalkStart | BGM_BTL_CP01 |
| 29E9 | 22 | TalkEvent | MS_09_BT_ELAICE |
| 29F6 | 22 | SoundBossTalkEnd |  |
| 2A2B | 23 | DefaultDieTalk |  |
| 2A36 | 23 | TalkEvent | MS_09_DIE_ELAICE |
| 2A68 | 24 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2A70 | 24 | TalkEvent | MS_09_BT_IKE |
| 2A7D | 24 | SoundBossTalkEnd |  |
| 2AB2 | 25 | BMGetPhase |  |
| 2AE2 | 25 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2AEA | 25 | TalkEvent | MS_09_BT |
| 2AF7 | 25 | SoundBossTalkEnd |  |
| 2B28 | 26 | TalkEvent | MS_09_DIE |
| 2B8C | 28 | UnitDead | ? |
| 2BAF | 29 | InstantDispos | bmap09_event01_c |
| 2BB7 | 29 | InstantDispos | bmap09_enemy_common_c |
| 2BBF | 29 | InstantDispos | bmap09_event_tiamat_c |
| 2BCC | 29 | Dispos_ForEventSenerio | bmap09_event_senerio_c, bmap09_event_senerio2_c, 1 |
| 2BED | 29 | ForceGetFirst | 1 |
| 2BF6 | 29 | ForceGetCount | 1 |
| 2CF0 | 29 | UnitEscapeByPID | PID_KAMURA |
| 2CF8 | 29 | InstantDispos | bmap09_event_boss_c |
| 2DB3 | 30 | TalkEvent | MS_09_ED_01_00 |
| 2E03 | 31 | AllUnitEscape |  |
| 2E2C | 31 | InstantDispos | bmap09_event_mist_c |
| 2E34 | 31 | UnitEscapeByPID | PID_MIST_EV |
| 2EF3 | 31 | TalkEvent | MS_09_ED_01_00_1 |
| 3029 | 31 | Dispos | bmap09_event_mist_c |
| 3052 | 31 | TalkEvent | MS_09_ED_01_00_2 |
| 30AB | 31 | UnitEscapeByPID | PID_DAYNE_SOL_1 |
| 30B3 | 31 | UnitEscapeByPID | PID_DAYNE_SOL_2 |
| 30BB | 31 | UnitEscapeByPID | PID_DAYNE_SOL_5 |
| 30C3 | 31 | UnitEscapeByPID | PID_DAYNE_SOL_9 |
| 30CB | 31 | UnitEscapeByPID | PID_DAYNE_SKN_4 |
| 3125 | 31 | TalkEvent | MS_09_ED_01_00_2_2 |
| 3130 | 31 | TalkEvent | MS_09_ED_01_00_2_2_B |
| 31E5 | 31 | TalkEvent | MS_09_ED_01_00_3 |
| 31F0 | 31 | TalkEvent | MS_09_ED_01_00_3_B |
| 3215 | 31 | UnitEscapeByPID | PID_DAYNE_SOL_1 |
| 321D | 31 | UnitEscapeByPID | PID_DAYNE_SOL_2 |
| 3225 | 31 | UnitEscapeByPID | PID_DAYNE_SOL_5 |
| 322D | 31 | UnitEscapeByPID | PID_DAYNE_SOL_9 |
| 3235 | 31 | UnitEscapeByPID | PID_DAYNE_SKN_4 |
| 3266 | 31 | ForceGetCount | 1 |
| 3270 | 31 | ForceGetFirst | 1 |
| 32B8 | 31 | UnitEscape | ?, 0 |
| 32DE | 31 | InstantDispos | bmap09_event_gria_c |
| 33BF | 31 | TalkEvent | MS_09_ED_01_00_4 |
| 33CA | 31 | TalkEvent | MS_09_ED_01_00_4_B |
| 356C | 31 | TalkEvent | MS_09_ED_01_00_5 |
| 3577 | 31 | TalkEvent | MS_09_ED_01_00_5_B |
| 3672 | 31 | TalkEvent | MS_09_ED_01_00_6 |
| 367D | 31 | TalkEvent | MS_09_ED_01_00_6_B |
| 36AE | 31 | UnitDead | ? |
| 36BC | 31 | UnitEscape | ?, 0 |
| 374A | 31 | AllUnitEscape |  |
| 379A | 32 | MapLoad | bmap09_4 |
| 37B1 | 32 | InstantDispos | bmap09_4_event01_c |
| 37C3 | 32 | InstantDispos | bmap09_4_event01_wayu_c |
| 37D0 | 32 | Dispos_ForEventSenerio | bmap09_4_event_senerio_c, bmap09_4_event_senerio2_c, 1 |
| 37DD | 32 | UnitEscapeByPID | PID_ELAICE |
| 380E | 32 | TalkEvent | MS_09_ED_02_new |
| 381D | 32 | TalkResume |  |
| 3862 | 32 | TalkEvent | MS_09_ED_04 |
| 38FC | 32 | TalkEvent | MS_09_ED_05_02 |
| 395B | 32 | TalkEvent | MS_09_ED_06 |
| 3984 | 32 | TalkEvent | MS_09_ED_06_X |
| 39E8 | 32 | TalkEvent | MS_09_ED_06_XX |
| 3A17 | 32 | AllUnitEscape |  |
| 3A21 | 32 | AllUnitEscape |  |
| 3A3A | 32 | TalkEvent | MS_09_ED_07 |
| 3A53 | 32 | TalkResume |  |
| 3A96 | 33 | Dispos | bmap09_z01_c |
| 3AA5 | 33 | Dispos | bmap09_z02_c |
| 3AB4 | 33 | Dispos | bmap09_z04_c |
| 3AC3 | 33 | Dispos | bmap09_z01_1_c |
| 3B40 | 34 | TalkEvent | MS_09_GAMEOVER |
| 3B6E | 35 | SallyGetSurplus |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.9: Gallia — internal 10

Historical evidence: Ch9 several turns, incl. Netplay NET-01 (native partners Lethe/Mordecai).

Slot-group counts by file suffix: `{'c': 8, 'h': 8, 'm': 8, 'n': 8}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap10/dispos_c.bin:bmap10_event_01_c`: F2: PID_DUMMY1, PID_LOFA_EV, PID_MIST_EV
- `bmap10/dispos_c.bin:bmap10_event_bole_c`: F2: PID_BOLE_EV
- `bmap10/dispos_c.bin:bmap10_event_oscar_c`: F2: PID_OSCAR_EV
- `bmap10/dispos_c.bin:bmap10_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap10/dispos_c.bin:bmap10_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap10/dispos_c.bin:bmap10_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap10/dispos_c.bin:bmap10_m02_c`: F2: PID_MIST
- `bmap10/dispos_c.bin:bmap10_m03_c`: F2: PID_LOFA
- `bmap10/dispos_c.bin:bmap10_m04_c`: F2: PID_MARCIA
- `bmap10/dispos_c.bin:bmap10_m05_c`: F3: PID_LETHE, PID_MORDY
- `bmap10/dispos_c.bin:bmap10_mikata_c`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap10/dispos_h.bin:bmap10_first1_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM
- `bmap10/dispos_h.bin:bmap10_first2_h`: F1: PID_DAYNE_FIG, PID_DAYNE_MAG, PID_DAYNE_SOL, PID_DAYNE_SRD
- `bmap10/dispos_h.bin:bmap10_first3_h`: F1: PID_BANDIT_SEA
- `bmap10/dispos_h.bin:bmap10_first_h`: F1: PID_DAYNE_ARM, PID_DAYNE_MAG, PID_KOTAHU
- `bmap10/dispos_h.bin:bmap10_m01_h`: F3: PID_LETHE, PID_MORDY
- `bmap10/dispos_h.bin:bmap10_mikata_h`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap10/dispos_h.bin:bmap10_z01_h`: F1: PID_BANDIT_SEA, PID_NEDATA
- `bmap10/dispos_h.bin:bmap10_z02_h`: F1: PID_DAYNE_SOL, PID_DAYNE_SRD
- `bmap10/dispos_h.bin:bmap10_z03_h`: F1: PID_BANDIT_SEA
- `bmap10/dispos_m.bin:bmap10_first1_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM
- `bmap10/dispos_m.bin:bmap10_first2_m`: F1: PID_DAYNE_MAG, PID_DAYNE_SOL, PID_ZAKO_2
- `bmap10/dispos_m.bin:bmap10_first3_m`: F1: PID_BANDIT_SEA
- `bmap10/dispos_m.bin:bmap10_first_m`: F1: PID_DAYNE_MAG, PID_KOTAHU
- `bmap10/dispos_m.bin:bmap10_m01_m`: F3: PID_LETHE, PID_MORDY
- `bmap10/dispos_m.bin:bmap10_mikata_m`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap10/dispos_m.bin:bmap10_z01_m`: F1: PID_BANDIT_SEA, PID_NEDATA
- `bmap10/dispos_m.bin:bmap10_z02_m`: F1: PID_DAYNE_SOL, PID_ZAKO_2
- `bmap10/dispos_m.bin:bmap10_z03_m`: F1: PID_BANDIT_SEA
- `bmap10/dispos_n.bin:bmap10_first1_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM
- `bmap10/dispos_n.bin:bmap10_first2_n`: F1: PID_DAYNE_MAG, PID_DAYNE_SOL, PID_ZAKO_2
- `bmap10/dispos_n.bin:bmap10_first3_n`: F1: PID_BANDIT_SEA
- `bmap10/dispos_n.bin:bmap10_first_n`: F1: PID_DAYNE_MAG, PID_KOTAHU
- `bmap10/dispos_n.bin:bmap10_m01_n`: F3: PID_LETHE, PID_MORDY
- `bmap10/dispos_n.bin:bmap10_mikata_n`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap10/dispos_n.bin:bmap10_z01_n`: F1: PID_BANDIT_SEA, PID_NEDATA
- `bmap10/dispos_n.bin:bmap10_z02_n`: F1: PID_DAYNE_SOL, PID_ZAKO_2
- `bmap10/dispos_n.bin:bmap10_z03_n`: F1: PID_BANDIT_SEA

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 1202 | 0 | regist | 情報１フラグ |
| 1209 | 0 | regist | 情報２フラグ |
| 1210 | 0 | regist | 情報３フラグ |
| 1217 | 0 | regist | 情報４フラグ |
| 121E | 0 | regist | 情報５フラグ |
| 1253 | 1 | TalkEvent | MS_10_INFO_01 |
| 1290 | 2 | TalkEvent | MS_10_INFO_02 |
| 12D6 | 3 | TalkEvent | MS_10_INFO_03 |
| 131E | 4 | TalkEvent | MS_10_INFO_04 |
| 135C | 5 | TalkEvent | MS_10_INFO_05 |
| 13C1 | 7 | TalkEvent | MS_10_VIL_02 |
| 1479 | 9 | TalkEvent | MS_10_VIL_01 |
| 1587 | 13 | regist | 訪問１ |
| 158F | 13 | regist | 訪問２ |
| 1617 | 16 | regist | 増援Ｚ０２ |
| 161F | 16 | regist | 増援Ｚ０２終 |
| 1627 | 16 | regist | 増援Ｚ０３ |
| 162F | 16 | regist | 増援Ｚ０３終 |
| 1637 | 16 | regist | ノーマル：増援トリガ２ |
| 163F | 16 | regist | ノーマル：増援トリガ３ |
| 1647 | 16 | regist | ノーマル：増援イベント２ |
| 164F | 16 | regist | ノーマル：増援イベント３ |
| 1657 | 16 | regist | MS_10_OP02_02Aを見た |
| 165F | 16 | regist | 村訪問ｏｒ破壊１ |
| 1667 | 16 | regist | 村訪問ｏｒ破壊２ |
| 166F | 16 | regist | 蛮族ＣＰ変更 |
| 1677 | 16 | regist | マーシャ仲間 |
| 167F | 16 | regist | ヨファボーレ |
| 1687 | 16 | regist | ヨファオスカー |
| 168F | 16 | regist | ネダタ戦闘 |
| 1697 | 16 | regist | ネダタ戦闘アイク |
| 169F | 16 | regist | ネダタ戦闘レテ |
| 16A7 | 16 | regist | ネダタ戦闘モゥディ |
| 16AF | 16 | regist | ボス戦闘会話 |
| 16B7 | 16 | regist | ボス戦闘会話アイク |
| 16BF | 16 | regist | ボス戦闘会話レテ |
| 16C7 | 16 | regist | ボス戦闘会話モゥディ |
| 16CF | 16 | regist | ボス死亡 |
| 1712 | 17 | InstantDisposRank | bmap10_first |
| 171A | 17 | InstantDisposRank | bmap10_first1 |
| 1722 | 17 | InstantDisposRank | bmap10_first2 |
| 172A | 17 | InstantDisposRank | bmap10_first3 |
| 1732 | 17 | InstantDispos | bmap10_m05_c |
| 1773 | 18 | SallySetByGroup | bmap10_mikata_c |
| 17AB | 19 | ForceGetCount | 5 |
| 17D7 | 19 | MapLoad | bmap10 |
| 17E5 | 19 | InstantDisposSetMode | bmap10_mikata_n, bmap10_mikata_h, bmap10_mikata_m |
| 17EA | 19 | AllUnitEscape |  |
| 1830 | 19 | ChapterMoviePlay | 10 |
| 18AB | 20 | MapLoad | bmap10 |
| 18D6 | 20 | InstantDisposRank | bmap10_first |
| 18DE | 20 | InstantDisposRank | bmap10_first1 |
| 18E6 | 20 | InstantDisposRank | bmap10_first2 |
| 18EE | 20 | SallySetByGroup | bmap10_mikata_c |
| 18F6 | 20 | InstantDispos | bmap10_mikata_c |
| 18FB | 20 | AllUnitEscape |  |
| 190A | 20 | InstantDisposFirst | bmap10_mikata_c |
| 1912 | 20 | InstantDisposFirst | bmap10_event_01_c |
| 1927 | 20 | Dispos_ForEventTiamat | bmap10_event_tiamat_c, 1 |
| 193F | 20 | Dispos_ForEventSenerio | bmap10_event_senerio_c, bmap10_event_senerio2_c, 1 |
| 1947 | 20 | InstantDispos | bmap10_m05_c |
| 1A67 | 20 | TalkEvent | MS_10_OP01 |
| 1A76 | 20 | TalkResume |  |
| 1ABE | 20 | TalkEvent | MS_10_OP01_2 |
| 1B2D | 20 | TalkEvent | MS_10_OP01_2_2 |
| 1BDE | 20 | TalkEvent | MS_10_OP01_3 |
| 1BED | 20 | TalkResume |  |
| 1C6E | 20 | DisposSetMode | bmap10_first1_n, bmap10_first1_h, bmap10_first1_m |
| 1C8F | 20 | DisposSetMode | bmap10_first_n, bmap10_first_h, bmap10_first_m |
| 1D22 | 20 | TalkEvent | MS_10_OP01_3x |
| 1DA3 | 20 | DisposAsynchronous | bmap10_first2_n |
| 1DAB | 20 | DisposAsynchronous | bmap10_first3_n |
| 1DBD | 20 | DisposAsynchronous | bmap10_first2_h |
| 1DC5 | 20 | DisposAsynchronous | bmap10_first3_h |
| 1DD0 | 20 | DisposAsynchronous | bmap10_first2_m |
| 1DD8 | 20 | DisposAsynchronous | bmap10_first3_m |
| 1EB0 | 20 | TalkEvent | MS_10_OP01_4A |
| 1F8A | 20 | UnitEscapeByPID | PID_TIAMAT_EV |
| 1F92 | 20 | UnitEscapeByPID | PID_SENERIO_EV |
| 1F9A | 20 | UnitEscapeByPID | PID_MIST_EV |
| 1FA2 | 20 | UnitEscapeByPID | PID_LOFA_EV |
| 1FAA | 20 | UnitEscapeByPID | PID_DUMMY1 |
| 1FFB | 20 | UnitForcedSallyByPID | PID_IKE |
| 2003 | 20 | UnitDontMoveSallyByPID | PID_IKE |
| 20A0 | 21 | Dispos | bmap10_m02_c |
| 20CB | 21 | TalkEvent | MS_10_OP02_01_A |
| 20D6 | 21 | TalkEvent | MS_10_OP02_01_B |
| 2117 | 21 | Dispos | bmap10_m03_c |
| 2177 | 21 | TalkEvent | MS_10_OP02_02A |
| 21A1 | 21 | Dispos | bmap10_event_bole_c |
| 21C7 | 21 | TalkEvent | MS_10_OP02_02A |
| 2205 | 21 | TalkEvent | MS_10_OP02_02B |
| 2227 | 21 | Dispos | bmap10_event_oscar_c |
| 224D | 21 | TalkEvent | MS_10_OP02_02B |
| 2287 | 21 | TalkEvent | MS_10_OP02_02C |
| 2291 | 21 | UnitTransferToForceByPID | PID_MIST, 0 |
| 229B | 21 | UnitTransferToForceByPID | PID_LOFA, 0 |
| 22C8 | 21 | UnitEscapeByPID | PID_BOLE_EV |
| 22F5 | 21 | UnitEscapeByPID | PID_OSCAR_EV |
| 2417 | 22 | TalkEvent | MS_10_EV_yellow |
| 24C1 | 23 | Dispos | bmap10_m04_c |
| 2511 | 23 | TalkEvent | MS_10_EV01 |
| 2575 | 24 | DisposSetMode | bmap10_z02_n, bmap10_z02_h, bmap10_z02_m |
| 25D1 | 25 | DisposSetMode | bmap10_z03_n, bmap10_z03_h, bmap10_z03_m |
| 2659 | 26 | DisposSetMode | bmap10_z01_n, bmap10_z01_h, bmap10_z01_m |
| 2752 | 26 | TalkEvent | MS_10_EV02 |
| 286B | 27 | ForceGetCount | 1 |
| 2875 | 27 | ForceGetFirst | 1 |
| 2938 | 28 | TalkEvent | MS_10_TK01 |
| 2942 | 28 | UnitTransferToForceByPID | PID_MARCIA, 0 |
| 299E | 29 | TalkEvent | MS_10_TK02 |
| 29E8 | 30 | TalkEvent | MS_10_TK03_A |
| 29F3 | 30 | TalkEvent | MS_10_TK03_B |
| 2A2A | 31 | LocalDieTalkWithBgmChange | マーシャ仲間, MS_10_DIE_MARCIA |
| 2A52 | 32 | LocalDieTalkWithBgmChange | , MS_10_DIE_LETE |
| 2A82 | 33 | LocalDieTalkWithBgmChange | , MS_10_DIE_MORDY |
| 2AB5 | 34 | BMGetPhase |  |
| 2AC2 | 34 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2ACD | 34 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2AD5 | 34 | TalkEvent | MS_10_01_BT_IKE |
| 2AE2 | 34 | SoundBossTalkEnd |  |
| 2B11 | 35 | BMGetPhase |  |
| 2B1E | 35 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2B29 | 35 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2B31 | 35 | TalkEvent | MS_10_01_BT_LE |
| 2B3E | 35 | SoundBossTalkEnd |  |
| 2B6D | 36 | BMGetPhase |  |
| 2B7A | 36 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2B85 | 36 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2B8D | 36 | TalkEvent | MS_10_01_BT_MO |
| 2B9A | 36 | SoundBossTalkEnd |  |
| 2BE2 | 37 | BMGetPhase |  |
| 2C1F | 37 | BMGetPhase |  |
| 2C2C | 37 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2C37 | 37 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2C3F | 37 | TalkEvent | MS_10_01_BT |
| 2C4C | 37 | SoundBossTalkEnd |  |
| 2C7C | 38 | TalkEvent | MS_10_01_DIE |
| 2CB8 | 39 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2CC0 | 39 | TalkEvent | MS_10_BT_IKE |
| 2CCD | 39 | SoundBossTalkEnd |  |
| 2D00 | 40 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D08 | 40 | TalkEvent | MS_10_BT_LE |
| 2D15 | 40 | SoundBossTalkEnd |  |
| 2D48 | 41 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D50 | 41 | TalkEvent | MS_10_BT_MO |
| 2D5D | 41 | SoundBossTalkEnd |  |
| 2DA6 | 42 | BMGetPhase |  |
| 2DE6 | 42 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2DEE | 42 | TalkEvent | MS_10_BT |
| 2DFB | 42 | SoundBossTalkEnd |  |
| 2E2C | 43 | TalkEvent | MS_10_DIE |
| 2E87 | 44 | AllUnitEscape |  |
| 2EA6 | 44 | TalkEvent | MS_10_ED00 |
| 2F85 | 44 | TalkEvent | MS_10_ED01 |
| 2F9E | 44 | TalkResume |  |
| 2FBF | 44 | TalkResume |  |
| 303A | 46 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.10: Prisoner Release — internal 11

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 8, 'h': 11, 'm': 11, 'n': 11}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap11/dispos_c.bin:bmap11_event1_c`: F2: PID_LAY
- `bmap11/dispos_c.bin:bmap11_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap11/dispos_c.bin:bmap11_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap11/dispos_c.bin:bmap11_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap11/dispos_c.bin:bmap11_first_c`: F2: PID_CEPHERAN_FAKE, PID_CHAP, PID_KEVIN, PID_NEPENEE
- `bmap11/dispos_c.bin:bmap11_m02_c`: F2: PID_VOKE
- `bmap11/dispos_c.bin:bmap11_mikata_c`: F0: PID_IKE, PID_KILROY, PID_LOFA, PID_MARCIA, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap11/dispos_h.bin:bmap11_first_h`: F1: PID_DANOMIRU, PID_DAYNE_ARC, PID_D_ZAKO_11_1, PID_D_ZAKO_11_2, PID_D_ZAKO_11_3
- `bmap11/dispos_h.bin:bmap11_mikata_h`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_LOFA, PID_MARCIA, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap11/dispos_h.bin:bmap11_zoen1_h`: F1: PID_DAYNE_ARM, PID_DAYNE_HAL, PID_DAYNE_SOL
- `bmap11/dispos_h.bin:bmap11_zoen2_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_SOL, PID_DAYNE_SRD
- `bmap11/dispos_h.bin:bmap11_zoen3_h`: F1: PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_SOL
- `bmap11/dispos_m.bin:bmap11_first_m`: F1: PID_DANOMIRU, PID_D_ZAKO_11_1, PID_D_ZAKO_11_2, PID_D_ZAKO_11_3, PID_ZAKO
- `bmap11/dispos_m.bin:bmap11_mikata_m`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_LOFA, PID_MARCIA, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap11/dispos_m.bin:bmap11_zoen1_m`: F1: PID_DAYNE_ARM, PID_DAYNE_HAL, PID_DAYNE_SOL
- `bmap11/dispos_m.bin:bmap11_zoen2_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_ZAKO
- `bmap11/dispos_m.bin:bmap11_zoen3_m`: F1: PID_DAYNE_ARM, PID_DAYNE_MAG
- `bmap11/dispos_n.bin:bmap11_first_n`: F1: PID_DANOMIRU, PID_D_ZAKO_11_1, PID_D_ZAKO_11_2, PID_D_ZAKO_11_3, PID_ZAKO
- `bmap11/dispos_n.bin:bmap11_mikata_n`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_LOFA, PID_MARCIA, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap11/dispos_n.bin:bmap11_zoen1_n`: F1: PID_DAYNE_ARM, PID_DAYNE_HAL, PID_DAYNE_SOL
- `bmap11/dispos_n.bin:bmap11_zoen2_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_ZAKO
- `bmap11/dispos_n.bin:bmap11_zoen3_n`: F1: PID_DAYNE_ARM, PID_DAYNE_MAG

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 13EE | 0 | regist | 情報１フラグ |
| 13F5 | 0 | regist | 情報２フラグ |
| 13FC | 0 | regist | 情報３フラグ |
| 1403 | 0 | regist | 情報４フラグ |
| 140A | 0 | regist | 情報５フラグ |
| 143F | 1 | TalkEvent | MS_11_INFO_01 |
| 1486 | 2 | TalkEvent | MS_11_INFO_03 |
| 14CE | 3 | TalkEvent | MS_11_INFO_04 |
| 1590 | 5 | TalkEvent | MESC_IKE |
| 1598 | 5 | DefaultEscapeTalk |  |
| 15D8 | 5 | UnitTransferToForceByPID | PID_KEVIN, 0 |
| 15FA | 5 | UnitTransferToForceByPID | PID_CHAP, 0 |
| 161C | 5 | UnitTransferToForceByPID | PID_NEPENEE, 0 |
| 1625 | 5 | UnitEscape | ?, 0 |
| 19A3 | 18 | regist | 宝箱１ |
| 19AB | 18 | regist | 宝箱２ |
| 19B3 | 18 | regist | 宝箱３ |
| 19BB | 18 | regist | 宝箱４ |
| 19C3 | 18 | regist | 宝箱５ |
| 19CB | 18 | regist | F0814 |
| 19D3 | 18 | regist | F1107 |
| 19DB | 18 | regist | F1914 |
| 19E3 | 18 | regist | F1905 |
| 19EB | 18 | regist | F02022109 |
| 1A6B | 20 | regist | アイクセフェラン |
| 1A73 | 20 | regist | オスカーケビン |
| 1A7B | 20 | regist | アイクネフェニー |
| 1A83 | 20 | regist | アイクチャップ |
| 1A8B | 20 | regist | 扉チャップケヴィン |
| 1A93 | 20 | regist | 扉ネフェニー |
| 1A9B | 20 | regist | 扉セフェラン |
| 1AA3 | 20 | regist | 扉宝箱 |
| 1AAB | 20 | regist | フォルカ仲間C11 |
| 1AB3 | 20 | regist | 発見イベントトリガ |
| 1ABB | 20 | regist | 敵死亡で増援イベント発動 |
| 1AC3 | 20 | regist | 門番発見イベント |
| 1ACB | 20 | regist | ボス戦闘会話 |
| 1AD3 | 20 | regist | ボス戦闘会話アイク |
| 1ADB | 20 | regist | ボス戦闘会話レテ |
| 1AE3 | 20 | regist | ボス戦闘会話モゥディ |
| 1AEB | 20 | regist | マニア：増援イベント |
| 1AF3 | 20 | regist | ケヴィン離脱 |
| 1AFB | 20 | regist | チャップ離脱 |
| 1B03 | 20 | regist | ネフェニー離脱 |
| 1B0B | 20 | regist | ボス死亡 |
| 1B4E | 21 | InstantDisposRank | bmap11_first |
| 1B56 | 21 | InstantDispos | bmap11_first_c |
| 1B66 | 21 | ForceGetCount | 1 |
| 1B6F | 21 | ForceGetFirst | 1 |
| 1C47 | 22 | SallySetByGroup | bmap11_mikata_c |
| 1C59 | 22 | SallyAddByGroup | bmap11_m02_c |
| 1C93 | 23 | ForceGetCount | 5 |
| 1CBF | 23 | MapLoad | bmap11 |
| 1CCD | 23 | InstantDisposSetMode | bmap11_mikata_n, bmap11_mikata_h, bmap11_mikata_m |
| 1CD2 | 23 | AllUnitEscape |  |
| 1D18 | 23 | ChapterMoviePlay | 11 |
| 1D5A | 23 | TalkEvent | MS_11_OP01 |
| 1D76 | 23 | TalkResume |  |
| 1DC6 | 23 | TalkResume |  |
| 1E49 | 23 | TalkEvent | MS_11_OP01_A |
| 1E5F | 23 | TalkEvent | MS_11_OP01_B |
| 1E75 | 23 | TalkEvent | MS_11_OP01_C |
| 1EA7 | 23 | Join | always_lete |
| 1EBA | 23 | Join | always_mordy |
| 206E | 24 | TalkEvent | MS_11_GMAP_1 |
| 2135 | 24 | TalkEvent | MS_11_GMAP_2 |
| 226F | 24 | TalkEvent | MS_11_GMAP_4 |
| 22A0 | 24 | TalkResume |  |
| 232D | 25 | TalkEvent | MS_11_OP02_00 |
| 235C | 25 | MapLoad | bmap11 |
| 2390 | 25 | SallySetByGroup | bmap11_mikata_c |
| 2398 | 25 | InstantDispos | bmap11_mikata_c |
| 23A0 | 25 | InstantDispos | bmap11_event1_c |
| 23A8 | 25 | InstantDispos | bmap11_m02_c |
| 23AD | 25 | AllUnitEscape |  |
| 2484 | 25 | InstantDispos | bmap11_event1_c |
| 24B9 | 25 | Dispos | bmap11_mikata_c |
| 24E1 | 25 | Dispos_ForEventTiamat | bmap11_event_tiamat_c, 0 |
| 2507 | 25 | Dispos_ForEventSenerio | bmap11_event_senerio_c, bmap11_event_senerio2_c, 0 |
| 2561 | 25 | TalkEvent | MS_11_OP02_01 |
| 2569 | 25 | InstantDispos | bmap11_m02_c |
| 264D | 25 | TalkEvent | MS_11_OP02_02 |
| 2665 | 25 | TalkEvent | MS_11_OP02_02_DEL |
| 2698 | 25 | TalkEvent | MS_11_OP02_02_SKIP |
| 26D5 | 25 | UnitTransferToForceByPID | PID_VOKE, 0 |
| 26DD | 25 | SallyAddByGroup | bmap11_m02_c |
| 26F6 | 25 | TalkEvent | MS_11_OP02_02A |
| 272D | 25 | TalkEvent | MS_11_OP02_02B |
| 2761 | 25 | UnitEscapeByPID | PID_VOKE |
| 276C | 25 | TalkEvent | MS_11_OP02_02C |
| 27CC | 25 | TalkEvent | MS_11_OP04 |
| 27EE | 25 | UnitEscapeByPID | PID_LAY |
| 2878 | 25 | TalkEvent | MS_11_OP05_SEN_TMT |
| 2883 | 25 | TalkEvent | MS_11_OP05_TMT |
| 2899 | 25 | TalkEvent | MS_11_OP05_SEN |
| 28F5 | 25 | UnitEscapeByPID | PID_TIAMAT_EV |
| 28FD | 25 | UnitEscapeByPID | PID_SENERIO_EV |
| 297B | 25 | UnitForcedSallyByPID | PID_IKE |
| 2983 | 25 | UnitDontMoveSallyByPID | PID_IKE |
| 2AA0 | 27 | TalkEvent | MS_11_EV01 |
| 2B20 | 27 | TalkEvent | MS_11_EV01_KE_CH |
| 2BB4 | 27 | TalkEvent | MS_11_EV01_NE |
| 2C0A | 28 | TalkEvent | MS_11_TK01 |
| 2C4A | 29 | TalkEvent | MS_11_TK02 |
| 2C5B | 29 | UnitTransferToForceByPID | PID_KEVIN, 3 |
| 2C92 | 30 | TalkEvent | MS_11_TK03 |
| 2CA3 | 30 | UnitTransferToForceByPID | PID_NEPENEE, 3 |
| 2CDA | 31 | TalkEvent | MS_11_TK04 |
| 2CEB | 31 | UnitTransferToForceByPID | PID_CHAP, 3 |
| 2D72 | 32 | TalkEvent | MS_11_EV02_02_01 |
| 2D99 | 32 | DisposSetMode | bmap11_zoen1_n, bmap11_zoen1_h, bmap11_zoen1_m |
| 2DB3 | 32 | DisposSetMode | bmap11_zoen2_n, bmap11_zoen2_h, bmap11_zoen2_m |
| 2DCD | 32 | DisposSetMode | bmap11_zoen3_n, bmap11_zoen3_h, bmap11_zoen3_m |
| 2E38 | 32 | TalkEvent | MS_11_EV02_03 |
| 2E86 | 33 | TalkEvent | MS_11_EV02_01 |
| 2EBE | 34 | TalkEvent | MS_11_EV02_02 |
| 2FA8 | 38 | BMGetPhase |  |
| 2FF4 | 38 | UnitGetForce | ? |
| 309E | 39 | BMGetPhase |  |
| 30CE | 40 | LocalDieTalkWithBgmChange | , MS_11_DIE_SEFELAN |
| 30F6 | 41 | LocalDieTalkWithBgmChange | , MS_11_DIE_CHAP |
| 311E | 42 | LocalDieTalkWithBgmChange | , MS_11_DIE_KEVIN |
| 3146 | 43 | LocalDieTalkWithBgmChange | , MS_11_DIE_NEPHENEE |
| 3174 | 44 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 317C | 44 | TalkEvent | MS_11_BT_IKE |
| 3189 | 44 | SoundBossTalkEnd |  |
| 31BC | 45 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 31C4 | 45 | TalkEvent | MS_11_BT_LE |
| 31D1 | 45 | SoundBossTalkEnd |  |
| 3204 | 46 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 320C | 46 | TalkEvent | MS_11_BT_MO |
| 3219 | 46 | SoundBossTalkEnd |  |
| 3262 | 47 | BMGetPhase |  |
| 32A2 | 47 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 32AA | 47 | TalkEvent | MS_11_BT |
| 32B7 | 47 | SoundBossTalkEnd |  |
| 32E8 | 48 | TalkEvent | MS_11_DIE |
| 3494 | 57 | UnitTransferToForce | ?, 0 |
| 34B8 | 57 | UnitTransferToForce | ?, 0 |
| 34E6 | 57 | UnitTransferToForce | ?, 0 |
| 34EB | 57 | AllUnitEscape |  |
| 3530 | 57 | TalkEvent | MS_11_ED01_A |
| 3549 | 57 | TalkResume |  |
| 3590 | 57 | TalkEvent | MS_11_ED03_KCN |
| 35B0 | 57 | TalkEvent | MS_11_ED03_KC- |
| 35D0 | 57 | TalkEvent | MS_11_ED03_K-N |
| 35F0 | 57 | TalkEvent | MS_11_ED03_-CN |
| 3611 | 57 | TalkEvent | MS_11_ED03_-C- |
| 3632 | 57 | TalkEvent | MS_11_ED03_--N |
| 3660 | 57 | TalkEvent | MS_11_ED05_01A |
| 3675 | 57 | TalkEvent | MS_11_ED05_01B |
| 3680 | 57 | TalkEvent | MS_11_ED05_01C |
| 3688 | 57 | TalkEvent | MS_11_ED05_02 |
| 36D2 | 57 | TalkEvent | MS_11_ED06_01 |
| 36E4 | 57 | TalkEvent | MS_11_ED06_01_DEL |
| 372A | 57 | TalkEvent | MS_11_ED06_01_SKIP |
| 3759 | 57 | TalkEvent | MS_11_ED06_02A |
| 376C | 57 | TalkEvent | MS_11_ED06_02B |
| 3776 | 57 | UnitTransferToForceByPID | PID_VOKE, 7 |
| 379F | 57 | TalkEvent | MS_11_ED07_A |
| 37AA | 57 | TalkEvent | MS_11_ED07_B |
| 381A | 59 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.11: Blood Runs Red — internal 12

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 13, 'h': 17, 'm': 17, 'n': 17}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap12/dispos_c.bin:bmap12_event_00_c`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LOFA, PID_MARCIA, PID_NEPENEE, PID_OSCAR, PID_VOKE, PID_WAYU; F2: PID_DUMMY1, PID_LAY_EV, PID_LETHE_EV, PID_MORDY_EV, PID_NASIR, PID_PEOPLE_EV1, PID_PEOPLE_EV10, PID_PEOPLE_EV11, PID_PEOPLE_EV12, PID_PEOPLE_EV2, PID_PEOPLE_EV3, PID_PEOPLE_EV4, PID_PEOPLE_EV5, PID_PEOPLE_EV6, PID_PEOPLE_EV7, PID_PEOPLE_EV8, PID_PEOPLE_EV9, PID_TIAMAT_EV
- `bmap12/dispos_c.bin:bmap12_event_01_c`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LOFA, PID_MARCIA, PID_NEPENEE, PID_OSCAR, PID_VOKE, PID_WAYU; F1: PID_DAYNE_SKN_1, PID_DAYNE_SKN_2, PID_DAYNE_SOL_1, PID_DAYNE_SOL_2, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4; F2: PID_DUMMY1, PID_LAY_EV, PID_LAY_EV2, PID_LETHE_EV, PID_MORDY_EV, PID_NASIR, PID_OLDMAN_1, PID_PEOPLE_EV1, PID_PEOPLE_EV10, PID_PEOPLE_EV11, PID_PEOPLE_EV12, PID_PEOPLE_EV2, PID_PEOPLE_EV3, PID_PEOPLE_EV4, PID_PEOPLE_EV5, PID_PEOPLE_EV6, PID_PEOPLE_EV7, PID_PEOPLE_EV8, PID_PEOPLE_EV9, PID_TIAMAT_EV
- `bmap12/dispos_c.bin:bmap12_event_blackknight_c`: F1: PID_BLACKKNIGHT
- `bmap12/dispos_c.bin:bmap12_event_dein_c`: F1: PID_DAYNE_SKN_1, PID_DAYNE_SOL_1, PID_DAYNE_SOL_2
- `bmap12/dispos_c.bin:bmap12_event_haar_c`: F1: PID_DAYNE_DKN, PID_HAAR
- `bmap12/dispos_c.bin:bmap12_event_ike_c`: F2: PID_IKE_EV
- `bmap12/dispos_c.bin:bmap12_event_jikeidan_c`: F1: PID_ZAKO_EV1, PID_ZAKO_EV2
- `bmap12/dispos_c.bin:bmap12_event_jill_c`: F1: PID_JILL
- `bmap12/dispos_c.bin:bmap12_event_makkoyar`: F1: PID_MAKKOYAR
- `bmap12/dispos_c.bin:bmap12_event_makkoyar_c`: F1: PID_MAKKOYAR
- `bmap12/dispos_c.bin:bmap12_event_mist_c`: F2: PID_MIST_EV
- `bmap12/dispos_c.bin:bmap12_event_narsil_c`: F2: PID_NASIR
- `bmap12/dispos_c.bin:bmap12_event_nositohi_c`: F1: PID_NOSHITHI
- `bmap12/dispos_c.bin:bmap12_event_rai_c`: F2: PID_LAY
- `bmap12/dispos_c.bin:bmap12_event_sefe_c`: F2: PID_CEPHERAN_FAKE
- `bmap12/dispos_c.bin:bmap12_event_zako_c`: F1: PID_DAYNE_SOL_1
- `bmap12/dispos_c.bin:bmap12_m01_c`: F1: PID_ZIHARK
- `bmap12/dispos_c.bin:bmap12_mikata_c`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MORDY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap12/dispos_c.bin:bmap12_mist2_c`: F2: PID_MIST_EV
- `bmap12/dispos_c.bin:bmap12_mist_c`: F2: PID_MIST_EV
- `bmap12/dispos_c.bin:bmap12_narsil_c`: F2: PID_NASIR
- `bmap12/dispos_c.bin:bmap12_senerio2_c`: F2: PID_SENERIO_EV
- `bmap12/dispos_c.bin:bmap12_senerio_c`: F2: PID_SENERIO_EV
- `bmap12/dispos_c.bin:bmap12_z_blk_c`: F1: PID_BLACKKNIGHT
- `bmap12/dispos_h.bin:bmap12_first2_h`: F1: PID_12_SELFDEFENCE
- `bmap12/dispos_h.bin:bmap12_first3_h`: F1: PID_12_THIEF
- `bmap12/dispos_h.bin:bmap12_first_h`: F1: PID_DAYNE_ARM, PID_DAYNE_MAG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_MAKKOYAR
- `bmap12/dispos_h.bin:bmap12_mikata_h`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_VOKE, PID_WAYU
- `bmap12/dispos_h.bin:bmap12_z_jill_h`: F1: PID_DAYNE_DKN
- `bmap12/dispos_m.bin:bmap12_first2_m`: F1: PID_12_SELFDEFENCE
- `bmap12/dispos_m.bin:bmap12_first3_m`: F1: PID_12_THIEF
- `bmap12/dispos_m.bin:bmap12_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_MAKKOYAR
- `bmap12/dispos_m.bin:bmap12_mikata_m`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_VOKE, PID_WAYU
- `bmap12/dispos_m.bin:bmap12_z_jill_m`: F1: PID_DAYNE_DKN
- `bmap12/dispos_n.bin:bmap12_first2_n`: F1: PID_12_SELFDEFENCE
- `bmap12/dispos_n.bin:bmap12_first3_n`: F1: PID_12_THIEF
- `bmap12/dispos_n.bin:bmap12_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_MAKKOYAR
- `bmap12/dispos_n.bin:bmap12_mikata_n`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_VOKE, PID_WAYU
- `bmap12/dispos_n.bin:bmap12_z_jill_n`: F1: PID_DAYNE_DKN
- `bmap12_2/dispos_c.bin:bmap12_2_event_blackknight_c`: F1: PID_BLACKKNIGHT
- `bmap12_2/dispos_c.bin:bmap12_2_event_makkoyar`: F1: PID_MAKKOYAR
- `bmap12_2/dispos_c.bin:bmap12_2_event_makkoyar_c`: F1: PID_MAKKOYAR
- `bmap12_2/dispos_c.bin:bmap12_2_event_nositohi_c`: F1: PID_NOSHITHI
- `bmap12_2/dispos_c.bin:bmap12_2_event_rai_c`: F2: PID_LAY
- `bmap12_2/dispos_c.bin:bmap12_2_event_sefe_c`: F2: PID_CEPHERAN_FAKE
- `bmap12_2/dispos_c.bin:bmap12_2_event_zako_c`: F1: PID_DAYNE_SOL_1
- `bmap12_2/dispos_c.bin:bmap12_2_z_blk_c`: F1: PID_BLACKKNIGHT

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 184F | 0 | TalkEvent | MS_12_VIL_01_LM |
| 1888 | 0 | TalkEvent | MS_12_VIL_01 |
| 1910 | 1 | TalkEvent | MS_12_VIL_03_LM |
| 1949 | 1 | TalkEvent | MS_12_VIL_03 |
| 19D4 | 2 | TalkEvent | MS_12_VIL_02_LM |
| 1A0D | 2 | TalkEvent | MS_12_VIL_02 |
| 1B21 | 6 | UnitEscape | ?, 0 |
| 1B7E | 8 | regist | 訪問１ |
| 1B86 | 8 | regist | 訪問２ |
| 1B8E | 8 | regist | 訪問３ |
| 1BEB | 10 | regist | 情報１フラグ |
| 1BF3 | 10 | regist | 情報２フラグ |
| 1BFB | 10 | regist | 情報３フラグ |
| 1C03 | 10 | regist | 情報４フラグ |
| 1C0B | 10 | regist | 情報５フラグ |
| 1C13 | 10 | regist | 情報６フラグ |
| 1C48 | 11 | TalkEvent | MS_12_INFO_01 |
| 1C88 | 12 | TalkEvent | MS_12_INFO_02 |
| 1CDC | 13 | TalkEvent | MS_12_INFO_03 |
| 1D26 | 14 | TalkEvent | MS_12_INFO_04 |
| 1D6E | 15 | TalkEvent | MS_12_INFO_05 |
| 1DB6 | 16 | TalkEvent | MS_12_INFO_06 |
| 1E07 | 18 | regist | ツイハーク仲間 |
| 1E0F | 18 | regist | ツイハーク戦闘レテ |
| 1E17 | 18 | regist | ツイハーク戦闘モウディ |
| 1E1F | 18 | regist | ツイハーク戦闘 |
| 1E27 | 18 | regist | ジル戦闘 |
| 1E2F | 18 | regist | ジル戦闘レテ |
| 1E37 | 18 | regist | ジル戦闘モウディ |
| 1E3F | 18 | regist | 漆黒の騎士配置トリガ |
| 1E47 | 18 | regist | 漆黒の騎士配置イベント |
| 1E4F | 18 | regist | 漆黒の騎士戦闘アイク |
| 1E57 | 18 | regist | 漆黒の騎士戦闘レテモウディ |
| 1E5F | 18 | regist | 漆黒の騎士戦闘通常 |
| 1E67 | 18 | regist | アイクと漆黒の騎士の戦闘後会話 |
| 1E6F | 18 | regist | ボス戦闘アイク |
| 1E77 | 18 | regist | ボス戦闘レテモウディ |
| 1E7F | 18 | regist | ボス戦闘会話 |
| 1E87 | 18 | regist | ボス死亡 |
| 1E8F | 18 | regist | レテかモウディでジル倒した |
| 1E97 | 18 | regist | それ以外でジル倒した |
| 1E9F | 18 | regist | ボス戦闘会話イベント |
| 1EE2 | 19 | InstantDisposRank | bmap12_first |
| 1EEA | 19 | InstantDisposRank | bmap12_first2 |
| 1EF2 | 19 | InstantDisposRank | bmap12_first3 |
| 1EFA | 19 | InstantDispos | bmap12_m01_c |
| 1F02 | 19 | InstantDispos | bmap12_event_haar_c |
| 1F12 | 19 | ForceGetCount | 1 |
| 1F1B | 19 | ForceGetFirst | 1 |
| 1FDF | 19 | InstantDispos | bmap12_narsil_c |
| 1FE7 | 19 | UnitEscapeByPID | PID_NASIR |
| 201F | 20 | SallySetByGroup | bmap12_mikata_c |
| 21A2 | 21 | InstantDispos | bmap12_event_00_c |
| 21AF | 21 | Dispos_ForEventSenerio | bmap12_senerio_c, bmap12_senerio2_c, 1 |
| 21C2 | 21 | Dispos_ForEvent | PID_MIST, JID_CLERIC/F, bmap12_mist_c, bmap12_mist2_c, 1 |
| 21CF | 21 | UnitEscapeByPID | PID_LETHE_EV |
| 21DC | 21 | UnitEscapeByPID | PID_MORDY_EV |
| 21E9 | 21 | UnitEscapeByPID | PID_OSCAR |
| 21F6 | 21 | UnitEscapeByPID | PID_BOLE |
| 2203 | 21 | UnitEscapeByPID | PID_KILROY |
| 2210 | 21 | UnitEscapeByPID | PID_WAYU |
| 221D | 21 | UnitEscapeByPID | PID_ELAICE |
| 222A | 21 | UnitEscapeByPID | PID_MARCIA |
| 2237 | 21 | UnitEscapeByPID | PID_MIST |
| 2244 | 21 | UnitEscapeByPID | PID_LOFA |
| 2251 | 21 | UnitEscapeByPID | PID_CHAP |
| 225E | 21 | UnitEscapeByPID | PID_NEPENEE |
| 226B | 21 | UnitEscapeByPID | PID_KEVIN |
| 2278 | 21 | UnitEscapeByPID | PID_VOKE |
| 246B | 22 | ForceGetCount | 5 |
| 248E | 22 | Join | always_dbg_12 |
| 24A6 | 22 | MapLoad | bmap12 |
| 24B4 | 22 | InstantDisposSetMode | bmap12_mikata_n, bmap12_mikata_h, bmap12_mikata_m |
| 24B9 | 22 | AllUnitEscape |  |
| 24E4 | 22 | ForceGetCount | 5 |
| 24ED | 22 | ForceGetFirst | 5 |
| 2541 | 22 | ChapterMoviePlay | 12 |
| 257B | 22 | MapLoad | bmap12 |
| 2650 | 22 | AllUnitEscape |  |
| 265A | 22 | AllUnitEscape |  |
| 2674 | 22 | TalkEvent | MS_12_OP_01 |
| 26E3 | 23 | MapLoad | bmap12 |
| 287C | 23 | InstantDispos | bmap12_event_01_c |
| 2889 | 23 | Dispos_ForEventSenerio | bmap12_senerio_c, bmap12_senerio2_c, 1 |
| 289C | 23 | Dispos_ForEvent | PID_MIST, JID_CLERIC/F, bmap12_mist_c, bmap12_mist2_c, 1 |
| 28A9 | 23 | UnitEscapeByPID | PID_LETHE_EV |
| 28B6 | 23 | UnitEscapeByPID | PID_MORDY_EV |
| 28C3 | 23 | UnitEscapeByPID | PID_OSCAR |
| 28D0 | 23 | UnitEscapeByPID | PID_BOLE |
| 28DD | 23 | UnitEscapeByPID | PID_KILROY |
| 28EA | 23 | UnitEscapeByPID | PID_WAYU |
| 28F7 | 23 | UnitEscapeByPID | PID_ELAICE |
| 2904 | 23 | UnitEscapeByPID | PID_MARCIA |
| 2911 | 23 | UnitEscapeByPID | PID_MIST |
| 291E | 23 | UnitEscapeByPID | PID_LOFA |
| 292B | 23 | UnitEscapeByPID | PID_CHAP |
| 2938 | 23 | UnitEscapeByPID | PID_NEPENEE |
| 2945 | 23 | UnitEscapeByPID | PID_KEVIN |
| 2952 | 23 | UnitEscapeByPID | PID_VOKE |
| 2C4F | 23 | TalkEvent | MS_12_OP_02_new |
| 2CA9 | 23 | TalkEvent | MS_12_OP_03_00 |
| 2D1F | 23 | TalkEvent | MS_12_OP_03_01 |
| 2DEA | 23 | TalkEvent | MS_12_OP_03_02 |
| 2E48 | 23 | TalkEvent | MS_12_OP_03_03 |
| 2EEE | 23 | TalkEvent | MS_12_OP_03_04 |
| 2EFD | 23 | TalkResume |  |
| 2F97 | 23 | TalkEvent | MS_12_OP_03_06_A |
| 30D7 | 23 | TalkEvent | MS_12_OP_03_06_B |
| 3148 | 23 | TalkEvent | MS_12_OP_03_06_C |
| 3244 | 23 | TalkEvent | MS_12_OP_03_07 |
| 3374 | 23 | TalkEvent | MS_12_OP_03_08A |
| 3385 | 23 | TalkEvent | MS_12_OP_03_08B |
| 3390 | 23 | TalkEvent | MS_12_OP_03_08C |
| 345F | 23 | TalkEvent | MS_12_OP_03_09 |
| 3464 | 23 | TalkResume |  |
| 34EE | 23 | TalkEvent | MS_12_OP_03_10 |
| 356E | 23 | TalkEvent | MS_12_OP_03_11 |
| 357E | 23 | InstantDispos | bmap12_event_jikeidan_c |
| 36E5 | 23 | TalkEvent | MS_12_OP_03_11_2 |
| 3784 | 23 | TalkEvent | MS_12_OP_03_12 |
| 37E5 | 23 | TalkEvent | MS_12_OP_03_13 |
| 3801 | 23 | AllUnitEscape |  |
| 380B | 23 | AllUnitEscape |  |
| 381D | 23 | SallySetByGroup | bmap12_mikata_c |
| 3825 | 23 | InstantDispos | bmap12_mikata_c |
| 3933 | 23 | UnitForcedSallyByPID | PID_IKE |
| 393B | 23 | UnitDontMoveSallyByPID | PID_IKE |
| 39BB | 24 | InstantDispos | bmap12_narsil_c |
| 3A0A | 24 | TalkEvent | MS_12_OP_03_14 |
| 3A34 | 24 | UnitEscapeByPID | PID_NASIR |
| 3A53 | 24 | TalkEvent | MS_12_OP_03_14_02 |
| 3AA3 | 24 | InstantDispos | bmap12_event_rai_c |
| 3AB2 | 24 | InstantDispos | bmap12_event_dein_c |
| 3B0C | 24 | TalkEvent | MS_12_OP_04 |
| 3B22 | 24 | TalkResume |  |
| 3C3C | 24 | TalkEvent | MS_12_EV_Lay |
| 3CC0 | 24 | UnitEscapeByPID | PID_LAY |
| 3CC8 | 24 | TalkEvent | MS_12_EV_Lay_2 |
| 3D0E | 24 | UnitEscapeByPID | PID_DAYNE_SKN_1 |
| 3D16 | 24 | UnitEscapeByPID | PID_DAYNE_SKN_2 |
| 3D1E | 24 | UnitEscapeByPID | PID_DAYNE_SOL_1 |
| 3D26 | 24 | UnitEscapeByPID | PID_DAYNE_SOL_2 |
| 3D7C | 24 | TalkEvent | MS_12_EV_START |
| 3E6C | 26 | TalkEvent | MS_12_EV_XX |
| 3F1B | 27 | DisposSetMode | bmap12_z_jill_n, bmap12_z_jill_h, bmap12_z_jill_m |
| 3F53 | 27 | InstantDisposFirst | bmap12_event_jill_c |
| 3FA2 | 27 | TalkEvent | MS_12_EV_JILL |
| 3FB1 | 27 | DisposContinue | bmap12_event_jill_c |
| 40C5 | 28 | Dispos | bmap12_z_blk_c |
| 4101 | 28 | TalkEvent | MS_12_EV_DARK |
| 4158 | 28 | TalkEvent | MS_12_EV_DARK_2 |
| 41CB | 29 | TalkEvent | MS_12_ALIVE_IKE |
| 423E | 30 | TalkEvent | ? |
| 4248 | 30 | UnitTransferToForceByPID | PID_ZIHARK, 0 |
| 4355 | 35 | BMGetPhase |  |
| 4362 | 35 | SoundBossTalkStart | BGM_BTL_PL01 |
| 436D | 35 | SoundBossTalkStart | BGM_BTL_CP01 |
| 4375 | 35 | TalkEvent | MS_12_BT_02A |
| 4382 | 35 | SoundBossTalkEnd |  |
| 43B1 | 36 | BMGetPhase |  |
| 43BE | 36 | SoundBossTalkStart | BGM_BTL_PL01 |
| 43C9 | 36 | SoundBossTalkStart | BGM_BTL_CP01 |
| 43D1 | 36 | TalkEvent | MS_12_BT_02B |
| 43DE | 36 | SoundBossTalkEnd |  |
| 441A | 37 | BMGetPhase |  |
| 444F | 37 | BMGetPhase |  |
| 445C | 37 | SoundBossTalkStart | BGM_BTL_PL01 |
| 4467 | 37 | SoundBossTalkStart | BGM_BTL_CP01 |
| 446F | 37 | TalkEvent | MS_12_BT_02C |
| 447C | 37 | SoundBossTalkEnd |  |
| 44B3 | 38 | DefaultDieTalk |  |
| 44BE | 38 | TalkEvent | MS_12_DIE_02 |
| 44ED | 39 | BMGetPhase |  |
| 44FA | 39 | SoundBossTalkStart | BGM_BTL_PL01 |
| 4505 | 39 | SoundBossTalkStart | BGM_BTL_CP01 |
| 450D | 39 | TalkEvent | MS_12_BT_03A |
| 451A | 39 | SoundBossTalkEnd |  |
| 4549 | 40 | BMGetPhase |  |
| 4556 | 40 | SoundBossTalkStart | BGM_BTL_PL01 |
| 4561 | 40 | SoundBossTalkStart | BGM_BTL_CP01 |
| 4569 | 40 | TalkEvent | MS_12_BT_03B |
| 4576 | 40 | SoundBossTalkEnd |  |
| 45B2 | 41 | BMGetPhase |  |
| 45E7 | 41 | BMGetPhase |  |
| 45F4 | 41 | SoundBossTalkStart | BGM_BTL_PL01 |
| 45FF | 41 | SoundBossTalkStart | BGM_BTL_CP01 |
| 4607 | 41 | TalkEvent | MS_12_BT_03C |
| 4614 | 41 | SoundBossTalkEnd |  |
| 4641 | 42 | BMGetPhase |  |
| 467B | 42 | TalkEvent | MS_12_DIE_03A |
| 4696 | 42 | TalkEvent | MS_12_DIE_03B |
| 46A9 | 42 | TalkEvent | MS_12_DIE_03C |
| 46E4 | 43 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 46EC | 43 | TalkEvent | MS_12_BT_DARK |
| 46F1 | 43 | SoundBossTalkEnd |  |
| 4734 | 44 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 473C | 44 | TalkEvent | MS_12_BT_DARK_01 |
| 4749 | 44 | SoundBossTalkEnd |  |
| 477C | 45 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 4784 | 45 | TalkEvent | MS_12_BT_DARK_01 |
| 4791 | 45 | SoundBossTalkEnd |  |
| 47D8 | 46 | BMGetPhase |  |
| 4818 | 46 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 4820 | 46 | TalkEvent | MS_12_BT_DARK_00 |
| 482D | 46 | SoundBossTalkEnd |  |
| 4863 | 47 | BMGetPhase |  |
| 48A6 | 47 | TalkEvent | MS_12_DIE_IKE |
| 48CC | 47 | TalkEvent | MDIE_IKE_2 |
| 4908 | 48 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 4910 | 48 | TalkEvent | MS_12_BT_IKE |
| 4925 | 48 | SoundBossTalkEnd |  |
| 4958 | 49 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 4960 | 49 | TalkEvent | MS_12_BT_R1 |
| 4975 | 49 | SoundBossTalkEnd |  |
| 49A8 | 50 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 49B0 | 50 | TalkEvent | MS_12_BT_R1 |
| 49C5 | 50 | SoundBossTalkEnd |  |
| 4A14 | 51 | BMGetPhase |  |
| 4A54 | 51 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 4A5C | 51 | TalkEvent | MS_12_BT |
| 4A69 | 51 | SoundBossTalkEnd |  |
| 4A98 | 52 | TalkEvent | MS_12_DIE |
| 4B15 | 53 | AllUnitEscape |  |
| 4B33 | 53 | MapLoad | bmap12_2 |
| 4B72 | 53 | ForceGetCount | 0 |
| 4B81 | 53 | ForceGetFirst | 0 |
| 4B93 | 53 | UnitEscape | ?, 0 |
| 4BA6 | 53 | UnitEscapeByPID | PID_BLACKKNIGHT |
| 4BF8 | 53 | UnitEscape | ?, 0 |
| 4C28 | 53 | InstantDispos | bmap12_2_event_blackknight_c |
| 4C30 | 53 | InstantDispos | bmap12_2_event_rai_c |
| 4C46 | 53 | InstantDispos | bmap12_2_event_sefe_c |
| 4C67 | 53 | InstantDispos | bmap12_2_event_nositohi_c |
| 4CFF | 53 | TalkEvent | MS_12_EV_DL_1 |
| 4D62 | 53 | TalkEvent | MS_12_EV_DL_1_2 |
| 4E9F | 53 | TalkEvent | MS_12_EV_DL_2 |
| 4EF9 | 53 | TalkEvent | MS_12_EV_DL_3 |
| 4F7B | 53 | TalkEvent | MS_12_EV_DL_4 |
| 4FC8 | 53 | UnitEscapeByPID | PID_LAY |
| 5034 | 53 | TalkEvent | MS_12_ED_XX |
| 5132 | 53 | UnitEscapeByPID | PID_LAY |
| 51BB | 53 | TalkEvent | MS_12_BT_DI_3A |
| 51C6 | 53 | TalkEvent | MS_12_BT_DI_3B |
| 51FC | 53 | AllUnitEscape |  |
| 5223 | 53 | TalkEvent | MS_12_ED_XXX |
| 525E | 53 | TalkEvent | MS_12_ED_01_BB |
| 5269 | 53 | TalkEvent | MS_12_ED_01_AA |
| 529D | 53 | TalkEvent | MS_12_ED_02_B |
| 52CE | 53 | TalkEvent | MS_12_ED_03 |
| 534E | 55 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.12: A Strange Land — internal 13

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 10, 'h': 13, 'm': 13, 'n': 13}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap13/dispos_c.bin:bmap13_event01_c`: F2: PID_G_ZAKO_EV1, PID_G_ZAKO_EV2, PID_G_ZAKO_EV3
- `bmap13/dispos_c.bin:bmap13_event02_c`: F2: PID_DUMMY6, PID_DUMMY7
- `bmap13/dispos_c.bin:bmap13_event03_c`: F2: PID_G_ZAKO_EV1, PID_G_ZAKO_EV2, PID_G_ZAKO_EV3
- `bmap13/dispos_c.bin:bmap13_event04_c`: F0: PID_ELAICE, PID_MARCIA, PID_NASIR, PID_SENERIO, PID_SOTHE, PID_VOKE, PID_WAYU, PID_ZIHARK; F2: PID_IKE_EV, PID_MIST_EV, PID_TIAMAT_EV
- `bmap13/dispos_c.bin:bmap13_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap13/dispos_c.bin:bmap13_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap13/dispos_c.bin:bmap13_jill_c`: F2: PID_JILL
- `bmap13/dispos_c.bin:bmap13_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap13/dispos_h.bin:bmap13_first01_h`: F1: PID_CHIGU
- `bmap13/dispos_h.bin:bmap13_first02_h`: F1: PID_K_ZAKO
- `bmap13/dispos_h.bin:bmap13_first_h`: F1: PID_K_ZAKO
- `bmap13/dispos_h.bin:bmap13_mikata_h`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap13/dispos_h.bin:bmap13_z01_h`: F1: PID_K_ZAKO
- `bmap13/dispos_h.bin:bmap13_z02_2_h`: F1: PID_K_ZAKO
- `bmap13/dispos_h.bin:bmap13_z02_h`: F1: PID_K_ZAKO
- `bmap13/dispos_h.bin:bmap13_z03_h`: F1: PID_K_ZAKO
- `bmap13/dispos_h.bin:bmap13_z04_h`: F1: PID_K_ZAKO
- `bmap13/dispos_m.bin:bmap13_first01_m`: F1: PID_CHIGU
- `bmap13/dispos_m.bin:bmap13_first02_m`: F1: PID_K_ZAKO
- `bmap13/dispos_m.bin:bmap13_first_m`: F1: PID_K_ZAKO
- `bmap13/dispos_m.bin:bmap13_mikata_m`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap13/dispos_m.bin:bmap13_z01_m`: F1: PID_K_ZAKO
- `bmap13/dispos_m.bin:bmap13_z02_2_m`: F1: PID_K_ZAKO
- `bmap13/dispos_m.bin:bmap13_z02_m`: F1: PID_K_ZAKO
- `bmap13/dispos_m.bin:bmap13_z03_m`: F1: PID_K_ZAKO
- `bmap13/dispos_m.bin:bmap13_z04_m`: F1: PID_K_ZAKO
- `bmap13/dispos_n.bin:bmap13_first01_n`: F1: PID_CHIGU
- `bmap13/dispos_n.bin:bmap13_first02_n`: F1: PID_K_ZAKO
- `bmap13/dispos_n.bin:bmap13_first_n`: F1: PID_K_ZAKO
- `bmap13/dispos_n.bin:bmap13_mikata_n`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap13/dispos_n.bin:bmap13_z01_n`: F1: PID_K_ZAKO
- `bmap13/dispos_n.bin:bmap13_z02_2_n`: F1: PID_K_ZAKO
- `bmap13/dispos_n.bin:bmap13_z02_n`: F1: PID_K_ZAKO
- `bmap13/dispos_n.bin:bmap13_z03_n`: F1: PID_K_ZAKO
- `bmap13/dispos_n.bin:bmap13_z04_n`: F1: PID_K_ZAKO

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 103E | 0 | regist | 情報１フラグ |
| 1045 | 0 | regist | 情報２フラグ |
| 104C | 0 | regist | 情報３フラグ |
| 1053 | 0 | regist | 情報４フラグ |
| 105A | 0 | regist | 情報５フラグ |
| 1061 | 0 | regist | 情報６フラグ |
| 1068 | 0 | regist | サザ仲間 |
| 10AC | 1 | TalkEvent | MS_13_INFO_01 |
| 10E6 | 1 | TalkEvent | MS_13_INFO_01_02_2A |
| 1107 | 1 | Join | always_saza |
| 1119 | 1 | TalkEvent | MS_13_INFO_01_02_2B |
| 115A | 2 | TalkEvent | MS_13_INFO_03 |
| 11A2 | 3 | TalkEvent | MS_13_INFO_04 |
| 11EA | 4 | TalkEvent | MS_13_INFO_05 |
| 121B | 5 | regist | ジル仲間会話 |
| 1223 | 5 | regist | ボス戦闘会話アイク |
| 122B | 5 | regist | ボス戦闘会話レテ |
| 1233 | 5 | regist | ボス戦闘会話モウディ |
| 123B | 5 | regist | ボス戦闘会話 |
| 127A | 6 | InstantDisposRank | bmap13_first |
| 1289 | 6 | InstantDisposRank | bmap13_first01 |
| 1291 | 6 | InstantDisposRank | bmap13_first02 |
| 131F | 7 | SallySetByGroup | bmap13_mikata_c |
| 14DC | 8 | TalkEvent | MS_13_GMAP_1 |
| 153C | 8 | TalkEvent | MS_13_GMAP_3 |
| 15B2 | 8 | TalkEvent | MS_13_GMAP_4 |
| 16F2 | 8 | TalkEvent | MS_13_GMAP_6 |
| 1746 | 8 | TalkEvent | MS_13_GMAP_7 |
| 1813 | 8 | TalkEvent | MS_13_GMAP_8 |
| 186A | 8 | TalkEvent | MS_13_GMAP_9 |
| 189B | 8 | TalkResume |  |
| 192A | 9 | ChapterMoviePlay | 13 |
| 1977 | 10 | ForceGetCount | 5 |
| 19A3 | 10 | MapLoad | bmap13 |
| 19B1 | 10 | InstantDisposSetMode | bmap13_mikata_n, bmap13_mikata_h, bmap13_mikata_m |
| 19B6 | 10 | AllUnitEscape |  |
| 1A08 | 10 | TalkEvent | MS_13_OP_01 |
| 1A77 | 11 | MapLoad | bmap13 |
| 1AB1 | 11 | InstantDisposRank | bmap13_first01 |
| 1AB9 | 11 | InstantDisposRank | bmap13_first02 |
| 1ACB | 11 | InstantDispos | bmap13_jill_c |
| 1AD0 | 11 | AllUnitEscape |  |
| 1ADF | 11 | InstantDisposRank | bmap13_first |
| 1AEE | 11 | SallySetByGroup | bmap13_mikata_c |
| 1AF6 | 11 | InstantDispos | bmap13_mikata_c |
| 1B0E | 11 | Dispos_ForEventSenerio | bmap13_event_senerio_c, bmap13_event_senerio2_c, 0 |
| 1C35 | 11 | TalkEvent | MS_13_OP_02 |
| 1CD9 | 11 | TalkResume |  |
| 1D94 | 11 | DisposSetMode | bmap13_first02_n, bmap13_first02_h, bmap13_first02_m |
| 1DA2 | 11 | DisposSetMode | bmap13_first01_n, bmap13_first01_h, bmap13_first01_m |
| 1E32 | 11 | TalkEvent | MS_13_EV_01 |
| 1EF0 | 11 | TalkEvent | MS_13_OP_03 |
| 1F01 | 11 | ForceGetCount | 0 |
| 1F0A | 11 | ForceGetFirst | 0 |
| 1F54 | 11 | UnitEscapeByPID | PID_SENERIO_EV |
| 1F99 | 11 | UnitForcedSallyByPID | PID_IKE |
| 1FA1 | 11 | UnitDontMoveSallyByPID | PID_IKE |
| 2093 | 13 | InstantDispos | bmap13_jill_c |
| 2138 | 13 | TalkEvent | MS_13_OP_XX |
| 2182 | 13 | DisposContinue | bmap13_jill_c |
| 222F | 14 | TalkEvent | MS_13_EV_X |
| 2239 | 14 | UnitTransferToForceByPID | PID_JILL, 0 |
| 2291 | 15 | DisposSetMode | bmap13_z01_n, bmap13_z01_h, bmap13_z01_m |
| 22C1 | 16 | DisposSetMode | bmap13_z02_n, bmap13_z02_h, bmap13_z02_m |
| 22CF | 16 | DisposSetMode | bmap13_z02_2_n, bmap13_z02_2_h, bmap13_z02_2_m |
| 22FD | 17 | DisposSetMode | bmap13_z03_n, bmap13_z03_h, bmap13_z03_m |
| 230C | 17 | Dispos | bmap13_z03_2_m |
| 233D | 18 | DisposSetMode | bmap13_z04_n, bmap13_z04_h, bmap13_z04_m |
| 236D | 19 | DisposSetMode | bmap13_z01_n, bmap13_z01_h, bmap13_z01_m |
| 239D | 20 | DisposSetMode | bmap13_z02_n, bmap13_z02_h, bmap13_z02_m |
| 23B5 | 20 | DisposSetMode | bmap13_z02_2_n, bmap13_z02_2_h, bmap13_z02_2_m |
| 2422 | 22 | LocalDieTalkWithBgmChange | ジル仲間会話, MS_13_DIE_JILL |
| 2450 | 23 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2458 | 23 | TalkEvent | MS_13_BT_IKE |
| 2465 | 23 | SoundBossTalkEnd |  |
| 2498 | 24 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 24A0 | 24 | TalkEvent | MS_13_BT_RE |
| 24AD | 24 | SoundBossTalkEnd |  |
| 24E0 | 25 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 24E8 | 25 | TalkEvent | MS_13_BT_MO |
| 24F5 | 25 | SoundBossTalkEnd |  |
| 253E | 26 | BMGetPhase |  |
| 257E | 26 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2586 | 26 | TalkEvent | MS_13_BT |
| 2593 | 26 | SoundBossTalkEnd |  |
| 25C4 | 27 | TalkEvent | MS_13_DIE |
| 25EA | 28 | ForceGetCount | 1 |
| 2656 | 29 | AllUnitEscape |  |
| 265E | 29 | InstantDispos | bmap13_event01_c |
| 2666 | 29 | InstantDispos | bmap13_event02_c |
| 266E | 29 | InstantDispos | bmap13_event03_c |
| 2673 | 29 | AllUnitEscape |  |
| 2717 | 29 | InstantDispos | bmap13_event04_c |
| 2724 | 29 | UnitEscapeByPID | PID_WAYU |
| 2731 | 29 | UnitEscapeByPID | PID_ELAICE |
| 273E | 29 | UnitEscapeByPID | PID_MARCIA |
| 274B | 29 | UnitEscapeByPID | PID_VOKE |
| 2758 | 29 | UnitEscapeByPID | PID_ZIHARK |
| 2765 | 29 | UnitEscapeByPID | PID_SOTHE |
| 283A | 29 | TalkEvent | MS_13_ED_01 |
| 2962 | 29 | TalkEvent | MS_13_ED_02 |
| 2988 | 29 | TalkEvent | MS_13_ED_02_2 |
| 29A1 | 29 | TalkResume |  |
| 29D0 | 29 | UnitEscapeByPID | PID_NASIR |
| 2A0A | 29 | InstantDispos | bmap13_event01_c |
| 2AE0 | 29 | TalkEvent | MS_13_ED_03 |
| 2B43 | 29 | TalkEvent | MS_13_ED_04 |
| 2B4F | 29 | TalkResume |  |
| 2B6B | 29 | InstantDispos | bmap13_event02_c |
| 2C29 | 29 | TalkEvent | MS_13_ED_05 |
| 2CA4 | 29 | UnitEscapeByPID | PID_G_ZAKO_EV1 |
| 2CAC | 29 | UnitEscapeByPID | PID_G_ZAKO_EV2 |
| 2CB4 | 29 | UnitEscapeByPID | PID_G_ZAKO_EV3 |
| 2D46 | 29 | TalkEvent | MS_13_ED_06 |
| 2D5F | 29 | TalkResume |  |
| 2D9B | 29 | TalkEvent | MS_13_ED_06_2 |
| 2E25 | 29 | TalkEvent | MS_13_ED_07 |
| 2E6C | 29 | AllUnitEscape |  |
| 2E76 | 29 | AllUnitEscape |  |
| 2E95 | 29 | TalkEvent | MS_13_ED_08 |
| 2F1E | 31 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.13: A Guiding Wind — internal 14

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 12, 'h': 16, 'm': 16, 'n': 16}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap14/dispos_c.bin:bmap14_beg01_c`: F2: PID_B_ZAKO, PID_B_ZAKO_EV1, PID_STELLA
- `bmap14/dispos_c.bin:bmap14_beg02_c`: F2: PID_B_ZAKO
- `bmap14/dispos_c.bin:bmap14_event2_c`: F2: PID_JANAFF, PID_TIBARN, PID_VULCI
- `bmap14/dispos_c.bin:bmap14_event3_c`: F2: PID_SIGRUN, PID_ZAKO_EV1
- `bmap14/dispos_c.bin:bmap14_event4_c`: F2: PID_NAESALA, PID_NEALUCHI
- `bmap14/dispos_c.bin:bmap14_event5_c`: F2: PID_B_ZAKO_EV1, PID_B_ZAKO_EV2, PID_TANIS
- `bmap14/dispos_c.bin:bmap14_event6_c`: F2: PID_K_ZAKO
- `bmap14/dispos_c.bin:bmap14_event7_c`: F0: PID_MIST, PID_SENERIO; F2: PID_B_ZAKO_EV1, PID_IKE_EV, PID_NASIR, PID_TIAMAT_EV
- `bmap14/dispos_c.bin:bmap14_event8_c`: F2: PID_SIGRUN
- `bmap14/dispos_c.bin:bmap14_event9_c`: F2: PID_DUMMY2
- `bmap14/dispos_c.bin:bmap14_gatrie_c`: F2: PID_GATRIE
- `bmap14/dispos_c.bin:bmap14_mikata_c`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MORDY, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap14/dispos_h.bin:bmap14_first2_h`: F1: PID_K_ZAKO
- `bmap14/dispos_h.bin:bmap14_first_h`: F1: PID_14_ARC, PID_14_FIG, PID_14_HAL, PID_14_MAG, PID_14_SOL, PID_14_SRD, PID_NOSHITHI
- `bmap14/dispos_h.bin:bmap14_m01_h`: F2: PID_ZAKO_3
- `bmap14/dispos_h.bin:bmap14_mikata_h`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_JILL, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap14/dispos_h.bin:bmap14_z01_h`: F1: PID_K_ZAKO_EV1, PID_K_ZAKO_EV2
- `bmap14/dispos_h.bin:bmap14_z02_h`: F1: PID_K_ZAKO_EV1
- `bmap14/dispos_m.bin:bmap14_first2_m`: F1: PID_K_ZAKO
- `bmap14/dispos_m.bin:bmap14_first_m`: F1: PID_14_ARC, PID_14_FIG, PID_14_HAL, PID_14_MAG, PID_14_SOL, PID_14_SRD, PID_NOSHITHI
- `bmap14/dispos_m.bin:bmap14_m01_m`: F2: PID_ZAKO_3
- `bmap14/dispos_m.bin:bmap14_mikata_m`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_JILL, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap14/dispos_m.bin:bmap14_z01_m`: F1: PID_K_ZAKO_EV1, PID_K_ZAKO_EV2
- `bmap14/dispos_m.bin:bmap14_z02_m`: F1: PID_K_ZAKO_EV1
- `bmap14/dispos_n.bin:bmap14_first2_n`: F1: PID_K_ZAKO
- `bmap14/dispos_n.bin:bmap14_first_n`: F1: PID_14_ARC, PID_14_FIG, PID_14_HAL, PID_14_MAG, PID_14_SOL, PID_14_SRD, PID_NOSHITHI
- `bmap14/dispos_n.bin:bmap14_m01_n`: F2: PID_ZAKO_3
- `bmap14/dispos_n.bin:bmap14_mikata_n`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_JILL, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap14/dispos_n.bin:bmap14_z01_n`: F1: PID_K_ZAKO_EV1, PID_K_ZAKO_EV2
- `bmap14/dispos_n.bin:bmap14_z02_n`: F1: PID_K_ZAKO_EV1
- `bmap14_2/dispos_c.bin:bmap14_2_event01_c`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_JILL, PID_KEVIN, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MORDY, PID_OSCAR, PID_WAYU; F2: PID_DUMMY1, PID_MIST_EV, PID_NASIR, PID_TIAMAT_EV
- `bmap14_2/dispos_c.bin:bmap14_2_event_beg_c`: F2: PID_TANIS, PID_ZAKO_EV1
- `bmap14_2/dispos_c.bin:bmap14_2_event_dayn_c`: F1: PID_14_ARC, PID_14_FIG, PID_14_HAL, PID_14_MAG, PID_14_SRD, PID_NOSHITHI
- `bmap14_2/dispos_c.bin:bmap14_2_event_gatrie_c`: F2: PID_GATRIE
- `bmap14_2/dispos_c.bin:bmap14_2_event_green2_c`: F2: PID_B_ZAKO
- `bmap14_2/dispos_c.bin:bmap14_2_event_green_c`: F2: PID_B_ZAKO, PID_STELLA
- `bmap14_2/dispos_c.bin:bmap14_2_event_kilv2_c`: F1: PID_K_ZAKO_EV2, PID_K_ZAKO_EV3
- `bmap14_2/dispos_c.bin:bmap14_2_event_kilv_c`: F1: PID_K_ZAKO_EV1
- `bmap14_2/dispos_c.bin:bmap14_2_event_nes_c`: F2: PID_NAESALA, PID_NEALUCHI
- `bmap14_2/dispos_c.bin:bmap14_2_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap14_2/dispos_c.bin:bmap14_2_event_senerio_c`: F2: PID_SENERIO_EV

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 1162 | 0 | regist | 情報１フラグ |
| 1169 | 0 | regist | 情報２フラグ |
| 1170 | 0 | regist | 情報３フラグ |
| 1177 | 0 | regist | 情報４フラグ |
| 11AB | 1 | TalkEvent | MS_14_INFO_01 |
| 11E7 | 2 | TalkEvent | MS_14_INFO_02 |
| 122E | 3 | TalkEvent | MS_14_INFO_03 |
| 128A | 4 | TalkEvent | MS_14_INFO_04 |
| 1297 | 4 | TalkEvent | MS_14_INFO_04_2 |
| 14F2 | 13 | UnitEscape | ?, 0 |
| 1546 | 14 | UnitEscape | ?, 0 |
| 157B | 15 | regist | F31293129 |
| 1583 | 15 | regist | 宝箱１ |
| 158B | 15 | regist | 宝箱２ |
| 1593 | 15 | regist | 宝箱３ |
| 159B | 15 | regist | 宝箱４ |
| 15A3 | 15 | regist | 宝箱５ |
| 15AB | 15 | regist | 宝箱６ |
| 15B3 | 15 | regist | 宝箱７ |
| 1607 | 17 | regist | ステラ仲間 |
| 160F | 17 | regist | ガトリー会話アイク |
| 1617 | 17 | regist | ガトリー会話傭兵団 |
| 161F | 17 | regist | ガトリー仲間 |
| 1627 | 17 | regist | ボス戦闘会話アイク |
| 162F | 17 | regist | ボス戦闘会話獣 |
| 1637 | 17 | regist | ボス戦闘会話 |
| 163F | 17 | regist | ボス死亡 |
| 1682 | 18 | InstantDisposRank | bmap14_first |
| 168A | 18 | InstantDisposRank | bmap14_first2 |
| 16A0 | 18 | InstantDispos | bmap14_beg01_c |
| 16C0 | 18 | InstantDispos | bmap14_gatrie_c |
| 1708 | 18 | InstantDispos | bmap14_beg02_c |
| 1747 | 19 | SallySetByGroup | bmap14_mikata_c |
| 177F | 20 | ForceGetCount | 5 |
| 17AB | 20 | MapLoad | bmap14 |
| 17B9 | 20 | InstantDisposSetMode | bmap14_mikata_n, bmap14_mikata_h, bmap14_mikata_m |
| 17BE | 20 | AllUnitEscape |  |
| 17D3 | 20 | Join | always_dbg_mik_04g |
| 17E4 | 20 | UnitTransferToForceByPID | PID_GATRIE, 7 |
| 1825 | 20 | ChapterMoviePlay | 14 |
| 1A0A | 21 | MapLoad | bmap14_2 |
| 1A3C | 21 | InstantDispos | bmap14_2_event01_c |
| 1A4B | 21 | InstantDispos | bmap14_2_event_beg_c |
| 1A5A | 21 | InstantDispos | bmap14_2_event_kilv_c |
| 1A69 | 21 | InstantDispos | bmap14_2_event_dayn_c |
| 1A78 | 21 | InstantDispos | bmap14_2_event_nes_c |
| 1A87 | 21 | InstantDispos | bmap14_2_event_green_c |
| 1A95 | 21 | InstantDispos | bmap14_2_event_gatrie_c |
| 1AA0 | 21 | InstantDispos | bmap14_2_event_green2_c |
| 1AB4 | 21 | InstantDispos | bmap14_2_event_senerio_c |
| 1ABF | 21 | InstantDispos | bmap14_2_event_senerio2_c |
| 1AD3 | 21 | UnitEscapeByPID | PID_OSCAR |
| 1AE0 | 21 | UnitEscapeByPID | PID_BOLE |
| 1AED | 21 | UnitEscapeByPID | PID_KILROY |
| 1AFA | 21 | UnitEscapeByPID | PID_WAYU |
| 1B07 | 21 | UnitEscapeByPID | PID_ELAICE |
| 1B14 | 21 | UnitEscapeByPID | PID_MARCIA |
| 1B21 | 21 | UnitEscapeByPID | PID_LOFA |
| 1B2E | 21 | UnitEscapeByPID | PID_LETHE |
| 1B3B | 21 | UnitEscapeByPID | PID_MORDY |
| 1B48 | 21 | UnitEscapeByPID | PID_CHAP |
| 1B55 | 21 | UnitEscapeByPID | PID_NEPENEE |
| 1B62 | 21 | UnitEscapeByPID | PID_KEVIN |
| 1B6F | 21 | UnitEscapeByPID | PID_VOKE |
| 1B7C | 21 | UnitEscapeByPID | PID_JILL |
| 1B89 | 21 | UnitEscapeByPID | PID_SOTHE |
| 1C21 | 21 | Dispos | bmap14_2_event_kilv2_c |
| 1C40 | 21 | TalkEvent | MS_14_OP_03 |
| 1CD0 | 21 | TalkEvent | MS_14_OP_04_01 |
| 1CFD | 21 | TalkEvent | MS_14_OP_04_02 |
| 1D47 | 21 | AllUnitEscape |  |
| 1D51 | 21 | AllUnitEscape |  |
| 1D8F | 22 | TalkEvent | MS_14_OP_01 |
| 1DB0 | 22 | TalkEvent | MS_14_OP_02 |
| 1DC9 | 22 | TalkResume |  |
| 1DF1 | 22 | TalkEvent | MS_14_OP_03 |
| 1DF9 | 22 | TalkEvent | MS_14_OP_04_01 |
| 1E01 | 22 | TalkEvent | MS_14_OP_04_02 |
| 1E19 | 22 | MapLoad | bmap14 |
| 1E8A | 22 | SallySetByGroup | bmap14_mikata_c |
| 1E92 | 22 | InstantDisposFirst | bmap14_mikata_c |
| 1F3F | 22 | TalkEvent | MS_14_OP_05_0 |
| 1FF4 | 22 | TalkEvent | MS_14_OP_05_0_2 |
| 207D | 22 | TalkEvent | MS_14_OP_05_00 |
| 20FB | 22 | DisposContinue | bmap14_mikata_c |
| 214F | 22 | ForceGetCount | 2 |
| 2158 | 22 | ForceGetFirst | 2 |
| 21A9 | 22 | TalkEvent | MS_14_OP_05 |
| 21CB | 22 | TalkEvent | MS_14_OP_06 |
| 21E9 | 22 | ForceGetCount | 2 |
| 21F2 | 22 | ForceGetFirst | 2 |
| 225C | 22 | UnitForcedSallyByPID | PID_IKE |
| 2264 | 22 | UnitDontMoveSallyByPID | PID_IKE |
| 2340 | 24 | Dispos | bmap14_event4_c |
| 238D | 24 | TalkEvent | MS_14_EV_01 |
| 240A | 25 | BMGetTurn |  |
| 241A | 25 | BMGetTurn |  |
| 2479 | 25 | TalkEvent | MS_14_EV_02_01 |
| 248F | 25 | InstantDisposFirstSetMode | bmap14_z01_n, bmap14_z01_h, bmap14_z01_m |
| 24D7 | 25 | TalkEvent | MS_14_EV_02_02 |
| 24F2 | 25 | DisposContinueSetMode | bmap14_z01_n, bmap14_z01_h, bmap14_z01_m |
| 2554 | 26 | InstantDispos | bmap14_event2_c |
| 25AC | 26 | TalkEvent | MS_14_EV_03 |
| 25F0 | 26 | UnitEscapeByPID | PID_TIBARN |
| 25F8 | 26 | UnitEscapeByPID | PID_VULCI |
| 2600 | 26 | UnitEscapeByPID | PID_JANAFF |
| 2664 | 27 | BMGetPhase |  |
| 2751 | 28 | DisposSetMode | bmap14_z02_n, bmap14_z02_h, bmap14_z02_m |
| 2781 | 29 | DisposSetMode | bmap14_z02_n, bmap14_z02_h, bmap14_z02_m |
| 27B1 | 30 | DisposSetMode | bmap14_z02_n, bmap14_z02_h, bmap14_z02_m |
| 27DC | 31 | ForceGetCount | 1 |
| 27E5 | 31 | ForceGetFirst | 1 |
| 2B5B | 36 | TalkEvent | MS_14_TK01 |
| 2B65 | 36 | UnitTransferToForceByPID | PID_STELLA, 0 |
| 2C0B | 37 | TalkEvent | MS_14_TK02 |
| 2C15 | 37 | UnitTransferToForceByPID | PID_GATRIE, 0 |
| 2C7A | 38 | UnitGetForce | ? |
| 2C91 | 38 | TalkEvent | MS_14_TK_G_1B |
| 2C9C | 38 | TalkEvent | MS_14_TK_G_1A |
| 2CDA | 39 | TalkEvent | MS_14_TK_G_2 |
| 2D1A | 40 | TalkEvent | MS_14_TK_G_3 |
| 2D5A | 41 | TalkEvent | MS_14_TK_G_4 |
| 2D9A | 42 | TalkEvent | MS_14_TK_G_5 |
| 2DDA | 43 | TalkEvent | MS_14_TK_G_6 |
| 2E1A | 44 | TalkEvent | MS_14_TK_G_7 |
| 2E5A | 45 | TalkEvent | MS_14_TK_G_8 |
| 2E92 | 46 | LocalDieTalkWithBgmChange | ガトリー仲間, MS_14_DIE_GATRIE |
| 2EBA | 47 | LocalDieTalkWithBgmChange | ステラ仲間, MS_14_DIE_STELA |
| 2EE8 | 48 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2EF0 | 48 | TalkEvent | MS_14_BT_IKE |
| 2EFD | 48 | SoundBossTalkEnd |  |
| 2F30 | 49 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2F38 | 49 | TalkEvent | MS_14_BT_R1 |
| 2F45 | 49 | SoundBossTalkEnd |  |
| 2F78 | 50 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2F80 | 50 | TalkEvent | MS_14_BT_R1 |
| 2F8D | 50 | SoundBossTalkEnd |  |
| 2FD6 | 51 | BMGetPhase |  |
| 3016 | 51 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 301E | 51 | TalkEvent | MS_14_BT |
| 302B | 51 | SoundBossTalkEnd |  |
| 305C | 52 | TalkEvent | MS_14_DIE |
| 3090 | 53 | BMGetTurn |  |
| 30A5 | 53 | BMGetTurn |  |
| 30B1 | 53 | ForceGetCount | 1 |
| 313B | 54 | Dispos | bmap14_event3_c |
| 3150 | 54 | TalkEvent | MS_14_EV_04 |
| 319D | 54 | UnitTransferToForceByPID | PID_NAESALA, 3 |
| 31A7 | 54 | UnitTransferToForceByPID | PID_NEALUCHI, 3 |
| 31B0 | 54 | ForceGetCount | 2 |
| 31BF | 54 | ForceGetFirst | 2 |
| 31CE | 54 | UnitEscape | ?, 0 |
| 31E2 | 54 | ForceGetCount | 1 |
| 31EC | 54 | ForceGetFirst | 1 |
| 3228 | 54 | UnitEscape | ?, 0 |
| 3242 | 54 | ForceGetCount | 1 |
| 3254 | 54 | ForceGetCount | 1 |
| 3263 | 54 | ForceGetFirst | 1 |
| 3275 | 54 | UnitEscape | ?, 0 |
| 32B3 | 54 | TalkEvent | MS_14_ED_01 |
| 32BE | 54 | TalkEvent | MS_14_ED_01_2 |
| 332E | 54 | TalkEvent | MS_14_ED_02 |
| 3372 | 54 | AllUnitEscape |  |
| 3387 | 54 | InstantDispos | bmap14_event7_c |
| 341D | 54 | TalkEvent | MS_14_ED_03_00 |
| 3436 | 54 | AllUnitEscape |  |
| 3440 | 54 | AllUnitEscape |  |
| 346E | 54 | TalkEvent | MS_14_ED_03_01 |
| 3487 | 54 | TalkEvent | MS_14_ED_03 |
| 34A3 | 54 | TalkEvent | MS_14_ED_04 |
| 34BC | 54 | TalkEvent | MS_14_ED_05 |
| 34CD | 54 | TalkResume |  |
| 34F0 | 54 | TalkEvent | MS_14_ED_06 |
| 3570 | 55 | TalkEvent | MS_14_GAMEOVER |
| 35EA | 57 | SallyGetSurplus |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.14: Training — internal 15

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 13, 'h': 17, 'm': 17, 'n': 17}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap15/dispos_c.bin:bmap15_first_c`: F1: PID_MAKAROV
- `bmap15/dispos_c.bin:bmap15_mikata_c`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap15/dispos_h.bin:bmap15_first_h`: F1: PID_15_PEDDLING, PID_GASIRAMA
- `bmap15/dispos_h.bin:bmap15_mikata_h`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_GATRIE, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_STELLA, PID_TIAMAT, PID_WAYU
- `bmap15/dispos_h.bin:bmap15_z01_h`: F1: PID_15_PEDDLING_T
- `bmap15/dispos_m.bin:bmap15_first_m`: F1: PID_15_PEDDLING, PID_GASIRAMA
- `bmap15/dispos_m.bin:bmap15_mikata_m`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_GATRIE, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_STELLA, PID_TIAMAT, PID_WAYU
- `bmap15/dispos_m.bin:bmap15_z01_m`: F1: PID_15_PEDDLING_T
- `bmap15/dispos_n.bin:bmap15_first_n`: F1: PID_15_PEDDLING, PID_GASIRAMA
- `bmap15/dispos_n.bin:bmap15_mikata_n`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_GATRIE, PID_IKE, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_STELLA, PID_TIAMAT, PID_WAYU
- `bmap15/dispos_n.bin:bmap15_z01_n`: F1: PID_15_PEDDLING_T

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| D32 | 0 | regist | 情報１フラグ |
| D39 | 0 | regist | 情報２フラグ |
| D40 | 0 | regist | 情報３フラグ |
| D47 | 0 | regist | 情報４フラグ |
| D4E | 0 | regist | 情報５フラグ |
| D83 | 1 | TalkEvent | MS_15_INFO_02 |
| DCA | 2 | TalkEvent | MS_15_INFO_03 |
| E12 | 3 | TalkEvent | MS_15_INFO_04 |
| E5A | 4 | TalkEvent | MS_15_INFO_05 |
| F3C | 8 | TalkEvent | MS_15_VIL_03 |
| FBC | 9 | TalkEvent | MS_15_VIL_02 |
| 103C | 10 | TalkEvent | MS_15_VIL_01 |
| 10E7 | 12 | regist | 訪問１ |
| 10EF | 12 | regist | 訪問２ |
| 10F7 | 12 | regist | 訪問３ |
| 10FF | 12 | regist | F16022511 |
| 1153 | 14 | regist | 降参勧告イベント |
| 115B | 14 | regist | ラグズ増援トリガ |
| 1163 | 14 | regist | ラグズ増援イベント |
| 116B | 14 | regist | レテｖｓ虎 |
| 1173 | 14 | regist | モウディｖｓ虎 |
| 117B | 14 | regist | マカロフ仲間 |
| 1183 | 14 | regist | マカロフ戦闘 |
| 118B | 14 | regist | マカロフ戦闘マーシャ |
| 1193 | 14 | regist | ボス戦闘会話 |
| 119B | 14 | regist | ボス戦闘会話アイク |
| 11A3 | 14 | regist | ボス戦闘会話レテ |
| 11AB | 14 | regist | ボス戦闘会話モゥディ |
| 11E7 | 15 | InstantDisposRank | bmap15_first |
| 11EF | 15 | InstantDispos | bmap15_first_c |
| 1227 | 16 | SallySetByGroup | bmap15_mikata_c |
| 141F | 17 | TalkEvent | MS_15_GMAP_1 |
| 148E | 17 | TalkEvent | MS_15_GMAP_2 |
| 14E9 | 17 | TalkEvent | MS_15_GMAP_3 |
| 151A | 17 | TalkResume |  |
| 15A2 | 18 | ChapterMoviePlay | 15 |
| 15EF | 19 | ForceGetCount | 5 |
| 161B | 19 | MapLoad | bmap15 |
| 1629 | 19 | InstantDisposSetMode | bmap15_mikata_n, bmap15_mikata_h, bmap15_mikata_m |
| 162E | 19 | AllUnitEscape |  |
| 1733 | 19 | TalkEvent | MS_15_OP_01 |
| 1744 | 19 | TalkResume |  |
| 1755 | 19 | TalkResume |  |
| 1764 | 19 | TalkResume |  |
| 1773 | 19 | TalkResume |  |
| 17A7 | 19 | TalkEvent | MS_15_OP_02 |
| 17C5 | 19 | TalkResume |  |
| 17E0 | 19 | TalkResume |  |
| 1854 | 20 | TalkEvent | MS_15_OP_03 |
| 1880 | 20 | TalkEvent | MS_15_OP_04 |
| 18AF | 20 | MapLoad | bmap15 |
| 18E6 | 20 | InstantDisposRank | bmap15_first |
| 18EE | 20 | InstantDispos | bmap15_first_c |
| 18FD | 20 | SallySetByGroup | bmap15_mikata_c |
| 1905 | 20 | InstantDispos | bmap15_mikata_c |
| 19FF | 20 | TalkEvent | MS_15_OP_05_A |
| 1AB0 | 20 | TalkEvent | MS_15_OP_05_B |
| 1AE7 | 20 | TalkEvent | MS_15_OP_06 |
| 1B21 | 20 | UnitForcedSallyByPID | PID_IKE |
| 1B29 | 20 | UnitDontMoveSallyByPID | PID_IKE |
| 1BE0 | 22 | TalkEvent | MS_15_OP_X |
| 1C69 | 22 | TalkEvent | MS_15_OP_X2 |
| 1D41 | 23 | TalkEvent | MS_15_EV_02_N |
| 1D95 | 23 | TalkEvent | MS_15_EV_02_HM |
| 1DEF | 23 | TalkEvent | MS_15_EV_02_N |
| 1E19 | 23 | DisposSetMode | bmap15_z01_n, bmap15_z01_h, bmap15_z01_m |
| 1E6F | 24 | ForceGetCount | 1 |
| 1F25 | 24 | TalkEvent | MS_15_EV_01 |
| 1FBB | 25 | TalkEvent | MS_15_TK_01 |
| 1FC5 | 25 | UnitTransferToForceByPID | PID_MAKAROV, 0 |
| 2029 | 26 | BMGetPhase |  |
| 2036 | 26 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2041 | 26 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2049 | 26 | TalkEvent | MS_15_BT_RETHE_TIGER |
| 2056 | 26 | SoundBossTalkEnd |  |
| 2085 | 27 | BMGetPhase |  |
| 2092 | 27 | SoundBossTalkStart | BGM_BTL_PL01 |
| 209D | 27 | SoundBossTalkStart | BGM_BTL_CP01 |
| 20A5 | 27 | TalkEvent | MS_15_BT_MORDY_TIGER |
| 20B2 | 27 | SoundBossTalkEnd |  |
| 20E1 | 28 | BMGetPhase |  |
| 20EE | 28 | SoundBossTalkStart | BGM_BTL_PL01 |
| 20F9 | 28 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2101 | 28 | TalkEvent | MS_15_BT_MAKAROV_M |
| 210E | 28 | SoundBossTalkEnd |  |
| 2142 | 29 | BMGetPhase |  |
| 216F | 29 | BMGetPhase |  |
| 217C | 29 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2187 | 29 | SoundBossTalkStart | BGM_BTL_CP01 |
| 218F | 29 | TalkEvent | MS_15_BT_MAKAROV |
| 219C | 29 | SoundBossTalkEnd |  |
| 21D3 | 30 | DefaultDieTalk |  |
| 21DE | 30 | TalkEvent | MS_15_DIE_MAKAROV |
| 2213 | 31 | BMGetPhase |  |
| 224D | 31 | TalkEvent | MS_15_DIE_MARCIA |
| 225A | 31 | DefaultDieTalk |  |
| 2294 | 32 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 229C | 32 | TalkEvent | MS_15_BT_IKE |
| 22A9 | 32 | SoundBossTalkEnd |  |
| 22EC | 33 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 22F4 | 33 | TalkEvent | MS_15_BT_LE |
| 2301 | 33 | SoundBossTalkEnd |  |
| 233C | 34 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2344 | 34 | TalkEvent | MS_15_BT_MO |
| 2351 | 34 | SoundBossTalkEnd |  |
| 23A2 | 35 | BMGetPhase |  |
| 23E2 | 35 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 23EA | 35 | TalkEvent | MS_15_BT |
| 23EF | 35 | SoundBossTalkEnd |  |
| 2428 | 36 | TalkEvent | MS_15_DIE |
| 24CF | 37 | TalkEvent | MS_15_ED_00 |
| 2507 | 37 | AllUnitEscape |  |
| 252B | 37 | TalkEvent | MS_15_ED_01 |
| 25AB | 37 | TalkEvent | MS_15_ED_02 |
| 25C5 | 37 | TalkResume |  |
| 25DE | 37 | TalkResume |  |
| 266A | 39 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.15: The Feral Frontier — internal 16

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 14, 'h': 14, 'm': 14, 'n': 14}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap16/dispos_c.bin:bmap16_event1_c`: F2: PID_TOPUCK_EV
- `bmap16/dispos_c.bin:bmap16_event_2_c`: F2: PID_IKE_EV, PID_TOPUCK_EV
- `bmap16/dispos_c.bin:bmap16_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap16/dispos_c.bin:bmap16_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap16/dispos_c.bin:bmap16_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap16/dispos_c.bin:bmap16_first_c`: F1: PID_MWARIM
- `bmap16/dispos_c.bin:bmap16_m01_c`: F2: PID_SOANVALCKE
- `bmap16/dispos_c.bin:bmap16_mikata_c`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap16/dispos_h.bin:bmap16_first_h`: F1: PID_16_LIBERATION
- `bmap16/dispos_h.bin:bmap16_mikata_h`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap16/dispos_h.bin:bmap16_z02_h`: F1: PID_16_LIBERATION
- `bmap16/dispos_h.bin:bmap16_z03_h`: F1: PID_16_LIBERATION
- `bmap16/dispos_h.bin:bmap16_z04_h`: F1: PID_16_LIBERATION
- `bmap16/dispos_m.bin:bmap16_first_m`: F1: PID_16_LIBERATION
- `bmap16/dispos_m.bin:bmap16_mikata_m`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap16/dispos_m.bin:bmap16_z02_m`: F1: PID_16_LIBERATION
- `bmap16/dispos_m.bin:bmap16_z03_m`: F1: PID_16_LIBERATION
- `bmap16/dispos_m.bin:bmap16_z04_m`: F1: PID_16_LIBERATION
- `bmap16/dispos_n.bin:bmap16_first_n`: F1: PID_16_LIBERATION
- `bmap16/dispos_n.bin:bmap16_mikata_n`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap16/dispos_n.bin:bmap16_z02_n`: F1: PID_16_LIBERATION
- `bmap16/dispos_n.bin:bmap16_z03_n`: F1: PID_16_LIBERATION
- `bmap16/dispos_n.bin:bmap16_z04_n`: F1: PID_16_LIBERATION

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| F2E | 0 | regist | 情報１フラグ |
| F35 | 0 | regist | 情報２フラグ |
| F3C | 0 | regist | 情報３フラグ |
| F43 | 0 | regist | 情報４フラグ |
| F77 | 1 | TalkEvent | MS_16_INFO_01 |
| FB3 | 2 | TalkEvent | MS_16_INFO_02 |
| FFA | 3 | TalkEvent | MS_16_INFO_04 |
| 154F | 14 | regist | ソーンバルケ登場トリガ |
| 1557 | 14 | regist | 砂漠宝１ |
| 155F | 14 | regist | 砂漠宝２ |
| 1567 | 14 | regist | 砂漠宝３ |
| 156F | 14 | regist | 砂漠宝４ |
| 1577 | 14 | regist | 砂漠宝５ |
| 157F | 14 | regist | 砂漠宝６ |
| 1587 | 14 | regist | 砂漠宝７ |
| 158F | 14 | regist | 砂漠宝８ |
| 1597 | 14 | regist | 砂漠宝９ |
| 160B | 17 | regist | ソーンバルケ仲間 |
| 1613 | 17 | regist | ソーンバルケ顔見せ |
| 161B | 17 | regist | ソーンバルケイベント |
| 1623 | 17 | regist | ボス戦闘会話 |
| 162B | 17 | regist | ボス戦闘会話アイク |
| 1633 | 17 | regist | ボス戦闘会話レテ |
| 163B | 17 | regist | ボス戦闘会話モゥディ |
| 1643 | 17 | regist | ボス戦闘会話セネリオ |
| 164B | 17 | regist | ボス戦闘会話ヨファ |
| 1653 | 17 | regist | ボス戦闘会話ミスト |
| 165B | 17 | regist | ボス戦闘会話サザ |
| 1663 | 17 | regist | ムワリムをオンバトで倒した |
| 166B | 17 | regist | アイクがムワリム倒した |
| 1673 | 17 | regist | ラグズ解放軍死亡 |
| 16B6 | 18 | InstantDisposRank | bmap16_first |
| 16BE | 18 | InstantDispos | bmap16_first_c |
| 172F | 19 | SallySetByGroup | bmap16_mikata_c |
| 1765 | 20 | ForceGetCount | 5 |
| 1787 | 20 | MapLoad | bmap16 |
| 1795 | 20 | InstantDisposSetMode | bmap16_mikata_n, bmap16_mikata_h, bmap16_mikata_m |
| 179A | 20 | AllUnitEscape |  |
| 17AF | 20 | Join | always_dbg_mik_08 |
| 17B7 | 20 | Join | always_dbg_mik_09 |
| 17BF | 20 | Join | always_dbg_mik_10 |
| 17C7 | 20 | Join | always_dbg_mik_11 |
| 17CF | 20 | Join | always_dbg_mik_12 |
| 17D7 | 20 | Join | always_dbg_mik_13 |
| 17DF | 20 | Join | always_dbg_mik_14 |
| 17E7 | 20 | Join | always_dbg_mik_15 |
| 1828 | 20 | ChapterMoviePlay | 16 |
| 191B | 20 | TalkEvent | MS_16_OP_01 |
| 1934 | 20 | TalkResume |  |
| 1945 | 20 | TalkResume |  |
| 1956 | 20 | TalkResume |  |
| 1A0C | 20 | TalkEvent | MS_16_OP_02_1 |
| 1A7B | 21 | MapLoad | bmap16 |
| 1A9D | 21 | InstantDisposRank | bmap16_first |
| 1AA2 | 21 | AllUnitEscape |  |
| 1AB1 | 21 | SallySetByGroup | bmap16_mikata_c |
| 1AB9 | 21 | InstantDispos | bmap16_mikata_c |
| 1AD1 | 21 | Dispos_ForEventSenerio | bmap16_event_senerio_c, bmap16_event_senerio2_c, 1 |
| 1B18 | 21 | InstantDispos | bmap16_event1_c |
| 1B2E | 21 | InstantDispos | bmap16_first_c |
| 1B79 | 21 | TalkEvent | MS_16_OP_02_2 |
| 1C41 | 21 | TalkEvent | MS_16_OP_03 |
| 1CDA | 21 | DisposSetMode | bmap16_first_n, bmap16_first_h, bmap16_first_m |
| 1CE7 | 21 | UnitEscapeByPID | PID_TOPUCK_EV |
| 1E11 | 21 | TalkEvent | MS_16_OP_04 |
| 1E45 | 21 | UnitEscapeByPID | PID_SENERIO_EV |
| 1EBA | 21 | UnitForcedSallyByPID | PID_IKE |
| 1EC2 | 21 | UnitDontMoveSallyByPID | PID_IKE |
| 2015 | 23 | InstantDispos | bmap16_m01_c |
| 202B | 23 | UnitEscapeByPID | PID_SOANVALCKE |
| 2039 | 23 | TalkEvent | ? |
| 2080 | 23 | InstantDispos | bmap16_m01_c |
| 20AC | 23 | InstantDispos | bmap16_m01_c |
| 20D0 | 23 | Dispos | bmap16_m01_c |
| 20F8 | 23 | TalkEvent | ? |
| 2124 | 23 | TalkResume |  |
| 213A | 23 | TalkResume |  |
| 2144 | 23 | UnitTransferToForceByPID | PID_SOANVALCKE, 0 |
| 21BB | 23 | Dispos | bmap16_m01_c |
| 21FE | 23 | TalkEvent | MS_16_EV_02d |
| 2209 | 23 | TalkEvent | MS_16_EV_02C |
| 2243 | 23 | UnitEscapeByPID | PID_SOANVALCKE |
| 22AC | 25 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 22B3 | 25 | TalkEvent | ? |
| 22B8 | 25 | SoundBossTalkEnd |  |
| 230A | 26 | SoundBossTalkEnd |  |
| 245C | 32 | BMGetPhase |  |
| 24E2 | 33 | BMGetPhase |  |
| 252C | 33 | TalkEvent | MS_16_DIE |
| 25F7 | 34 | AllUnitEscape |  |
| 260E | 34 | TalkEvent | MS_16_ED_02X |
| 2641 | 34 | TalkEvent | MS_16_ED_03 |
| 267D | 34 | MapLoad | bmap18 |
| 26A9 | 34 | InstantDispos | bmap18_event_c16_1_c |
| 2756 | 34 | TalkEvent | MS_16_ED_04X |
| 2881 | 34 | TalkEvent | MS_16_ED_05 |
| 2964 | 34 | TalkEvent | MS_16_ED_06 |
| 2A83 | 34 | TalkEvent | MS_16_ED_07 |
| 2B01 | 34 | TalkEvent | MS_16_ED_08 |
| 2B12 | 34 | TalkResume |  |
| 2BB9 | 34 | TalkEvent | MS_16_ED_08_2 |
| 2C2E | 34 | AllUnitEscape |  |
| 2C50 | 34 | TalkEvent | MS_16_ED_09 |
| 2C84 | 34 | TalkEvent | MS_16_ED_10 |
| 2CFA | 36 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.16: The Atonement — internal 17

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 11, 'h': 11, 'm': 11, 'n': 11}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap17/dispos_c.bin:bmap17_event1_c`: F1: PID_OLIVER
- `bmap17/dispos_c.bin:bmap17_first_c`: F1: PID_DALAHOWE
- `bmap17/dispos_c.bin:bmap17_mikata_c`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_LOFA, PID_MARCIA, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_VOKE, PID_WAYU
- `bmap17/dispos_h.bin:bmap17_first_h`: F1: PID_178_TANAS, PID_KIMARSI
- `bmap17/dispos_h.bin:bmap17_mikata_h`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_LOFA, PID_MARCIA, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_VOKE, PID_WAYU
- `bmap17/dispos_h.bin:bmap17_z01_h`: F1: PID_12_THIEF
- `bmap17/dispos_h.bin:bmap17_z02_h`: F1: PID_178_TANAS
- `bmap17/dispos_h.bin:bmap17_z03_h`: F1: PID_178_TANAS
- `bmap17/dispos_m.bin:bmap17_first_m`: F1: PID_178_TANAS, PID_KIMARSI
- `bmap17/dispos_m.bin:bmap17_mikata_m`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_LOFA, PID_MARCIA, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_VOKE, PID_WAYU
- `bmap17/dispos_m.bin:bmap17_z01_m`: F1: PID_12_THIEF
- `bmap17/dispos_m.bin:bmap17_z02_m`: F1: PID_178_TANAS
- `bmap17/dispos_m.bin:bmap17_z03_m`: F1: PID_178_TANAS
- `bmap17/dispos_n.bin:bmap17_first_n`: F1: PID_178_TANAS, PID_KIMARSI
- `bmap17/dispos_n.bin:bmap17_mikata_n`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_LOFA, PID_MARCIA, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_VOKE, PID_WAYU
- `bmap17/dispos_n.bin:bmap17_z01_n`: F1: PID_12_THIEF
- `bmap17/dispos_n.bin:bmap17_z02_n`: F1: PID_178_TANAS
- `bmap17/dispos_n.bin:bmap17_z03_n`: F1: PID_178_TANAS

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| D42 | 0 | regist | 情報１フラグ |
| D49 | 0 | regist | 情報２フラグ |
| D50 | 0 | regist | 情報３フラグ |
| D57 | 0 | regist | 情報４フラグ |
| D5E | 0 | regist | 情報５フラグ |
| DBC | 1 | TalkEvent | MS_17_INFO_04 |
| E1A | 2 | TalkEvent | MS_17_INFO_05 |
| E54 | 2 | TalkEvent | MS_17_INFO_05_A |
| E83 | 2 | TalkEvent | MS_17_INFO_05_B |
| 112A | 13 | UnitEscape | ?, 0 |
| 1182 | 14 | UnitEscape | ?, 0 |
| 11B7 | 15 | regist | 宝箱１ |
| 11BF | 15 | regist | 宝箱２ |
| 11C7 | 15 | regist | 宝箱３ |
| 11CF | 15 | regist | 宝箱４ |
| 11D7 | 15 | regist | 宝箱５ |
| 11DF | 15 | regist | 宝箱６ |
| 11E7 | 15 | regist | F1217 |
| 11EF | 15 | regist | F2410 |
| 11F7 | 15 | regist | F0309 |
| 126F | 17 | regist | 増援トリガ１ |
| 1277 | 17 | regist | 増援トリガ２ |
| 127F | 17 | regist | 増援トリガ３ |
| 1287 | 17 | regist | 増援イベント１ |
| 128F | 17 | regist | 増援イベント２ |
| 1297 | 17 | regist | 増援イベント３ |
| 129F | 17 | regist | 盗賊配置 |
| 12A7 | 17 | regist | 盗賊ＣＰ変更 |
| 12AF | 17 | regist | ダラハウ仲間 |
| 12B7 | 17 | regist | ダラハウ戦闘子ども |
| 12BF | 17 | regist | ダラハウ戦闘 |
| 12C7 | 17 | regist | ボス戦闘会話 |
| 12CF | 17 | regist | ボス戦闘会話アイク |
| 12D7 | 17 | regist | ボス戦闘会話獣 |
| 131A | 18 | InstantDisposRank | bmap17_first |
| 1322 | 18 | InstantDispos | bmap17_first_c |
| 1363 | 19 | SallySetByGroup | bmap17_mikata_c |
| 1399 | 20 | ForceGetCount | 5 |
| 13BB | 20 | MapLoad | bmap17 |
| 13C9 | 20 | InstantDisposSetMode | bmap17_mikata_n, bmap17_mikata_h, bmap17_mikata_m |
| 13CE | 20 | AllUnitEscape |  |
| 1423 | 20 | ChapterMoviePlay | 17 |
| 1457 | 20 | TalkEvent | MS_17_OP_00 |
| 148C | 20 | TalkResume |  |
| 1554 | 20 | TalkEvent | MS_17_OP_01 |
| 1563 | 20 | TalkResume |  |
| 1572 | 20 | TalkResume |  |
| 1581 | 20 | TalkResume |  |
| 1596 | 20 | Join | always_c16 |
| 15E7 | 21 | MapLoad | bmap17 |
| 1621 | 21 | InstantDisposRank | bmap17_first |
| 1626 | 21 | AllUnitEscape |  |
| 1635 | 21 | InstantDispos | bmap17_first_c |
| 164B | 21 | SallySetByGroup | bmap17_mikata_c |
| 1653 | 21 | InstantDispos | bmap17_mikata_c |
| 1669 | 21 | InstantDispos | bmap17_event1_c |
| 1685 | 21 | TalkEvent | MS_17_OP_03 |
| 1692 | 21 | TalkResume |  |
| 169F | 21 | TalkResume |  |
| 16D3 | 21 | TalkEvent | MS_17_OP_04 |
| 16EC | 21 | TalkResume |  |
| 1798 | 21 | DisposSetMode | bmap17_first_n, bmap17_first_h, bmap17_first_m |
| 187D | 21 | TalkEvent | MS_17_OP_05 |
| 1916 | 21 | TalkEvent | MS_17_OP_06 |
| 1991 | 21 | UnitEscapeByPID | PID_OLIVER |
| 19A2 | 21 | UnitForcedSallyByPID | PID_IKE |
| 19AA | 21 | UnitDontMoveSallyByPID | PID_IKE |
| 1A22 | 23 | Dispos | bmap17_z01_m |
| 1A4F | 24 | BMGetTurn |  |
| 1A5F | 24 | BMGetTurn |  |
| 1A75 | 24 | DisposSetMode | bmap17_z01_n, bmap17_z01_h, bmap17_z01_m |
| 1AA6 | 25 | Dispos | bmap17_z02_m |
| 1AD6 | 26 | Dispos | bmap17_z03_m |
| 1B05 | 27 | DisposSetMode | bmap17_z02_n, bmap17_z02_h, bmap17_z02_m |
| 1B35 | 28 | DisposSetMode | bmap17_z03_n, bmap17_z03_h, bmap17_z03_m |
| 1BAA | 29 | TalkEvent | ? |
| 1BB4 | 29 | UnitTransferToForceByPID | PID_DALAHOWE, 0 |
| 1CE1 | 35 | BMGetPhase |  |
| 1CEE | 35 | SoundBossTalkStart | BGM_BTL_PL01 |
| 1CF9 | 35 | SoundBossTalkStart | BGM_BTL_CP01 |
| 1D01 | 35 | TalkEvent | MS_17_BT_DALAHOWE_CHILD |
| 1D0E | 35 | SoundBossTalkEnd |  |
| 1D3D | 36 | BMGetPhase |  |
| 1D4A | 36 | SoundBossTalkStart | BGM_BTL_PL01 |
| 1D55 | 36 | SoundBossTalkStart | BGM_BTL_CP01 |
| 1D5D | 36 | TalkEvent | MS_17_BT_DALAHOWE_CHILD |
| 1D6A | 36 | SoundBossTalkEnd |  |
| 1D99 | 37 | BMGetPhase |  |
| 1DA6 | 37 | SoundBossTalkStart | BGM_BTL_PL01 |
| 1DB1 | 37 | SoundBossTalkStart | BGM_BTL_CP01 |
| 1DB9 | 37 | TalkEvent | MS_17_BT_DALAHOWE_CHILD |
| 1DC6 | 37 | SoundBossTalkEnd |  |
| 1DF5 | 38 | BMGetPhase |  |
| 1E02 | 38 | SoundBossTalkStart | BGM_BTL_PL01 |
| 1E0D | 38 | SoundBossTalkStart | BGM_BTL_CP01 |
| 1E15 | 38 | TalkEvent | MS_17_BT_DALAHOWE_CHILD |
| 1E22 | 38 | SoundBossTalkEnd |  |
| 1E51 | 39 | BMGetPhase |  |
| 1E5E | 39 | SoundBossTalkStart | BGM_BTL_PL01 |
| 1E69 | 39 | SoundBossTalkStart | BGM_BTL_CP01 |
| 1E71 | 39 | TalkEvent | MS_17_BT_DALAHOWE_CHILD |
| 1E7E | 39 | SoundBossTalkEnd |  |
| 1ED9 | 40 | BMGetPhase |  |
| 1F26 | 40 | BMGetPhase |  |
| 1F33 | 40 | SoundBossTalkStart | BGM_BTL_PL01 |
| 1F3E | 40 | SoundBossTalkStart | BGM_BTL_CP01 |
| 1F46 | 40 | TalkEvent | MS_17_BT_DALAHOWE |
| 1F4B | 40 | SoundBossTalkEnd |  |
| 1F8B | 41 | DefaultDieTalk |  |
| 1F96 | 41 | TalkEvent | MS_17_DIE_DALAHOWE |
| 1FC8 | 42 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 1FD0 | 42 | TalkEvent | MS_17_BT_IKE |
| 1FDD | 42 | SoundBossTalkEnd |  |
| 2010 | 43 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2018 | 43 | TalkEvent | MS_17_BT_R1 |
| 2025 | 43 | SoundBossTalkEnd |  |
| 2058 | 44 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2060 | 44 | TalkEvent | MS_17_BT_R1 |
| 206D | 44 | SoundBossTalkEnd |  |
| 20A0 | 45 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 20A8 | 45 | TalkEvent | MS_17_BT_R1 |
| 20B5 | 45 | SoundBossTalkEnd |  |
| 2107 | 46 | BMGetPhase |  |
| 214F | 46 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2157 | 46 | TalkEvent | MS_17_BT |
| 2164 | 46 | SoundBossTalkEnd |  |
| 2194 | 47 | TalkEvent | MS_17_DIE |
| 21EF | 48 | AllUnitEscape |  |
| 2261 | 48 | TalkEvent | MS_17_ED_01 |
| 2280 | 48 | TalkResume |  |
| 2357 | 48 | TalkResume |  |
| 24E7 | 48 | TalkResume |  |
| 256F | 48 | TalkResume |  |
| 25A8 | 48 | TalkEvent | MS_17_ED_03 |
| 25B7 | 48 | TalkResume |  |
| 266E | 48 | TalkEvent | MS_17_ED_04 |
| 267B | 48 | TalkEvent | MS_17_ED_05 |
| 268C | 48 | TalkResume |  |
| 26A1 | 48 | TalkEvent | MS_17_ED_06 |
| 26BD | 48 | TalkResume |  |
| 26DE | 48 | TalkResume |  |
| 276A | 50 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.17: Day Breaks — internal 18

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 10, 'h': 15, 'm': 15, 'n': 15}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap18/dispos_c.bin:bmap18_event_c16_1_c`: F2: PID_NAESALA, PID_RIEUSION
- `bmap18/dispos_c.bin:bmap18_event_c16_2_c`: F2: PID_K_ZAKO
- `bmap18/dispos_c.bin:bmap18_event_janaff_c`: F2: PID_JANAFF
- `bmap18/dispos_c.bin:bmap18_event_learne2_c`: F2: PID_LEARNE_EV
- `bmap18/dispos_c.bin:bmap18_event_learne_c`: F2: PID_LEARNE
- `bmap18/dispos_c.bin:bmap18_event_narsil_c`: F2: PID_NASIR
- `bmap18/dispos_c.bin:bmap18_event_oliver2_c`: F1: PID_OLIVER
- `bmap18/dispos_c.bin:bmap18_event_oliver_c`: F1: PID_OLIVER, PID_ZAKO_EV1, PID_ZAKO_EV2, PID_ZAKO_EV3, PID_ZAKO_EV4, PID_ZAKO_EV5, PID_ZAKO_EV6, PID_ZAKO_EV7, PID_ZAKO_EV8, PID_ZAKO_EV9
- `bmap18/dispos_c.bin:bmap18_event_rieusion_c`: F2: PID_RIEUSION
- `bmap18/dispos_c.bin:bmap18_event_ryusion_c`: F2: PID_RIEUSION
- `bmap18/dispos_c.bin:bmap18_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap18/dispos_c.bin:bmap18_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap18/dispos_c.bin:bmap18_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap18/dispos_c.bin:bmap18_event_tibarn_c`: F2: PID_TIBARN
- `bmap18/dispos_c.bin:bmap18_event_tibern_c`: F2: PID_JANAFF, PID_TIBARN, PID_VULCI
- `bmap18/dispos_c.bin:bmap18_event_vulci_c`: F2: PID_VULCI
- `bmap18/dispos_c.bin:bmap18_mik02_c`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_LOFA, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_c.bin:bmap18_mik03_c`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_c.bin:bmap18_mik04_c`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_c.bin:bmap18_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU, PID_ZIHARK
- `bmap18/dispos_c.bin:bmap18_mikata_zoen_02_c`: F0: PID_BOLE, PID_OSCAR
- `bmap18/dispos_c.bin:bmap18_mikata_zoen_03_c`: F0: PID_BOLE, PID_OSCAR
- `bmap18/dispos_c.bin:bmap18_mikata_zoen_04_c`: F0: PID_BOLE, PID_OSCAR
- `bmap18/dispos_c.bin:bmap18_zoen_01_c`: F2: PID_JANAFF, PID_RIEUSION, PID_TIBARN, PID_VULCI
- `bmap18/dispos_h.bin:bmap18_f02_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_f03_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_f04_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_f_oliver_h`: F1: PID_OLIVER
- `bmap18/dispos_h.bin:bmap18_first_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_m02_h`: F2: PID_LEARNE
- `bmap18/dispos_h.bin:bmap18_m03_h`: F2: PID_LEARNE
- `bmap18/dispos_h.bin:bmap18_mik02_h`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_ZIHARK
- `bmap18/dispos_h.bin:bmap18_mik03_h`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_ZIHARK
- `bmap18/dispos_h.bin:bmap18_mik04_h`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_h.bin:bmap18_mikata_h`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_h.bin:bmap18_z01_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z02_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z03_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z04_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z05_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z06_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z07_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z08_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z09_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z10_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z11_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z12_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z13_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z14_h`: F1: PID_178_TANAS
- `bmap18/dispos_h.bin:bmap18_z15_h`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_f02_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_f03_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_f04_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_f_oliver_m`: F1: PID_OLIVER
- `bmap18/dispos_m.bin:bmap18_first_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_m02_m`: F2: PID_LEARNE
- `bmap18/dispos_m.bin:bmap18_m03_m`: F2: PID_LEARNE
- `bmap18/dispos_m.bin:bmap18_mik02_m`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_ZIHARK
- `bmap18/dispos_m.bin:bmap18_mik03_m`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_ZIHARK
- `bmap18/dispos_m.bin:bmap18_mik04_m`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_m.bin:bmap18_mikata_m`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_m.bin:bmap18_z01_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z02_2_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z02_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z03_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z04_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z05_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z06_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z07_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z08_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z09_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z10_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z11_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z12_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z13_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z14_m`: F1: PID_178_TANAS
- `bmap18/dispos_m.bin:bmap18_z15_m`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_f02_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_f03_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_f04_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_f_oliver_n`: F1: PID_OLIVER
- `bmap18/dispos_n.bin:bmap18_first_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_m02_n`: F2: PID_LEARNE
- `bmap18/dispos_n.bin:bmap18_m03_n`: F2: PID_LEARNE
- `bmap18/dispos_n.bin:bmap18_mik02_n`: F0: PID_BOLE, PID_CHAP, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_ZIHARK
- `bmap18/dispos_n.bin:bmap18_mik03_n`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_ZIHARK
- `bmap18/dispos_n.bin:bmap18_mik04_n`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_n.bin:bmap18_mikata_n`: F0: PID_BOLE, PID_CHAP, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MARCIA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_WAYU
- `bmap18/dispos_n.bin:bmap18_z01_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z02_2_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z02_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z03_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z04_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z05_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z06_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z07_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z08_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z09_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z10_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z11_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z12_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z13_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z14_n`: F1: PID_178_TANAS
- `bmap18/dispos_n.bin:bmap18_z15_n`: F1: PID_178_TANAS
- `bmap18_3/dispos_c.bin:bmap18_3_event01_c`: F2: PID_DUMMY1, PID_DUMMY2, PID_IKE_EV, PID_NASIR, PID_SIGRUN, PID_TANIS
- `bmap18_3/dispos_c.bin:bmap18_3_event02_c`: F2: PID_JANAFF, PID_LEARNE_EV, PID_RIEUSION, PID_TIBARN, PID_VULCI
- `bmap18_3/dispos_c.bin:bmap18_3_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap18_3/dispos_c.bin:bmap18_3_event_senerio_c`: F2: PID_SENERIO_EV

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 1F56 | 0 | regist | 情報１フラグ |
| 1F5D | 0 | regist | 情報２フラグ |
| 1F64 | 0 | regist | 情報３フラグ |
| 1F6B | 0 | regist | 情報４フラグ |
| 1F9F | 1 | TalkEvent | MS_18_INFO_01 |
| 1FFB | 2 | TalkEvent | MS_18_INFO_02 |
| 204E | 3 | TalkEvent | MS_18_INFO_04 |
| 2B43 | 31 | regist | F19082709 |
| 2B4B | 31 | regist | F20102710 |
| 2B53 | 31 | regist | F21112711 |
| 2B5B | 31 | regist | F06002707 |
| 2B63 | 31 | regist | 鳥さんたち増援トリガ |
| 2B6B | 31 | regist | S2増援トリガ１ |
| 2B73 | 31 | regist | S2増援トリガ２ |
| 2B7B | 31 | regist | S3増援トリガ２ |
| 2B83 | 31 | regist | S3増援トリガ１ |
| 2B8B | 31 | regist | S3増援トリガ４ |
| 2B93 | 31 | regist | S3増援トリガ５ |
| 2B9B | 31 | regist | F28043113 |
| 2BA3 | 31 | regist | F32043908 |
| 2BAB | 31 | regist | F46165126 |
| 2BB3 | 31 | regist | F39204526 |
| 2BBB | 31 | regist | S3増援トリガ３ |
| 2BC3 | 31 | regist | S4増援トリガ１ |
| 2C17 | 33 | regist | クリア条件１ |
| 2C1F | 33 | regist | クリア条件２ |
| 2C27 | 33 | regist | クリア条件３ |
| 2C2F | 33 | regist | セクション２ |
| 2C37 | 33 | regist | セクション３ |
| 2C3F | 33 | regist | セクション４ |
| 2C47 | 33 | regist | 味方増援呼んだ２ |
| 2C4F | 33 | regist | 味方増援呼んだ３ |
| 2C57 | 33 | regist | 味方増援呼んだ４ |
| 2C5F | 33 | regist | 味方増援イベント２ |
| 2C67 | 33 | regist | 味方増援イベント３ |
| 2C6F | 33 | regist | 味方増援イベント４ |
| 2C77 | 33 | regist | エンディングその２ |
| 2C7F | 33 | regist | アイクリアーネ |
| 2C87 | 33 | regist | アイクリアーネイベント |
| 2C8F | 33 | regist | 鳥さんたち増援トリガ |
| 2C97 | 33 | regist | 鳥さんたち増援イベント |
| 2C9F | 33 | regist | ボス戦闘会話 |
| 2CA7 | 33 | regist | ボス戦闘会話アイク |
| 2CAF | 33 | regist | ボス戦闘会話レテ |
| 2CB7 | 33 | regist | ボス戦闘会話モゥディ |
| 2CBF | 33 | regist | ボス戦闘会話ムワリム |
| 2CC7 | 33 | regist | ボス戦闘会話ダラハウ |
| 2CD5 | 33 | regist | S4増援イベント１ |
| 2CDD | 33 | regist | S4増援イベント２ |
| 2CE5 | 33 | regist | S4増援イベント３ |
| 2CED | 33 | regist | S4増援イベント４ |
| 2CF5 | 33 | regist | S4増援イベント５ |
| 2CFD | 33 | regist | S4増援トリガ１ |
| 2D05 | 33 | regist | S4増援トリガ２ |
| 2D0D | 33 | regist | S2増援イベント１ |
| 2D15 | 33 | regist | S2増援イベント２ |
| 2D1D | 33 | regist | S3増援イベント１ |
| 2D25 | 33 | regist | S3増援イベント２ |
| 2D2D | 33 | regist | S3増援イベント３ |
| 2D35 | 33 | regist | S3増援イベント４ |
| 2D3D | 33 | regist | S3増援イベント５ |
| 2D7A | 34 | InstantDisposRank | bmap18_first |
| 2DBB | 35 | SallySetByGroup | bmap18_mikata_c |
| 2DF1 | 36 | ForceGetCount | 5 |
| 2E0E | 36 | MapLoad | bmap18 |
| 2E1C | 36 | InstantDisposSetMode | bmap18_mikata_n, bmap18_mikata_h, bmap18_mikata_m |
| 2E21 | 36 | AllUnitEscape |  |
| 2E36 | 36 | Join | always_dbg_mik_04c |
| 2E3E | 36 | Join | always_dbg_mik_08 |
| 2E46 | 36 | Join | always_dbg_mik_09 |
| 2E4E | 36 | Join | always_dbg_mik_10 |
| 2E56 | 36 | Join | always_dbg_mik_11 |
| 2E5E | 36 | Join | always_dbg_mik_12 |
| 2E66 | 36 | Join | always_dbg_mik_13 |
| 2E6E | 36 | Join | always_dbg_mik_14 |
| 2E76 | 36 | Join | always_dbg_mik_15 |
| 2E7E | 36 | Join | always_dbg_mik_16 |
| 2E86 | 36 | Join | always_dbg_mik_17 |
| 2E97 | 36 | UnitTransferToForceByPID | PID_CHINON, 7 |
| 2ED8 | 36 | ChapterMoviePlay | 18 |
| 2FCA | 36 | TalkEvent | MS_18_OP_01 |
| 3087 | 36 | TalkEvent | MS_18_OP_01_2 |
| 30FF | 37 | MapLoad | bmap18_3 |
| 311A | 37 | InstantDispos | bmap18_3_event01_c |
| 3127 | 37 | Dispos_ForEventSenerio | bmap18_3_event_senerio_c, bmap18_3_event_senerio2_c, 1 |
| 3241 | 37 | TalkEvent | MS_18_OP_02 |
| 32B4 | 37 | TalkEvent | MS_18_OP_02_2 |
| 333E | 37 | AllUnitEscape |  |
| 335B | 37 | MapLoad | bmap18 |
| 337F | 37 | InstantDispos | bmap18_event_oliver_c |
| 3387 | 37 | SallySetByGroup | bmap18_mikata_c |
| 338F | 37 | InstantDispos | bmap18_mikata_c |
| 3394 | 37 | AllUnitEscape |  |
| 33A3 | 37 | InstantDispos | bmap18_mikata_c |
| 33CF | 37 | ForceGetCount | 0 |
| 33D8 | 37 | ForceGetFirst | 0 |
| 3532 | 37 | TalkEvent | MS_18_OP_03 |
| 3542 | 37 | InstantDispos | bmap18_event_oliver_c |
| 36F7 | 37 | TalkEvent | MS_18_OP_04 |
| 37BC | 37 | UnitEscapeByPID | PID_OLIVER |
| 37C4 | 37 | UnitEscapeByPID | PID_ZAKO_EV1 |
| 37CC | 37 | UnitEscapeByPID | PID_ZAKO_EV2 |
| 37D4 | 37 | UnitEscapeByPID | PID_ZAKO_EV3 |
| 37DC | 37 | UnitEscapeByPID | PID_ZAKO_EV4 |
| 37E4 | 37 | UnitEscapeByPID | PID_ZAKO_EV5 |
| 37EC | 37 | UnitEscapeByPID | PID_ZAKO_EV6 |
| 37F4 | 37 | UnitEscapeByPID | PID_ZAKO_EV7 |
| 37FC | 37 | UnitEscapeByPID | PID_ZAKO_EV8 |
| 3804 | 37 | UnitEscapeByPID | PID_ZAKO_EV9 |
| 3872 | 37 | DisposSetMode | bmap18_first_n, bmap18_first_h, bmap18_first_m |
| 3889 | 37 | TalkEvent | MS_18_OP_05_01 |
| 38D3 | 37 | ForceGetCount | 0 |
| 38DC | 37 | ForceGetFirst | 0 |
| 3921 | 37 | TalkEvent | MS_18_OP_05_02 |
| 399D | 37 | UnitForcedSallyByPID | PID_IKE |
| 39A5 | 37 | UnitDontMoveSallyByPID | PID_IKE |
| 3A30 | 39 | DisposSetMode | bmap18_z01_n, bmap18_z01_h, bmap18_z01_m |
| 3A6C | 40 | DisposSetMode | bmap18_z02_n, bmap18_z02_h, bmap18_z02_m |
| 3AA8 | 41 | DisposSetMode | bmap18_z03_n, bmap18_z03_h, bmap18_z03_m |
| 3AEE | 42 | DisposSetMode | bmap18_z07_n, bmap18_z07_h, bmap18_z07_m |
| 3B45 | 43 | DisposSetMode | bmap18_z06_n, bmap18_z06_h, bmap18_z06_m |
| 3B9D | 44 | DisposSetMode | bmap18_z05_n, bmap18_z05_h, bmap18_z05_m |
| 3BE2 | 45 | DisposSetMode | bmap18_z12_n, bmap18_z12_h, bmap18_z12_m |
| 3C26 | 46 | DisposSetMode | bmap18_z13_n, bmap18_z13_h, bmap18_z13_m |
| 3C6A | 47 | DisposSetMode | bmap18_z11_n, bmap18_z11_h, bmap18_z11_m |
| 3CAE | 48 | DisposSetMode | bmap18_z14_n, bmap18_z14_h, bmap18_z14_m |
| 3CF2 | 49 | DisposSetMode | bmap18_z14_n, bmap18_z14_h, bmap18_z14_m |
| 3D3E | 50 | DisposSetMode | bmap18_z07_n, bmap18_z07_h, bmap18_z07_m |
| 3D8A | 51 | DisposSetMode | bmap18_z08_n, bmap18_z08_h, bmap18_z08_m |
| 3DD6 | 52 | DisposSetMode | bmap18_z09_n, bmap18_z09_h, bmap18_z09_m |
| 3E22 | 53 | DisposSetMode | bmap18_z10_n, bmap18_z10_h, bmap18_z10_m |
| 3FBB | 56 | DisposSetMode | bmap18_z04_n, bmap18_z04_h, bmap18_z04_m |
| 4006 | 57 | DisposSetMode | bmap18_z15_n, bmap18_z15_h, bmap18_z15_m |
| 4034 | 58 | TalkEvent | MS_18_EV_Z_TIAMAT |
| 404C | 58 | TalkEvent | MS_18_EV_Z_SENERIO |
| 4064 | 58 | TalkEvent | MS_18_EV_Z_OSCAR |
| 407C | 58 | TalkEvent | MS_18_EV_Z_BOLE |
| 4094 | 58 | TalkEvent | MS_18_EV_Z_KILROY |
| 40AC | 58 | TalkEvent | MS_18_EV_Z_WAYU |
| 40C4 | 58 | TalkEvent | MS_18_EV_Z_MIST |
| 40DC | 58 | TalkEvent | MS_18_EV_Z_LOFA |
| 40F4 | 58 | TalkEvent | MS_18_EV_Z_MARSHA |
| 410C | 58 | TalkEvent | MS_18_EV_Z_LETE |
| 4124 | 58 | TalkEvent | MS_18_EV_Z_MORDY |
| 413C | 58 | TalkEvent | MS_18_EV_Z_VOKE |
| 4154 | 58 | TalkEvent | MS_18_EV_Z_KEVIN |
| 416C | 58 | TalkEvent | MS_18_EV_Z_CHAP |
| 4184 | 58 | TalkEvent | MS_18_EV_Z_NEFENEE |
| 419C | 58 | TalkEvent | MS_18_EV_Z_ZIHARK |
| 41B4 | 58 | TalkEvent | MS_18_EV_Z_ELAICE |
| 41CC | 58 | TalkEvent | MS_18_EV_Z_SOTHE |
| 41E3 | 58 | TalkEvent | MS_18_EV_Z_JILL |
| 41FB | 58 | TalkEvent | MS_18_EV_Z_STELLA |
| 4213 | 58 | TalkEvent | MS_18_EV_Z_GATREE |
| 422B | 58 | TalkEvent | MS_18_EV_Z_MAKAROV |
| 4243 | 58 | TalkEvent | MS_18_EV_Z_SOANVALCKE |
| 425B | 58 | TalkEvent | MS_18_EV_Z_MWARIM |
| 4273 | 58 | TalkEvent | MS_18_EV_Z_TOPUCK |
| 428B | 58 | TalkEvent | MS_18_EV_Z_DALAHOWE |
| 42B4 | 59 | ForceGetCount | 0 |
| 42BD | 59 | ForceGetFirst | 0 |
| 43D8 | 60 | DisposAuxiliary | bmap18_mikata_zoen_02_c |
| 449D | 60 | DisposAuxiliary | bmap18_mikata_zoen_03_c |
| 4561 | 60 | DisposAuxiliary | bmap18_mikata_zoen_04_c |
| 4731 | 62 | InstantDispos | bmap18_zoen_01_c |
| 4827 | 62 | TalkEvent | MS_18_EV_D_ev |
| 48FC | 62 | TalkEvent | MS_18_EV_D_ev_2 |
| 4945 | 62 | TalkResume |  |
| 495E | 62 | TalkResume |  |
| 4A78 | 63 | BMGetTurn |  |
| 4A7E | 63 | BMGetTurn |  |
| 5230 | 70 | LocalDieTalkWithBgmChange | , MS_18_DIE_RIEUSION |
| 523E | 70 | LocalDieTalkWithBgmChange | , MS_18_DIE_RIEUSION_2 |
| 526E | 71 | LocalDieTalkWithBgmChange | , MS_18_DIE_JANAFF |
| 529E | 72 | LocalDieTalkWithBgmChange | , MS_18_DIE_VULCI |
| 52CE | 73 | LocalDieTalkWithBgmChange | , MS_18_DIE_TIBARN |
| 5304 | 74 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 530C | 74 | TalkEvent | MS_18_BT_IKE |
| 5319 | 74 | SoundBossTalkEnd |  |
| 534C | 75 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 5354 | 75 | TalkEvent | MS_18_BT_LE |
| 5361 | 75 | SoundBossTalkEnd |  |
| 5394 | 76 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 539C | 76 | TalkEvent | MS_18_BT_MO |
| 53A9 | 76 | SoundBossTalkEnd |  |
| 53DC | 77 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 53E4 | 77 | TalkEvent | MS_18_BT_MW |
| 53F1 | 77 | SoundBossTalkEnd |  |
| 5424 | 78 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 542C | 78 | TalkEvent | MS_18_BT_DA |
| 5439 | 78 | SoundBossTalkEnd |  |
| 5496 | 79 | BMGetPhase |  |
| 54E6 | 79 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 54EE | 79 | TalkEvent | MS_18_BT |
| 54FB | 79 | SoundBossTalkEnd |  |
| 552C | 80 | TalkEvent | MS_18_DIE |
| 5566 | 81 | ForceGetCount | 0 |
| 5574 | 81 | ForceGetFirst | 0 |
| 56B2 | 82 | BMGetTurn |  |
| 5714 | 82 | ForceGetFirst | 1 |
| 5729 | 82 | UnitEscape | ?, 0 |
| 5749 | 82 | ForceGetCount | 5 |
| 5765 | 82 | TalkEvent | MS_18_EV_A_ed |
| 5777 | 82 | TalkEvent | MS_18_EV_A_ed_T |
| 5782 | 82 | TalkEvent | MS_18_EV_A_ed_N |
| 578D | 82 | TalkEvent | MS_18_EV_A_ed_B |
| 579F | 82 | TalkEvent | MS_18_EV_A_ed_T |
| 57AA | 82 | TalkEvent | MS_18_EV_A_ed_N2 |
| 57C4 | 82 | Complete18 | 1 |
| 57F2 | 83 | BMSetTurn | 1 |
| 580A | 83 | MapLoad | bmap18 |
| 5833 | 83 | InstantDispos | bmap18_event_tibern_c |
| 5865 | 83 | InstantDispos | bmap18_event_ryusion_c |
| 5912 | 83 | TalkEvent | MS_18_EV_B_op |
| 595D | 83 | UnitEscapeByPID | PID_TIBARN |
| 5965 | 83 | UnitEscapeByPID | PID_VULCI |
| 596D | 83 | UnitEscapeByPID | PID_JANAFF |
| 597E | 83 | InstantDisposSetMode | bmap18_f02_n, bmap18_f02_h, bmap18_f02_m |
| 59C5 | 83 | TalkEvent | MS_18_EV_B_op_1 |
| 59D5 | 83 | TalkEvent | MS_18_EV_B_op_2_A |
| 59E5 | 83 | TalkEvent | MS_18_EV_B_op_2_B |
| 59F0 | 83 | TalkEvent | MS_18_EV_B_op_2_C |
| 5A00 | 83 | TalkEvent | MS_18_EV_B_op_2_D |
| 5A10 | 83 | TalkEvent | MS_18_EV_B_op_2_E |
| 5A1B | 83 | TalkEvent | MS_18_EV_B_op_2_F |
| 5AE6 | 83 | TalkEvent | MS_18_EV_B_op_3 |
| 5B58 | 83 | UnitEscapeByPID | PID_RIEUSION |
| 5B92 | 83 | ForceGetCount | 5 |
| 5B9E | 83 | DispLoadWholeForce | 5 |
| 5BDB | 83 | ForceGetCount | 5 |
| 5BE4 | 83 | ForceGetFirst | 5 |
| 5CC3 | 83 | TalkEvent | MS_18_EV_B_op_4_0 |
| 5D7F | 83 | TalkEvent | MS_18_EV_B_op_4A |
| 5D8A | 83 | TalkEvent | MS_18_EV_B_op_4A_B |
| 5D9F | 83 | TalkEvent | MS_18_EV_B_op_4B |
| 5DAA | 83 | TalkEvent | MS_18_EV_B_op_4B_B |
| 5E26 | 85 | BMGetTurn |  |
| 5E93 | 85 | ForceGetFirst | 1 |
| 5EA8 | 85 | UnitEscape | ?, 0 |
| 5EC8 | 85 | ForceGetCount | 5 |
| 5EDF | 85 | TalkEvent | MS_18_EV_B_ed |
| 5EEA | 85 | TalkEvent | MS_18_EV_B_ed_B |
| 5F00 | 85 | Complete18 | 2 |
| 5F2E | 86 | BMSetTurn | 1 |
| 5F46 | 86 | MapLoad | bmap18 |
| 5F5C | 86 | InstantDisposRank | bmap18_f03 |
| 5F65 | 86 | ForceGetCount | 1 |
| 5F6E | 86 | ForceGetFirst | 1 |
| 5FA6 | 86 | InstantDispos | bmap18_event_narsil_c |
| 5FF7 | 86 | ForceGetCount | 0 |
| 6005 | 86 | ForceGetFirst | 0 |
| 6096 | 86 | InstantDispos | bmap18_event_learne_c |
| 609E | 86 | InstantDispos | bmap18_event_learne2_c |
| 60E7 | 86 | TalkEvent | MS_18_EV_C_op_00_A |
| 60F2 | 86 | TalkEvent | MS_18_EV_C_op_00_B |
| 61F9 | 86 | TalkEvent | MS_18_EV_C_op_000 |
| 62BE | 86 | TalkEvent | MS_18_EV_C_op_01 |
| 62E0 | 86 | TalkEvent | MS_18_EV_C_op_01_B2 |
| 630D | 86 | TalkEvent | MS_18_EV_C_op_02 |
| 637B | 86 | TalkEvent | MS_18_EV_C_op_03 |
| 63FD | 86 | TalkEvent | MS_18_EV_C_op_04 |
| 6408 | 86 | TalkEvent | MS_18_EV_C_op_04_B |
| 6454 | 86 | InstantDispos | bmap18_event_oliver2_c |
| 64B3 | 86 | TalkEvent | MS_18_EV_C_op_05 |
| 6513 | 86 | TalkEvent | MS_18_EV_C_op_05_2 |
| 6657 | 86 | DisposSetMode | bmap18_f03_n, bmap18_f03_h, bmap18_f03_m |
| 6678 | 86 | UnitEscapeByPID | PID_LEARNE_EV |
| 6680 | 86 | UnitEscapeByPID | PID_NASIR |
| 6688 | 86 | UnitEscapeByPID | PID_OLIVER |
| 66F7 | 86 | TalkEvent | MS_18_EV_C_op_05_3 |
| 6714 | 86 | ForceGetCount | 0 |
| 671E | 86 | ForceGetFirst | 0 |
| 694B | 86 | BMGetTurn |  |
| 697C | 86 | UnitEscape | ?, 0 |
| 6995 | 86 | ForceGetCount | 5 |
| 69D7 | 86 | DispLoadWholeForce | 5 |
| 6A19 | 86 | ForceGetCount | 5 |
| 6A22 | 86 | ForceGetFirst | 5 |
| 6AEA | 87 | ForceGetCount | 0 |
| 6AF8 | 87 | ForceGetFirst | 0 |
| 6C8E | 88 | BMGetTurn |  |
| 6D27 | 88 | InstantDispos | bmap18_event_oliver2_c |
| 6D7C | 88 | TalkEvent | MS_18_EV_C_ed |
| 6DA7 | 88 | UnitEscapeByPID | PID_OLIVER |
| 6DDD | 88 | ForceGetFirst | 1 |
| 6DF2 | 88 | UnitEscape | ?, 0 |
| 6E1A | 88 | InstantDispos | bmap18_event_narsil_c |
| 6F89 | 88 | TalkEvent | MS_18_EV_C_ed_XA |
| 6FE6 | 88 | TalkEvent | MS_18_EV_C_ed_XA_2 |
| 7019 | 88 | TalkEvent | MS_18_EV_C_ed_XB |
| 702C | 88 | TalkEvent | MS_18_EV_C_ed_XC |
| 703B | 88 | ForceGetCount | 5 |
| 70C7 | 88 | TalkEvent | MS_18_EV_C_ed_A |
| 70D2 | 88 | TalkEvent | MS_18_EV_C_ed_B |
| 7100 | 88 | UnitEscapeByPID | PID_NASIR |
| 713A | 88 | Complete18 | 3 |
| 7166 | 89 | BMSetTurn | 1 |
| 717E | 89 | MapLoad | bmap18 |
| 71A2 | 89 | InstantDisposRank | bmap18_f04 |
| 71AB | 89 | ForceGetCount | 1 |
| 71B4 | 89 | ForceGetFirst | 1 |
| 722E | 89 | InstantDisposRank | bmap18_f_oliver |
| 7261 | 89 | InstantDispos | bmap18_event_ryusion_c |
| 7277 | 89 | InstantDispos | bmap18_event_tibern_c |
| 72F1 | 89 | TalkEvent | MS_18_EV_D_op |
| 73C3 | 89 | TalkEvent | MS_18_EV_D_op_2 |
| 73E2 | 89 | TalkResume |  |
| 73F1 | 89 | TalkResume |  |
| 73F6 | 89 | TalkResume |  |
| 7526 | 89 | UnitEscapeByPID | PID_RIEUSION |
| 752E | 89 | UnitEscapeByPID | PID_TIBARN |
| 7536 | 89 | UnitEscapeByPID | PID_VULCI |
| 753E | 89 | UnitEscapeByPID | PID_JANAFF |
| 75EF | 89 | TalkEvent | MS_18_EV_D_op_4 |
| 7673 | 89 | DisposSetMode | bmap18_f04_n, bmap18_f04_h, bmap18_f04_m |
| 7681 | 89 | DisposContinueSetMode | bmap18_f_oliver_n, bmap18_f_oliver_h, bmap18_f_oliver_m |
| 76F4 | 89 | TalkEvent | MS_18_EV_D_op_5 |
| 77A0 | 89 | UnitEscape | ?, 0 |
| 77E6 | 89 | ForceGetCount | 5 |
| 77F2 | 89 | DispLoadWholeForce | 5 |
| 782F | 89 | ForceGetCount | 5 |
| 7838 | 89 | ForceGetFirst | 5 |
| 7917 | 90 | ForceGetCount | 1 |
| 7921 | 90 | ForceGetFirst | 1 |
| 7980 | 90 | ForceGetCount | 1 |
| 798A | 90 | ForceGetFirst | 1 |
| 79E9 | 90 | ForceGetCount | 1 |
| 79F3 | 90 | ForceGetFirst | 1 |
| 7A70 | 91 | ForceGetCount | 1 |
| 7B0A | 93 | ForceGetCount | 0 |
| 7B18 | 93 | ForceGetFirst | 0 |
| 7D17 | 94 | ForceGetFirst | 1 |
| 7D2C | 94 | UnitEscape | ?, 0 |
| 7D38 | 94 | ForceGetCount | 0 |
| 7D41 | 94 | ForceGetFirst | 0 |
| 7D92 | 94 | InstantDispos | bmap18_event_rieusion_c |
| 7DA5 | 94 | InstantDispos | bmap18_event_tibarn_c |
| 7DB8 | 94 | InstantDispos | bmap18_event_vulci_c |
| 7DCB | 94 | InstantDispos | bmap18_event_janaff_c |
| 7E38 | 94 | InstantDispos | bmap18_event_learne2_c |
| 7ECB | 94 | TalkEvent | MS_18_ED_01 |
| 7ED7 | 94 | TalkResume |  |
| 7EE6 | 94 | TalkResume |  |
| 7F7F | 94 | TalkEvent | MS_18_ED_02 |
| 7F9B | 94 | TalkResume |  |
| 7FD6 | 94 | AllUnitEscape |  |
| 7FF9 | 94 | MapLoad | bmap18_3 |
| 801B | 94 | InstantDispos | bmap18_3_event01_c |
| 8098 | 94 | Dispos_ForEventSenerio | bmap18_3_event_senerio_c, bmap18_3_event_senerio2_c, 1 |
| 80AE | 94 | InstantDispos | bmap18_3_event02_c |
| 8141 | 94 | TalkEvent | MS_18_ED_03_1 |
| 81EE | 94 | TalkEvent | MS_18_ED_03_1_2 |
| 827E | 94 | TalkEvent | MS_18_ED_03_1_3 |
| 8312 | 94 | TalkEvent | MS_18_ED_03_2 |
| 836A | 94 | AllUnitEscape |  |
| 8381 | 94 | TalkEvent | MS_18_ED_04 |
| 83B5 | 94 | TalkEvent | MS_18_ED_05 |
| 84BD | 94 | TalkEvent | MS_18_ED_06_00 |
| 84F4 | 94 | TalkEvent | MS_18_ED_06 |
| 8572 | 96 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.18: Crimea Marches — internal 19

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 9, 'h': 23, 'm': 23, 'n': 23}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap19/dispos_c.bin:bmap19_engn0_c`: F3: PID_MELTY
- `bmap19/dispos_c.bin:bmap19_event1_c`: F2: PID_NAESALA
- `bmap19/dispos_c.bin:bmap19_event_birds_c`: F2: PID_LEARNE, PID_TIBARN
- `bmap19/dispos_c.bin:bmap19_event_elinsia_c`: F2: PID_DUMMY1
- `bmap19/dispos_c.bin:bmap19_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap19/dispos_c.bin:bmap19_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap19/dispos_c.bin:bmap19_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap19/dispos_c.bin:bmap19_m01_c`: F0: PID_TANIS
- `bmap19/dispos_c.bin:bmap19_m_birds_c`: F2: PID_JANAFF, PID_RIEUSION, PID_VULCI
- `bmap19/dispos_c.bin:bmap19_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TIAMAT, PID_VOKE, PID_ZIHARK
- `bmap19/dispos_h.bin:bmap19_boss_h`: F1: PID_KAYACHE
- `bmap19/dispos_h.bin:bmap19_chinon_h`: F1: PID_CHINON
- `bmap19/dispos_h.bin:bmap19_engn0_h`: F3: PID_MELTY
- `bmap19/dispos_h.bin:bmap19_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_DKN, PID_DAYNE_FIG, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PRS, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_WAR
- `bmap19/dispos_h.bin:bmap19_mikata_h`: F0: PID_BOLE, PID_CHINON, PID_DALAHOWE, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MAKAROV, PID_MARCIA, PID_MIST, PID_MORDY, PID_MWARIM, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_SOTHE, PID_TIAMAT, PID_TOPUCK, PID_VOKE, PID_WAYU, PID_ZIHARK
- `bmap19/dispos_h.bin:bmap19_z02_h`: F1: PID_K_ZAKO
- `bmap19/dispos_h.bin:bmap19_z03_h`: F1: PID_DAYNE_SKN
- `bmap19/dispos_h.bin:bmap19_z04_h`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN
- `bmap19/dispos_h.bin:bmap19_zoen1_h`: F1: PID_K_ZAKO
- `bmap19/dispos_m.bin:bmap19_boss_m`: F1: PID_KAYACHE
- `bmap19/dispos_m.bin:bmap19_chinon_m`: F1: PID_CHINON
- `bmap19/dispos_m.bin:bmap19_engn0_m`: F3: PID_MELTY
- `bmap19/dispos_m.bin:bmap19_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_DKN, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PRS, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_WAR
- `bmap19/dispos_m.bin:bmap19_mikata_m`: F0: PID_BOLE, PID_CHINON, PID_DALAHOWE, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MAKAROV, PID_MARCIA, PID_MIST, PID_MORDY, PID_MWARIM, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_SOTHE, PID_TIAMAT, PID_TOPUCK, PID_VOKE, PID_WAYU, PID_ZIHARK
- `bmap19/dispos_m.bin:bmap19_z02_m`: F1: PID_K_ZAKO
- `bmap19/dispos_m.bin:bmap19_z03_m`: F1: PID_DAYNE_SKN
- `bmap19/dispos_m.bin:bmap19_z04_m`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN
- `bmap19/dispos_m.bin:bmap19_zoen1_m`: F1: PID_K_ZAKO
- `bmap19/dispos_n.bin:bmap19_boss_n`: F1: PID_KAYACHE
- `bmap19/dispos_n.bin:bmap19_chinon_n`: F1: PID_CHINON
- `bmap19/dispos_n.bin:bmap19_engn0_n`: F3: PID_MELTY
- `bmap19/dispos_n.bin:bmap19_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_DKN, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PRS, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SOL, PID_DAYNE_WAR
- `bmap19/dispos_n.bin:bmap19_mikata_n`: F0: PID_BOLE, PID_CHINON, PID_DALAHOWE, PID_ELAICE, PID_IKE, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MAKAROV, PID_MARCIA, PID_MIST, PID_MORDY, PID_MWARIM, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_SOTHE, PID_TIAMAT, PID_TOPUCK, PID_VOKE, PID_WAYU, PID_ZIHARK
- `bmap19/dispos_n.bin:bmap19_z02_n`: F1: PID_K_ZAKO
- `bmap19/dispos_n.bin:bmap19_z03_n`: F1: PID_DAYNE_SKN
- `bmap19/dispos_n.bin:bmap19_z04_n`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN
- `bmap19/dispos_n.bin:bmap19_zoen1_n`: F1: PID_K_ZAKO

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 136E | 0 | regist | 情報１フラグ |
| 1375 | 0 | regist | 情報２フラグ |
| 137C | 0 | regist | 情報３フラグ |
| 1383 | 0 | regist | 情報４フラグ |
| 138A | 0 | regist | 情報５フラグ |
| 13BF | 1 | TalkEvent | MS_19_INFO_01 |
| 13FC | 2 | TalkEvent | MS_19_INFO_02 |
| 144C | 3 | TalkEvent | MS_19_INFO_03 |
| 15E3 | 10 | regist | 宝箱１ |
| 15EB | 10 | regist | 宝箱２ |
| 15F3 | 10 | regist | 宝箱３ |
| 15FB | 10 | regist | F22082919 |
| 1603 | 10 | regist | F24202925 |
| 160B | 10 | regist | F30083623 |
| 168B | 13 | regist | 増援トリガ１ |
| 1693 | 13 | regist | 増援トリガ２ |
| 169B | 13 | regist | 増援イベント１ |
| 16A3 | 13 | regist | 増援イベント２ |
| 16AB | 13 | regist | シノン戦闘アイク |
| 16B3 | 13 | regist | シノン戦闘ティアマト |
| 16BB | 13 | regist | シノン戦闘ミスト |
| 16C3 | 13 | regist | シノン戦闘ヨファ |
| 16CB | 13 | regist | シノン戦闘オスカー |
| 16D3 | 13 | regist | シノン戦闘ボーレ |
| 16DB | 13 | regist | シノン戦闘ガトリー |
| 16E3 | 13 | regist | シノン戦闘キルロイ |
| 16EB | 13 | regist | シノン戦闘セネリオ |
| 16F3 | 13 | regist | シノン戦闘 |
| 16FB | 13 | regist | シノン会話ヨファ |
| 1703 | 13 | regist | シノン会話キルロイ |
| 170B | 13 | regist | シノン会話ミスト |
| 1713 | 13 | regist | シノンを倒したのがアイク |
| 171B | 13 | regist | ボス戦闘会話獣 |
| 1723 | 13 | regist | ボス戦闘会話鳥 |
| 172B | 13 | regist | ボス戦闘会話リュシオン |
| 1733 | 13 | regist | ボス戦闘会話アイク |
| 173B | 13 | regist | ボス戦闘会話 |
| 1743 | 13 | regist | リュシオン仲間 |
| 1786 | 14 | InstantDisposRank | bmap19_first |
| 178E | 14 | InstantDisposRank | bmap19_boss |
| 17A0 | 14 | InstantDisposRank | bmap19_chinon |
| 183B | 15 | SallySetByGroup | bmap19_mikata_c |
| 1843 | 15 | SallyAddByGroup | bmap19_m01_c |
| 1855 | 15 | SallyAddByGroup | bmap19_m_birds_c |
| 19F9 | 16 | TalkEvent | MS_19_GMAP_1 |
| 1A01 | 16 | TalkEvent | MS_19_GMAP_2 |
| 1A73 | 16 | TalkEvent | MS_19_GMAP_3 |
| 1ABB | 16 | TalkEvent | MS_19_GMAP_4 |
| 1B33 | 16 | TalkEvent | MS_19_GMAP_5 |
| 1B3B | 16 | TalkEvent | MS_19_GMAP_6 |
| 1BE7 | 16 | TalkEvent | MS_19_GMAP_7 |
| 1C36 | 16 | TalkEvent | MS_19_GMAP_8 |
| 1CA1 | 16 | TalkEvent | MS_19_GMAP_9 |
| 1CA9 | 16 | TalkEvent | MS_19_GMAP_10 |
| 1E02 | 17 | ChapterMoviePlay | 19 |
| 1E4D | 18 | ForceGetCount | 5 |
| 1E6F | 18 | MapLoad | bmap19 |
| 1E7D | 18 | InstantDisposSetMode | bmap19_mikata_n, bmap19_mikata_h, bmap19_mikata_m |
| 1E87 | 18 | UnitTransferToForceByPID | PID_CHINON, 7 |
| 1E8C | 18 | AllUnitEscape |  |
| 1EB7 | 18 | ForceGetCount | 5 |
| 1EC0 | 18 | ForceGetFirst | 5 |
| 1FA9 | 18 | TalkEvent | MS_19_EV_C_01 |
| 1FC4 | 18 | TalkResume |  |
| 1FDD | 18 | TalkResume |  |
| 2058 | 18 | TalkEvent | MS_19_EV_C_02 |
| 20A1 | 18 | TalkEvent | MS_19_OP_01 |
| 20D2 | 18 | TalkEvent | MS_19_OP_03 |
| 213F | 19 | MapLoad | bmap19 |
| 2175 | 19 | InstantDispos | bmap19_event_elinsia_c |
| 217D | 19 | InstantDispos | bmap19_event1_c |
| 2185 | 19 | InstantDispos | bmap19_m_birds_c |
| 218D | 19 | InstantDispos | bmap19_event_birds_c |
| 21D4 | 19 | AllUnitEscape |  |
| 21E6 | 19 | SallySetByGroup | bmap19_mikata_c |
| 21EE | 19 | SallyAddByGroup | bmap19_m01_c |
| 21F6 | 19 | InstantDispos | bmap19_mikata_c |
| 21FE | 19 | InstantDispos | bmap19_m01_c |
| 2223 | 19 | ForceGetCount | 0 |
| 222C | 19 | ForceGetFirst | 0 |
| 237C | 19 | InstantDispos | bmap19_event_elinsia_c |
| 23DF | 19 | InstantDispos | bmap19_m_birds_c |
| 23E7 | 19 | InstantDispos | bmap19_event_birds_c |
| 245B | 19 | TalkEvent | MS_19_OP_04 |
| 249F | 19 | TalkEvent | MS_19_OP_EV_00_B |
| 256E | 19 | ForceGetCount | 0 |
| 2577 | 19 | ForceGetFirst | 0 |
| 25BF | 19 | TalkEvent | MS_19_OP_EV_01 |
| 25E1 | 19 | TalkEvent | MS_19_OP_EV_01_DEL |
| 2656 | 19 | UnitTransferToForceByPID | PID_RIEUSION, 0 |
| 2660 | 19 | UnitTransferToForceByPID | PID_JANAFF, 0 |
| 266A | 19 | UnitTransferToForceByPID | PID_VULCI, 0 |
| 267A | 19 | SallyAddByGroup | bmap19_m_birds_c |
| 2687 | 19 | TalkEvent | MS_19_OP_EV_A0 |
| 2692 | 19 | TalkEvent | MS_19_OP_EV_A |
| 2756 | 19 | UnitEscapeByPID | PID_TIBARN |
| 275E | 19 | UnitEscapeByPID | PID_LEARNE |
| 276E | 19 | TalkEvent | MS_19_OP_EV_B0 |
| 2779 | 19 | TalkEvent | MS_19_OP_EV_B |
| 2843 | 19 | UnitEscapeByPID | PID_RIEUSION |
| 284B | 19 | UnitEscapeByPID | PID_JANAFF |
| 2853 | 19 | UnitEscapeByPID | PID_VULCI |
| 285B | 19 | UnitEscapeByPID | PID_TIBARN |
| 2863 | 19 | UnitEscapeByPID | PID_LEARNE |
| 28B2 | 19 | ForceGetCount | 0 |
| 28BB | 19 | ForceGetFirst | 0 |
| 2931 | 19 | TalkEvent | MS_19_OP_EV_02 |
| 2952 | 19 | UnitEscapeByPID | PID_DUMMY1 |
| 2979 | 19 | ForceGetCount | 0 |
| 2982 | 19 | ForceGetFirst | 0 |
| 29ED | 19 | UnitForcedSallyByPID | PID_IKE |
| 29F5 | 19 | UnitDontMoveSallyByPID | PID_IKE |
| 2ADB | 20 | InstantDispos | bmap19_event1_c |
| 2B26 | 20 | TalkEvent | MS_19_OP_06 |
| 2B69 | 20 | TalkEvent | MS_19_OP_06_2 |
| 2C04 | 20 | TalkEvent | MS_19_OP_06_s |
| 2C71 | 20 | TalkEvent | MS_19_OP_07 |
| 2CD1 | 20 | UnitEscapeByPID | PID_NAESALA |
| 2D12 | 21 | TalkEvent | MS_19_TK_CHINON_MIST |
| 2D52 | 22 | TalkEvent | MS_19_TK_CHINON_LOFA |
| 2DA2 | 23 | TalkEvent | MS_19_TK_CHINON_KILROY |
| 2DE1 | 24 | DisposSetMode | bmap19_z03_n, bmap19_z03_h, bmap19_z03_m |
| 2E11 | 25 | DisposSetMode | bmap19_z04_n, bmap19_z04_h, bmap19_z04_m |
| 2E5E | 26 | DisposSetMode | bmap19_zoen1_n, bmap19_zoen1_h, bmap19_zoen1_m |
| 2ED8 | 26 | TalkEvent | MS_19_EV_00_y |
| 2F24 | 26 | TalkEvent | MS_19_EV_00_u |
| 2F6F | 26 | TalkEvent | MS_19_EV_r |
| 2FE2 | 27 | DisposSetMode | bmap19_z02_n, bmap19_z02_h, bmap19_z02_m |
| 300D | 28 | BMGetPhase |  |
| 301A | 28 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3025 | 28 | SoundBossTalkStart | BGM_BTL_CP01 |
| 302D | 28 | TalkEvent | MS_19_BT_2_IKE |
| 3032 | 28 | SoundBossTalkEnd |  |
| 3069 | 29 | BMGetPhase |  |
| 3076 | 29 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3081 | 29 | SoundBossTalkStart | BGM_BTL_CP01 |
| 3089 | 29 | TalkEvent | MS_19_BT_2_TI |
| 308E | 29 | SoundBossTalkEnd |  |
| 30C5 | 30 | BMGetPhase |  |
| 30D2 | 30 | SoundBossTalkStart | BGM_BTL_PL01 |
| 30DD | 30 | SoundBossTalkStart | BGM_BTL_CP01 |
| 30E5 | 30 | TalkEvent | MS_19_BT_2_SE |
| 30EA | 30 | SoundBossTalkEnd |  |
| 3121 | 31 | BMGetPhase |  |
| 312E | 31 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3139 | 31 | SoundBossTalkStart | BGM_BTL_CP01 |
| 3141 | 31 | TalkEvent | MS_19_BT_2_MI |
| 3146 | 31 | SoundBossTalkEnd |  |
| 317D | 32 | BMGetPhase |  |
| 318A | 32 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3195 | 32 | SoundBossTalkStart | BGM_BTL_CP01 |
| 319D | 32 | TalkEvent | MS_19_BT_2_YO |
| 31A2 | 32 | SoundBossTalkEnd |  |
| 31D9 | 33 | BMGetPhase |  |
| 31E6 | 33 | SoundBossTalkStart | BGM_BTL_PL01 |
| 31F1 | 33 | SoundBossTalkStart | BGM_BTL_CP01 |
| 31F9 | 33 | TalkEvent | MS_19_BT_2_GA |
| 31FE | 33 | SoundBossTalkEnd |  |
| 3235 | 34 | BMGetPhase |  |
| 3242 | 34 | SoundBossTalkStart | BGM_BTL_PL01 |
| 324D | 34 | SoundBossTalkStart | BGM_BTL_CP01 |
| 3255 | 34 | TalkEvent | MS_19_BT_2_OS |
| 325A | 34 | SoundBossTalkEnd |  |
| 3291 | 35 | BMGetPhase |  |
| 329E | 35 | SoundBossTalkStart | BGM_BTL_PL01 |
| 32A9 | 35 | SoundBossTalkStart | BGM_BTL_CP01 |
| 32B1 | 35 | TalkEvent | MS_19_BT_2_BO |
| 32B6 | 35 | SoundBossTalkEnd |  |
| 32ED | 36 | BMGetPhase |  |
| 32FA | 36 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3305 | 36 | SoundBossTalkStart | BGM_BTL_CP01 |
| 330D | 36 | TalkEvent | MS_19_BT_2_KI |
| 3312 | 36 | SoundBossTalkEnd |  |
| 339E | 37 | BMGetPhase |  |
| 340B | 37 | BMGetPhase |  |
| 3418 | 37 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3423 | 37 | SoundBossTalkStart | BGM_BTL_CP01 |
| 342B | 37 | TalkEvent | MS_19_BT_ETC |
| 3430 | 37 | SoundBossTalkEnd |  |
| 3479 | 38 | BMGetPhase |  |
| 34A1 | 38 | TalkEvent | MS_19_DIE_Ike |
| 34BC | 38 | TalkEvent | MS_19_DIE_Jofa |
| 34C7 | 38 | TalkEvent | MS_19_DIE_sinon |
| 34FC | 39 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3504 | 39 | TalkEvent | MS_19_BT_IKE |
| 3511 | 39 | SoundBossTalkEnd |  |
| 3544 | 40 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 354C | 40 | TalkEvent | MS_19_BT_R1 |
| 3559 | 40 | SoundBossTalkEnd |  |
| 358C | 41 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3594 | 41 | TalkEvent | MS_19_BT_R1 |
| 35A1 | 41 | SoundBossTalkEnd |  |
| 35D4 | 42 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 35DC | 42 | TalkEvent | MS_19_BT_R1 |
| 35E9 | 42 | SoundBossTalkEnd |  |
| 361C | 43 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3624 | 43 | TalkEvent | MS_19_BT_R2 |
| 3631 | 43 | SoundBossTalkEnd |  |
| 3664 | 44 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 366C | 44 | TalkEvent | MS_19_BT_R2 |
| 3679 | 44 | SoundBossTalkEnd |  |
| 36AC | 45 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 36B4 | 45 | TalkEvent | MS_19_BT_RI |
| 36C1 | 45 | SoundBossTalkEnd |  |
| 3732 | 46 | BMGetPhase |  |
| 3792 | 46 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 379A | 46 | TalkEvent | MS_19_BT |
| 37A7 | 46 | SoundBossTalkEnd |  |
| 37D8 | 47 | TalkEvent | MS_19_DIE |
| 37FE | 48 | ForceGetCount | 1 |
| 38A7 | 49 | UnitTransferToForceByPID | PID_CHINON, 0 |
| 38BF | 49 | UnitTransferToForce | ?, 0 |
| 38FF | 49 | InstantDisposRank | bmap19_chinon |
| 3909 | 49 | UnitTransferToForceByPID | PID_CHINON, 1 |
| 390E | 49 | AllUnitEscape |  |
| 3939 | 49 | TalkEvent | MS_19_ED_00 |
| 396A | 49 | TalkEvent | MS_19_ED_01 |
| 399B | 49 | TalkEvent | MS_19_ED_02 |
| 39CF | 49 | TalkEvent | MS_19_ED_03 |
| 3A52 | 51 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.19: Entrusted — internal 20

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 13, 'h': 17, 'm': 17, 'n': 17}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap20/dispos_c.bin:bmap20_engn0_c`: F3: PID_MELTY
- `bmap20/dispos_c.bin:bmap20_event_narsil_c`: F2: PID_NASIR
- `bmap20/dispos_c.bin:bmap20_event_nesala_c`: F2: PID_NAESALA
- `bmap20/dispos_c.bin:bmap20_event_prague_c`: F1: PID_DAYNE_PLD_1, PID_DAYNE_PLD_2, PID_DAYNE_PLD_3, PID_PRAGUE
- `bmap20/dispos_c.bin:bmap20_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap20/dispos_c.bin:bmap20_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap20/dispos_c.bin:bmap20_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap20/dispos_c.bin:bmap20_f01_c`: F1: PID_TAURONEO
- `bmap20/dispos_c.bin:bmap20_first_c`: F1: PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_PRS, PID_DAYNE_SNP_1, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_HOMAS, PID_K_ZAKO, PID_NAESALA
- `bmap20/dispos_c.bin:bmap20_mikata_c`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap20/dispos_h.bin:bmap20_engn0_h`: F3: PID_MELTY
- `bmap20/dispos_h.bin:bmap20_first2_h`: F1: PID_K_ZAKO, PID_NAESALA
- `bmap20/dispos_h.bin:bmap20_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_FIG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_HOMAS
- `bmap20/dispos_h.bin:bmap20_mikata_h`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LETHE, PID_MIST, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_WAYU, PID_ZIHARK
- `bmap20/dispos_h.bin:bmap20_zoen1_h`: F1: PID_DAYNE_DKN
- `bmap20/dispos_h.bin:bmap20_zoen2_h`: F1: PID_DAYNE_DKN
- `bmap20/dispos_h.bin:bmap20_zoen3_h`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN
- `bmap20/dispos_m.bin:bmap20_engn0_m`: F3: PID_MELTY
- `bmap20/dispos_m.bin:bmap20_first2_m`: F1: PID_K_ZAKO, PID_NAESALA
- `bmap20/dispos_m.bin:bmap20_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_FIG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_HOMAS
- `bmap20/dispos_m.bin:bmap20_mikata_m`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LETHE, PID_MIST, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_WAYU, PID_ZIHARK
- `bmap20/dispos_m.bin:bmap20_zoen1_m`: F1: PID_DAYNE_DKN
- `bmap20/dispos_m.bin:bmap20_zoen2_m`: F1: PID_DAYNE_DKN
- `bmap20/dispos_m.bin:bmap20_zoen3_m`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN
- `bmap20/dispos_n.bin:bmap20_engun0_n`: F3: PID_MELTY
- `bmap20/dispos_n.bin:bmap20_first2_n`: F1: PID_K_ZAKO, PID_NAESALA
- `bmap20/dispos_n.bin:bmap20_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_FIG, PID_DAYNE_PRS, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_HOMAS
- `bmap20/dispos_n.bin:bmap20_mikata_n`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LETHE, PID_MIST, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_WAYU, PID_ZIHARK
- `bmap20/dispos_n.bin:bmap20_zoen1_n`: F1: PID_DAYNE_DKN
- `bmap20/dispos_n.bin:bmap20_zoen2_n`: F1: PID_DAYNE_DKN
- `bmap20/dispos_n.bin:bmap20_zoen3_n`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 151A | 0 | regist | 情報１フラグ |
| 1521 | 0 | regist | 情報２フラグ |
| 1528 | 0 | regist | 情報３フラグ |
| 152F | 0 | regist | 情報４フラグ |
| 1536 | 0 | regist | 情報５フラグ |
| 153D | 0 | regist | 情報６フラグ |
| 1593 | 1 | TalkEvent | MS_20_INFO_03 |
| 15A0 | 1 | TalkEvent | MS_20_INFO_03_2 |
| 1687 | 2 | TalkEvent | MS_20_INFO_04 |
| 170A | 3 | TalkEvent | MS_20_INFO_05 |
| 1752 | 4 | TalkEvent | MS_20_INFO_06 |
| 1788 | 5 | UnitGetForce | ? |
| 17EF | 5 | UnitEscape | ?, 0 |
| 21D7 | 68 | regist | F06062516 |
| 21DF | 68 | regist | F06062524 |
| 21E7 | 68 | regist | F06062520 |
| 2247 | 70 | regist | ネサラ会話 |
| 224F | 70 | regist | ネサラ会話リュシオン |
| 2257 | 70 | regist | ネサラ戦闘 |
| 225F | 70 | regist | ネサラ戦闘ヤナフ |
| 2267 | 70 | regist | ネサラ戦闘ウルキ |
| 226F | 70 | regist | ネサラ戦闘アイク |
| 2277 | 70 | regist | ネサラ戦闘レテ |
| 227F | 70 | regist | ネサラ戦闘モウディ |
| 2287 | 70 | regist | ネサラ戦闘ムワリム |
| 228F | 70 | regist | ネサラ死亡 |
| 2297 | 70 | regist | 増援トリガ１ |
| 229F | 70 | regist | 増援トリガ２ |
| 22A7 | 70 | regist | 増援イベント１ |
| 22AF | 70 | regist | 増援イベント２ |
| 22B7 | 70 | regist | ネサラ退却 |
| 22BF | 70 | regist | 怒る赤軍 |
| 22C7 | 70 | regist | ボス戦闘会話アイク |
| 22CF | 70 | regist | ボス戦闘会話獣 |
| 22D7 | 70 | regist | ボス戦闘会話鳥 |
| 22DF | 70 | regist | ボス戦闘会話リュシオン |
| 22E7 | 70 | regist | ボス戦闘会話ツイハーク |
| 22EF | 70 | regist | ボス戦闘会話ソーンバルケ |
| 22F7 | 70 | regist | ボス戦闘会話 |
| 22FF | 70 | regist | ネサラ死亡オンバト |
| 2307 | 70 | regist | カラス兵死亡 |
| 234A | 71 | InstantDisposRank | bmap20_first |
| 2352 | 71 | InstantDisposRank | bmap20_first2 |
| 238E | 71 | ForceGetCount | 1 |
| 2397 | 71 | ForceGetFirst | 1 |
| 2423 | 72 | SallySetByGroup | bmap20_mikata_c |
| 256F | 73 | TalkEvent | MS_20_GMAP |
| 262E | 74 | ChapterMoviePlay | 20 |
| 2680 | 75 | MapLoad | bmap20 |
| 26A2 | 75 | InstantDispos | bmap20_event_prague_c |
| 26A7 | 75 | AllUnitEscape |  |
| 26B6 | 75 | InstantDispos | bmap20_first_c |
| 2705 | 75 | Dispos | bmap20_event_prague_c |
| 27CC | 75 | TalkEvent | MS_20_OP_01 |
| 2854 | 75 | TalkEvent | MS_20_OP_01_2 |
| 28F2 | 75 | AllUnitEscape |  |
| 292D | 76 | ForceGetCount | 5 |
| 294F | 76 | MapLoad | bmap20 |
| 295D | 76 | InstantDisposSetMode | bmap20_mikata_n, bmap20_mikata_h, bmap20_mikata_m |
| 2962 | 76 | AllUnitEscape |  |
| 2977 | 76 | Join | always_dbg_mik_02 |
| 297F | 76 | Join | always_dbg_mik_03 |
| 2987 | 76 | Join | always_dbg_mik_05 |
| 298F | 76 | Join | always_dbg_mik_08 |
| 2997 | 76 | Join | always_dbg_mik_09 |
| 299F | 76 | Join | always_dbg_mik_10 |
| 29A7 | 76 | Join | always_dbg_mik_11 |
| 29AF | 76 | Join | always_dbg_mik_12 |
| 29B7 | 76 | Join | always_dbg_mik_13 |
| 29BF | 76 | Join | always_dbg_mik_14 |
| 29C7 | 76 | Join | always_dbg_mik_15 |
| 29CF | 76 | Join | always_dbg_mik_16 |
| 29D7 | 76 | Join | always_dbg_mik_17 |
| 29DF | 76 | Join | always_dbg_mik_19 |
| 2A63 | 77 | MapLoad | bmap20 |
| 2A9D | 77 | SallySetByGroup | bmap20_mikata_c |
| 2AA5 | 77 | InstantDisposFirst | bmap20_mikata_c |
| 2ABA | 77 | Dispos_ForEventTiamat | bmap20_event_tiamat_c, 1 |
| 2AEE | 77 | Dispos_ForEventSenerio | bmap20_event_senerio_c, bmap20_event_senerio2_c, 1 |
| 2B8E | 77 | DisposContinue | bmap20_mikata_c |
| 2C78 | 77 | UnitEscapeByPID | PID_TIAMAT_EV |
| 2C80 | 77 | UnitEscapeByPID | PID_SENERIO_EV |
| 2CBB | 77 | TalkEvent | MS_20_OP_02_01A |
| 2CD0 | 77 | TalkEvent | MS_20_OP_02_01B |
| 2CDB | 77 | TalkEvent | MS_20_OP_02_01C |
| 2CE3 | 77 | TalkEvent | MS_20_OP_02_02 |
| 2D09 | 77 | TalkEvent | MS_20_OP_02_03 |
| 2D1B | 77 | TalkEvent | MS_20_OP_02_04S |
| 2D2D | 77 | TalkEvent | MS_20_OP_02_05S |
| 2D3F | 77 | TalkEvent | MS_20_OP_02_06S |
| 2D47 | 77 | TalkEvent | MS_20_OP_02_07 |
| 2D59 | 77 | TalkEvent | MS_20_OP_02_08S |
| 2D6B | 77 | TalkEvent | MS_20_OP_02_09S |
| 2D7D | 77 | TalkEvent | MS_20_OP_02_10S |
| 2D85 | 77 | TalkEvent | MS_20_OP_02_11 |
| 2DC2 | 77 | UnitForcedSallyByPID | PID_IKE |
| 2DCA | 77 | UnitDontMoveSallyByPID | PID_IKE |
| 2EFD | 78 | TalkEvent | MS_20_OP_03 |
| 2F05 | 78 | InstantDispos | bmap20_event_narsil_c |
| 2FBA | 78 | TalkEvent | MS_20_OP_04 |
| 30A6 | 78 | TalkEvent | MS_20_OP_05_01 |
| 30B8 | 78 | TalkEvent | MS_20_OP_05_02 |
| 30D4 | 78 | TalkEvent | MS_20_OP_05_03 |
| 30DC | 78 | TalkEvent | MS_20_OP_05_04 |
| 3144 | 78 | UnitEscapeByPID | PID_NASIR |
| 31ED | 79 | TalkEvent | MS_20_EV_03 |
| 32A3 | 80 | TalkEvent | ? |
| 32AC | 80 | ForceGetCount | 1 |
| 32B6 | 80 | ForceGetFirst | 1 |
| 32E6 | 80 | UnitTransferToForce | ?, 2 |
| 33E6 | 81 | UnitEscapeByPID | PID_NAESALA |
| 33EB | 81 | BMGetPhase |  |
| 3436 | 82 | TalkEvent | MS_20_TK_01A |
| 349A | 83 | TalkEvent | MS_20_TK_01B |
| 3508 | 84 | TalkEvent | MS_20_TK_02 |
| 3513 | 84 | TalkEvent | MS_20_TK_02_GET |
| 3559 | 84 | UnitTransferToForceByPID | PID_NAESALA, 2 |
| 35CD | 86 | BMGetPhase |  |
| 35DA | 86 | SoundBossTalkStart | BGM_BTL_PL01 |
| 35E5 | 86 | SoundBossTalkStart | BGM_BTL_CP01 |
| 35ED | 86 | TalkEvent | MS_20_BT_NAESALA_02 |
| 35FA | 86 | SoundBossTalkEnd |  |
| 3629 | 87 | BMGetPhase |  |
| 3636 | 87 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3641 | 87 | SoundBossTalkStart | BGM_BTL_CP01 |
| 3649 | 87 | TalkEvent | MS_20_BT_NAESALA_03 |
| 3656 | 87 | SoundBossTalkEnd |  |
| 3685 | 88 | BMGetPhase |  |
| 3692 | 88 | SoundBossTalkStart | BGM_BTL_PL01 |
| 369D | 88 | SoundBossTalkStart | BGM_BTL_CP01 |
| 36A5 | 88 | TalkEvent | MS_20_BT_NAESALA_04 |
| 36B2 | 88 | SoundBossTalkEnd |  |
| 36E1 | 89 | BMGetPhase |  |
| 36EE | 89 | SoundBossTalkStart | BGM_BTL_PL01 |
| 36F9 | 89 | SoundBossTalkStart | BGM_BTL_CP01 |
| 3701 | 89 | TalkEvent | MS_20_BT_NAESALA_05 |
| 370E | 89 | SoundBossTalkEnd |  |
| 373D | 90 | BMGetPhase |  |
| 374A | 90 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3755 | 90 | SoundBossTalkStart | BGM_BTL_CP01 |
| 375D | 90 | TalkEvent | MS_20_BT_NAESALA_06 |
| 376A | 90 | SoundBossTalkEnd |  |
| 3799 | 91 | BMGetPhase |  |
| 37A6 | 91 | SoundBossTalkStart | BGM_BTL_PL01 |
| 37B1 | 91 | SoundBossTalkStart | BGM_BTL_CP01 |
| 37B9 | 91 | TalkEvent | MS_20_BT_NAESALA_MW |
| 37C6 | 91 | SoundBossTalkEnd |  |
| 382C | 92 | BMGetPhase |  |
| 3881 | 92 | BMGetPhase |  |
| 388E | 92 | SoundBossTalkStart | BGM_BTL_PL01 |
| 3899 | 92 | SoundBossTalkStart | BGM_BTL_CP01 |
| 38A1 | 92 | TalkEvent | MS_20_BT_NAESALA |
| 38AE | 92 | SoundBossTalkEnd |  |
| 38F1 | 93 | TalkEvent | MS_20_DIE_NAESALA |
| 394C | 94 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3954 | 94 | TalkEvent | MS_20_BT_IKE |
| 3961 | 94 | SoundBossTalkEnd |  |
| 3994 | 95 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 399C | 95 | TalkEvent | MS_20_BT_R1 |
| 39A9 | 95 | SoundBossTalkEnd |  |
| 39DC | 96 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 39E4 | 96 | TalkEvent | MS_20_BT_R1 |
| 39F1 | 96 | SoundBossTalkEnd |  |
| 3A24 | 97 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3A2C | 97 | TalkEvent | MS_20_BT_R1 |
| 3A39 | 97 | SoundBossTalkEnd |  |
| 3A6C | 98 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3A74 | 98 | TalkEvent | MS_20_BT_R2 |
| 3A81 | 98 | SoundBossTalkEnd |  |
| 3AB4 | 99 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3ABC | 99 | TalkEvent | MS_20_BT_R2 |
| 3AC9 | 99 | SoundBossTalkEnd |  |
| 3AFC | 100 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3B04 | 100 | TalkEvent | MS_20_BT_RI |
| 3B11 | 100 | SoundBossTalkEnd |  |
| 3B44 | 101 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3B4C | 101 | TalkEvent | MS_20_BT_TU |
| 3B59 | 101 | SoundBossTalkEnd |  |
| 3B8C | 102 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3B94 | 102 | TalkEvent | MS_20_BT_SO |
| 3BA1 | 102 | SoundBossTalkEnd |  |
| 3C26 | 103 | BMGetPhase |  |
| 3C96 | 103 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3C9E | 103 | TalkEvent | MS_20_BT |
| 3CAB | 103 | SoundBossTalkEnd |  |
| 3CDC | 104 | TalkEvent | MS_20_DIE |
| 3DA5 | 105 | TalkEvent | MS_20_EV_04 |
| 3DFC | 105 | AllUnitEscape |  |
| 3E25 | 105 | TalkEvent | MS_20_ED_01_A |
| 3E30 | 105 | TalkEvent | MS_20_ED_01_B |
| 3E64 | 105 | TalkEvent | MS_20_ED_02 |
| 3E95 | 105 | TalkEvent | MS_20_ED_03 |
| 3ECE | 105 | TalkEvent | MS_20_ED_04_01_01 |
| 3EDD | 105 | TalkResume |  |
| 3EEC | 105 | TalkResume |  |
| 3F7C | 105 | TalkEvent | MS_20_ED_04_01_2 |
| 4022 | 105 | TalkEvent | MS_20_ED_04_01_3 |
| 40A4 | 105 | TalkEvent | MS_20_ED_04_01_4 |
| 40B3 | 105 | TalkResume |  |
| 40EC | 105 | TalkEvent | MS_20_ED_04_01_5 |
| 4139 | 105 | TalkEvent | MS_20_ED_04_02_C |
| 414B | 105 | TalkEvent | MS_20_ED_04_02_C_DEL |
| 4191 | 105 | TalkEvent | MS_20_ED_04_02_C_SKIP |
| 41C0 | 105 | TalkEvent | MS_20_ED_04_04Y |
| 4224 | 105 | TalkEvent | MS_20_ED_04_05Y |
| 4234 | 105 | TalkEvent | MS_20_ED_04_04N |
| 4244 | 105 | TalkEvent | MS_20_ED_04_02_B |
| 4254 | 105 | TalkEvent | MS_20_ED_04_02_A |
| 427B | 105 | TalkEvent | MS_20_ED_05 |
| 42FE | 107 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.20: Defending Talrega — internal 21

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 11, 'h': 19, 'm': 19, 'n': 19}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap21/dispos_c.bin:bmap21_engn0_c`: F3: PID_MELTY
- `bmap21/dispos_c.bin:bmap21_event_beg_c`: F2: PID_B_ZAKO
- `bmap21/dispos_c.bin:bmap21_event_haar_c`: F1: PID_HAAR
- `bmap21/dispos_c.bin:bmap21_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap21/dispos_c.bin:bmap21_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap21/dispos_c.bin:bmap21_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap21/dispos_c.bin:bmap21_mikata_c`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap21/dispos_h.bin:bmap21_engn0_h`: F3: PID_MELTY
- `bmap21/dispos_h.bin:bmap21_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_DKN, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_MAG, PID_DAYNE_PLD, PID_DAYNE_PRS, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_MAP21_DKN_1, PID_MAP21_DKN_2, PID_MAP21_DKN_3, PID_SIHARAMU
- `bmap21/dispos_h.bin:bmap21_mikata_h`: F0: PID_BOLE, PID_CALILL, PID_IKE, PID_JANAFF, PID_JILL, PID_KEVIN, PID_KILROY, PID_LETHE, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap21/dispos_h.bin:bmap21_z01_h`: F1: PID_DAYNE_DKN, PID_DAYNE_SRD
- `bmap21/dispos_h.bin:bmap21_z02_h`: F1: PID_DAYNE_ARM
- `bmap21/dispos_h.bin:bmap21_z03_h`: F1: PID_DAYNE_MAG, PID_DAYNE_SAG
- `bmap21/dispos_h.bin:bmap21_z04_h`: F1: PID_DAYNE_DKN
- `bmap21/dispos_h.bin:bmap21_z05_h`: F1: PID_DAYNE_DKN
- `bmap21/dispos_h.bin:bmap21_z06_h`: F1: PID_DAYNE_DKN
- `bmap21/dispos_m.bin:bmap21_engn0_m`: F3: PID_MELTY
- `bmap21/dispos_m.bin:bmap21_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_DKN, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_PRS, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_MAP21_DKN_1, PID_MAP21_DKN_2, PID_MAP21_DKN_3, PID_SIHARAMU
- `bmap21/dispos_m.bin:bmap21_mikata_m`: F0: PID_BOLE, PID_CALILL, PID_IKE, PID_JANAFF, PID_JILL, PID_KEVIN, PID_KILROY, PID_LETHE, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap21/dispos_m.bin:bmap21_z01_m`: F1: PID_DAYNE_DKN, PID_DAYNE_SRD
- `bmap21/dispos_m.bin:bmap21_z02_m`: F1: PID_DAYNE_ARM
- `bmap21/dispos_m.bin:bmap21_z03_m`: F1: PID_DAYNE_MAG, PID_DAYNE_SAG
- `bmap21/dispos_m.bin:bmap21_z04_m`: F1: PID_DAYNE_DKN
- `bmap21/dispos_m.bin:bmap21_z05_m`: F1: PID_DAYNE_DKN
- `bmap21/dispos_m.bin:bmap21_z06_m`: F1: PID_DAYNE_DKN
- `bmap21/dispos_n.bin:bmap21_engn0_n`: F3: PID_MELTY
- `bmap21/dispos_n.bin:bmap21_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_DKN, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_PRS, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_MAP21_DKN_1, PID_MAP21_DKN_2, PID_MAP21_DKN_3, PID_SIHARAMU
- `bmap21/dispos_n.bin:bmap21_mikata_n`: F0: PID_BOLE, PID_CALILL, PID_IKE, PID_JANAFF, PID_JILL, PID_KEVIN, PID_KILROY, PID_LETHE, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap21/dispos_n.bin:bmap21_z01_n`: F1: PID_DAYNE_DKN, PID_DAYNE_SRD
- `bmap21/dispos_n.bin:bmap21_z02_n`: F1: PID_DAYNE_ARM
- `bmap21/dispos_n.bin:bmap21_z03_n`: F1: PID_DAYNE_MAG, PID_DAYNE_SAG
- `bmap21/dispos_n.bin:bmap21_z04_n`: F1: PID_DAYNE_DKN
- `bmap21/dispos_n.bin:bmap21_z05_n`: F1: PID_DAYNE_DKN
- `bmap21/dispos_n.bin:bmap21_z06_n`: F1: PID_DAYNE_DKN

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 1052 | 0 | regist | 情報１フラグ |
| 1059 | 0 | regist | 情報２フラグ |
| 1060 | 0 | regist | 情報３フラグ |
| 1067 | 0 | regist | 情報４フラグ |
| 106E | 0 | regist | 情報５フラグ |
| 1075 | 0 | regist | カリル仲間 |
| 10B7 | 1 | TalkEvent | MS_21_INFO_02 |
| 10F1 | 1 | TalkEvent | MS_21_INFO_02_A |
| 1109 | 1 | Join | always_kariru |
| 111B | 1 | TalkEvent | MS_21_INFO_02_B |
| 115A | 2 | TalkEvent | MS_21_INFO_05 |
| 11D2 | 4 | TalkEvent | MS_21_VIL_01 |
| 1282 | 6 | TalkEvent | MS_21_VIL_02 |
| 15BF | 14 | regist | 訪問１ |
| 15C7 | 14 | regist | 訪問２ |
| 15CF | 14 | regist | F17032621 |
| 15D7 | 14 | regist | F19032613 |
| 15DF | 14 | regist | F15032621 |
| 15E7 | 14 | regist | F21062612 |
| 15EF | 14 | regist | F14032621 |
| 15F7 | 14 | regist | F12171321 |
| 164B | 16 | regist | 増援トリガ１ |
| 1653 | 16 | regist | 増援トリガ２ |
| 165B | 16 | regist | 増援トリガ３ |
| 1663 | 16 | regist | 増援イベント１ |
| 166B | 16 | regist | 増援イベント２ |
| 1673 | 16 | regist | 増援イベント３ |
| 167B | 16 | regist | ＣＰ変更トリガ１ |
| 1683 | 16 | regist | ＣＰ変更イベント１ |
| 168B | 16 | regist | ＭＳ２１ＸＡＸＢ |
| 1693 | 16 | regist | 会話ジル−シハラム |
| 169B | 16 | regist | 会話ジル−シハラム終了 |
| 16A3 | 16 | regist | ジル戦闘会話竜騎士１ |
| 16AB | 16 | regist | ジル戦闘会話竜騎士２ |
| 16B3 | 16 | regist | ジル戦闘会話竜騎士３ |
| 16BB | 16 | regist | ボス戦闘会話 |
| 16C3 | 16 | regist | ボス戦闘会話アイク |
| 16CB | 16 | regist | ボス戦闘会話牙 |
| 16D3 | 16 | regist | ボス戦闘会話ウルキ−ヤナフ |
| 16DB | 16 | regist | ボス戦闘会話リュシオン |
| 16E3 | 16 | regist | ボス戦闘会話ジル |
| 16EB | 16 | regist | ボス戦闘会話タニス |
| 16F3 | 16 | regist | シハラム死亡 |
| 1736 | 17 | InstantDisposRank | bmap21_first |
| 1746 | 17 | ForceGetCount | 1 |
| 174F | 17 | ForceGetFirst | 1 |
| 17DF | 18 | SallySetByGroup | bmap21_mikata_c |
| 187A | 19 | TalkEvent | MS_21_GMAP_01 |
| 18AB | 19 | TalkResume |  |
| 190E | 20 | ChapterMoviePlay | 21 |
| 1959 | 21 | ForceGetCount | 5 |
| 197B | 21 | MapLoad | bmap21 |
| 1989 | 21 | InstantDisposSetMode | bmap21_mikata_n, bmap21_mikata_h, bmap21_mikata_m |
| 1999 | 21 | Join | always_dbg_mik_10 |
| 19A1 | 21 | Join | always_dbg_mik_11 |
| 19A9 | 21 | Join | always_dbg_mik_12 |
| 19B1 | 21 | Join | always_dbg_mik_13 |
| 19B9 | 21 | Join | always_dbg_mik_14 |
| 19C1 | 21 | Join | always_dbg_mik_15 |
| 19C9 | 21 | Join | always_dbg_mik_16 |
| 19D1 | 21 | Join | always_dbg_mik_17 |
| 19D9 | 21 | Join | always_dbg_mik_19 |
| 19DE | 21 | AllUnitEscape |  |
| 1A36 | 21 | TalkEvent | MS_21_OP_01 |
| 1A45 | 21 | TalkResume |  |
| 1A64 | 21 | TalkEvent | MS_21_OP_02 |
| 1A75 | 21 | TalkResume |  |
| 1AE5 | 22 | TalkEvent | MS_21_OP_03_01 |
| 1B0E | 22 | TalkEvent | MS_21_OP_03_02 |
| 1B3E | 22 | TalkEvent | MS_21_OP_03_03_A |
| 1B53 | 22 | TalkEvent | MS_21_OP_03_03_B |
| 1B5E | 22 | TalkEvent | MS_21_OP_03_03_C |
| 1B7B | 22 | MapLoad | bmap21 |
| 1BA4 | 22 | SallySetByGroup | bmap21_mikata_c |
| 1BAC | 22 | InstantDispos | bmap21_mikata_c |
| 1CE7 | 22 | TalkEvent | MS_21_OP_05 |
| 1D58 | 22 | TalkEvent | MS_21_OP_06 |
| 1DCF | 22 | UnitForcedSallyByPID | PID_IKE |
| 1DD7 | 22 | UnitDontMoveSallyByPID | PID_IKE |
| 1EC4 | 23 | TalkEvent | MS_21_OP_XA |
| 1EE7 | 23 | TalkEvent | MS_21_OP_XB |
| 1EFA | 23 | TalkEvent | MS_21_OP_XC |
| 202C | 25 | InstantDispos | bmap21_event_haar_c |
| 2048 | 25 | TalkEvent | MS_21_EV_X |
| 2064 | 25 | TalkResume |  |
| 2081 | 25 | TalkEvent | MS_21_EV_X_A |
| 208C | 25 | TalkEvent | MS_21_EV_X_B |
| 20C9 | 25 | UnitEscapeByPID | PID_HAAR |
| 219C | 26 | TalkEvent | MS_21_TK_03 |
| 21A7 | 26 | TalkEvent | MS_21_TK_01 |
| 21B1 | 26 | UnitTransferToForceByPID | PID_JILL, 1 |
| 22A0 | 27 | TalkEvent | MS_21_TK_04 |
| 22B3 | 27 | TalkEvent | MS_21_TK_02 |
| 22BD | 27 | UnitTransferToForceByPID | PID_JILL, 1 |
| 2325 | 28 | DisposSetMode | bmap21_z05_n, bmap21_z05_h, bmap21_z05_m |
| 2355 | 29 | DisposSetMode | bmap21_z02_n, bmap21_z02_h, bmap21_z02_m |
| 2385 | 30 | DisposSetMode | bmap21_z06_n, bmap21_z06_h, bmap21_z06_m |
| 23B5 | 31 | DisposSetMode | bmap21_z06_n, bmap21_z06_h, bmap21_z06_m |
| 2402 | 32 | DisposSetMode | bmap21_z01_n, bmap21_z01_h, bmap21_z01_m |
| 244E | 33 | DisposSetMode | bmap21_z02_n, bmap21_z02_h, bmap21_z02_m |
| 249A | 34 | DisposSetMode | bmap21_z03_n, bmap21_z03_h, bmap21_z03_m |
| 24E1 | 35 | ForceGetCount | 1 |
| 24F4 | 35 | ForceGetFirst | 1 |
| 25A0 | 36 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 25A8 | 36 | TalkEvent | MS_21_BT_V1 |
| 25B5 | 36 | SoundBossTalkEnd |  |
| 25E8 | 37 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 25F0 | 37 | TalkEvent | MS_21_BT_V2 |
| 25FD | 37 | SoundBossTalkEnd |  |
| 2630 | 38 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2638 | 38 | TalkEvent | MS_21_BT_V3 |
| 2645 | 38 | SoundBossTalkEnd |  |
| 267B | 39 | BMGetPhase |  |
| 26B5 | 39 | TalkEvent | MS_21_DIE_JILL |
| 26C2 | 39 | DefaultDieTalk |  |
| 2702 | 40 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 270A | 40 | TalkEvent | MS_21_BT_IKE |
| 2717 | 40 | SoundBossTalkEnd |  |
| 274C | 41 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2754 | 41 | TalkEvent | MS_21_BT_R1 |
| 2761 | 41 | SoundBossTalkEnd |  |
| 2794 | 42 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 279C | 42 | TalkEvent | MS_21_BT_R1 |
| 27A9 | 42 | SoundBossTalkEnd |  |
| 27DC | 43 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 27E4 | 43 | TalkEvent | MS_21_BT_R1 |
| 27F1 | 43 | SoundBossTalkEnd |  |
| 2824 | 44 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 282C | 44 | TalkEvent | MS_21_BT_R2 |
| 2839 | 44 | SoundBossTalkEnd |  |
| 286C | 45 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2874 | 45 | TalkEvent | MS_21_BT_R2 |
| 2881 | 45 | SoundBossTalkEnd |  |
| 28B4 | 46 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 28BC | 46 | TalkEvent | MS_21_BT_RI |
| 28C9 | 46 | SoundBossTalkEnd |  |
| 28FC | 47 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2904 | 47 | TalkEvent | MS_21_BT_JI |
| 2911 | 47 | SoundBossTalkEnd |  |
| 2944 | 48 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 294C | 48 | TalkEvent | MS_21_BT_TA |
| 2959 | 48 | SoundBossTalkEnd |  |
| 29EF | 49 | BMGetPhase |  |
| 2A5F | 49 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2A67 | 49 | TalkEvent | MS_21_BT |
| 2A74 | 49 | SoundBossTalkEnd |  |
| 2AA4 | 50 | TalkEvent | MS_21_DIE |
| 2B07 | 51 | AllUnitEscape |  |
| 2B26 | 51 | TalkEvent | MS_21_ED_01 |
| 2B61 | 51 | TalkEvent | MS_21_ED_X1 |
| 2B88 | 51 | TalkEvent | MS_21_ED_XX |
| 2C57 | 51 | TalkEvent | MS_21_ED_02 |
| 2C83 | 51 | TalkEvent | MS_21_ED_03 |
| 2D01 | 52 | BMGetTurn |  |
| 2D70 | 53 | TalkEvent | MS_21_GAMEOVER |
| 2DDA | 55 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.21: Without a King — internal 22

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 13, 'h': 19, 'm': 19, 'n': 19}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap22/dispos_c.bin:bmap22_ena_c`: F2: PID_ENA
- `bmap22/dispos_c.bin:bmap22_ena_preload_c`: F1: PID_ENA_EV2
- `bmap22/dispos_c.bin:bmap22_engn0_c`: F3: PID_MELTY
- `bmap22/dispos_c.bin:bmap22_event_sol_c`: F1: PID_ZAKO_EV1, PID_ZAKO_EV2
- `bmap22/dispos_c.bin:bmap22_evt_senerio2_c`: F2: PID_SENERIO_EV
- `bmap22/dispos_c.bin:bmap22_evt_senerio_c`: F2: PID_SENERIO_EV
- `bmap22/dispos_c.bin:bmap22_evt_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap22/dispos_c.bin:bmap22_mikata_c`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LAY, PID_LOFA, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_ZIHARK
- `bmap22/dispos_c.bin:bmap22_narsil_c`: F2: PID_NASIR
- `bmap22/dispos_c.bin:bmap22_tauroneo_c`: F1: PID_TAURONEO
- `bmap22/dispos_h.bin:bmap22_engn0_h`: F3: PID_MELTY
- `bmap22/dispos_h.bin:bmap22_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_FIG, PID_DAYNE_GNL_1, PID_DAYNE_HAL, PID_DAYNE_MAG, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_ENA, PID_KASATAI
- `bmap22/dispos_h.bin:bmap22_mikata_h`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KEVIN, PID_KILROY, PID_LAY, PID_LETHE, PID_LOFA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap22/dispos_h.bin:bmap22_z01_h`: F1: PID_DAYNE_SMS, PID_DAYNE_SRD
- `bmap22/dispos_h.bin:bmap22_z02_h`: F1: PID_DAYNE_HAL, PID_DAYNE_SNP
- `bmap22/dispos_h.bin:bmap22_z03_h`: F1: PID_ZAKO
- `bmap22/dispos_h.bin:bmap22_z04_h`: F1: PID_DAYNE_FIG, PID_DAYNE_WAR
- `bmap22/dispos_h.bin:bmap22_z05_h`: F1: PID_12_THIEF
- `bmap22/dispos_m.bin:bmap22_engn0_m`: F3: PID_MELTY
- `bmap22/dispos_m.bin:bmap22_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_FIG, PID_DAYNE_GNL_1, PID_DAYNE_HAL, PID_DAYNE_MAG, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_ENA, PID_KASATAI
- `bmap22/dispos_m.bin:bmap22_mikata_m`: F0: PID_BOLE, PID_CALILL, PID_IKE, PID_JANAFF, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap22/dispos_m.bin:bmap22_z01_m`: F1: PID_DAYNE_SMS, PID_DAYNE_SRD
- `bmap22/dispos_m.bin:bmap22_z02_m`: F1: PID_DAYNE_HAL, PID_DAYNE_SNP
- `bmap22/dispos_m.bin:bmap22_z03_m`: F1: PID_ZAKO
- `bmap22/dispos_m.bin:bmap22_z04_m`: F1: PID_DAYNE_FIG, PID_DAYNE_WAR
- `bmap22/dispos_m.bin:bmap22_z05_m`: F1: PID_12_THIEF
- `bmap22/dispos_n.bin:bmap22_engn0_n`: F3: PID_MELTY
- `bmap22/dispos_n.bin:bmap22_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_FIG, PID_DAYNE_GNL_1, PID_DAYNE_HAL, PID_DAYNE_MAG, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_ENA, PID_KASATAI
- `bmap22/dispos_n.bin:bmap22_mikata_n`: F0: PID_BOLE, PID_CALILL, PID_IKE, PID_JANAFF, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_RIEUSION, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap22/dispos_n.bin:bmap22_z01_n`: F1: PID_DAYNE_SMS, PID_DAYNE_SRD
- `bmap22/dispos_n.bin:bmap22_z02_n`: F1: PID_DAYNE_HAL, PID_DAYNE_SNP
- `bmap22/dispos_n.bin:bmap22_z03_n`: F1: PID_ZAKO
- `bmap22/dispos_n.bin:bmap22_z04_n`: F1: PID_DAYNE_FIG, PID_DAYNE_WAR
- `bmap22/dispos_n.bin:bmap22_z05_n`: F1: PID_12_THIEF

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 11F6 | 0 | regist | 情報１フラグ |
| 11FD | 0 | regist | 情報２フラグ |
| 1204 | 0 | regist | 情報３フラグ |
| 120B | 0 | regist | 情報４フラグ |
| 125E | 1 | TalkEvent | MS_22_INFO_02 |
| 12B9 | 2 | TalkEvent | MS_22_INFO_04 |
| 18D6 | 22 | UnitEscape | ?, 0 |
| 190B | 23 | regist | 宝箱１ |
| 1913 | 23 | regist | 宝箱２ |
| 191B | 23 | regist | 宝箱３ |
| 1923 | 23 | regist | 宝箱４ |
| 192B | 23 | regist | 宝箱５ |
| 1933 | 23 | regist | 宝箱６ |
| 193B | 23 | regist | 宝箱７ |
| 1943 | 23 | regist | 宝箱８ |
| 194B | 23 | regist | F2917 |
| 1953 | 23 | regist | F2406 |
| 195B | 23 | regist | F1406 |
| 1963 | 23 | regist | F0809 |
| 196B | 23 | regist | F1726 |
| 1973 | 23 | regist | F02151829 |
| 197B | 23 | regist | F02021029 |
| 1983 | 23 | regist | F02021329 |
| 198B | 23 | regist | F02211829 |
| 1993 | 23 | regist | イナとアイクのイベントトリガ |
| 1A1F | 25 | regist | 増援トリガ１ |
| 1A27 | 25 | regist | 増援トリガ２ |
| 1A2F | 25 | regist | 増援トリガ３ |
| 1A37 | 25 | regist | 増援イベント１ |
| 1A3F | 25 | regist | 増援イベント２ |
| 1A47 | 25 | regist | 増援イベント３ |
| 1A4F | 25 | regist | イナとアイクのイベント |
| 1A57 | 25 | regist | タウロニオ仲間 |
| 1A5F | 25 | regist | タウロニオ戦闘子供 |
| 1A67 | 25 | regist | タウロニオ戦闘会話 |
| 1A6F | 25 | regist | カタサイ戦闘会話 |
| 1A77 | 25 | regist | カタサイ戦闘会話タウロニオ |
| 1A7F | 25 | regist | ボス戦闘会話アイク |
| 1A87 | 25 | regist | ボス戦闘会話牙 |
| 1A8F | 25 | regist | ボス戦闘会話鷹 |
| 1A97 | 25 | regist | ボス戦闘会話リュシオン |
| 1A9F | 25 | regist | ボス戦闘会話ミスト |
| 1AA7 | 25 | regist | ボス戦闘会話 |
| 1AEA | 26 | InstantDisposRank | bmap22_first |
| 1AF2 | 26 | InstantDispos | bmap22_tauroneo_c |
| 1B33 | 27 | SallySetByGroup | bmap22_mikata_c |
| 1BF8 | 28 | TalkEvent | MS_22_GMAP_01 |
| 1C18 | 28 | TalkResume |  |
| 1C3E | 28 | TalkResume |  |
| 1CF6 | 29 | ChapterMoviePlay | 22 |
| 1D41 | 30 | ForceGetCount | 5 |
| 1D63 | 30 | MapLoad | bmap22 |
| 1D71 | 30 | InstantDisposSetMode | bmap22_mikata_n, bmap22_mikata_h, bmap22_mikata_m |
| 1D76 | 30 | AllUnitEscape |  |
| 1D8B | 30 | Join | always_dbg_mik_02 |
| 1D93 | 30 | Join | always_dbg_mik_03 |
| 1D9B | 30 | Join | always_dbg_mik_05 |
| 1DA3 | 30 | Join | always_dbg_mik_08 |
| 1DAB | 30 | Join | always_dbg_mik_09 |
| 1DB3 | 30 | Join | always_dbg_mik_10 |
| 1DBB | 30 | Join | always_dbg_mik_11 |
| 1DC3 | 30 | Join | always_dbg_mik_12 |
| 1DCB | 30 | Join | always_dbg_mik_13 |
| 1DD3 | 30 | Join | always_dbg_mik_14 |
| 1DDB | 30 | Join | always_dbg_mik_15 |
| 1DE3 | 30 | Join | always_dbg_mik_16 |
| 1DEB | 30 | Join | always_dbg_mik_17 |
| 1DF3 | 30 | Join | always_dbg_mik_19 |
| 1DFB | 30 | Join | always_dbg_mik_21 |
| 1EFA | 30 | TalkEvent | MS_22_OP_01_00 |
| 1F28 | 30 | TalkEvent | MS_22_OP_02 |
| 1F41 | 30 | TalkResume |  |
| 1F50 | 30 | TalkResume |  |
| 1F69 | 30 | TalkResume |  |
| 1FDB | 31 | TalkEvent | MS_22_OP_03 |
| 2002 | 31 | MapLoad | bmap22 |
| 202D | 31 | InstantDisposRank | bmap22_first |
| 2035 | 31 | InstantDispos | bmap22_tauroneo_c |
| 2045 | 31 | ForceGetCount | 1 |
| 204E | 31 | ForceGetFirst | 1 |
| 20EA | 31 | InstantDispos | bmap22_ena_preload_c |
| 22A5 | 31 | TalkEvent | MS_22_OP_04 |
| 237A | 31 | UnitEscapeByPID | PID_ENA_EV2 |
| 238A | 31 | TalkEvent | MS_22_OP_04_1 |
| 2399 | 31 | TalkResume |  |
| 23D9 | 31 | TalkResume |  |
| 2426 | 31 | ForceGetCount | 1 |
| 242F | 31 | ForceGetFirst | 1 |
| 249F | 31 | TalkEvent | MS_22_OP_05 |
| 2547 | 31 | SallySetByGroup | bmap22_mikata_c |
| 254F | 31 | Dispos | bmap22_mikata_c |
| 25BF | 31 | UnitForcedSallyByPID | PID_IKE |
| 25C7 | 31 | UnitDontMoveSallyByPID | PID_IKE |
| 281E | 35 | TalkEvent | MS_22_EV_XX |
| 28C3 | 36 | TalkEvent | MS_22_02_TK_IKE |
| 28CD | 36 | UnitTransferToForceByPID | PID_TAURONEO, 0 |
| 2952 | 37 | DisposSetMode | bmap22_z01_n, bmap22_z01_h, bmap22_z01_m |
| 299E | 38 | DisposSetMode | bmap22_z02_n, bmap22_z02_h, bmap22_z02_m |
| 29EA | 39 | DisposSetMode | bmap22_z03_n, bmap22_z03_h, bmap22_z03_m |
| 2A1A | 40 | Dispos | bmap22_z05_m |
| 2A4A | 41 | Dispos | bmap22_z04_m |
| 2A79 | 42 | DisposSetMode | bmap22_z04_n, bmap22_z04_h, bmap22_z04_m |
| 2AA9 | 43 | DisposSetMode | bmap22_z05_n, bmap22_z05_h, bmap22_z05_m |
| 2AD5 | 44 | BMGetPhase |  |
| 2AE2 | 44 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2AED | 44 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2AF5 | 44 | TalkEvent | MS_22_02_BT_CHILD |
| 2B02 | 44 | SoundBossTalkEnd |  |
| 2B31 | 45 | BMGetPhase |  |
| 2B3E | 45 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2B49 | 45 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2B51 | 45 | TalkEvent | MS_22_02_BT_CHILD |
| 2B5E | 45 | SoundBossTalkEnd |  |
| 2B8D | 46 | BMGetPhase |  |
| 2B9A | 46 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2BA5 | 46 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2BAD | 46 | TalkEvent | MS_22_02_BT_CHILD |
| 2BBA | 46 | SoundBossTalkEnd |  |
| 2BE9 | 47 | BMGetPhase |  |
| 2BF6 | 47 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2C01 | 47 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2C09 | 47 | TalkEvent | MS_22_02_BT_CHILD |
| 2C16 | 47 | SoundBossTalkEnd |  |
| 2C45 | 48 | BMGetPhase |  |
| 2C52 | 48 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2C5D | 48 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2C65 | 48 | TalkEvent | MS_22_02_BT_CHILD |
| 2C72 | 48 | SoundBossTalkEnd |  |
| 2CCE | 49 | BMGetPhase |  |
| 2D1B | 49 | BMGetPhase |  |
| 2D28 | 49 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2D33 | 49 | SoundBossTalkStart | BGM_BTL_CP01 |
| 2D3B | 49 | TalkEvent | MS_22_02_BT |
| 2D40 | 49 | SoundBossTalkEnd |  |
| 2D7F | 50 | DefaultDieTalk |  |
| 2D8A | 50 | TalkEvent | MS_22_02_DIE |
| 2DBC | 51 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2DC4 | 51 | TalkEvent | MS_22_01_BT_R3 |
| 2DD1 | 51 | SoundBossTalkEnd |  |
| 2E06 | 52 | BMGetPhase |  |
| 2E36 | 52 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2E3E | 52 | TalkEvent | MS_22_01_BT |
| 2E4B | 52 | SoundBossTalkEnd |  |
| 2E7C | 53 | TalkEvent | MS_22_01_DIE |
| 2EB0 | 54 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2EB8 | 54 | TalkEvent | MS_22_BT_IKE |
| 2EC5 | 54 | SoundBossTalkEnd |  |
| 2EF8 | 55 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2F00 | 55 | TalkEvent | MS_22_BT_R1 |
| 2F0D | 55 | SoundBossTalkEnd |  |
| 2F40 | 56 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2F48 | 56 | TalkEvent | MS_22_BT_R1 |
| 2F55 | 56 | SoundBossTalkEnd |  |
| 2F88 | 57 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2F90 | 57 | TalkEvent | MS_22_BT_R1 |
| 2F9D | 57 | SoundBossTalkEnd |  |
| 2FD0 | 58 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2FD8 | 58 | TalkEvent | MS_22_BT_R2 |
| 2FE5 | 58 | SoundBossTalkEnd |  |
| 3018 | 59 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 3020 | 59 | TalkEvent | MS_22_BT_R2 |
| 302D | 59 | SoundBossTalkEnd |  |
| 3060 | 60 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 3068 | 60 | TalkEvent | MS_22_BT_RI |
| 3075 | 60 | SoundBossTalkEnd |  |
| 30A8 | 61 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 30B0 | 61 | TalkEvent | MS_22_BT_MI |
| 30BD | 61 | SoundBossTalkEnd |  |
| 3138 | 62 | BMGetPhase |  |
| 31A0 | 62 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 31A8 | 62 | TalkEvent | MS_22_BT |
| 31B5 | 62 | SoundBossTalkEnd |  |
| 31E4 | 63 | TalkEvent | MS_22_DIE |
| 3258 | 64 | InstantDispos | bmap22_ena_c |
| 3260 | 64 | InstantDispos | bmap22_narsil_c |
| 3268 | 64 | InstantDispos | bmap22_evt_tiamat_c |
| 3275 | 64 | Dispos_ForEventSenerio | bmap22_evt_senerio_c, bmap22_evt_senerio2_c, 1 |
| 327E | 64 | ForceGetFirst | 1 |
| 328A | 64 | UnitEscape | ?, 0 |
| 3296 | 64 | ForceGetFirst | 3 |
| 32A2 | 64 | UnitEscape | ?, 0 |
| 32AD | 64 | UnitEscapeByPID | PID_TIAMAT |
| 32B5 | 64 | UnitEscapeByPID | PID_SENERIO |
| 3300 | 64 | ForceGetCount | 0 |
| 3309 | 64 | ForceGetFirst | 0 |
| 3365 | 64 | TalkEvent | MS_22_ED_01 |
| 33B7 | 64 | TalkEvent | MS_22_ED_02 |
| 344D | 64 | TalkEvent | MS_22_ED_02_2 |
| 34EE | 64 | TalkEvent | MS_22_ED_03 |
| 3529 | 64 | TalkEvent | MS_22_ED_03_2 |
| 354D | 64 | TalkEvent | MS_22_ED_03_3 |
| 35F5 | 64 | UnitEscapeByPID | PID_ENA |
| 35FD | 64 | InstantDispos | bmap22_event_sol_c |
| 3639 | 64 | TalkEvent | MS_22_ED_04 |
| 366A | 64 | TalkEvent | MS_22_ED_05 |
| 36E5 | 64 | TalkEvent | MS_22_ED_06 |
| 3714 | 64 | AllUnitEscape |  |
| 37D8 | 64 | TalkEvent | MS_22_ED_07 |
| 37F4 | 64 | TalkResume |  |
| 3820 | 64 | TalkResume |  |
| 389E | 66 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.22: Solo — internal 23

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 11, 'h': 17, 'm': 17, 'n': 17}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap23/dispos_c.bin:bmap23_engn0_c`: F3: PID_MELTY
- `bmap23/dispos_c.bin:bmap23_mikata_c`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LOFA, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap23/dispos_h.bin:bmap23_engn0_h`: F3: PID_MELTY
- `bmap23/dispos_h.bin:bmap23_f01_h`: F1: PID_23_PAL_BSH_EV
- `bmap23/dispos_h.bin:bmap23_f_boss_h`: F1: PID_23_SIK_BUKA1, PID_23_SIK_BUKA2, PID_SIRKUKO
- `bmap23/dispos_h.bin:bmap23_first2_h`: F1: PID_23_PAL_BSH, PID_23_PAL_PRS
- `bmap23/dispos_h.bin:bmap23_first3_h`: F1: PID_12_THIEF
- `bmap23/dispos_h.bin:bmap23_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_MAG, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR
- `bmap23/dispos_h.bin:bmap23_mikata_h`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap23/dispos_h.bin:bmap23_z01_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_FIG
- `bmap23/dispos_h.bin:bmap23_z02_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SAG
- `bmap23/dispos_h.bin:bmap23_z03_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SMS
- `bmap23/dispos_h.bin:bmap23_z04_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SNP
- `bmap23/dispos_h.bin:bmap23_z05_h`: F1: PID_12_THIEF
- `bmap23/dispos_m.bin:bmap23_engn0_m`: F3: PID_MELTY
- `bmap23/dispos_m.bin:bmap23_f01_m`: F1: PID_23_PAL_BSH_EV
- `bmap23/dispos_m.bin:bmap23_f_boss_m`: F1: PID_23_SIK_BUKA1, PID_23_SIK_BUKA2, PID_SIRKUKO
- `bmap23/dispos_m.bin:bmap23_first2_m`: F1: PID_23_PAL_BSH, PID_23_PAL_PRS
- `bmap23/dispos_m.bin:bmap23_first3_m`: F1: PID_12_THIEF
- `bmap23/dispos_m.bin:bmap23_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_MAG, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR
- `bmap23/dispos_m.bin:bmap23_mikata_m`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap23/dispos_m.bin:bmap23_z01_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_FIG
- `bmap23/dispos_m.bin:bmap23_z02_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SAG
- `bmap23/dispos_m.bin:bmap23_z03_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SMS
- `bmap23/dispos_m.bin:bmap23_z04_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SNP
- `bmap23/dispos_m.bin:bmap23_z05_m`: F1: PID_12_THIEF
- `bmap23/dispos_n.bin:bmap23_engn0_n`: F3: PID_MELTY
- `bmap23/dispos_n.bin:bmap23_f01_n`: F1: PID_23_PAL_BSH_EV
- `bmap23/dispos_n.bin:bmap23_f_boss_n`: F1: PID_23_SIK_BUKA1, PID_23_SIK_BUKA2, PID_SIRKUKO
- `bmap23/dispos_n.bin:bmap23_first2_n`: F1: PID_23_PAL_BSH, PID_23_PAL_PRS
- `bmap23/dispos_n.bin:bmap23_first3_n`: F1: PID_12_THIEF
- `bmap23/dispos_n.bin:bmap23_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_MAG, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR
- `bmap23/dispos_n.bin:bmap23_mikata_n`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KEVIN, PID_KILROY, PID_LETHE, PID_LOFA, PID_MIST, PID_MORDY, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_VULCI, PID_ZIHARK
- `bmap23/dispos_n.bin:bmap23_z01_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_FIG
- `bmap23/dispos_n.bin:bmap23_z02_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SAG
- `bmap23/dispos_n.bin:bmap23_z03_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SMS
- `bmap23/dispos_n.bin:bmap23_z04_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SNP
- `bmap23/dispos_n.bin:bmap23_z05_n`: F1: PID_12_THIEF

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| FC6 | 0 | regist | 情報１フラグ |
| FCD | 0 | regist | 情報２フラグ |
| FD4 | 0 | regist | 情報３フラグ |
| FDB | 0 | regist | 情報４フラグ |
| FE2 | 0 | regist | 情報５フラグ |
| 1017 | 1 | TalkEvent | MS_23_INFO_02 |
| 105D | 2 | TalkEvent | MS_23_INFO_05 |
| 123E | 9 | UnitEscape | ?, 0 |
| 1296 | 10 | UnitEscape | ?, 0 |
| 12EE | 11 | UnitEscape | ?, 0 |
| 1346 | 12 | UnitEscape | ?, 0 |
| 1507 | 18 | regist | F0306 |
| 150F | 18 | regist | F0308 |
| 1517 | 18 | regist | F0310 |
| 151F | 18 | regist | F2306 |
| 1527 | 18 | regist | F2308 |
| 152F | 18 | regist | F2310 |
| 1537 | 18 | regist | F03070815 |
| 153F | 18 | regist | F14071915 |
| 1547 | 18 | regist | F08031409 |
| 154F | 18 | regist | F14081915 |
| 1557 | 18 | regist | F03080815 |
| 15AB | 20 | regist | 増援トリガ３ |
| 15B3 | 20 | regist | 増援トリガ４ |
| 15BB | 20 | regist | 増援トリガ５ |
| 15C3 | 20 | regist | 増援イベント３ |
| 15CB | 20 | regist | 増援イベント４ |
| 15D3 | 20 | regist | 増援イベント５ |
| 15DB | 20 | regist | 神官死亡 |
| 15E3 | 20 | regist | トメナミ死亡 |
| 15EB | 20 | regist | ボス戦闘会話 |
| 15F3 | 20 | regist | ボス戦闘会話アイク |
| 15FB | 20 | regist | ボス戦闘会話獣 |
| 1603 | 20 | regist | ボス戦闘会話鳥 |
| 160B | 20 | regist | ボス戦闘会話タウロニオ |
| 1613 | 20 | regist | ボス戦闘会話リュシオン |
| 1656 | 21 | InstantDisposRank | bmap23_f_boss |
| 165E | 21 | InstantDisposRank | bmap23_first |
| 1666 | 21 | InstantDisposRank | bmap23_first2 |
| 166E | 21 | InstantDisposRank | bmap23_f01 |
| 1684 | 21 | InstantDisposRank | bmap23_first3 |
| 16C3 | 22 | SallySetByGroup | bmap23_mikata_c |
| 1787 | 23 | TalkEvent | MS_23_GMAP_01 |
| 17A7 | 23 | TalkResume |  |
| 17D8 | 23 | TalkResume |  |
| 1842 | 24 | ChapterMoviePlay | 23 |
| 188D | 25 | ForceGetCount | 5 |
| 18AF | 25 | MapLoad | bmap23 |
| 18BD | 25 | InstantDisposSetMode | bmap23_mikata_n, bmap23_mikata_h, bmap23_mikata_m |
| 18C2 | 25 | AllUnitEscape |  |
| 18D7 | 25 | Join | always_dbg_mik_13 |
| 18DF | 25 | Join | always_dbg_mik_14 |
| 18E7 | 25 | Join | always_dbg_mik_15 |
| 18EF | 25 | Join | always_dbg_mik_16 |
| 18F7 | 25 | Join | always_dbg_mik_17 |
| 18FF | 25 | Join | always_dbg_mik_19 |
| 1910 | 25 | UnitTransferToForceByPID | PID_RIEUSION, 6 |
| 1A04 | 25 | TalkEvent | MS_23_OP_01 |
| 1A35 | 25 | TalkEvent | MS_23_OP_02 |
| 1A69 | 25 | TalkEvent | MS_23_OP_03 |
| 1ADC | 26 | TalkEvent | MS_23_OP_04 |
| 1B11 | 26 | TalkEvent | MS_23_OP_05 |
| 1B33 | 26 | UnitGetForce | ? |
| 1B5A | 26 | TalkEvent | MS_23_OP_05_X |
| 1B9A | 26 | TalkResume |  |
| 1BB3 | 26 | TalkResume |  |
| 1BE5 | 26 | TalkEvent | MS_23_OP_05_XX |
| 1C25 | 26 | TalkResume |  |
| 1C3E | 26 | TalkResume |  |
| 1C84 | 26 | TalkEvent | MS_23_OP_06 |
| 1CAB | 26 | MapLoad | bmap23 |
| 1CC6 | 26 | InstantDisposRank | bmap23_f_boss |
| 1CCE | 26 | InstantDisposRank | bmap23_first |
| 1CD6 | 26 | InstantDisposRank | bmap23_first2 |
| 1CDB | 26 | AllUnitEscape |  |
| 1CE3 | 26 | InstantDisposRank | bmap23_f01 |
| 1D0D | 26 | SallySetByGroup | bmap23_mikata_c |
| 1D15 | 26 | InstantDispos | bmap23_mikata_c |
| 1F44 | 26 | TalkEvent | MS_23_OP_07_01 |
| 1F50 | 26 | TalkResume |  |
| 1F9B | 26 | InstantDisposSetMode | bmap23_f_boss_n, bmap23_f_boss_h, bmap23_f_boss_m |
| 2113 | 26 | TalkEvent | MS_23_OP_07_02 |
| 21DC | 26 | TalkEvent | MS_23_OP_07_03 |
| 2259 | 26 | DisposAsynchronous | bmap23_first_n |
| 226B | 26 | DisposAsynchronous | bmap23_first_h |
| 2276 | 26 | DisposAsynchronous | bmap23_first_m |
| 2285 | 26 | DisposAsynchronous | bmap23_first2_n |
| 2297 | 26 | DisposAsynchronous | bmap23_first2_h |
| 22A2 | 26 | DisposAsynchronous | bmap23_first2_m |
| 23F1 | 26 | TalkEvent | MS_23_OP_07_04 |
| 24F9 | 26 | TalkEvent | MS_23_OP_07_05 |
| 2615 | 26 | InstantDisposRank | bmap23_first3 |
| 262E | 26 | UnitForcedSallyByPID | PID_IKE |
| 2636 | 26 | UnitDontMoveSallyByPID | PID_IKE |
| 26A7 | 28 | Dispos | bmap23_z05_h |
| 26E3 | 29 | DisposSetMode | bmap23_z01_n, bmap23_z01_h, bmap23_z01_m |
| 271F | 30 | DisposSetMode | bmap23_z02_n, bmap23_z02_h, bmap23_z02_m |
| 2778 | 31 | DisposSetMode | bmap23_z03_n, bmap23_z03_h, bmap23_z03_m |
| 27D4 | 32 | DisposSetMode | bmap23_z04_n, bmap23_z04_h, bmap23_z04_m |
| 2848 | 35 | TalkEvent | MS_23_DIE_TOMENAMI |
| 288C | 36 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2894 | 36 | TalkEvent | MS_23_BT_IKE |
| 28A1 | 36 | SoundBossTalkEnd |  |
| 28D4 | 37 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 28DC | 37 | TalkEvent | MS_23_BT_R1 |
| 28E9 | 37 | SoundBossTalkEnd |  |
| 291C | 38 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2924 | 38 | TalkEvent | MS_23_BT_R1 |
| 2931 | 38 | SoundBossTalkEnd |  |
| 2964 | 39 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 296C | 39 | TalkEvent | MS_23_BT_R1 |
| 2979 | 39 | SoundBossTalkEnd |  |
| 29AC | 40 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 29B4 | 40 | TalkEvent | MS_23_BT_R2 |
| 29C1 | 40 | SoundBossTalkEnd |  |
| 29F4 | 41 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 29FC | 41 | TalkEvent | MS_23_BT_R2 |
| 2A09 | 41 | SoundBossTalkEnd |  |
| 2A3C | 42 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2A44 | 42 | TalkEvent | MS_23_BT_R3 |
| 2A51 | 42 | SoundBossTalkEnd |  |
| 2A84 | 43 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2A8C | 43 | TalkEvent | MS_23_BT_RI |
| 2A99 | 43 | SoundBossTalkEnd |  |
| 2B14 | 44 | BMGetPhase |  |
| 2B7C | 44 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2B84 | 44 | TalkEvent | MS_23_BT |
| 2B91 | 44 | SoundBossTalkEnd |  |
| 2BC0 | 45 | TalkEvent | MS_23_DIE |
| 2C4D | 46 | ForceGetCount | 1 |
| 2C56 | 46 | ForceGetFirst | 1 |
| 2CA0 | 46 | AllUnitEscape |  |
| 2D0D | 46 | TalkEvent | MS_23_ED_SPECIAL |
| 2D3C | 46 | TalkEvent | MS_23_ED_SPECIAL_DEL |
| 2D68 | 46 | TalkEvent | MS_23_ED_SPECIAL_2 |
| 2DB7 | 46 | TalkEvent | MS_23_ED_00A |
| 2DC2 | 46 | TalkEvent | MS_23_ED_00A_B |
| 2DCD | 46 | TalkEvent | MS_23_ED_00B |
| 2E22 | 46 | UnitCheckDeadHereByPID | PID_RIEUSION |
| 2E2C | 46 | TalkEvent | MS_23_ED_01_X |
| 2E37 | 46 | TalkEvent | MS_23_ED_01 |
| 2E4C | 46 | UnitCheckDeadHereByPID | PID_RIEUSION |
| 2E56 | 46 | TalkEvent | MS_23_ED_02B |
| 2E61 | 46 | TalkEvent | MS_23_ED_02A |
| 2F4D | 46 | TalkEvent | MS_23_ED_02X |
| 2F94 | 46 | TalkEvent | MS_23_ED_02XX |
| 2FB5 | 46 | TalkEvent | MS_23_ED_03 |
| 2FD5 | 46 | TalkResume |  |
| 2FE4 | 46 | TalkResume |  |
| 2FF3 | 46 | TalkResume |  |
| 3024 | 46 | TalkEvent | MS_23_ED_03_2 |
| 3048 | 46 | TalkResume |  |
| 3064 | 46 | TalkResume |  |
| 30A2 | 46 | UnitGetForce | ? |
| 30B3 | 46 | TalkEvent | MS_23_ED_03_3 |
| 30BE | 46 | TalkEvent | MS_23_ED_03_4 |
| 3142 | 48 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.23: The Great Bridge — internal 24

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 12, 'h': 12, 'm': 12, 'n': 12}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap24/dispos_c.bin:bmap24_engn0_c`: F3: PID_MELTY
- `bmap24/dispos_c.bin:bmap24_first_c`: F1: PID_HAAR
- `bmap24/dispos_c.bin:bmap24_m01_c`: F0: PID_LAY
- `bmap24/dispos_c.bin:bmap24_m02_c`: F2: PID_C_ZAKO, PID_LUCHINO, PID_ULYSSES
- `bmap24/dispos_c.bin:bmap24_mikata_c`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_ZIHARK
- `bmap24/dispos_c.bin:bmap24_z_ev01_c`: F2: PID_C_ZAKO
- `bmap24/dispos_h.bin:bmap24_engn0_h`: F3: PID_MELTY
- `bmap24/dispos_h.bin:bmap24_first_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_ARC, PID_DAYNE_BSH, PID_DAYNE_DKN, PID_DAYNE_DKN_1, PID_DAYNE_DKN_2, PID_DAYNE_DKN_3, PID_DAYNE_FIG, PID_DAYNE_MAG, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_PRAGUE
- `bmap24/dispos_h.bin:bmap24_mikata_h`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_ZIHARK
- `bmap24/dispos_h.bin:bmap24_z01_h`: F1: PID_DAYNE_DKN_1, PID_DAYNE_DKN_2, PID_DAYNE_DKN_3
- `bmap24/dispos_h.bin:bmap24_zoen1_h`: F1: PID_DAYNE_DKN
- `bmap24/dispos_h.bin:bmap24_zoen2_h`: F1: PID_DAYNE_SMS, PID_DAYNE_SRD
- `bmap24/dispos_h.bin:bmap24_zoen3_h`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN
- `bmap24/dispos_m.bin:bmap24_engn0_m`: F3: PID_MELTY
- `bmap24/dispos_m.bin:bmap24_first_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DKN_1, PID_DAYNE_DKN_2, PID_DAYNE_FIG, PID_DAYNE_MAG, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_PRAGUE
- `bmap24/dispos_m.bin:bmap24_mikata_m`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_ZIHARK
- `bmap24/dispos_m.bin:bmap24_z01_m`: F1: PID_DAYNE_DKN_1, PID_DAYNE_DKN_2, PID_DAYNE_DKN_3
- `bmap24/dispos_m.bin:bmap24_zoen1_m`: F1: PID_DAYNE_DKN
- `bmap24/dispos_m.bin:bmap24_zoen2_m`: F1: PID_DAYNE_SMS, PID_DAYNE_SRD
- `bmap24/dispos_m.bin:bmap24_zoen3_m`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN
- `bmap24/dispos_n.bin:bmap24_engn0_n`: F3: PID_MELTY
- `bmap24/dispos_n.bin:bmap24_first_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DKN_1, PID_DAYNE_DKN_2, PID_DAYNE_FIG, PID_DAYNE_MAG, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_PRAGUE
- `bmap24/dispos_n.bin:bmap24_mikata_n`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_VOKE, PID_ZIHARK
- `bmap24/dispos_n.bin:bmap24_z01_n`: F1: PID_DAYNE_DKN_1, PID_DAYNE_DKN_2, PID_DAYNE_DKN_3
- `bmap24/dispos_n.bin:bmap24_zoen1_n`: F1: PID_DAYNE_DKN
- `bmap24/dispos_n.bin:bmap24_zoen2_n`: F1: PID_DAYNE_SMS, PID_DAYNE_SRD
- `bmap24/dispos_n.bin:bmap24_zoen3_n`: F1: PID_DAYNE_PLD, PID_DAYNE_SKN

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 104E | 0 | regist | 情報１フラグ |
| 1055 | 0 | regist | 情報２フラグ |
| 105C | 0 | regist | 情報３フラグ |
| 1063 | 0 | regist | 情報４フラグ |
| 106A | 0 | regist | 情報５フラグ |
| 109F | 1 | TalkEvent | MS_24_INFO_02 |
| 10AB | 1 | TalkEvent | MS_24_INFO_02_2 |
| 1106 | 2 | TalkEvent | MS_24_INFO_04 |
| 14E7 | 26 | regist | F07072414 |
| 14EF | 26 | regist | F07073714 |
| 14F7 | 26 | regist | F07072714 |
| 14FF | 26 | regist | F07073014 |
| 1507 | 26 | regist | F07073414 |
| 158F | 28 | regist | 増援トリガ１ |
| 1597 | 28 | regist | 増援トリガ２ |
| 159F | 28 | regist | 増援トリガ３ |
| 15A7 | 28 | regist | 増援イベント１ |
| 15AF | 28 | regist | 増援イベント２ |
| 15B7 | 28 | regist | 増援イベント３ |
| 15BF | 28 | regist | クリミア増援トリガ |
| 15C7 | 28 | regist | クリミア増援イベント１ |
| 15CF | 28 | regist | クリミア増援イベント２ |
| 15D7 | 28 | regist | ハール退場イベント |
| 15DF | 28 | regist | ハール再登場トリガ |
| 15E7 | 28 | regist | ハール再登場イベント |
| 15EF | 28 | regist | ドラゴンナイト１死亡 |
| 15F7 | 28 | regist | ドラゴンナイト２死亡 |
| 15FF | 28 | regist | ドラゴンナイト３死亡 |
| 1607 | 28 | regist | ハール会話 |
| 160F | 28 | regist | ハール戦闘 |
| 1617 | 28 | regist | ハール戦闘ジル |
| 161F | 28 | regist | ハール死亡 |
| 1627 | 28 | regist | ボス戦闘会話 |
| 162F | 28 | regist | ボス戦闘会話アイク |
| 1637 | 28 | regist | ボス戦闘会話セネリオ |
| 163F | 28 | regist | ボス戦闘会話獣 |
| 1647 | 28 | regist | ボス戦闘会話鳥 |
| 164F | 28 | regist | ボス戦闘会話ジル−タウロニオ |
| 1657 | 28 | regist | ボス戦闘会話リュシオン |
| 165F | 28 | regist | ボス戦闘会話ハール |
| 166D | 28 | regist | クリミアCP変更イベント |
| 16AA | 29 | InstantDisposRank | bmap24_first |
| 16B2 | 29 | InstantDispos | bmap24_first_c |
| 16FF | 30 | SallySetByGroup | bmap24_mikata_c |
| 1707 | 30 | SallyAddByGroup | bmap24_m01_c |
| 17CB | 31 | TalkEvent | MS_24_GMAP_01 |
| 17E2 | 31 | TalkResume |  |
| 1805 | 31 | TalkResume |  |
| 1912 | 32 | ChapterMoviePlay | 24 |
| 195D | 33 | ForceGetCount | 5 |
| 197F | 33 | MapLoad | bmap24 |
| 198D | 33 | InstantDisposSetMode | bmap24_mikata_n, bmap24_mikata_h, bmap24_mikata_m |
| 1992 | 33 | AllUnitEscape |  |
| 19A7 | 33 | Join | always_dbg_mik_12 |
| 19AF | 33 | Join | always_dbg_mik_13 |
| 19B7 | 33 | Join | always_dbg_mik_14 |
| 19BF | 33 | Join | always_dbg_mik_15 |
| 19C7 | 33 | Join | always_dbg_mik_16 |
| 19CF | 33 | Join | always_dbg_mik_17 |
| 19D7 | 33 | Join | always_dbg_mik_19 |
| 1A09 | 33 | TalkEvent | MS_24_OP_00 |
| 1A5F | 33 | TalkEvent | MS_24_OP_01 |
| 1A6E | 33 | TalkResume |  |
| 1A87 | 33 | TalkResume |  |
| 1AF9 | 34 | TalkEvent | MS_24_OP_02 |
| 1B2D | 34 | TalkEvent | MS_24_OP_03 |
| 1B5A | 34 | TalkEvent | MS_24_OP_03_2 |
| 1B81 | 34 | MapLoad | bmap24 |
| 1BD1 | 34 | SallySetByGroup | bmap24_mikata_c |
| 1BD9 | 34 | SallyAddByGroup | bmap24_m01_c |
| 1BE1 | 34 | InstantDispos | bmap24_mikata_c |
| 1BE9 | 34 | InstantDispos | bmap24_m01_c |
| 1C15 | 34 | ForceGetCount | 0 |
| 1C1E | 34 | ForceGetFirst | 0 |
| 1DE2 | 34 | TalkEvent | MS_24_OP_04 |
| 1F3E | 34 | TalkEvent | MS_24_OP_05 |
| 1F4F | 34 | ForceGetCount | 0 |
| 1F58 | 34 | ForceGetFirst | 0 |
| 1FCC | 34 | UnitForcedSallyByPID | PID_IKE |
| 1FD4 | 34 | UnitDontMoveSallyByPID | PID_IKE |
| 2060 | 35 | TalkEvent | MS_24_EV_03 |
| 20AB | 35 | UnitEscapeByPID | PID_HAAR |
| 20B3 | 35 | UnitEscapeByPID | PID_DAYNE_DKN_1 |
| 20BB | 35 | UnitEscapeByPID | PID_DAYNE_DKN_2 |
| 20C3 | 35 | UnitEscapeByPID | PID_DAYNE_DKN_3 |
| 21D0 | 36 | InstantDispos | bmap24_first_c |
| 21D8 | 36 | InstantDisposRank | bmap24_z01 |
| 21EA | 36 | UnitEscapeByPID | PID_DAYNE_DKN_1 |
| 21FC | 36 | UnitEscapeByPID | PID_DAYNE_DKN_2 |
| 220E | 36 | UnitEscapeByPID | PID_DAYNE_DKN_3 |
| 2310 | 36 | TalkEvent | MS_24_EV_04 |
| 2486 | 37 | InstantDispos | bmap24_m02_c |
| 248E | 37 | InstantDisposFirst | bmap24_z_ev01_c |
| 24B6 | 37 | TalkEvent | MS_24_EV_01 |
| 24E7 | 37 | UnitEscapeByPID | PID_ULYSSES |
| 259B | 37 | TalkEvent | MS_24_EV_02 |
| 26AB | 38 | TalkEvent | MS_24_TK_01 |
| 26B5 | 38 | UnitTransferToForceByPID | PID_HAAR, 0 |
| 273A | 39 | DisposSetMode | bmap24_zoen1_n, bmap24_zoen1_h, bmap24_zoen1_m |
| 2786 | 40 | DisposSetMode | bmap24_zoen2_n, bmap24_zoen2_h, bmap24_zoen2_m |
| 27D2 | 41 | DisposSetMode | bmap24_zoen3_n, bmap24_zoen3_h, bmap24_zoen3_m |
| 281B | 42 | ForceGetCount | 1 |
| 2834 | 42 | ForceGetCount | 2 |
| 283D | 42 | ForceGetFirst | 2 |
| 290D | 46 | BMGetPhase |  |
| 291A | 46 | SoundBossTalkStart | BGM_BTL_PL01 |
| 2925 | 46 | SoundBossTalkStart | BGM_BTL_CP01 |
| 292D | 46 | TalkEvent | MS_24_BT_JI |
| 2932 | 46 | SoundBossTalkEnd |  |
| 296E | 47 | BMGetPhase |  |
| 299B | 47 | BMGetPhase |  |
| 29A8 | 47 | SoundBossTalkStart | BGM_BTL_PL01 |
| 29B3 | 47 | SoundBossTalkStart | BGM_BTL_CP01 |
| 29BB | 47 | TalkEvent | MS_24_BT_HAAR |
| 29C0 | 47 | SoundBossTalkEnd |  |
| 29FF | 48 | DefaultDieTalk |  |
| 2A0A | 48 | TalkEvent | MS_24_DIE_HAAR |
| 2A44 | 49 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2A4C | 49 | TalkEvent | MS_24_BT_IKE |
| 2A59 | 49 | SoundBossTalkEnd |  |
| 2A8C | 50 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2A94 | 50 | TalkEvent | MS_24_BT_SE |
| 2AA1 | 50 | SoundBossTalkEnd |  |
| 2AD4 | 51 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2ADC | 51 | TalkEvent | MS_24_BT_R1 |
| 2AE9 | 51 | SoundBossTalkEnd |  |
| 2B1C | 52 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2B24 | 52 | TalkEvent | MS_24_BT_R1 |
| 2B31 | 52 | SoundBossTalkEnd |  |
| 2B64 | 53 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2B6C | 53 | TalkEvent | MS_24_BT_R1 |
| 2B79 | 53 | SoundBossTalkEnd |  |
| 2BAC | 54 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2BB4 | 54 | TalkEvent | MS_24_BT_R1 |
| 2BC1 | 54 | SoundBossTalkEnd |  |
| 2BF4 | 55 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2BFC | 55 | TalkEvent | MS_24_BT_R2 |
| 2C09 | 55 | SoundBossTalkEnd |  |
| 2C3C | 56 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2C44 | 56 | TalkEvent | MS_24_BT_R2 |
| 2C51 | 56 | SoundBossTalkEnd |  |
| 2C84 | 57 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2C8C | 57 | TalkEvent | MS_24_BT_R3 |
| 2C99 | 57 | SoundBossTalkEnd |  |
| 2CCC | 58 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2CD4 | 58 | TalkEvent | MS_24_BT_RI |
| 2CE1 | 58 | SoundBossTalkEnd |  |
| 2D14 | 59 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2D1C | 59 | TalkEvent | MS_24_BT_HA |
| 2D29 | 59 | SoundBossTalkEnd |  |
| 2DC2 | 60 | BMGetPhase |  |
| 2E42 | 60 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2E4A | 60 | TalkEvent | MS_24_BT |
| 2E57 | 60 | SoundBossTalkEnd |  |
| 2E88 | 61 | TalkEvent | MS_24_DIE |
| 2ED8 | 62 | AllUnitEscape |  |
| 2EF7 | 62 | TalkEvent | MS_24_ED_01 |
| 2F2D | 62 | UnitCheckDeadHereByPID | PID_LAY |
| 2F3B | 62 | TalkEvent | MS_24_ED_02_A |
| 2F46 | 62 | TalkEvent | MS_24_ED_02_B |
| 2F7B | 62 | TalkEvent | MS_24_ED_03 |
| 2F8A | 62 | TalkResume |  |
| 2FF6 | 64 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.24: Battle Reunion — internal 25

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 11, 'h': 11, 'm': 11, 'n': 11}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap25/dispos_c.bin:bmap25_engn0_c`: F3: PID_MELTY
- `bmap25/dispos_c.bin:bmap25_event_00_c`: F1: PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SNP, PID_DAYNE_SRD, PID_RIHITORU
- `bmap25/dispos_c.bin:bmap25_event_00b_c`: F2: PID_GEOFFRAY, PID_ULYSSES
- `bmap25/dispos_c.bin:bmap25_event_01_c`: F2: PID_DUMMY1
- `bmap25/dispos_c.bin:bmap25_event_04_c`: F1: PID_BLACKKNIGHT_EV2
- `bmap25/dispos_c.bin:bmap25_event_ike_c`: F2: PID_IKE_EV2
- `bmap25/dispos_c.bin:bmap25_m01_c`: F0: PID_LUCHINO, PID_ULYSSES
- `bmap25/dispos_c.bin:bmap25_m03_c`: F2: PID_C_ZAKO, PID_GEOFFRAY
- `bmap25/dispos_c.bin:bmap25_mikata_c`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap25/dispos_c.bin:bmap25_z_blk_c`: F1: PID_BLACKKNIGHT
- `bmap25/dispos_h.bin:bmap25_engn0_h`: F3: PID_MELTY
- `bmap25/dispos_h.bin:bmap25_event1_h`: F1: PID_BLACKKNIGHT
- `bmap25/dispos_h.bin:bmap25_first_h`: F1: PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_RIHITORU
- `bmap25/dispos_h.bin:bmap25_mikata_h`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap25/dispos_h.bin:bmap25_z01_h`: F1: PID_DAYNE_SKN
- `bmap25/dispos_h.bin:bmap25_z02_h`: F1: PID_DAYNE_DKN, PID_DAYNE_DMS
- `bmap25/dispos_h.bin:bmap25_z03_h`: F1: PID_BANDIT_MOU
- `bmap25/dispos_h.bin:bmap25_z04_h`: F1: PID_BANDIT_MOU
- `bmap25/dispos_h.bin:bmap25_z05_h`: F1: PID_DAYNE_BSH, PID_DAYNE_HAL, PID_DAYNE_SOL
- `bmap25/dispos_m.bin:bmap25_engn0_m`: F3: PID_MELTY
- `bmap25/dispos_m.bin:bmap25_event1_m`: F1: PID_BLACKKNIGHT
- `bmap25/dispos_m.bin:bmap25_first_m`: F1: PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_FIG, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_RIHITORU
- `bmap25/dispos_m.bin:bmap25_mikata_m`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap25/dispos_m.bin:bmap25_z02_m`: F1: PID_DAYNE_DKN, PID_DAYNE_DMS
- `bmap25/dispos_m.bin:bmap25_z03_m`: F1: PID_BANDIT_MOU
- `bmap25/dispos_m.bin:bmap25_z04_m`: F1: PID_BANDIT_MOU
- `bmap25/dispos_m.bin:bmap25_z05_m`: F1: PID_DAYNE_BSH, PID_DAYNE_HAL, PID_DAYNE_SOL
- `bmap25/dispos_n.bin:bmap25_engn0_n`: F3: PID_MELTY
- `bmap25/dispos_n.bin:bmap25_event1_n`: F1: PID_BLACKKNIGHT
- `bmap25/dispos_n.bin:bmap25_first_n`: F1: PID_DAYNE_ARC, PID_DAYNE_DKN, PID_DAYNE_DMS, PID_DAYNE_FIG, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SKN, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SOL, PID_DAYNE_SRD, PID_DAYNE_WAR, PID_RIHITORU
- `bmap25/dispos_n.bin:bmap25_mikata_n`: F0: PID_BOLE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap25/dispos_n.bin:bmap25_z02_n`: F1: PID_DAYNE_DKN, PID_DAYNE_DMS
- `bmap25/dispos_n.bin:bmap25_z03_n`: F1: PID_BANDIT_MOU
- `bmap25/dispos_n.bin:bmap25_z04_n`: F1: PID_BANDIT_MOU
- `bmap25/dispos_n.bin:bmap25_z05_n`: F1: PID_DAYNE_BSH, PID_DAYNE_HAL, PID_DAYNE_SOL
- `bmap25_2/dispos_c.bin:bmap25_2_event01_c`: F1: PID_BLACKKNIGHT_EV2; F2: PID_IKE_EV2

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 11D6 | 0 | regist | 情報１フラグ |
| 11DD | 0 | regist | 情報２フラグ |
| 11E4 | 0 | regist | 情報３フラグ |
| 11EB | 0 | regist | 情報４フラグ |
| 11F2 | 0 | regist | 情報５フラグ |
| 11F9 | 0 | regist | 情報６フラグ |
| 1243 | 1 | TalkEvent | MS_25_INFO_05 |
| 1286 | 2 | TalkEvent | MS_25_VIL_02 |
| 1336 | 4 | TalkEvent | MS_25_VIL_01 |
| 1AE3 | 17 | regist | F1237 |
| 1AEB | 17 | regist | F3412 |
| 1AF3 | 17 | regist | F10102625 |
| 1AFB | 17 | regist | F10104120 |
| 1B03 | 17 | regist | F10212633 |
| 1B0B | 17 | regist | F18213027 |
| 1B13 | 17 | regist | F10102520 |
| 1B1B | 17 | regist | F10212033 |
| 1B23 | 17 | regist | F21282333 |
| 1B83 | 19 | regist | 増援トリガ１ |
| 1B8B | 19 | regist | 増援トリガ２ |
| 1B93 | 19 | regist | 増援イベント１ |
| 1B9B | 19 | regist | 増援イベント２ |
| 1BA3 | 19 | regist | アイクジョフレ |
| 1BAB | 19 | regist | 漆黒の騎士戦闘アイクオンマップ |
| 1BB3 | 19 | regist | 漆黒の騎士戦闘アイク |
| 1BBB | 19 | regist | 漆黒の騎士退場イベント |
| 1BC3 | 19 | regist | 漆黒のとの戦闘後会話 |
| 1BCB | 19 | regist | ボス戦闘会話 |
| 1BD3 | 19 | regist | ボス戦闘会話アイク |
| 1BDB | 19 | regist | ボス戦闘会話獣 |
| 1BE3 | 19 | regist | ボス戦闘会話鳥 |
| 1BEB | 19 | regist | ボス戦闘会話タウロニオ |
| 1BF3 | 19 | regist | ボス戦闘会話リュシオン |
| 1C01 | 19 | regist | 会話ユリシーズ⇒アイク |
| 1C09 | 19 | regist | 会話ルキノ⇒アイク |
| 1C11 | 19 | regist | 会話アイク⇒ジョフレ |
| 1C19 | 19 | regist | 会話ジョフレ⇔ユリシーズ |
| 1C21 | 19 | regist | 会話ジョフレ⇔ルキノ |
| 1C29 | 19 | regist | 会話ジョフレ⇔ケビン |
| 1C31 | 19 | regist | 漆黒の騎士戦闘 |
| 1C6E | 20 | InstantDispos | bmap25_m03_c |
| 1C7D | 20 | InstantDisposRank | bmap25_first |
| 1C86 | 20 | ForceGetCount | 1 |
| 1C8F | 20 | ForceGetFirst | 1 |
| 1CFB | 21 | SallySetByGroup | bmap25_mikata_c |
| 1E44 | 22 | TalkEvent | MS_25_GMAP_01 |
| 1E5C | 22 | TalkResume |  |
| 1E85 | 22 | TalkResume |  |
| 1EF6 | 23 | ChapterMoviePlay | 25 |
| 1F41 | 24 | ForceGetCount | 5 |
| 1F63 | 24 | MapLoad | bmap25 |
| 1F71 | 24 | InstantDisposSetMode | bmap25_mikata_n, bmap25_mikata_h, bmap25_mikata_m |
| 1F76 | 24 | AllUnitEscape |  |
| 1F8B | 24 | Join | always_dbg_mik_11 |
| 1F93 | 24 | Join | always_dbg_mik_12 |
| 1F9B | 24 | Join | always_dbg_mik_13 |
| 1FA3 | 24 | Join | always_dbg_mik_14 |
| 1FF3 | 24 | MapLoad | bmap25 |
| 20C1 | 24 | AllUnitEscape |  |
| 20EC | 24 | TalkEvent | MS_25_OP_01 |
| 2129 | 24 | TalkEvent | MS_25_OP_02 |
| 2142 | 24 | TalkEvent | MS_25_OP_03 |
| 21AF | 25 | MapLoad | bmap25 |
| 21DA | 25 | InstantDispos | bmap25_event_00_c |
| 21F0 | 25 | InstantDispos | bmap25_event_00b_c |
| 2298 | 25 | TalkEvent | MS_25_OP_03X |
| 243C | 25 | TalkEvent | MS_25_OP_03X2 |
| 245F | 25 | TalkResume |  |
| 2485 | 25 | TalkResume |  |
| 2494 | 25 | TalkResume |  |
| 2523 | 25 | AllUnitEscape |  |
| 252B | 25 | InstantDispos | bmap25_m03_c |
| 2530 | 25 | AllUnitEscape |  |
| 2538 | 25 | InstantDisposRank | bmap25_first |
| 2541 | 25 | ForceGetCount | 1 |
| 254A | 25 | ForceGetFirst | 1 |
| 258B | 25 | SallySetByGroup | bmap25_mikata_c |
| 2593 | 25 | InstantDispos | bmap25_mikata_c |
| 25DA | 25 | TalkEvent | MS_25_OP_04 |
| 25F0 | 25 | TalkResume |  |
| 260E | 25 | Dispos | bmap25_m03_c |
| 262A | 25 | TalkEvent | MS_25_OP_04_02 |
| 26E6 | 25 | TalkEvent | MS_25_OP_04X |
| 273C | 25 | UnitForcedSallyByPID | PID_IKE |
| 2744 | 25 | UnitDontMoveSallyByPID | PID_IKE |
| 27EE | 26 | TalkEvent | MS_25_OP_05 |
| 2855 | 26 | TalkEvent | MS_25_OP_06 |
| 287A | 26 | ForceGetCount | 1 |
| 2883 | 26 | ForceGetFirst | 1 |
| 293F | 26 | TalkEvent | MS_25_OP_04X2 |
| 2A12 | 27 | InstantDispos | bmap25_m01_c |
| 2A1A | 27 | InstantDispos | bmap25_event_01_c |
| 2A91 | 27 | TalkEvent | MS_25_EV_01 |
| 2AE0 | 27 | DisposContinue | bmap25_m01_c |
| 2AF9 | 27 | UnitEscapeByPID | PID_DUMMY1 |
| 2B9F | 28 | Dispos | bmap25_z_blk_c |
| 2C05 | 28 | TalkEvent | MS_25_EV_02 |
| 2C6F | 28 | TalkEvent | MS_25_EV_03 |
| 2D21 | 29 | TalkEvent | MS_25_BT_02 |
| 2D8D | 29 | UnitEscapeByPID | PID_BLACKKNIGHT |
| 2DDE | 30 | TalkEvent | MS_25_TK_01 |
| 2E1E | 31 | TalkEvent | MS_25_TK_02 |
| 2E5E | 32 | TalkEvent | MS_25_TK_03 |
| 2E9E | 33 | TalkEvent | MS_25_TK_04 |
| 2EDE | 34 | TalkEvent | MS_25_TK_05 |
| 2F1E | 35 | TalkEvent | MS_25_TK_06 |
| 2F84 | 36 | DisposSetMode | bmap25_z01_h, bmap25_z01_h, bmap25_z01_m |
| 2FD2 | 37 | DisposSetMode | bmap25_z02_n, bmap25_z02_h, bmap25_z02_m |
| 3001 | 38 | DisposSetMode | bmap25_z04_n, bmap25_z04_h, bmap25_z04_m |
| 3031 | 39 | DisposSetMode | bmap25_z05_n, bmap25_z05_h, bmap25_z05_m |
| 3061 | 40 | DisposSetMode | bmap25_z03_n, bmap25_z03_h, bmap25_z03_m |
| 3093 | 41 | BMGetPhase |  |
| 30D6 | 41 | TalkEvent | MS_25_DIE_IKE |
| 30FC | 41 | TalkEvent | MDIE_IKE_4 |
| 3132 | 42 | LocalDieTalkWithBgmChange | , MS_25_DIE_GIOFLE |
| 3160 | 43 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 3168 | 43 | TalkEvent | MS_25_BT_BLK_IKE |
| 316D | 43 | SoundBossTalkEnd |  |
| 31AA | 44 | BMGetPhase |  |
| 31DA | 44 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 31E2 | 44 | TalkEvent | MS_25_BT_BLK |
| 31E7 | 44 | SoundBossTalkEnd |  |
| 3224 | 45 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 322C | 45 | TalkEvent | MS_25_BT_IKE |
| 3239 | 45 | SoundBossTalkEnd |  |
| 326C | 46 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3274 | 46 | TalkEvent | MS_25_BT_R1 |
| 3281 | 46 | SoundBossTalkEnd |  |
| 32B4 | 47 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 32BC | 47 | TalkEvent | MS_25_BT_R1 |
| 32C9 | 47 | SoundBossTalkEnd |  |
| 32FC | 48 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3304 | 48 | TalkEvent | MS_25_BT_R1 |
| 3311 | 48 | SoundBossTalkEnd |  |
| 3344 | 49 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 334C | 49 | TalkEvent | MS_25_BT_R1 |
| 3359 | 49 | SoundBossTalkEnd |  |
| 338C | 50 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3394 | 50 | TalkEvent | MS_25_BT_R2 |
| 33A1 | 50 | SoundBossTalkEnd |  |
| 33D4 | 51 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 33DC | 51 | TalkEvent | MS_25_BT_R2 |
| 33E9 | 51 | SoundBossTalkEnd |  |
| 341C | 52 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3424 | 52 | TalkEvent | MS_25_BT_R3 |
| 3431 | 52 | SoundBossTalkEnd |  |
| 3464 | 53 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 346C | 53 | TalkEvent | MS_25_BT_RI |
| 3479 | 53 | SoundBossTalkEnd |  |
| 34FE | 54 | BMGetPhase |  |
| 356E | 54 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 3576 | 54 | TalkEvent | MS_25_BT |
| 3583 | 54 | SoundBossTalkEnd |  |
| 35B4 | 55 | TalkEvent | MS_25_DIE |
| 368C | 56 | Dispos | bmap25_event_04_c |
| 36D3 | 56 | TalkEvent | MS_25_ED_01 |
| 372A | 56 | UnitTransferToForce | ?, 0 |
| 372F | 56 | AllUnitEscape |  |
| 379C | 56 | TalkEvent | MS_25_ED_02A |
| 37B7 | 56 | TalkEvent | MS_25_ED_02B |
| 37D2 | 56 | TalkEvent | MS_25_ED_02C |
| 37EE | 56 | TalkEvent | MS_25_ED_02D |
| 3809 | 56 | TalkEvent | MS_25_ED_02E |
| 3825 | 56 | TalkEvent | MS_25_ED_02F |
| 3841 | 56 | TalkEvent | MS_25_ED_02G |
| 385E | 56 | TalkEvent | MS_25_ED_02H |
| 38E2 | 56 | TalkEvent | MS_25_ED_03 |
| 395D | 56 | TalkEvent | MS_25_ED_03_2 |
| 39CA | 56 | MapLoad | bmap25_2 |
| 39F3 | 56 | InstantDispos | bmap25_2_event01_c |
| 3AAA | 56 | TalkEvent | MS_25_ED_X1 |
| 3BBE | 56 | TalkEvent | MS_25_ED_X2 |
| 3C7C | 56 | UnitEscapeByPID | PID_BLACKKNIGHT_EV2 |
| 3C9F | 56 | AllUnitEscape |  |
| 3D06 | 57 | BMGetTurn |  |
| 3D74 | 58 | TalkEvent | MS_25_GAMEOVER |
| 3DDE | 60 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.25: Strange Lands — internal 26

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 12, 'h': 12, 'm': 12, 'n': 12}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap26/dispos_c.bin:bmap26_engn0_c`: F3: PID_MELTY
- `bmap26/dispos_c.bin:bmap26_event_lay_c`: F2: PID_LAY_EV3
- `bmap26/dispos_c.bin:bmap26_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap26/dispos_c.bin:bmap26_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap26/dispos_c.bin:bmap26_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap26/dispos_c.bin:bmap26_event_tivern_c`: F2: PID_TIBARN
- `bmap26/dispos_c.bin:bmap26_mikata_c`: F0: PID_BOLE, PID_GEOFFRAY, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap26/dispos_h.bin:bmap26_engn0_h`: F3: PID_MELTY
- `bmap26/dispos_h.bin:bmap26_first_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_BSH, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_HAL_1, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_GURORMERU
- `bmap26/dispos_h.bin:bmap26_mikata_h`: F0: PID_BOLE, PID_GEOFFRAY, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap26/dispos_h.bin:bmap26_z01_h`: F1: PID_DAYNE_DKN, PID_DAYNE_DMS_1
- `bmap26/dispos_h.bin:bmap26_z02_h`: F1: PID_ACTORMANQUE_D
- `bmap26/dispos_m.bin:bmap26_engn0_m`: F3: PID_MELTY
- `bmap26/dispos_m.bin:bmap26_first_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_BSH, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_HAL_1, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_GURORMERU
- `bmap26/dispos_m.bin:bmap26_mikata_m`: F0: PID_BOLE, PID_GEOFFRAY, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap26/dispos_m.bin:bmap26_z01_m`: F1: PID_DAYNE_DMS_1
- `bmap26/dispos_m.bin:bmap26_z02_m`: F1: PID_DAYNE_DMS_1
- `bmap26/dispos_n.bin:bmap26_engn0_n`: F3: PID_MELTY
- `bmap26/dispos_n.bin:bmap26_first_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_BSH, PID_DAYNE_FIG, PID_DAYNE_HAL, PID_DAYNE_HAL_1, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_GURORMERU
- `bmap26/dispos_n.bin:bmap26_mikata_n`: F0: PID_BOLE, PID_GEOFFRAY, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap26/dispos_n.bin:bmap26_z01_n`: F1: PID_DAYNE_DMS_1
- `bmap26/dispos_n.bin:bmap26_z02_n`: F1: PID_DAYNE_DMS_1
- `bmap26_2/dispos_c.bin:bmap26_2_event01_c`: F1: PID_DAYNE_SOL_1, PID_DAYNE_SOL_2, PID_DAYNE_SOL_3, PID_DAYNE_SOL_4, PID_DAYNE_SOL_5; F2: PID_DUMMY1, PID_IKE_EV, PID_LAY_EV3, PID_RIEUSION_EV, PID_TIAMAT_EV, PID_TIBARN_EV
- `bmap26_2/dispos_c.bin:bmap26_2_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap26_2/dispos_c.bin:bmap26_2_event_senerio_c`: F2: PID_SENERIO_EV

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 12A2 | 0 | regist | 情報１フラグ |
| 12A9 | 0 | regist | 情報２フラグ |
| 12B0 | 0 | regist | 情報３フラグ |
| 12B7 | 0 | regist | 情報４フラグ |
| 12BE | 0 | regist | 情報５フラグ |
| 12C5 | 0 | regist | ラルゴ仲間 |
| 12FB | 1 | TalkEvent | MS_26_INFO_01 |
| 1342 | 2 | TalkEvent | MS_26_INFO_02 |
| 1396 | 3 | TalkEvent | MS_26_INFO_05_A |
| 13D0 | 3 | TalkEvent | MS_26_INFO_05_A_A |
| 13E8 | 3 | Join | always_rarugo |
| 13F3 | 3 | TalkEvent | MS_26_INFO_05_A_B |
| 1405 | 3 | TalkEvent | MS_26_INFO_05_B |
| 193F | 31 | regist | F03140327 |
| 1947 | 31 | regist | F08080827 |
| 194F | 31 | regist | F09080927 |
| 1957 | 31 | regist | F11091127 |
| 195F | 31 | regist | F13081327 |
| 1967 | 31 | regist | F17092112 |
| 196F | 31 | regist | F16072110 |
| 1977 | 31 | regist | F14161722 |
| 197F | 31 | regist | F18132118 |
| 1987 | 31 | regist | F03032416 |
| 198F | 31 | regist | F03032412 |
| 1997 | 31 | regist | F04150419 |
| 199F | 31 | regist | F05140615 |
| 1A7F | 33 | regist | 増援トリガ１ |
| 1A87 | 33 | regist | 増援トリガ２ |
| 1A8F | 33 | regist | 増援イベント１ |
| 1A97 | 33 | regist | 増援イベント２ |
| 1A9F | 33 | regist | 岩トリガ１ |
| 1AA7 | 33 | regist | 岩トリガ２ |
| 1AAF | 33 | regist | 岩トリガ３ |
| 1AB7 | 33 | regist | 岩トリガ４ |
| 1ABF | 33 | regist | 岩トリガ５ |
| 1AC7 | 33 | regist | 岩トリガ６ |
| 1ACF | 33 | regist | 岩トリガ７ |
| 1AD7 | 33 | regist | 岩トリガ８ |
| 1ADF | 33 | regist | 岩トリガ９ |
| 1AE7 | 33 | regist | 岩トリガ１０ |
| 1AEF | 33 | regist | 岩トリガ１１ |
| 1AF7 | 33 | regist | 岩ＣＰ変更１ |
| 1AFF | 33 | regist | 岩ＣＰ変更２ |
| 1B07 | 33 | regist | 岩ＣＰ変更３ |
| 1B0F | 33 | regist | 岩ＣＰ変更４ |
| 1B17 | 33 | regist | 岩ＣＰ変更５ |
| 1B1F | 33 | regist | 岩ＣＰ変更６ |
| 1B27 | 33 | regist | 岩ＣＰ変更７ |
| 1B2F | 33 | regist | 岩ＣＰ変更８ |
| 1B37 | 33 | regist | 岩ＣＰ変更９ |
| 1B3F | 33 | regist | 岩ＣＰ変更１０ |
| 1B47 | 33 | regist | 岩ＣＰ変更１１ |
| 1B4F | 33 | regist | ボス戦闘会話 |
| 1B57 | 33 | regist | ボス戦闘会話アイク |
| 1B5F | 33 | regist | ボス戦闘会話獣 |
| 1B67 | 33 | regist | ボス戦闘会話鳥 |
| 1B6F | 33 | regist | ボス戦闘会話タウロニオ |
| 1B77 | 33 | regist | ボス戦闘会話リュシオン |
| 1B7F | 33 | regist | ボス戦闘会話ハール |
| 1B87 | 33 | regist | ボス戦闘会話ジル |
| 1B8F | 33 | regist | ボス戦闘会話タニス |
| 1BD2 | 34 | InstantDisposRank | bmap26_first |
| 1C13 | 35 | SallySetByGroup | bmap26_mikata_c |
| 1CD8 | 36 | TalkEvent | MS_26_GMAP_01 |
| 1CF0 | 36 | TalkResume |  |
| 1D17 | 36 | TalkResume |  |
| 1DCE | 37 | ChapterMoviePlay | 26 |
| 1E19 | 38 | ForceGetCount | 5 |
| 1E3B | 38 | MapLoad | bmap26 |
| 1E49 | 38 | InstantDisposSetMode | bmap26_mikata_n, bmap26_mikata_h, bmap26_mikata_m |
| 1E4E | 38 | AllUnitEscape |  |
| 1E63 | 38 | Join | always_dbg_mik_12 |
| 1E6B | 38 | Join | always_dbg_mik_13 |
| 1E73 | 38 | Join | always_dbg_mik_14 |
| 1E7B | 38 | Join | always_dbg_mik_15 |
| 1E83 | 38 | Join | always_dbg_mik_16 |
| 1E8B | 38 | Join | always_dbg_mik_17 |
| 1E93 | 38 | Join | always_dbg_mik_19 |
| 1E9B | 38 | Join | always_dbg_mik_21 |
| 1EA3 | 38 | Join | always_dbg_mik_22 |
| 1EAB | 38 | Join | always_dbg_mik_24 |
| 1FBF | 38 | TalkEvent | MS_26_OP_01 |
| 1FF2 | 38 | TalkEvent | MS_26_OP_02 |
| 2026 | 38 | TalkEvent | MS_26_OP_03 |
| 2035 | 38 | TalkResume |  |
| 204A | 38 | TalkResume |  |
| 2059 | 38 | TalkResume |  |
| 212A | 38 | TalkEvent | MS_26_OP_04 |
| 213F | 38 | TalkEvent | MS_26_OP_05 |
| 2166 | 38 | TalkEvent | MS_26_OP_06 |
| 21C8 | 39 | TalkEvent | MS_26_OP_07 |
| 21EF | 39 | MapLoad | bmap26 |
| 2236 | 39 | SallySetByGroup | bmap26_mikata_c |
| 223E | 39 | InstantDispos | bmap26_mikata_c |
| 2261 | 39 | Dispos_ForEventTiamat | bmap26_event_tiamat_c, 1 |
| 2279 | 39 | Dispos_ForEventSenerio | bmap26_event_senerio_c, bmap26_event_senerio2_c, 1 |
| 228E | 39 | Dispos_ForEventTiamat | bmap26_event_lay_c, 1 |
| 23D5 | 39 | TalkEvent | MS_26_OP_08 |
| 2570 | 39 | TalkEvent | MS_26_OP_09 |
| 2613 | 39 | UnitEscapeByPID | PID_TIAMAT_EV |
| 261B | 39 | UnitEscapeByPID | PID_SENERIO_EV |
| 2623 | 39 | UnitEscapeByPID | PID_LAY_EV3 |
| 262B | 39 | UnitForcedSallyByPID | PID_IKE |
| 2633 | 39 | UnitDontMoveSallyByPID | PID_IKE |
| 26C6 | 41 | DisposSetMode | bmap26_z01_n, bmap26_z01_h, bmap26_z01_m |
| 2712 | 42 | DisposSetMode | bmap26_z02_n, bmap26_z02_h, bmap26_z02_m |
| 2B08 | 54 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2B10 | 54 | TalkEvent | MS_26_BT_IKE |
| 2B1D | 54 | SoundBossTalkEnd |  |
| 2B50 | 55 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2B58 | 55 | TalkEvent | MS_26_BT_R1 |
| 2B65 | 55 | SoundBossTalkEnd |  |
| 2B98 | 56 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2BA0 | 56 | TalkEvent | MS_26_BT_R1 |
| 2BAD | 56 | SoundBossTalkEnd |  |
| 2BE0 | 57 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2BE8 | 57 | TalkEvent | MS_26_BT_R1 |
| 2BF5 | 57 | SoundBossTalkEnd |  |
| 2C28 | 58 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2C30 | 58 | TalkEvent | MS_26_BT_R1 |
| 2C3D | 58 | SoundBossTalkEnd |  |
| 2C70 | 59 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2C78 | 59 | TalkEvent | MS_26_BT_R2 |
| 2C85 | 59 | SoundBossTalkEnd |  |
| 2CB8 | 60 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2CC0 | 60 | TalkEvent | MS_26_BT_R2 |
| 2CCD | 60 | SoundBossTalkEnd |  |
| 2D00 | 61 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D08 | 61 | TalkEvent | MS_26_BT_R3 |
| 2D15 | 61 | SoundBossTalkEnd |  |
| 2D48 | 62 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D50 | 62 | TalkEvent | MS_26_BT_RYU |
| 2D5D | 62 | SoundBossTalkEnd |  |
| 2D90 | 63 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2D98 | 63 | TalkEvent | MS_26_BT_R4 |
| 2DA5 | 63 | SoundBossTalkEnd |  |
| 2DD8 | 64 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2DE0 | 64 | TalkEvent | MS_26_BT_R5 |
| 2DED | 64 | SoundBossTalkEnd |  |
| 2E20 | 65 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2E28 | 65 | TalkEvent | MS_26_BT_R6 |
| 2E35 | 65 | SoundBossTalkEnd |  |
| 2ED8 | 66 | BMGetPhase |  |
| 2F60 | 66 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2F68 | 66 | TalkEvent | MS_26_BT |
| 2F75 | 66 | SoundBossTalkEnd |  |
| 2FA4 | 67 | TalkEvent | MS_26_DIE |
| 2FCA | 68 | ForceGetCount | 1 |
| 303E | 69 | AllUnitEscape |  |
| 305C | 69 | MapLoad | bmap26_2 |
| 3072 | 69 | InstantDispos | bmap26_2_event01_c |
| 307F | 69 | Dispos_ForEventSenerio | bmap26_2_event_senerio_c, bmap26_2_event_senerio2_c, 1 |
| 31FC | 69 | TalkEvent | MS_26_ED_01 |
| 329F | 69 | TalkEvent | MS_26_ED_01_2 |
| 32DC | 69 | TalkEvent | MS_26_ED_02 |
| 353C | 69 | UnitDead | ? |
| 3543 | 69 | UnitDead | ? |
| 354A | 69 | UnitDead | ? |
| 3551 | 69 | UnitDead | ? |
| 3558 | 69 | UnitDead | ? |
| 3565 | 69 | UnitEscapeByPID | PID_DAYNE_SOL_1 |
| 356D | 69 | UnitEscapeByPID | PID_DAYNE_SOL_2 |
| 3575 | 69 | UnitEscapeByPID | PID_DAYNE_SOL_3 |
| 357D | 69 | UnitEscapeByPID | PID_DAYNE_SOL_4 |
| 3585 | 69 | UnitEscapeByPID | PID_DAYNE_SOL_5 |
| 3689 | 69 | AllUnitEscape |  |
| 3696 | 69 | TalkEvent | MS_26_ED_02_2 |
| 36C7 | 69 | TalkEvent | MS_26_ED_02_3 |
| 36D4 | 69 | TalkEvent | MS_26_ED_04 |
| 36E3 | 69 | TalkResume |  |
| 36F5 | 69 | TalkResume |  |
| 3717 | 69 | TalkEvent | MS_26_ED_05 |
| 3728 | 69 | TalkResume |  |
| 3739 | 69 | TalkResume |  |
| 3767 | 69 | TalkResume |  |
| 37E6 | 71 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.26: Clash! — internal 27

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 18, 'h': 18, 'm': 18, 'n': 18}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap27/dispos_c.bin:bmap27_engn0_c`: F3: PID_MELTY
- `bmap27/dispos_c.bin:bmap27_event_beg_c`: F2: PID_C_ZAKO
- `bmap27/dispos_c.bin:bmap27_event_jofure_c`: F2: PID_GEOFFRAY_EV
- `bmap27/dispos_c.bin:bmap27_event_lukino_c`: F2: PID_LUCHINO_EV
- `bmap27/dispos_c.bin:bmap27_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap27/dispos_c.bin:bmap27_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap27/dispos_c.bin:bmap27_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap27/dispos_c.bin:bmap27_event_yurisizu_c`: F2: PID_ULYSSES_EV
- `bmap27/dispos_c.bin:bmap27_m_erincia1_c`: F0: PID_ERINCIA_QUEEN
- `bmap27/dispos_c.bin:bmap27_m_erincia2_c`: F0: PID_ERINCIA_QUEEN
- `bmap27/dispos_c.bin:bmap27_mikata_c`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LARGO, PID_MAKAROV, PID_MARCIA, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_TOPUCK, PID_ZIHARK
- `bmap27/dispos_h.bin:bmap27_engn0_h`: F3: PID_MELTY
- `bmap27/dispos_h.bin:bmap27_engn1_h`: F3: PID_MELTY
- `bmap27/dispos_h.bin:bmap27_first_h`: F1: PID_ACTORMANQUE_D, PID_BEUFORRES, PID_DAYNE_BSH, PID_DAYNE_DMS, PID_DAYNE_DMS_1, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_HAL_1, PID_DAYNE_PLD, PID_DAYNE_PLD_1, PID_DAYNE_SAG, PID_DAYNE_SKN_2, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SNP_1, PID_DAYNE_WAR
- `bmap27/dispos_h.bin:bmap27_mikata_h`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LARGO, PID_MAKAROV, PID_MARCIA, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_TOPUCK, PID_ZIHARK
- `bmap27/dispos_h.bin:bmap27_z01_h`: F1: PID_DAYNE_PLD_1
- `bmap27/dispos_h.bin:bmap27_z02_h`: F1: PID_DAYNE_PLD_1
- `bmap27/dispos_h.bin:bmap27_z03_h`: F1: PID_DAYNE_PLD, PID_DAYNE_PLD_1
- `bmap27/dispos_h.bin:bmap27_z04_h`: F1: PID_DAYNE_DMS, PID_DAYNE_DMS_1
- `bmap27/dispos_h.bin:bmap27_z05_h`: F1: PID_DAYNE_DMS, PID_DAYNE_DMS_1
- `bmap27/dispos_h.bin:bmap27_z06_h`: F1: PID_DAYNE_SAG, PID_DAYNE_SMS
- `bmap27/dispos_m.bin:bmap27_engn0_m`: F3: PID_MELTY
- `bmap27/dispos_m.bin:bmap27_engn1_m`: F3: PID_MELTY
- `bmap27/dispos_m.bin:bmap27_first_m`: F1: PID_ACTORMANQUE_D, PID_BEUFORRES, PID_DAYNE_BSH, PID_DAYNE_DMS, PID_DAYNE_DMS_1, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_PLD_1, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SNP_1, PID_DAYNE_WAR
- `bmap27/dispos_m.bin:bmap27_mikata_m`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LARGO, PID_MAKAROV, PID_MARCIA, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_TOPUCK, PID_ZIHARK
- `bmap27/dispos_m.bin:bmap27_z01_m`: F1: PID_DAYNE_PLD_1
- `bmap27/dispos_m.bin:bmap27_z02_m`: F1: PID_DAYNE_PLD_1
- `bmap27/dispos_m.bin:bmap27_z03_m`: F1: PID_DAYNE_PLD, PID_DAYNE_PLD_1
- `bmap27/dispos_m.bin:bmap27_z04_m`: F1: PID_DAYNE_DMS, PID_DAYNE_DMS_1
- `bmap27/dispos_m.bin:bmap27_z05_m`: F1: PID_DAYNE_DMS, PID_DAYNE_DMS_1
- `bmap27/dispos_m.bin:bmap27_z06_m`: F1: PID_DAYNE_SAG
- `bmap27/dispos_n.bin:bmap27_engn0_n`: F3: PID_MELTY
- `bmap27/dispos_n.bin:bmap27_engn1_n`: F3: PID_MELTY
- `bmap27/dispos_n.bin:bmap27_first_n`: F1: PID_ACTORMANQUE_D, PID_BEUFORRES, PID_DAYNE_BSH, PID_DAYNE_DMS, PID_DAYNE_DMS_1, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_PLD_1, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_SNP_1, PID_DAYNE_WAR
- `bmap27/dispos_n.bin:bmap27_mikata_n`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_IKE, PID_JANAFF, PID_KILROY, PID_LARGO, PID_MAKAROV, PID_MARCIA, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_TOPUCK, PID_ZIHARK
- `bmap27/dispos_n.bin:bmap27_z01_n`: F1: PID_DAYNE_PLD_1
- `bmap27/dispos_n.bin:bmap27_z02_n`: F1: PID_DAYNE_PLD_1
- `bmap27/dispos_n.bin:bmap27_z03_n`: F1: PID_DAYNE_PLD, PID_DAYNE_PLD_1
- `bmap27/dispos_n.bin:bmap27_z04_n`: F1: PID_DAYNE_DMS, PID_DAYNE_DMS_1
- `bmap27/dispos_n.bin:bmap27_z05_n`: F1: PID_DAYNE_DMS, PID_DAYNE_DMS_1
- `bmap27/dispos_n.bin:bmap27_z06_n`: F1: PID_DAYNE_SAG

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| C66 | 0 | regist | 情報１フラグ |
| C6D | 0 | regist | 情報２フラグ |
| C74 | 0 | regist | 情報３フラグ |
| C7B | 0 | regist | 情報４フラグ |
| C82 | 0 | regist | 情報５フラグ |
| CB7 | 1 | TalkEvent | MS_27_INFO_01 |
| CFE | 2 | TalkEvent | MS_27_INFO_02 |
| D8D | 5 | ForceGetCount | 5 |
| DA2 | 5 | regist | ボス戦闘会話 |
| DAA | 5 | regist | ボス戦闘会話エリンシア |
| DB2 | 5 | regist | ボス戦闘会話アイク |
| DBA | 5 | regist | ボス戦闘会話獣 |
| DC2 | 5 | regist | ボス戦闘会話鳥 |
| DCA | 5 | regist | ボス戦闘会話ジル−タウロ−ハア |
| DD2 | 5 | regist | ボス戦闘会話リュシオン |
| E12 | 6 | InstantDisposRank | bmap27_first |
| E22 | 6 | ForceGetCount | 1 |
| E2B | 6 | ForceGetFirst | 1 |
| EBB | 7 | SallySetByGroup | bmap27_mikata_c |
| ECD | 7 | SallyAddByGroup | bmap27_m_erincia1_c |
| ED8 | 7 | SallyAddByGroup | bmap27_m_erincia2_c |
| F95 | 8 | TalkEvent | MS_27_GMAP_01 |
| FA9 | 8 | TalkResume |  |
| FCD | 8 | TalkResume |  |
| FF1 | 8 | TalkResume |  |
| 10A2 | 9 | TalkEvent | MS_27_GMAP2_02 |
| 10C6 | 9 | TalkResume |  |
| 1162 | 9 | TalkEvent | MS_27_GMAP2_04A |
| 116D | 9 | TalkEvent | MS_27_GMAP2_04B |
| 11EA | 10 | ChapterMoviePlay | 27 |
| 1235 | 11 | ForceGetCount | 5 |
| 1257 | 11 | MapLoad | bmap27 |
| 1265 | 11 | InstantDisposSetMode | bmap27_mikata_n, bmap27_mikata_h, bmap27_mikata_m |
| 126A | 11 | AllUnitEscape |  |
| 1368 | 11 | TalkEvent | MS_27_OP_01 |
| 139C | 11 | TalkEvent | MS_27_GMAP2_01 |
| 13D4 | 11 | TalkEvent | MS_27_GMAP2_06 |
| 1443 | 12 | MapLoad | bmap27 |
| 146C | 12 | SallySetByGroup | bmap27_mikata_c |
| 1474 | 12 | InstantDispos | bmap27_mikata_c |
| 1497 | 12 | Dispos_ForEventTiamat | bmap27_event_tiamat_c, 1 |
| 14AF | 12 | Dispos_ForEventSenerio | bmap27_event_senerio_c, bmap27_event_senerio2_c, 1 |
| 14D4 | 12 | SallyAddByGroup | bmap27_m_erincia1_c |
| 14DC | 12 | InstantDispos | bmap27_m_erincia1_c |
| 14E7 | 12 | SallyAddByGroup | bmap27_m_erincia2_c |
| 14EF | 12 | InstantDispos | bmap27_m_erincia2_c |
| 1519 | 12 | TalkEvent | MS_27_OP_02 |
| 15BF | 12 | TalkEvent | MS_27_OP_03_a |
| 15CA | 12 | TalkEvent | MS_27_OP_03_b |
| 1614 | 12 | TalkEvent | MS_27_OP_03_a2 |
| 161F | 12 | TalkEvent | MS_27_OP_03_b2 |
| 16B2 | 12 | TalkEvent | MS_27_OP_04 |
| 1802 | 12 | TalkEvent | MS_27_OP_05 |
| 184B | 12 | UnitEscapeByPID | PID_TIAMAT_EV |
| 1853 | 12 | UnitEscapeByPID | PID_SENERIO_EV |
| 18A1 | 12 | UnitForcedSallyByPID | PID_IKE |
| 18A9 | 12 | UnitForcedSallyByPID | PID_ERINCIA_QUEEN |
| 18B1 | 12 | UnitDontMoveSallyByPID | PID_ERINCIA_QUEEN |
| 18B9 | 12 | UnitDontMoveSallyByPID | PID_IKE |
| 194A | 13 | TalkEvent | MS_27_OP_06 |
| 1970 | 13 | Dispos_ForEventTiamat | bmap27_event_tiamat_c, 1 |
| 1988 | 13 | Dispos_ForEventSenerio | bmap27_event_senerio_c, bmap27_event_senerio2_c, 1 |
| 19E1 | 13 | ForceGetCount | 0 |
| 19EA | 13 | ForceGetFirst | 0 |
| 1A6D | 13 | TalkEvent | MS_27_EV_01 |
| 1AB6 | 13 | UnitEscapeByPID | PID_TIAMAT_EV |
| 1ABE | 13 | UnitEscapeByPID | PID_SENERIO_EV |
| 1AC7 | 13 | ForceGetCount | 0 |
| 1AD0 | 13 | ForceGetFirst | 0 |
| 1B5D | 14 | DisposSetMode | bmap27_z04_n, bmap27_z04_h, bmap27_z04_m |
| 1B94 | 15 | DisposSetMode | bmap27_z01_n, bmap27_z01_h, bmap27_z01_m |
| 1BC9 | 16 | DisposSetMode | bmap27_z06_n, bmap27_z06_h, bmap27_z06_m |
| 1C0A | 17 | DisposSetMode | bmap27_z01_n, bmap27_z01_h, bmap27_z01_m |
| 1C48 | 18 | DisposSetMode | bmap27_z02_n, bmap27_z02_h, bmap27_z02_m |
| 1C84 | 19 | DisposSetMode | bmap27_z03_n, bmap27_z03_h, bmap27_z03_m |
| 1CB9 | 20 | DisposSetMode | bmap27_z05_n, bmap27_z05_h, bmap27_z05_m |
| 1CE8 | 21 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1CF0 | 21 | TalkEvent | MS_27_BT_01 |
| 1CFD | 21 | SoundBossTalkEnd |  |
| 1D30 | 22 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1D38 | 22 | TalkEvent | MS_27_BT_IKE |
| 1D45 | 22 | SoundBossTalkEnd |  |
| 1D78 | 23 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1D80 | 23 | TalkEvent | MS_27_BT_R1 |
| 1D8D | 23 | SoundBossTalkEnd |  |
| 1DC0 | 24 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1DC8 | 24 | TalkEvent | MS_27_BT_R1 |
| 1DD5 | 24 | SoundBossTalkEnd |  |
| 1E08 | 25 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1E10 | 25 | TalkEvent | MS_27_BT_R1 |
| 1E1D | 25 | SoundBossTalkEnd |  |
| 1E50 | 26 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1E58 | 26 | TalkEvent | MS_27_BT_R1 |
| 1E65 | 26 | SoundBossTalkEnd |  |
| 1E98 | 27 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1EA0 | 27 | TalkEvent | MS_27_BT_R2 |
| 1EAD | 27 | SoundBossTalkEnd |  |
| 1EE0 | 28 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1EE8 | 28 | TalkEvent | MS_27_BT_R2 |
| 1EF5 | 28 | SoundBossTalkEnd |  |
| 1F28 | 29 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1F30 | 29 | TalkEvent | MS_27_BT_R3 |
| 1F3D | 29 | SoundBossTalkEnd |  |
| 1F70 | 30 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1F78 | 30 | TalkEvent | MS_27_BT_R3 |
| 1F85 | 30 | SoundBossTalkEnd |  |
| 1FB8 | 31 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 1FC0 | 31 | TalkEvent | MS_27_BT_R3 |
| 1FCD | 31 | SoundBossTalkEnd |  |
| 2000 | 32 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2008 | 32 | TalkEvent | MS_27_BT_RI |
| 2015 | 32 | SoundBossTalkEnd |  |
| 20B8 | 33 | BMGetPhase |  |
| 2140 | 33 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 2148 | 33 | TalkEvent | MS_27_BT |
| 2155 | 33 | SoundBossTalkEnd |  |
| 2184 | 34 | TalkEvent | MS_27_DIE |
| 21EE | 35 | ForceGetFirst | 1 |
| 2203 | 35 | UnitEscape | ?, 0 |
| 227D | 35 | InstantDispos | bmap27_event_beg_c |
| 22CE | 35 | TalkEvent | MS_27_ED_01 |
| 22FF | 35 | AllUnitEscape |  |
| 2389 | 35 | TalkEvent | MS_27_ED_02 |
| 240A | 37 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.27: Moment of Fate — internal 28

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 11, 'h': 12, 'm': 12, 'n': 12}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap28/dispos_c.bin:bmap28_engn0_c`: F3: PID_MELTY
- `bmap28/dispos_c.bin:bmap28_event01_c`: F1: PID_BLACKKNIGHT, PID_HAHUXEDO
- `bmap28/dispos_c.bin:bmap28_event02_c`: F1: PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_ZAKO
- `bmap28/dispos_c.bin:bmap28_event_ending_c`: F0: PID_IKE
- `bmap28/dispos_c.bin:bmap28_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap28/dispos_c.bin:bmap28_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap28/dispos_c.bin:bmap28_event_tiamat_c`: F2: PID_TIAMAT_EV
- `bmap28/dispos_c.bin:bmap28_m01_c`: F0: PID_ERINCIA_QUEEN
- `bmap28/dispos_c.bin:bmap28_mikata_c`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TIAMAT, PID_ZIHARK
- `bmap28/dispos_h.bin:bmap28_engn0_h`: F3: PID_MELTY
- `bmap28/dispos_h.bin:bmap28_first2_h`: F1: PID_12_THIEF
- `bmap28/dispos_h.bin:bmap28_first_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_HAHUXEDO
- `bmap28/dispos_h.bin:bmap28_mikata_h`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap28/dispos_m.bin:bmap28_engn0_m`: F3: PID_MELTY
- `bmap28/dispos_m.bin:bmap28_first2_m`: F1: PID_12_THIEF
- `bmap28/dispos_m.bin:bmap28_first_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_HAHUXEDO
- `bmap28/dispos_m.bin:bmap28_mikata_m`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap28/dispos_n.bin:bmap28_engn0_n`: F3: PID_MELTY
- `bmap28/dispos_n.bin:bmap28_first2_n`: F1: PID_12_THIEF
- `bmap28/dispos_n.bin:bmap28_first_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_ARM, PID_DAYNE_BSH, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_WAR, PID_HAHUXEDO
- `bmap28/dispos_n.bin:bmap28_mikata_n`: F0: PID_BOLE, PID_ELAICE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| D5E | 0 | regist | 情報１フラグ |
| D65 | 0 | regist | 情報２フラグ |
| D6C | 0 | regist | 情報３フラグ |
| D73 | 0 | regist | 情報４フラグ |
| D7A | 0 | regist | 情報５フラグ |
| DC7 | 1 | TalkEvent | MS_28_INFO_04 |
| 1132 | 15 | UnitEscape | ?, 0 |
| 118A | 16 | UnitEscape | ?, 0 |
| 1237 | 18 | regist | 宝箱１ |
| 123F | 18 | regist | 宝箱２ |
| 1247 | 18 | regist | 宝箱３ |
| 124F | 18 | regist | 宝箱４ |
| 1257 | 18 | regist | 宝箱５ |
| 125F | 18 | regist | 宝箱６ |
| 1267 | 18 | regist | 宝箱７ |
| 126F | 18 | regist | F2118 |
| 1277 | 18 | regist | F1118 |
| 127F | 18 | regist | F0514 |
| 1287 | 18 | regist | F2714 |
| 128F | 18 | regist | F1611 |
| 1297 | 18 | regist | F09042310 |
| 1318 | 20 | BMGetTurn |  |
| 1343 | 21 | regist | クリア条件１ |
| 134B | 21 | regist | ボス戦闘会話 |
| 1353 | 21 | regist | ボス戦闘会話アイク |
| 135B | 21 | regist | ボス戦闘会話獣 |
| 1363 | 21 | regist | ボス戦闘会話鳥 |
| 136B | 21 | regist | ボス戦闘会話タウロニオ |
| 1373 | 21 | regist | ボス戦闘会話リュシオン |
| 13B6 | 22 | InstantDisposRank | bmap28_first |
| 13BE | 22 | InstantDisposRank | bmap28_first2 |
| 13CE | 22 | ForceGetCount | 1 |
| 13D7 | 22 | ForceGetFirst | 1 |
| 147B | 23 | SallySetByGroup | bmap28_mikata_c |
| 1540 | 24 | TalkEvent | MS_28_GMAP_01 |
| 1554 | 24 | TalkResume |  |
| 1583 | 24 | TalkResume |  |
| 162E | 25 | ChapterMoviePlay | 28 |
| 1679 | 26 | ForceGetCount | 5 |
| 169B | 26 | MapLoad | bmap28 |
| 16A9 | 26 | InstantDisposSetMode | bmap28_mikata_n, bmap28_mikata_h, bmap28_mikata_m |
| 16AE | 26 | AllUnitEscape |  |
| 16C3 | 26 | Join | always_dbg_mik_02 |
| 16CB | 26 | Join | always_dbg_mik_03 |
| 16D3 | 26 | Join | always_dbg_mik_05 |
| 16DB | 26 | Join | always_dbg_mik_08 |
| 16E3 | 26 | Join | always_dbg_mik_09 |
| 16EB | 26 | Join | always_dbg_mik_10 |
| 16F3 | 26 | Join | always_dbg_mik_11 |
| 16FB | 26 | Join | always_dbg_mik_12 |
| 1703 | 26 | Join | always_dbg_mik_13 |
| 170B | 26 | Join | always_dbg_mik_14 |
| 1713 | 26 | Join | always_dbg_mik_15 |
| 171B | 26 | Join | always_dbg_mik_16 |
| 1723 | 26 | Join | always_dbg_mik_17 |
| 172B | 26 | Join | always_dbg_mik_19 |
| 1733 | 26 | Join | always_dbg_mik_21 |
| 173B | 26 | Join | always_dbg_mik_22 |
| 1743 | 26 | Join | always_dbg_mik_24 |
| 174B | 26 | Join | always_dbg_mik_25 |
| 1753 | 26 | Join | always_dbg_mik_27 |
| 1798 | 26 | TalkEvent | MS_28_OP_01 |
| 1816 | 27 | TalkEvent | MS_28_OP_02A |
| 1821 | 27 | TalkEvent | MS_28_OP_02B |
| 185E | 27 | TalkEvent | MS_28_OP_02_A |
| 187E | 27 | TalkEvent | MS_28_OP_02_B |
| 189E | 27 | TalkEvent | MS_28_OP_02_C |
| 18A9 | 27 | TalkEvent | MS_28_OP_02_D |
| 18C4 | 27 | TalkResume |  |
| 18F5 | 27 | TalkEvent | MS_28_OP_03 |
| 193A | 27 | TalkEvent | MS_28_OP_04_A |
| 1953 | 27 | TalkResume |  |
| 198A | 27 | MapLoad | bmap28 |
| 19B5 | 27 | InstantDisposRank | bmap28_first |
| 19BA | 27 | AllUnitEscape |  |
| 19C9 | 27 | InstantDispos | bmap28_event01_c |
| 19D1 | 27 | InstantDispos | bmap28_event02_c |
| 1B44 | 27 | TalkEvent | MS_28_OP_05 |
| 1B8B | 27 | UnitEscapeByPID | PID_BLACKKNIGHT |
| 1BDA | 27 | AllUnitEscape |  |
| 1BE5 | 27 | SallySetByGroup | bmap28_mikata_c |
| 1BED | 27 | InstantDispos | bmap28_mikata_c |
| 1C00 | 27 | ForceGetCount | 0 |
| 1C0E | 27 | ForceGetFirst | 0 |
| 1FCF | 27 | ForceGetCount | 0 |
| 1FD8 | 27 | ForceGetFirst | 0 |
| 2036 | 27 | TalkEvent | MS_28_OP_06 |
| 2051 | 27 | ForceGetCount | 0 |
| 205A | 27 | ForceGetFirst | 0 |
| 20D6 | 27 | UnitForcedSallyByPID | PID_IKE |
| 20DE | 27 | UnitDontMoveSallyByPID | PID_IKE |
| 2188 | 29 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2190 | 29 | TalkEvent | MS_28_BT_IKE |
| 219D | 29 | SoundBossTalkEnd |  |
| 21D0 | 30 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 21D8 | 30 | TalkEvent | MS_28_BT_R1 |
| 21E5 | 30 | SoundBossTalkEnd |  |
| 2218 | 31 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2220 | 31 | TalkEvent | MS_28_BT_R1 |
| 222D | 31 | SoundBossTalkEnd |  |
| 2260 | 32 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2268 | 32 | TalkEvent | MS_28_BT_R1 |
| 2275 | 32 | SoundBossTalkEnd |  |
| 22A8 | 33 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 22B0 | 33 | TalkEvent | MS_28_BT_R1 |
| 22BD | 33 | SoundBossTalkEnd |  |
| 22F0 | 34 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 22F8 | 34 | TalkEvent | MS_28_BT_R2 |
| 2305 | 34 | SoundBossTalkEnd |  |
| 2338 | 35 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2340 | 35 | TalkEvent | MS_28_BT_R2 |
| 234D | 35 | SoundBossTalkEnd |  |
| 2380 | 36 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2388 | 36 | TalkEvent | MS_28_BT_R3 |
| 2395 | 36 | SoundBossTalkEnd |  |
| 23C8 | 37 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 23D0 | 37 | TalkEvent | MS_28_BT_RI |
| 23DD | 37 | SoundBossTalkEnd |  |
| 2462 | 38 | BMGetPhase |  |
| 24D2 | 38 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 24DA | 38 | TalkEvent | MS_28_BT |
| 24DF | 38 | SoundBossTalkEnd |  |
| 2518 | 39 | TalkEvent | MS_28_DIE |
| 256F | 40 | ForceGetFirst | 1 |
| 257B | 40 | UnitEscape | ?, 0 |
| 2587 | 40 | ForceGetFirst | 3 |
| 2593 | 40 | UnitEscape | ?, 0 |
| 25B0 | 40 | Dispos_ForEventTiamat | bmap28_event_tiamat_c, 1 |
| 25C8 | 40 | Dispos_ForEventSenerio | bmap28_event_senerio_c, bmap28_event_senerio2_c, 1 |
| 264D | 40 | ForceGetCount | 0 |
| 265B | 40 | ForceGetFirst | 0 |
| 287F | 40 | TalkEvent | MS_28_ED_01 |
| 28F8 | 40 | TalkEvent | MS_28_ED_02 |
| 292E | 40 | AllUnitEscape |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.27-2: Moment of Fate — internal 29

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 1, 'h': 2, 'm': 2, 'n': 2}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap29/dispos_c.bin:bmap29_event_ena2_c`: F2: PID_ENA_EV
- `bmap29/dispos_c.bin:bmap29_event_ena_c`: F2: PID_ENA
- `bmap29/dispos_c.bin:bmap29_event_narsil_c`: F2: PID_NASIR_EV
- `bmap29/dispos_c.bin:bmap29_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap29/dispos_c.bin:bmap29_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap29/dispos_c.bin:bmap29_event_zako_c`: F1: PID_ZAKO_EV1, PID_ZAKO_EV2
- `bmap29/dispos_c.bin:bmap29_m01_c`: F0: PID_MIST
- `bmap29/dispos_c.bin:bmap29_mikata_c`: F0: PID_IKE
- `bmap29/dispos_h.bin:bmap29_first_h`: F1: PID_BLACKKNIGHT
- `bmap29/dispos_h.bin:bmap29_mikata_h`: F0: PID_IKE, PID_MIST
- `bmap29/dispos_h.bin:bmap29_zoen1_h`: F1: PID_DAYNE_HAL
- `bmap29/dispos_h.bin:bmap29_zoen2_h`: F1: PID_DAYNE_BSH
- `bmap29/dispos_m.bin:bmap29_first_m`: F1: PID_BLACKKNIGHT
- `bmap29/dispos_m.bin:bmap29_mikata_m`: F0: PID_IKE, PID_MIST
- `bmap29/dispos_m.bin:bmap29_zoen1_m`: F1: PID_DAYNE_HAL
- `bmap29/dispos_m.bin:bmap29_zoen2_m`: F1: PID_DAYNE_BSH
- `bmap29/dispos_n.bin:bmap29_first_n`: F1: PID_BLACKKNIGHT
- `bmap29/dispos_n.bin:bmap29_mikata_n`: F0: PID_IKE, PID_MIST
- `bmap29/dispos_n.bin:bmap29_zoen1_n`: F1: PID_DAYNE_HAL
- `bmap29/dispos_n.bin:bmap29_zoen2_n`: F1: PID_DAYNE_BSH

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| CF1 | 0 | TalkEvent | MESC_MIST_29 |
| D13 | 0 | UnitEscape | ?, 0 |
| DD2 | 5 | regist | 離脱した |
| DDA | 5 | regist | ５ターン経過 |
| DE2 | 5 | regist | ボス戦闘会話アイク |
| DEA | 5 | regist | ボス戦闘会話ミスト |
| E1F | 6 | MapLoad | bmap29 |
| E57 | 6 | SallySetByGroup | bmap29_mikata_c |
| E5F | 6 | InstantDisposFirst | bmap29_mikata_c |
| E67 | 6 | InstantDisposFirst | bmap29_m01_c |
| E6F | 6 | InstantDispos | bmap29_event_ena2_c |
| E74 | 6 | AllUnitEscape |  |
| E83 | 6 | InstantDisposRank | bmap29_first |
| E8B | 6 | InstantDispos | bmap29_event_ena_c |
| F2A | 6 | TalkEvent | MS_29_OP_01 |
| F4C | 6 | InstantDisposFirst | bmap29_mikata_c |
| FFD | 6 | TalkEvent | MS_29_OP_02 |
| 1002 | 6 | TalkResume |  |
| 109B | 6 | TalkEvent | MS_29_OP_03 |
| 1181 | 6 | TalkEvent | MS_29_OP_04_A |
| 11A2 | 6 | InstantDisposFirst | bmap29_m01_c |
| 1233 | 6 | TalkEvent | MS_29_OP_05_A |
| 125D | 6 | TalkEvent | MS_29_OP_04_B |
| 129C | 6 | InstantDispos | bmap29_event_ena2_c |
| 12B2 | 6 | UnitEscapeByPID | PID_ENA |
| 1335 | 7 | ForceGetCount | 5 |
| 1357 | 7 | MapLoad | bmap29 |
| 1365 | 7 | InstantDisposSetMode | bmap29_mikata_n, bmap29_mikata_h, bmap29_mikata_m |
| 136A | 7 | AllUnitEscape |  |
| 1432 | 8 | DisposAsynchronous | bmap29_zoen2_n |
| 1444 | 8 | DisposAsynchronous | bmap29_zoen2_h |
| 144F | 8 | DisposAsynchronous | bmap29_zoen2_m |
| 146C | 8 | DisposSetMode | bmap29_zoen1_n, bmap29_zoen1_h, bmap29_zoen1_m |
| 14AD | 8 | TalkEvent | MS_29_EV_04_A |
| 14D8 | 8 | TalkEvent | MS_29_EV_04_B |
| 14FB | 8 | ForceGetCount | 1 |
| 150E | 8 | ForceGetFirst | 1 |
| 1593 | 9 | BMGetPhase |  |
| 15EA | 9 | TalkEvent | MS_29_DIE_IKE |
| 1615 | 9 | TalkEvent | MDIE_IKE_0 |
| 1654 | 10 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 165C | 10 | TalkEvent | MS_29_BT_IKE |
| 1669 | 10 | SoundBossTalkEnd |  |
| 169C | 11 | SoundBossTalkStart | BGM_BTL_DARK_KNIGHT1 |
| 16A4 | 11 | TalkEvent | MS_29_BT_MIST |
| 16B1 | 11 | SoundBossTalkEnd |  |
| 16E7 | 12 | TalkEvent | MS_29_ED_01_01B |
| 182F | 14 | TalkEvent | MS_29_ED_01_01A |
| 1844 | 14 | InstantDispos | bmap29_event_narsil_c |
| 1960 | 14 | TalkEvent | MS_29_ED_01_02A |
| 1A0F | 14 | TalkEvent | MS_29_ED_01_03A |
| 1AA6 | 14 | TalkEvent | MS_29_ED_01_03_2A |
| 1AE2 | 14 | TalkEvent | MS_29_ED_01_03_3A |
| 1CFF | 14 | TalkEvent | MS_29_ED_01_04A |
| 1DCC | 14 | TalkEvent | MS_29_ED_01_05A |
| 1EDE | 15 | ForceGetCount | 1 |
| 1EF0 | 15 | InstantDispos | bmap29_event_zako_c |
| 1F44 | 15 | TalkEvent | MS_29_ED_01_02B |
| 1F74 | 15 | TalkEvent | MS_29_ED_01_02B |
| 204D | 15 | UnitEscapeByPID | PID_ZAKO_EV1 |
| 2055 | 15 | UnitEscapeByPID | PID_ZAKO_EV2 |
| 205D | 15 | UnitEscapeByPID | PID_ZAKO_EV3 |
| 20AC | 15 | TalkEvent | MS_29_ED_01_03B |
| 2129 | 15 | InstantDispos | bmap29_event_narsil_c |
| 21AA | 15 | TalkEvent | MS_29_ED_01_04B |
| 2235 | 15 | TalkEvent | MS_29_ED_01_05B |
| 227E | 15 | TalkEvent | MS_29_ED_01_06B |
| 2323 | 15 | TalkEvent | MS_29_ED_01_07B |
| 245B | 15 | UnitEscapeByPID | PID_IKE |
| 2463 | 15 | UnitEscapeByPID | PID_MIST |
| 2980 | 17 | AllUnitEscape |  |
| 29BC | 17 | TalkEvent | MS_29_ED_02 |
| 29CB | 17 | TalkResume |  |
| 29EA | 17 | TalkEvent | MS_29_ED_03 |
| 2A33 | 17 | TalkEvent | MS_29_ED_04_01A |
| 2A54 | 17 | TalkEvent | MS_29_ED_04_02A |
| 2A70 | 17 | TalkResume |  |
| 2A7F | 17 | TalkResume |  |
| 2A8E | 17 | TalkResume |  |
| 2AA5 | 17 | TalkEvent | MS_29_ED_04_01B |
| 2AC1 | 17 | TalkResume |  |
| 2B4A | 19 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Ch.28: Twisted Tower — internal 30

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 11, 'h': 11, 'm': 11, 'n': 11}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap30/dispos_c.bin:bmap30_engn0_c`: F3: PID_MELTY
- `bmap30/dispos_c.bin:bmap30_event1_c`: F2: PID_DAYNE_SOL_1, PID_LEARNE, PID_NAESALA
- `bmap30/dispos_c.bin:bmap30_event_learne_c`: F2: PID_LEARNE
- `bmap30/dispos_c.bin:bmap30_event_nealuchi_c`: F2: PID_NEALUCHI
- `bmap30/dispos_c.bin:bmap30_event_nesala_c`: F2: PID_NAESALA
- `bmap30/dispos_c.bin:bmap30_event_niaruchi_c`: F2: PID_K_ZAKO_EV1, PID_K_ZAKO_EV2, PID_NEALUCHI
- `bmap30/dispos_c.bin:bmap30_event_rai_c`: F2: PID_LAY_EV3
- `bmap30/dispos_c.bin:bmap30_event_ryusion_c`: F2: PID_RIEUSION_EV
- `bmap30/dispos_c.bin:bmap30_m01_c`: F0: PID_ENA
- `bmap30/dispos_c.bin:bmap30_m02_c`: F0: PID_NASIR
- `bmap30/dispos_c.bin:bmap30_m03_c`: F3: PID_TIBARN
- `bmap30/dispos_c.bin:bmap30_mikata_c`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap30/dispos_h.bin:bmap30_engn0_h`: F3: PID_MELTY
- `bmap30/dispos_h.bin:bmap30_first_boss_h`: F1: PID_DAYNE_BSH, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_KOYUJO
- `bmap30/dispos_h.bin:bmap30_first_h`: F1: PID_ACTORMANQUE_D, PID_DAYNE_SAG, PID_DAYNE_WAR
- `bmap30/dispos_h.bin:bmap30_mikata_h`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap30/dispos_h.bin:bmap30_z01_h`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_h.bin:bmap30_z02_h`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_h.bin:bmap30_z03_h`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_h.bin:bmap30_z04_h`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_m.bin:bmap30_engn0_m`: F3: PID_MELTY
- `bmap30/dispos_m.bin:bmap30_first_boss_m`: F1: PID_DAYNE_BSH, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_SMS, PID_KOYUJO
- `bmap30/dispos_m.bin:bmap30_first_m`: F1: PID_ACTORMANQUE_D, PID_DAYNE_WAR
- `bmap30/dispos_m.bin:bmap30_mikata_m`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap30/dispos_m.bin:bmap30_z01_m`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_m.bin:bmap30_z02_m`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_m.bin:bmap30_z03_m`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_n.bin:bmap30_engn0_n`: F3: PID_MELTY
- `bmap30/dispos_n.bin:bmap30_first_boss_n`: F1: PID_DAYNE_BSH, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_SMS, PID_KOYUJO
- `bmap30/dispos_n.bin:bmap30_first_n`: F1: PID_ACTORMANQUE_D, PID_DAYNE_WAR
- `bmap30/dispos_n.bin:bmap30_mikata_n`: F0: PID_BOLE, PID_IKE, PID_KILROY, PID_MIST, PID_NEPENEE, PID_RIEUSION, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap30/dispos_n.bin:bmap30_z01_n`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_n.bin:bmap30_z02_n`: F1: PID_ACTORMANQUE_D
- `bmap30/dispos_n.bin:bmap30_z03_n`: F1: PID_ACTORMANQUE_D

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| F5E | 0 | regist | 情報１フラグ |
| F65 | 0 | regist | 情報２フラグ |
| F6C | 0 | regist | 情報３フラグ |
| F73 | 0 | regist | 情報４フラグ |
| F7A | 0 | regist | 情報５フラグ |
| FE3 | 1 | TalkEvent | MS_30_INFO_05 |
| FF0 | 1 | TalkEvent | MS_30_INFO_05_2 |
| 11EF | 11 | regist | 増援トリガ１ |
| 125B | 13 | regist | 増援イベント１ |
| 1263 | 13 | regist | ネサラリアーネ死亡イベント |
| 126B | 13 | regist | ネサラリアーネ死亡トリガ |
| 1273 | 13 | regist | ティバーン死亡 |
| 127B | 13 | regist | ネサラ死亡 |
| 1283 | 13 | regist | リアーネ死亡 |
| 128B | 13 | regist | ネサラ会話 |
| 1293 | 13 | regist | ボス戦闘会話 |
| 129B | 13 | regist | ボス戦闘会話アイク |
| 12A3 | 13 | regist | ボス戦闘会話獣 |
| 12AB | 13 | regist | ボス戦闘会話鳥 |
| 12B3 | 13 | regist | ボス戦闘会話タウロニオ |
| 12BB | 13 | regist | ボス戦闘会話リュシオン |
| 12C3 | 13 | regist | ボス戦闘会話イナ |
| 1306 | 14 | InstantDisposRank | bmap30_first |
| 130E | 14 | InstantDisposRank | bmap30_first_boss |
| 1324 | 14 | InstantDispos | bmap30_m03_c |
| 138F | 15 | SallySetByGroup | bmap30_mikata_c |
| 13A1 | 15 | SallyAddByGroup | bmap30_m02_c |
| 13AC | 15 | SallyAddByGroup | bmap30_m01_c |
| 1495 | 16 | TalkEvent | MS_30_GMAP_A_01 |
| 14A0 | 16 | TalkEvent | MS_30_GMAP_B_01 |
| 14CE | 16 | TalkResume |  |
| 1503 | 16 | TalkResume |  |
| 1534 | 16 | TalkResume |  |
| 159E | 17 | ChapterMoviePlay | 30 |
| 15E9 | 18 | ForceGetCount | 5 |
| 160B | 18 | MapLoad | bmap30 |
| 1619 | 18 | InstantDisposSetMode | bmap30_mikata_n, bmap30_mikata_h, bmap30_mikata_m |
| 161E | 18 | AllUnitEscape |  |
| 1648 | 18 | Join | always_dbg_mik_10 |
| 1650 | 18 | Join | always_dbg_mik_11 |
| 1658 | 18 | Join | always_dbg_mik_12 |
| 1660 | 18 | Join | always_dbg_mik_13 |
| 1668 | 18 | Join | always_dbg_mik_14 |
| 1670 | 18 | Join | always_dbg_mik_15 |
| 1678 | 18 | Join | always_dbg_mik_16 |
| 1680 | 18 | Join | always_dbg_mik_17 |
| 1688 | 18 | Join | always_dbg_mik_19 |
| 1690 | 18 | Join | always_dbg_mik_21 |
| 1698 | 18 | Join | always_dbg_mik_22 |
| 16A0 | 18 | Join | always_dbg_mik_24 |
| 16A8 | 18 | Join | always_dbg_mik_25 |
| 16B0 | 18 | Join | always_dbg_mik_26 |
| 16B8 | 18 | Join | always_dbg_mik_27 |
| 1701 | 18 | TalkEvent | MS_30_OP_01A |
| 170C | 18 | TalkEvent | MS_30_OP_01B |
| 1721 | 18 | TalkEvent | MS_30_OP_01AB |
| 1780 | 19 | UnitTransferToForceByPID | PID_ERINCIA_QUEEN, 7 |
| 1798 | 19 | MapLoad | bmap30 |
| 18CE | 19 | AllUnitEscape |  |
| 18EB | 19 | TalkEvent | MS_30_OP_X |
| 1908 | 19 | TalkEvent | MS_30_OP_X2 |
| 191D | 19 | TalkResume |  |
| 195C | 19 | TalkEvent | MS_30_OP_02A |
| 1967 | 19 | TalkEvent | MS_30_OP_02B |
| 1980 | 19 | TalkResume |  |
| 1A1C | 19 | SallySetByGroup | bmap30_mikata_c |
| 1A24 | 19 | InstantDispos | bmap30_mikata_c |
| 1A36 | 19 | SallyAddByGroup | bmap30_m02_c |
| 1A3E | 19 | InstantDispos | bmap30_m02_c |
| 1A49 | 19 | SallyAddByGroup | bmap30_m01_c |
| 1A51 | 19 | InstantDispos | bmap30_m01_c |
| 1A59 | 19 | InstantDispos | bmap30_m03_c |
| 1A6C | 19 | InstantDispos | bmap30_event_ryusion_c |
| 1A7F | 19 | InstantDispos | bmap30_event_rai_c |
| 1A87 | 19 | InstantDisposRank | bmap30_first |
| 1A8F | 19 | InstantDisposRank | bmap30_first_boss |
| 1A94 | 19 | AllUnitEscape |  |
| 1ACB | 19 | TalkEvent | MS_30_OP_XX |
| 1B4F | 19 | DisposAsynchronous | bmap30_first_n |
| 1B68 | 19 | DisposAsynchronous | bmap30_first_h |
| 1B7A | 19 | DisposAsynchronous | bmap30_first_m |
| 1BD3 | 19 | DisposAsynchronous | bmap30_first_boss_n |
| 1BED | 19 | DisposAsynchronous | bmap30_first_boss_h |
| 1C08 | 19 | DisposAsynchronous | bmap30_first_boss_m |
| 1C26 | 19 | DisposAsynchronous | bmap30_mikata_c |
| 1C35 | 19 | DisposAsynchronous | bmap30_m03_c |
| 1C4E | 19 | DisposAsynchronous | bmap30_m02_c |
| 1C59 | 19 | DisposAsynchronous | bmap30_m01_c |
| 1C71 | 19 | DisposAsynchronous | bmap30_event_ryusion_c |
| 1C84 | 19 | DisposAsynchronous | bmap30_event_rai_c |
| 1D38 | 19 | TalkEvent | MS_30_OP_03X |
| 1D58 | 19 | TalkEvent | MS_30_OP_03X_1 |
| 1D78 | 19 | TalkEvent | MS_30_OP_03X_2 |
| 1D83 | 19 | TalkEvent | MS_30_OP_03X_3 |
| 1DDB | 19 | UnitEscapeByPID | PID_RIEUSION_EV |
| 1DE3 | 19 | UnitEscapeByPID | PID_LAY_EV3 |
| 1E35 | 19 | UnitForcedSallyByPID | PID_IKE |
| 1E3D | 19 | UnitDontMoveSallyByPID | PID_IKE |
| 1F27 | 21 | Dispos | bmap30_event1_c |
| 20A6 | 21 | TalkEvent | MS_30_EV_05_01 |
| 2158 | 21 | UnitEscapeByPID | PID_DAYNE_SOL_1 |
| 2160 | 21 | TalkEvent | MS_30_EV_05_02 |
| 2288 | 22 | TalkEvent | MS_30_EV_06_01X |
| 229D | 22 | Dispos | bmap30_event_niaruchi_c |
| 238B | 22 | TalkEvent | MS_30_EV_06_02X |
| 249B | 22 | UnitEscapeByPID | PID_NAESALA |
| 24A3 | 22 | UnitEscapeByPID | PID_LEARNE |
| 24AB | 22 | UnitEscapeByPID | PID_NEALUCHI |
| 24B3 | 22 | UnitEscapeByPID | PID_K_ZAKO_EV1 |
| 24BB | 22 | UnitEscapeByPID | PID_K_ZAKO_EV2 |
| 2530 | 23 | DisposSetMode | bmap30_z01_n, bmap30_z01_h, bmap30_z01_m |
| 2565 | 24 | DisposSetMode | bmap30_z02_n, bmap30_z02_h, bmap30_z02_m |
| 259C | 25 | DisposSetMode | bmap30_z03_n, bmap30_z04_h, bmap30_z03_m |
| 25DB | 26 | DisposSetMode | bmap30_z02_h, bmap30_z02_h, bmap30_z02_m |
| 263B | 27 | DisposSetMode | bmap30_z03_n, bmap30_z03_h, bmap30_z03_m |
| 266A | 28 | LocalDieTalkWithBgmChange | , MS_30_DIE_TIBARN |
| 26A0 | 29 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 26A8 | 29 | TalkEvent | MS_30_BT_IKE |
| 26B5 | 29 | SoundBossTalkEnd |  |
| 26E8 | 30 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 26F0 | 30 | TalkEvent | MS_30_BT_R1 |
| 26FD | 30 | SoundBossTalkEnd |  |
| 2730 | 31 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2738 | 31 | TalkEvent | MS_30_BT_R1 |
| 2745 | 31 | SoundBossTalkEnd |  |
| 2778 | 32 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2780 | 32 | TalkEvent | MS_30_BT_R1 |
| 278D | 32 | SoundBossTalkEnd |  |
| 27C0 | 33 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 27C8 | 33 | TalkEvent | MS_30_BT_R1 |
| 27D5 | 33 | SoundBossTalkEnd |  |
| 2808 | 34 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2810 | 34 | TalkEvent | MS_30_BT_R2 |
| 281D | 34 | SoundBossTalkEnd |  |
| 2850 | 35 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2858 | 35 | TalkEvent | MS_30_BT_R2 |
| 2865 | 35 | SoundBossTalkEnd |  |
| 2898 | 36 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 28A0 | 36 | TalkEvent | MS_30_BT_R3 |
| 28AD | 36 | SoundBossTalkEnd |  |
| 28E0 | 37 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 28E8 | 37 | TalkEvent | MS_30_BT_RI |
| 28F5 | 37 | SoundBossTalkEnd |  |
| 2928 | 38 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2930 | 38 | TalkEvent | MS_30_BT_R4 |
| 293D | 38 | SoundBossTalkEnd |  |
| 29CC | 39 | BMGetPhase |  |
| 2A44 | 39 | SoundBossTalkStart | BGM_BTL_BOSS1 |
| 2A4C | 39 | TalkEvent | MS_30_BT |
| 2A59 | 39 | SoundBossTalkEnd |  |
| 2A88 | 40 | TalkEvent | MS_30_DIE |
| 2ACD | 41 | UnitTransferToForceByPID | PID_ERINCIA_QUEEN, 0 |
| 2ADD | 41 | UnitForcedSally | ? |
| 2AE2 | 41 | AllUnitEscape |  |
| 2B8A | 41 | AllUnitEscape |  |
| 2C0C | 41 | TalkEvent | MS_30_ED_00_A |
| 2C25 | 41 | TalkResume |  |
| 2C41 | 41 | TalkResume |  |
| 2C86 | 41 | TalkEvent | MS_30_ED_00X_A |
| 2C91 | 41 | TalkEvent | MS_30_ED_00_B |
| 2CAA | 41 | TalkResume |  |
| 2CCE | 41 | TalkResume |  |
| 2D13 | 41 | TalkEvent | MS_30_ED_00X_B |
| 2D4C | 41 | TalkResume |  |
| 2D65 | 41 | TalkResume |  |
| 2DC4 | 41 | TalkEvent | MS_30_ED_00XX |
| 2E22 | 41 | TalkEvent | MS_30_ED_03 |
| 2E2D | 41 | TalkEvent | MS_30_ED_03_B |
| 2E42 | 41 | TalkEvent | MS_30_ED_04 |
| 2EC2 | 43 | BMGetTurn |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

## Endgame: Repatriation — internal 31

Historical evidence: none documented.

Slot-group counts by file suffix: `{'c': 13, 'h': 14, 'm': 14, 'n': 14}`. These are candidates, not final effective caps.

Disposition candidates by variant/group (reinforcement and event groups are separate; not an initial roster):

- `bmap31/dispos_c.bin:bmap31_engn0_c`: F3: PID_MELTY
- `bmap31/dispos_c.bin:bmap31_event_ed_01_c`: F2: PID_ENA_EV2, PID_ERINCIA_QUEEN_EV, PID_IKE_EV, PID_MIST_EV, PID_RIEUSION_EV, PID_TIAMAT_EV, PID_TIBARN_EV2
- `bmap31/dispos_c.bin:bmap31_event_ed_narsil_c`: F2: PID_NASIR_EV
- `bmap31/dispos_c.bin:bmap31_event_erincia_c`: F2: PID_ERINCIA_QUEEN_EV
- `bmap31/dispos_c.bin:bmap31_event_ike_c`: F2: PID_IKE_EV, PID_TIAMAT_EV
- `bmap31/dispos_c.bin:bmap31_event_senerio2_c`: F2: PID_SENERIO_EV
- `bmap31/dispos_c.bin:bmap31_event_senerio_c`: F2: PID_SENERIO_EV
- `bmap31/dispos_c.bin:bmap31_event_senerio_ed2_c`: F2: PID_SENERIO_EV
- `bmap31/dispos_c.bin:bmap31_event_senerio_ed_c`: F2: PID_SENERIO_EV
- `bmap31/dispos_c.bin:bmap31_m_ena_c`: F0: PID_ENA
- `bmap31/dispos_c.bin:bmap31_m_giffca_c`: F0: PID_GIFFCA
- `bmap31/dispos_c.bin:bmap31_m_naesala_c`: F0: PID_NAESALA
- `bmap31/dispos_c.bin:bmap31_m_narsil_c`: F0: PID_NASIR
- `bmap31/dispos_c.bin:bmap31_m_tibarn_c`: F0: PID_TIBARN
- `bmap31/dispos_c.bin:bmap31_mikata_c`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_ERINCIA_QUEEN, PID_IKE, PID_JANAFF, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap31/dispos_h.bin:bmap31_boss2_h`: F1: PID_ASHNARD2
- `bmap31/dispos_h.bin:bmap31_boss_h`: F1: PID_ASHNARD
- `bmap31/dispos_h.bin:bmap31_engn0_h`: F3: PID_MELTY
- `bmap31/dispos_h.bin:bmap31_first_h`: F1: PID_ACTORMANQUE_D, PID_BURAISU, PID_DAYNE_BSH, PID_DAYNE_DMS, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_SNP, PID_DAYNE_WAR
- `bmap31/dispos_h.bin:bmap31_mikata_h`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap31/dispos_h.bin:bmap31_z01_h`: F1: PID_DAYNE_BSH, PID_DAYNE_PLD
- `bmap31/dispos_m.bin:bmap31_boss2_m`: F1: PID_ASHNARD2
- `bmap31/dispos_m.bin:bmap31_boss_m`: F1: PID_ASHNARD
- `bmap31/dispos_m.bin:bmap31_engn0_m`: F3: PID_MELTY
- `bmap31/dispos_m.bin:bmap31_first_m`: F1: PID_ACTORMANQUE_D, PID_BURAISU, PID_DAYNE_BSH, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_WAR
- `bmap31/dispos_m.bin:bmap31_mikata_m`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap31/dispos_n.bin:bmap31_boss2_n`: F1: PID_ASHNARD2
- `bmap31/dispos_n.bin:bmap31_boss_n`: F1: PID_ASHNARD
- `bmap31/dispos_n.bin:bmap31_engn0_n`: F3: PID_MELTY
- `bmap31/dispos_n.bin:bmap31_first_n`: F1: PID_ACTORMANQUE_D, PID_BURAISU, PID_DAYNE_BSH, PID_DAYNE_GNL, PID_DAYNE_HAL, PID_DAYNE_PLD, PID_DAYNE_SAG, PID_DAYNE_SMS, PID_DAYNE_WAR
- `bmap31/dispos_n.bin:bmap31_mikata_n`: F0: PID_BOLE, PID_CALILL, PID_ELAICE, PID_IKE, PID_JANAFF, PID_KILROY, PID_MIST, PID_NEPENEE, PID_SENERIO, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TIAMAT, PID_ZIHARK
- `bmap31_2/dispos_c.bin:bmap31_2_event01_c`: F0: PID_BOLE, PID_GEOFFRAY, PID_HAAR, PID_IKE, PID_JANAFF, PID_LOFA, PID_LUCHINO, PID_MIST, PID_OSCAR, PID_SENERIO, PID_TIAMAT, PID_ULYSSES, PID_VULCI; F2: PID_ENA_EV2, PID_ERINCIA_QUEEN_EV, PID_LEARNE, PID_NAESALA_EV, PID_NASIR_EV, PID_RAJAION, PID_RIEUSION_EV, PID_TIBARN_EV
- `bmap31_3/dispos_c.bin:bmap31_3_begnion_c`: F0: PID_DALAHOWE, PID_MAKAROV, PID_MARCIA, PID_MWARIM, PID_SOANVALCKE, PID_STELLA, PID_TANIS, PID_TOPUCK; F2: PID_ZELGIUS
- `bmap31_3/dispos_c.bin:bmap31_3_birds_c`: F0: PID_JANAFF, PID_VULCI; F2: PID_NAESALA_EV, PID_NEALUCHI, PID_TIBARN_EV
- `bmap31_3/dispos_c.bin:bmap31_3_dein_c`: F0: PID_ELAICE, PID_HAAR, PID_JILL, PID_SOTHE, PID_TAURONEO, PID_ZIHARK
- `bmap31_3/dispos_c.bin:bmap31_3_ev3_senerio2_c`: F2: PID_SENERIO_EV
- `bmap31_3/dispos_c.bin:bmap31_3_ev3_senerio_c`: F2: PID_SENERIO_EV
- `bmap31_3/dispos_c.bin:bmap31_3_event01_c`: F0: PID_BOLE, PID_CALILL, PID_CHAP, PID_CHINON, PID_DALAHOWE, PID_ELAICE, PID_GATRIE, PID_GEOFFRAY, PID_HAAR, PID_JANAFF, PID_JILL, PID_KEVIN, PID_KILROY, PID_LARGO, PID_LETHE, PID_LOFA, PID_LUCHINO, PID_MAKAROV, PID_MARCIA, PID_MORDY, PID_MWARIM, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_SOANVALCKE, PID_SOTHE, PID_STELLA, PID_TANIS, PID_TAURONEO, PID_TOPUCK, PID_ULYSSES, PID_VOKE, PID_VULCI, PID_WAYU, PID_ZIHARK; F2: PID_DUMMY1, PID_GIFFCA_EV, PID_IKE_EV, PID_LAY_EV3, PID_LEARNE, PID_MIST_EV, PID_NAESALA_EV, PID_NEALUCHI, PID_RIEUSION_EV, PID_TIAMAT_EV, PID_TIBARN_EV, PID_ZELGIUS
- `bmap31_3/dispos_c.bin:bmap31_3_event02_c`: F2: PID_ENA, PID_NASIR
- `bmap31_3/dispos_c.bin:bmap31_3_event03_c`: F0: PID_BOLE, PID_CALILL, PID_CHAP, PID_CHINON, PID_GATRIE, PID_GEOFFRAY, PID_KEVIN, PID_KILROY, PID_LARGO, PID_LOFA, PID_LUCHINO, PID_NEPENEE, PID_OSCAR, PID_SENERIO, PID_ULYSSES, PID_WAYU; F2: PID_DUMMY1, PID_IKE_EV, PID_MIST_EV, PID_TIAMAT_EV
- `bmap31_3/dispos_c.bin:bmap31_3_event04_c`: F2: PID_C_ZAKO
- `bmap31_3/dispos_c.bin:bmap31_3_garia_c`: F0: PID_LETHE, PID_MORDY; F2: PID_GIFFCA_EV, PID_LAY_EV3, PID_LEARNE, PID_MIST_EV, PID_RIEUSION_EV
- `bmap31_3/dispos_c.bin:bmap31_3_ike_c`: F2: PID_IKE_EV
- `bmap31_3/dispos_c.bin:bmap31_3_kurimia_c`: F0: PID_CALILL, PID_CHAP, PID_GEOFFRAY, PID_KEVIN, PID_LARGO, PID_LUCHINO, PID_NEPENEE, PID_ULYSSES; F2: PID_DUMMY1
- `bmap31_3/dispos_c.bin:bmap31_3_mist_c`: F2: PID_MIST_EV
- `bmap31_3/dispos_c.bin:bmap31_3_senerio2_c`: F2: PID_SENERIO_EV
- `bmap31_3/dispos_c.bin:bmap31_3_senerio_c`: F2: PID_SENERIO_EV
- `bmap31_3/dispos_c.bin:bmap31_3_youheidan_c`: F0: PID_BOLE, PID_CHINON, PID_GATRIE, PID_KILROY, PID_LOFA, PID_OSCAR, PID_VOKE, PID_WAYU; F2: PID_MIST_EV, PID_TIAMAT_EV

Research checklist: all 15 requested behavioral areas remain open until their conditions are traced. The JSON contains each area explicitly; this listing is an evidence index, not a completed semantic audit.

Instruction-aligned calls in file order; function boundaries prevent treating the whole script as one sequence. `?` means computed/unknown. See CAMPAIGN_EVENTS.md for bounded conditions and decoded triggers; normal activation is unresolved.

| Offset | Function | Command | Literal suffix arguments |
|---|---|---|---|
| 1FB6 | 0 | regist | 情報１フラグ |
| 1FBD | 0 | regist | 情報２フラグ |
| 1FC4 | 0 | regist | 情報３フラグ |
| 1FCB | 0 | regist | 情報４フラグ |
| 1FD2 | 0 | regist | 情報５フラグ |
| 1FD9 | 0 | regist | 情報６フラグ |
| 2019 | 1 | TalkEvent | MS_31_INFO_03 |
| 2076 | 2 | TalkEvent | MS_31_INFO_04 |
| 2083 | 2 | TalkEvent | MS_31_INFO_04_2 |
| 20DE | 3 | TalkEvent | MS_31_INFO_05 |
| 20EB | 3 | TalkEvent | MS_31_INFO_05_2 |
| 23B6 | 6 | TalkEvent | MS_31_EV_01_N |
| 242F | 7 | regist | F15154730 |
| 2437 | 7 | regist | F26313632 |
| 243F | 7 | regist | F15154719 |
| 2493 | 9 | regist | アイク激励した |
| 249B | 9 | regist | ティバーン死亡 |
| 24A3 | 9 | regist | ブライス戦闘 |
| 24AB | 9 | regist | ブライス戦闘アイク |
| 24B3 | 9 | regist | ブライス戦闘タウロニオ |
| 24BB | 9 | regist | ブライス戦闘イナ |
| 24C3 | 9 | regist | アシュ１戦闘会話 |
| 24CB | 9 | regist | アシュ１戦闘会話アイク |
| 24D3 | 9 | regist | アシュ１戦闘会話イナ |
| 24DB | 9 | regist | アシュ１戦闘会話ナーシル |
| 24E3 | 9 | regist | アシュ１戦闘会話エリンシア |
| 24EB | 9 | regist | アシュ１戦闘会話ミスト |
| 24F3 | 9 | regist | アシュ１戦闘会話リュシオン |
| 24FB | 9 | regist | アシュ１戦闘会話牙 |
| 2503 | 9 | regist | アシュ１戦闘会話ウルキ−ヤナフ |
| 250B | 9 | regist | アシュ１戦闘会話タウロニオ |
| 2513 | 9 | regist | アシュ１戦闘会話ジル |
| 251B | 9 | regist | アシュ１戦闘会話ハール |
| 2523 | 9 | regist | アシュ１戦闘会話ティバーン |
| 252B | 9 | regist | アシュ１戦闘会話ネサラ |
| 2533 | 9 | regist | アシュ１戦闘会話ジフカ |
| 253B | 9 | regist | アシュ２戦闘会話ティバーン |
| 2543 | 9 | regist | アシュ２戦闘会話ネサラ |
| 254B | 9 | regist | アシュ２戦闘会話ジフカ |
| 2553 | 9 | regist | アシュナード１回戦闘後 |
| 255B | 9 | regist | アシュナード１倒した |
| 2563 | 9 | regist | アシュナード１オンバトで倒した |
| 256B | 9 | regist | アシュナード変身イベント |
| 2573 | 9 | regist | 呼んだユニット配置イベント |
| 257B | 9 | regist | アシュナード２戦闘 |
| 2583 | 9 | regist | アシュナード２戦闘後 |
| 25C6 | 10 | InstantDisposRank | bmap31_first |
| 25CE | 10 | InstantDisposRank | bmap31_boss |
| 260F | 11 | SallySetByGroup | bmap31_mikata_c |
| 262A | 11 | SallyAddByGroup | bmap31_m_narsil_c |
| 263F | 11 | SallyAddByGroup | bmap31_m_ena_c |
| 277B | 12 | TalkEvent | MS_31_GMAP_1 |
| 27FB | 12 | TalkEvent | MS_31_GMAP_2 |
| 28A9 | 12 | TalkEvent | MS_31_GMAP_3 |
| 28DA | 12 | TalkResume |  |
| 2962 | 13 | ChapterMoviePlay | 31 |
| 29AD | 14 | ForceGetCount | 5 |
| 29CF | 14 | MapLoad | bmap31 |
| 29DD | 14 | InstantDisposSetMode | bmap31_mikata_n, bmap31_mikata_h, bmap31_mikata_m |
| 29E2 | 14 | AllUnitEscape |  |
| 29F6 | 14 | Join | always_dbg_all_c |
| 2C2A | 15 | TalkEvent | MS_31_OP_01_A |
| 2C47 | 15 | TalkEvent | MS_31_OP_01_B |
| 2C62 | 15 | TalkEvent | MS_31_OP_01_C |
| 2C7D | 15 | TalkEvent | MS_31_OP_01_D |
| 2C98 | 15 | TalkEvent | MS_31_OP_01_E |
| 2CB4 | 15 | TalkEvent | MS_31_OP_01_F |
| 2CD0 | 15 | TalkEvent | MS_31_OP_01_G |
| 2CEC | 15 | TalkEvent | MS_31_OP_01_H |
| 2D15 | 15 | TalkEvent | MS_31_OP_02 |
| 2D55 | 15 | TalkResume |  |
| 2D6C | 15 | TalkEvent | MS_31_OP_03_A |
| 2DA0 | 15 | TalkEvent | MS_31_OP_04 |
| 2DB7 | 15 | TalkEvent | MS_31_OP_04_DEL |
| 2DFD | 15 | TalkEvent | MS_31_OP_04_DISP |
| 2E4B | 15 | TalkEvent | MS_31_OP_05_Y |
| 2E62 | 15 | TalkEvent | MS_31_OP_05_Y2 |
| 2F39 | 15 | TalkEvent | MS_31_OP_05_N |
| 2F70 | 15 | MapLoad | bmap31 |
| 2FA1 | 15 | SallySetByGroup | bmap31_mikata_c |
| 2FA9 | 15 | InstantDispos | bmap31_mikata_c |
| 2FAE | 15 | AllUnitEscape |  |
| 3019 | 15 | ForceGetCount | 1 |
| 3022 | 15 | ForceGetFirst | 1 |
| 30E2 | 15 | InstantDispos | bmap31_event_ike_c |
| 30EA | 15 | InstantDispos | bmap31_event_erincia_c |
| 30F7 | 15 | Dispos_ForEventSenerio | bmap31_event_senerio_c, bmap31_event_senerio2_c, 1 |
| 3109 | 15 | InstantDispos | bmap31_m_narsil_c |
| 3121 | 15 | InstantDispos | bmap31_m_ena_c |
| 3151 | 15 | SallyAddByGroup | bmap31_m_narsil_c |
| 3166 | 15 | SallyAddByGroup | bmap31_m_ena_c |
| 3221 | 15 | TalkEvent | MS_31_OP_06 |
| 337A | 15 | TalkEvent | MS_31_OP_07 |
| 342A | 15 | TalkEvent | MS_31_OP_08 |
| 3440 | 15 | TalkResume |  |
| 3531 | 15 | TalkEvent | MS_31_OP_09 |
| 35CA | 15 | TalkEvent | MS_31_OP_10 |
| 3676 | 15 | UnitEscapeByPID | PID_IKE_EV |
| 367E | 15 | UnitEscapeByPID | PID_ERINCIA_QUEEN_EV |
| 3686 | 15 | UnitEscapeByPID | PID_SENERIO_EV |
| 368E | 15 | UnitEscapeByPID | PID_TIAMAT_EV |
| 36AB | 15 | InstantDispos | bmap31_mikata_c |
| 36BD | 15 | InstantDisposContinue | bmap31_m_narsil_c |
| 36C8 | 15 | InstantDisposContinue | bmap31_m_ena_c |
| 3888 | 15 | TalkEvent | MS_31_OP_11 |
| 38EF | 15 | UnitForcedSallyByPID | PID_IKE |
| 38F7 | 15 | UnitForcedSallyByPID | PID_ENA |
| 38FE | 15 | UnitForcedSallyByPID | PID_NASIR |
| 3906 | 15 | UnitDontMoveSallyByPID | PID_IKE |
| 39C6 | 16 | InstantDispos | bmap31_event_erincia_c |
| 3A88 | 16 | TalkEvent | MS_31_OP_12_A |
| 3A93 | 16 | TalkEvent | MS_31_OP_12_B |
| 3AD1 | 16 | UnitEscapeByPID | PID_ERINCIA_QUEEN_EV |
| 3BF3 | 18 | TalkEvent | MS_31_EV_NASIR_01_N |
| 3C11 | 18 | TalkEvent | MS_31_EV_ENA_01_N |
| 3C7B | 18 | TalkEvent | MS_31_EV_NASIR_02_N |
| 3C86 | 18 | TalkEvent | MS_31_EV_ENA_02_N |
| 3D4D | 19 | Dispos | bmap31_m_tibarn_c |
| 3D68 | 19 | TalkEvent | MS_31_EV_TIBARN_N |
| 3D86 | 19 | Dispos | bmap31_m_naesala_c |
| 3DA9 | 19 | TalkEvent | MS_31_EV_NAESALA_N |
| 3DC7 | 19 | Dispos | bmap31_m_giffca_c |
| 3DE2 | 19 | TalkEvent | MS_31_EV_GIFFCA_N |
| 3E9B | 20 | DisposSetMode | bmap31_z01_n, bmap31_z01_h, bmap31_z01_m |
| 40F4 | 21 | TalkEvent | MS_31_EV_01 |
| 41ED | 22 | TalkEvent | MS_31_EV_02_01 |
| 4282 | 22 | UnitEscapeByPID | PID_ASHNARD |
| 4291 | 22 | InstantDisposRank | bmap31_boss2 |
| 42B6 | 22 | ForceGetCount | 0 |
| 42BF | 22 | ForceGetFirst | 0 |
| 42FA | 22 | ForceGetCount | 1 |
| 4303 | 22 | ForceGetFirst | 1 |
| 44CD | 22 | TalkEvent | MS_31_EV_02_02 |
| 44D9 | 22 | TalkResume |  |
| 44E8 | 22 | TalkResume |  |
| 457D | 22 | TalkEvent | MS_31_EV_NASIR_01 |
| 459B | 22 | TalkEvent | MS_31_EV_ENA_01 |
| 4624 | 22 | TalkEvent | MS_31_EV_NASIR_02 |
| 4663 | 22 | TalkEvent | MS_31_EV_ENA_02 |
| 4757 | 23 | Dispos | bmap31_m_tibarn_c |
| 4772 | 23 | TalkEvent | MS_31_EV_TIBARN |
| 4790 | 23 | Dispos | bmap31_m_naesala_c |
| 47B3 | 23 | TalkEvent | MS_31_EV_NAESALA |
| 47D1 | 23 | Dispos | bmap31_m_giffca_c |
| 47EC | 23 | TalkEvent | MS_31_EV_GIFFCA |
| 4892 | 24 | LocalDieTalkWithBgmChange | , MS_31_DIE_LAY |
| 48BA | 25 | LocalDieTalkWithBgmChange | , MS_31_DIE_ENA |
| 48E2 | 26 | LocalDieTalkWithBgmChange | , MS_31_DIE_NASIR |
| 4910 | 27 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 4918 | 27 | TalkEvent | MS_31_BT_G01 |
| 4925 | 27 | SoundBossTalkEnd |  |
| 4958 | 28 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 4960 | 28 | TalkEvent | MS_31_BT_G02 |
| 496D | 28 | SoundBossTalkEnd |  |
| 49A0 | 29 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 49A8 | 29 | TalkEvent | MS_31_BT_G03 |
| 49B5 | 29 | SoundBossTalkEnd |  |
| 49FE | 30 | BMGetPhase |  |
| 4A3E | 30 | SoundBossTalkStart | BGM_BTL_BOSS2 |
| 4A46 | 30 | TalkEvent | MS_31_BT_G |
| 4A53 | 30 | SoundBossTalkEnd |  |
| 4A8B | 31 | BMGetPhase |  |
| 4AB3 | 31 | TalkEvent | MS_31_DIE_G01 |
| 4ABE | 31 | TalkEvent | MS_31_DIE_G02 |
| 4AF0 | 32 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4AF8 | 32 | TalkEvent | MS_31_BT_01 |
| 4B05 | 32 | SoundBossTalkEnd |  |
| 4B40 | 33 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4B48 | 33 | TalkEvent | MS_31_BT_02 |
| 4B55 | 33 | SoundBossTalkEnd |  |
| 4B90 | 34 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4BAD | 34 | TalkEvent | MS_31_BT_03 |
| 4BB8 | 34 | TalkEvent | MS_31_BT_03_2 |
| 4BC5 | 34 | SoundBossTalkEnd |  |
| 4C00 | 35 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4C08 | 35 | TalkEvent | MS_31_BT_04 |
| 4C15 | 35 | SoundBossTalkEnd |  |
| 4C50 | 36 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4C58 | 36 | TalkEvent | MS_31_BT_07 |
| 4C65 | 36 | SoundBossTalkEnd |  |
| 4CA0 | 37 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4CA8 | 37 | TalkEvent | MS_31_BT_08 |
| 4CB5 | 37 | SoundBossTalkEnd |  |
| 4CF0 | 38 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4CF8 | 38 | TalkEvent | MS_31_BT_R1 |
| 4D05 | 38 | SoundBossTalkEnd |  |
| 4D40 | 39 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4D48 | 39 | TalkEvent | MS_31_BT_R1 |
| 4D55 | 39 | SoundBossTalkEnd |  |
| 4D90 | 40 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4D98 | 40 | TalkEvent | MS_31_BT_R1 |
| 4DA5 | 40 | SoundBossTalkEnd |  |
| 4DE0 | 41 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4DE8 | 41 | TalkEvent | MS_31_BT_R1 |
| 4DF5 | 41 | SoundBossTalkEnd |  |
| 4E30 | 42 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4E38 | 42 | TalkEvent | MS_31_BT_R2 |
| 4E45 | 42 | SoundBossTalkEnd |  |
| 4E80 | 43 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4E88 | 43 | TalkEvent | MS_31_BT_R2 |
| 4E95 | 43 | SoundBossTalkEnd |  |
| 4ED0 | 44 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4ED8 | 44 | TalkEvent | MS_31_BT_R4 |
| 4EE5 | 44 | SoundBossTalkEnd |  |
| 4F20 | 45 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4F28 | 45 | TalkEvent | MS_31_BT_R5 |
| 4F35 | 45 | SoundBossTalkEnd |  |
| 4F70 | 46 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4F78 | 46 | TalkEvent | MS_31_BT_R3 |
| 4F85 | 46 | SoundBossTalkEnd |  |
| 4FC0 | 47 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 4FC8 | 47 | TalkEvent | MS_31_BT_05N |
| 4FD5 | 47 | SoundBossTalkEnd |  |
| 5008 | 48 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 5010 | 48 | TalkEvent | MS_31_BT_06N |
| 501D | 48 | SoundBossTalkEnd |  |
| 5050 | 49 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 5058 | 49 | TalkEvent | MS_31_BT_09N |
| 5065 | 49 | SoundBossTalkEnd |  |
| 5135 | 50 | BMGetPhase |  |
| 5215 | 50 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1_LP |
| 521D | 50 | TalkEvent | MS_31_BT |
| 522A | 50 | SoundBossTalkEnd |  |
| 525F | 51 | TalkEvent | MS_31_DIE_1 |
| 5285 | 51 | BMGetPhase |  |
| 5300 | 52 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1 |
| 5308 | 52 | TalkEvent | MS_31_BT_05 |
| 5315 | 52 | SoundBossTalkEnd |  |
| 5348 | 53 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1 |
| 5350 | 53 | TalkEvent | MS_31_BT_06 |
| 535D | 53 | SoundBossTalkEnd |  |
| 5390 | 54 | SoundBossTalkStart | BGM_BTL_LAST_BOSS1 |
| 5398 | 54 | TalkEvent | MS_31_BT_09 |
| 53A5 | 54 | SoundBossTalkEnd |  |
| 544C | 57 | TalkEvent | MS_31_DIE_2 |
| 5576 | 58 | TalkEvent | MS_31_ED_00N |
| 5581 | 58 | TalkEvent | MS_31_ED_00 |
| 55B5 | 58 | AllUnitEscape |  |
| 5691 | 58 | MapLoad | bmap31_2 |
| 56B8 | 58 | InstantDispos | bmap31_2_event01_c |
| 56CC | 58 | UnitEscapeByPID | PID_OSCAR |
| 56D9 | 58 | UnitEscapeByPID | PID_BOLE |
| 56E6 | 58 | UnitEscapeByPID | PID_LOFA |
| 56F3 | 58 | UnitEscapeByPID | PID_VULCI |
| 5700 | 58 | UnitEscapeByPID | PID_JANAFF |
| 570D | 58 | UnitEscapeByPID | PID_HAAR |
| 571A | 58 | UnitEscapeByPID | PID_LUCHINO |
| 5727 | 58 | UnitEscapeByPID | PID_ULYSSES |
| 5734 | 58 | UnitEscapeByPID | PID_GEOFFRAY |
| 5747 | 58 | UnitEscapeByPID | PID_NASIR_EV |
| 59AF | 58 | TalkEvent | MS_31_ED_03 |
| 59BE | 58 | TalkResume |  |
| 5A75 | 58 | TalkEvent | MS_31_ED_04 |
| 5B30 | 58 | TalkEvent | MS_31_ED_04_2 |
| 5B4F | 58 | AllUnitEscape |  |
| 5B59 | 58 | AllUnitEscape |  |
| 5CC4 | 58 | TalkEvent | MS_31_ED_05 |
| 5CCF | 58 | TalkEvent | MS_31_ED_05_N |
| 5DA7 | 58 | TalkEvent | MS_31_ED_06 |
| 5E49 | 58 | TalkEvent | MS_31_ED_08 |
| 5E54 | 58 | TalkEvent | MS_31_ED_08_N |
| 5F7A | 58 | TalkEvent | MS_31_ED_09 |
| 5F8A | 58 | TalkEvent | MS_31_ED_10 |
| 5F9C | 58 | TalkEvent | MS_31_ED_12 |
| 5FA7 | 58 | TalkEvent | MS_31_ED_12_N |
| 60B3 | 58 | TalkEvent | MS_31_ED_13A |
| 60E4 | 58 | TalkResume |  |
| 6150 | 59 | ForceGetCount | ? |
| 6159 | 59 | ForceGetFirst | ? |
| 63B1 | 62 | UnitEscapeByPID | PID_TIAMAT_EV |
| 63B9 | 62 | UnitEscapeByPID | PID_SENERIO |
| 63C1 | 62 | UnitEscapeByPID | PID_BOLE |
| 63C9 | 62 | UnitEscapeByPID | PID_LOFA |
| 63D1 | 62 | UnitEscapeByPID | PID_OSCAR |
| 63D9 | 62 | UnitEscapeByPID | PID_KILROY |
| 63E1 | 62 | UnitEscapeByPID | PID_WAYU |
| 63E9 | 62 | UnitEscapeByPID | PID_CHINON |
| 63F1 | 62 | UnitEscapeByPID | PID_GATRIE |
| 63F9 | 62 | UnitEscapeByPID | PID_VOKE |
| 65C9 | 63 | UnitEscapeByPID | PID_DUMMY1 |
| 65D1 | 63 | UnitEscapeByPID | PID_GEOFFRAY |
| 65D9 | 63 | UnitEscapeByPID | PID_ULYSSES |
| 65E1 | 63 | UnitEscapeByPID | PID_LUCHINO |
| 65E9 | 63 | UnitEscapeByPID | PID_KEVIN |
| 65F1 | 63 | UnitEscapeByPID | PID_CHAP |
| 65F9 | 63 | UnitEscapeByPID | PID_NEPENEE |
| 6601 | 63 | UnitEscapeByPID | PID_LARGO |
| 6609 | 63 | UnitEscapeByPID | PID_CALILL |
| 679B | 64 | UnitEscapeByPID | PID_TANIS |
| 67A3 | 64 | UnitEscapeByPID | PID_ZELGIUS |
| 67AB | 64 | UnitEscapeByPID | PID_MARCIA |
| 67B3 | 64 | UnitEscapeByPID | PID_STELLA |
| 67BB | 64 | UnitEscapeByPID | PID_MAKAROV |
| 67C3 | 64 | UnitEscapeByPID | PID_MWARIM |
| 67CB | 64 | UnitEscapeByPID | PID_TOPUCK |
| 67D3 | 64 | UnitEscapeByPID | PID_SOANVALCKE |
| 67DB | 64 | UnitEscapeByPID | PID_DALAHOWE |
| 686B | 65 | UnitEscapeByPID | PID_LAY_EV3 |
| 6873 | 65 | UnitEscapeByPID | PID_GIFFCA_EV |
| 687B | 65 | UnitEscapeByPID | PID_LETHE |
| 6883 | 65 | UnitEscapeByPID | PID_MORDY |
| 688B | 65 | UnitEscapeByPID | PID_RIEUSION_EV |
| 6893 | 65 | UnitEscapeByPID | PID_LEARNE |
| 6909 | 66 | UnitEscapeByPID | PID_TIBARN_EV |
| 6911 | 66 | UnitEscapeByPID | PID_NAESALA_EV |
| 6919 | 66 | UnitEscapeByPID | PID_NEALUCHI |
| 6921 | 66 | UnitEscapeByPID | PID_JANAFF |
| 6929 | 66 | UnitEscapeByPID | PID_VULCI |
| 6D83 | 67 | MapLoad | bmap31_3 |
| 6DAA | 67 | InstantDispos | bmap31_3_event01_c |
| 6DBF | 67 | UnitEscapeByPID | PID_ZELGIUS |
| 6DD3 | 67 | UnitEscapeByPID | PID_OSCAR |
| 6DE0 | 67 | UnitEscapeByPID | PID_BOLE |
| 6DED | 67 | UnitEscapeByPID | PID_KILROY |
| 6DFA | 67 | UnitEscapeByPID | PID_GATRIE |
| 6E07 | 67 | UnitEscapeByPID | PID_CHINON |
| 6E14 | 67 | UnitEscapeByPID | PID_WAYU |
| 6E21 | 67 | UnitEscapeByPID | PID_ELAICE |
| 6E2E | 67 | UnitEscapeByPID | PID_LOFA |
| 6E3B | 67 | UnitEscapeByPID | PID_MARCIA |
| 6E48 | 67 | UnitEscapeByPID | PID_LETHE_EV |
| 6E55 | 67 | UnitEscapeByPID | PID_MORDY_EV |
| 6E62 | 67 | UnitEscapeByPID | PID_CHAP |
| 6E6F | 67 | UnitEscapeByPID | PID_NEPENEE |
| 6E7C | 67 | UnitEscapeByPID | PID_KEVIN |
| 6E89 | 67 | UnitEscapeByPID | PID_VOKE |
| 6E96 | 67 | UnitEscapeByPID | PID_ZIHARK |
| 6EA3 | 67 | UnitEscapeByPID | PID_SOTHE |
| 6EB0 | 67 | UnitEscapeByPID | PID_JILL |
| 6EBD | 67 | UnitEscapeByPID | PID_STELLA |
| 6ECA | 67 | UnitEscapeByPID | PID_MAKAROV |
| 6ED7 | 67 | UnitEscapeByPID | PID_MWARIM |
| 6EE4 | 67 | UnitEscapeByPID | PID_TOPUCK |
| 6EF1 | 67 | UnitEscapeByPID | PID_SOANVALCKE |
| 6EFE | 67 | UnitEscapeByPID | PID_DALAHOWE |
| 6F0B | 67 | UnitEscapeByPID | PID_VULCI |
| 6F18 | 67 | UnitEscapeByPID | PID_JANAFF |
| 6F25 | 67 | UnitEscapeByPID | PID_TANIS |
| 6F32 | 67 | UnitEscapeByPID | PID_CALILL |
| 6F3F | 67 | UnitEscapeByPID | PID_TAURONEO |
| 6F4C | 67 | UnitEscapeByPID | PID_HAAR |
| 6F59 | 67 | UnitEscapeByPID | PID_LUCHINO |
| 6F66 | 67 | UnitEscapeByPID | PID_ULYSSES |
| 6F73 | 67 | UnitEscapeByPID | PID_GEOFFRAY |
| 6F80 | 67 | UnitEscapeByPID | PID_LARGO |
| 72E0 | 67 | TalkEvent | MS_31_GED_Mer |
| 7310 | 67 | TalkEvent | MS_31_GED_Mer_sen_a |
| 731B | 67 | TalkEvent | MS_32_GED_Mer_sen_b |
| 7333 | 67 | TalkEvent | MS_31_GED_Mer_tia_a |
| 733E | 67 | TalkEvent | MS_32_GED_Mer_tia_b |
| 734C | 67 | TalkEvent | MS_31_ED_FACE_DEL_5 |
| 7374 | 67 | TalkEvent | MS_31_GED_Mer_osc_a |
| 737F | 67 | TalkEvent | MS_32_GED_Mer_osc_b |
| 7387 | 67 | TalkEvent | MS_31_GED_Mer_mis |
| 739A | 67 | TalkEvent | MS_31_ED_FACE_DEL_5 |
| 73B2 | 67 | TalkEvent | MS_31_GED_Mer_bol |
| 73C0 | 67 | TalkEvent | MS_31_ED_FACE_DEL_4 |
| 73D8 | 67 | TalkEvent | MS_31_GED_Mer_lof |
| 73EB | 67 | TalkEvent | MS_31_ED_FACE_DEL_5 |
| 7403 | 67 | TalkEvent | MS_31_GED_Mer_kil |
| 7416 | 67 | TalkEvent | MS_31_ED_FACE_DEL_4 |
| 742E | 67 | TalkEvent | MS_31_GED_Mer_gat |
| 7441 | 67 | TalkEvent | MS_31_ED_FACE_DEL_5 |
| 7459 | 67 | TalkEvent | MS_31_GED_Mer_chi |
| 746C | 67 | TalkEvent | MS_31_ED_FACE_DEL_4 |
| 7484 | 67 | TalkEvent | MS_31_GED_way |
| 7497 | 67 | TalkEvent | MS_31_ED_FACE_DEL_5 |
| 74AF | 67 | TalkEvent | MS_31_GED_vol |
| 74C7 | 67 | TalkEvent | MS_31_ED_WINDOW_DEL |
| 75C7 | 67 | TalkEvent | MS_31_GED_Cri_a |
| 75D2 | 67 | TalkEvent | MS_31_GED_Cri_b |
| 75F0 | 67 | TalkEvent | MS_31_GED_Cri_uly |
| 760E | 67 | TalkEvent | MS_31_GED_Cri_luc |
| 7621 | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 7639 | 67 | TalkEvent | MS_31_GED_Cri_geo |
| 764C | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 7664 | 67 | TalkEvent | MS_31_GED_Cri_kev |
| 7677 | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 768F | 67 | TalkEvent | MS_31_GED_Cri_cha |
| 76A2 | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 76BA | 67 | TalkEvent | MS_31_GED_Cri_nep |
| 76E1 | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 76F4 | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 76FC | 67 | TalkEvent | MS_31_GED_Cri_pair |
| 771C | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 7724 | 67 | TalkEvent | MS_31_GED_Cri_cal |
| 7744 | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 774C | 67 | TalkEvent | MS_31_GED_Cri_lar |
| 7754 | 67 | TalkEvent | MS_31_ED_WINDOW_DEL |
| 7851 | 67 | TalkEvent | MS_31_GED_Beg_a |
| 7862 | 67 | TalkEvent | MS_31_GED_Beg_b |
| 7898 | 67 | TalkEvent | MS_31_GED_Beg_mar |
| 78B6 | 67 | TalkEvent | MS_31_GED_Beg_mak |
| 78C9 | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 78E1 | 67 | TalkEvent | MS_31_GED_Beg_ste |
| 78F4 | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 790C | 67 | TalkEvent | MS_31_GED_Beg_dal |
| 791F | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 7937 | 67 | TalkEvent | MS_31_GED_Beg_top |
| 794A | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 7962 | 67 | TalkEvent | MS_31_GED_Beg_mwa |
| 797F | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 7992 | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 79A0 | 67 | TalkEvent | MS_31_GED_Beg_soa |
| 79A8 | 67 | TalkEvent | MS_31_ED_WINDOW_DEL |
| 7A74 | 67 | TalkEvent | MS_31_GED_Gal_a |
| 7A7F | 67 | TalkEvent | MS_31_GED_Gal_b |
| 7A9F | 67 | TalkEvent | MS_31_GED_Gal_2_a |
| 7AAA | 67 | TalkEvent | MS_31_GED_Gal_2_b |
| 7ABC | 67 | TalkEvent | MS_31_GED_Gal_mor |
| 7ADE | 67 | TalkEvent | MS_31_GED_Gal_ret_a |
| 7AE9 | 67 | TalkEvent | MS_31_GED_Gal_ret_b |
| 7AF1 | 67 | TalkEvent | MS_31_ED_WINDOW_DEL |
| 7B93 | 67 | TalkEvent | MS_31_GED_Pho |
| 7BAB | 67 | TalkEvent | MS_31_GED_Pho_vul |
| 7BC3 | 67 | TalkEvent | MS_31_GED_Pho_jan |
| 7BCB | 67 | TalkEvent | MS_31_ED_WINDOW_DEL |
| 7CC7 | 67 | TalkEvent | MS_31_GED_Day_Open |
| 7CE5 | 67 | TalkEvent | MS_31_GED_Day_jil |
| 7D03 | 67 | TalkEvent | MS_31_GED_Day_haa |
| 7D16 | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 7D29 | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 7D41 | 67 | TalkEvent | MS_31_GED_Day_sot |
| 7D54 | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 7D6C | 67 | TalkEvent | MS_31_GED_Day_tau |
| 7D7F | 67 | TalkEvent | MS_31_ED_FACE_DEL_1 |
| 7D97 | 67 | TalkEvent | MS_31_GED_Day_ela |
| 7DAA | 67 | TalkEvent | MS_31_ED_FACE_DEL_2 |
| 7DC2 | 67 | TalkEvent | MS_31_GED_Day_zih_b |
| 7DCA | 67 | TalkEvent | MS_31_ED_WINDOW_DEL |
| 7DEB | 67 | AllUnitEscape |  |
| 7DF5 | 67 | AllUnitEscape |  |
| 7E12 | 67 | InstantDispos | bmap31_3_ike_c |
| 7F61 | 67 | AllUnitEscape |  |
| 7F7B | 67 | TalkEvent | MS_31_GED_GOL_a |
| 7F86 | 67 | TalkEvent | MS_31_GED_GOL_b |
| 7FB7 | 67 | InstantDispos | bmap31_3_event03_c |
| 7FC4 | 67 | UnitEscapeByPID | PID_OSCAR |
| 7FD1 | 67 | UnitEscapeByPID | PID_BOLE |
| 7FDE | 67 | UnitEscapeByPID | PID_KILROY |
| 7FEB | 67 | UnitEscapeByPID | PID_GATRIE |
| 7FF8 | 67 | UnitEscapeByPID | PID_CHINON |
| 8005 | 67 | UnitEscapeByPID | PID_WAYU |
| 8012 | 67 | UnitEscapeByPID | PID_ELAICE |
| 801F | 67 | UnitEscapeByPID | PID_LOFA |
| 802C | 67 | UnitEscapeByPID | PID_MARCIA |
| 8039 | 67 | UnitEscapeByPID | PID_LETHE_EV |
| 8046 | 67 | UnitEscapeByPID | PID_MORDY_EV |
| 8053 | 67 | UnitEscapeByPID | PID_CHAP |
| 8060 | 67 | UnitEscapeByPID | PID_NEPENEE |
| 806D | 67 | UnitEscapeByPID | PID_KEVIN |
| 807A | 67 | UnitEscapeByPID | PID_VOKE |
| 8087 | 67 | UnitEscapeByPID | PID_ZIHARK |
| 8094 | 67 | UnitEscapeByPID | PID_SOTHE |
| 80A1 | 67 | UnitEscapeByPID | PID_JILL |
| 80AE | 67 | UnitEscapeByPID | PID_STELLA |
| 80BB | 67 | UnitEscapeByPID | PID_MAKAROV |
| 80C8 | 67 | UnitEscapeByPID | PID_MWARIM |
| 80D5 | 67 | UnitEscapeByPID | PID_TOPUCK |
| 80E2 | 67 | UnitEscapeByPID | PID_SOANVALCKE |
| 80EF | 67 | UnitEscapeByPID | PID_DALAHOWE |
| 80FC | 67 | UnitEscapeByPID | PID_VULCI |
| 8109 | 67 | UnitEscapeByPID | PID_JANAFF |
| 8116 | 67 | UnitEscapeByPID | PID_TANIS |
| 8123 | 67 | UnitEscapeByPID | PID_CALILL |
| 8130 | 67 | UnitEscapeByPID | PID_TAURONEO |
| 813D | 67 | UnitEscapeByPID | PID_HAAR |
| 814A | 67 | UnitEscapeByPID | PID_LUCHINO |
| 8157 | 67 | UnitEscapeByPID | PID_ULYSSES |
| 8164 | 67 | UnitEscapeByPID | PID_GEOFFRAY |
| 8171 | 67 | UnitEscapeByPID | PID_LARGO |
| 8183 | 67 | InstantDispos | bmap31_3_event04_c |
| 8202 | 67 | AllUnitEscape |  |
| 820C | 67 | AllUnitEscape |  |
| 82AA | 67 | TalkEvent | MS_31_ED_XX_01 |
| 8302 | 67 | TalkEvent | MS_31_ED_XX_02 |
| 833D | 67 | TalkResume |  |
| 8382 | 67 | MapLoad | bmap31_3 |
| 8426 | 67 | AllUnitEscape |  |
| 8448 | 67 | TalkEvent | MS_31_ED_18 |
| 8471 | 67 | TalkEvent | MS_31_ED_19 |
| 8480 | 67 | TalkResume |  |

Open: original objective predicates; script reachability and order; available roster vs scripted appearances; production runtime acceptance.

