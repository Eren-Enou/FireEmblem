# Native event-command usage

43 script containers; 406 literal native registrations; 327 native names have aligned reachable local call instructions.

This cross-reference excludes string-pool-only mentions. Each call is reachable in its local scene CFG; scene activation is unproven. Zero calls does not prove engine unreachability: indirect dispatch, native-to-native calls and imported script helpers are not resolved. Registration instruction evidence is generated in ignored work/native_usage.json.

| Command | Direct script calls | Containers |
|---|---:|---|
| PlayerEscapeCount | 0 |  |
| PlayerEscapeCheck | 0 |  |
| UnitEscape | 45 | C03.cmb, C04.cmb, C07.cmb, C08.cmb, C09.cmb, C11.cmb, C12.cmb, C14.cmb, C17.cmb, C18.cmb, C20.cmb, C22.cmb, C23.cmb, C27.cmb, C28.cmb, C29.cmb, C81.cmb, C95.cmb, startup.cmb |
| AllUnitEscape | 141 | C01.cmb, C02.cmb, C03.cmb, C04.cmb, C05.cmb, C06.cmb, C07.cmb, C08.cmb, C09.cmb, C10.cmb, C11.cmb, C12.cmb, C13.cmb, C14.cmb, C15.cmb, C16.cmb, C17.cmb, C18.cmb, C19.cmb, C20.cmb, C21.cmb, C22.cmb, C23.cmb, C24.cmb, C25.cmb, C26.cmb, C27.cmb, C28.cmb, C29.cmb, C30.cmb, C31.cmb, C91.cmb, C92.cmb, C93.cmb, C94.cmb, C95.cmb, C96.cmb |
| DefaultEscapeTalk | 2 | C07.cmb, C11.cmb |
| PlayerDeadCheck | 0 |  |
| EnemyDeadCheck | 0 |  |
| GetDiedPlayerCount | 0 |  |
| UnitDead | 8 | C03.cmb, C09.cmb, C26.cmb |
| UnitTransferToForce | 7 | C11.cmb, C19.cmb, C20.cmb, C25.cmb, startup.cmb |
| ForceGetCount | 167 | C02.cmb, C03.cmb, C04.cmb, C05.cmb, C06.cmb, C07.cmb, C08.cmb, C09.cmb, C10.cmb, C11.cmb, C12.cmb, C13.cmb, C14.cmb, C15.cmb, C16.cmb, C17.cmb, C18.cmb, C19.cmb, C20.cmb, C21.cmb, C22.cmb, C23.cmb, C24.cmb, C25.cmb, C26.cmb, C27.cmb, C28.cmb, C29.cmb, C30.cmb, C31.cmb, C91.cmb, C92.cmb, C93.cmb, C96.cmb, startup.cmb |
| UnitGetByPID | 554 | C00.cmb, C01.cmb, C02.cmb, C03.cmb, C04.cmb, C05.cmb, C06.cmb, C07.cmb, C08.cmb, C09.cmb, C10.cmb, C11.cmb, C12.cmb, C13.cmb, C14.cmb, C15.cmb, C16.cmb, C17.cmb, C18.cmb, C19.cmb, C20.cmb, C21.cmb, C22.cmb, C23.cmb, C24.cmb, C25.cmb, C26.cmb, C27.cmb, C28.cmb, C29.cmb, C30.cmb, C31.cmb, C80.cmb, C81.cmb, C82.cmb, C92.cmb, C93.cmb, C95.cmb, C96.cmb, startup.cmb |
| Join | 132 | C11.cmb, C12.cmb, C13.cmb, C14.cmb, C16.cmb, C17.cmb, C18.cmb, C20.cmb, C21.cmb, C22.cmb, C23.cmb, C24.cmb, C25.cmb, C26.cmb, C28.cmb, C30.cmb, C31.cmb, startup.cmb |
| SallySetByGroup | 67 | C00.cmb, C01.cmb, C02.cmb, C03.cmb, C04.cmb, C05.cmb, C06.cmb, C07.cmb, C08.cmb, C09.cmb, C10.cmb, C11.cmb, C12.cmb, C13.cmb, C14.cmb, C15.cmb, C16.cmb, C17.cmb, C18.cmb, C19.cmb, C20.cmb, C21.cmb, C22.cmb, C23.cmb, C24.cmb, C25.cmb, C26.cmb, C27.cmb, C28.cmb, C29.cmb, C30.cmb, C31.cmb, C80.cmb, C91.cmb, C92.cmb, C93.cmb, C94.cmb, C95.cmb, C96.cmb |
| UnitForcedSally | 3 | C30.cmb, startup.cmb |
| BMSetPhase | 0 |  |
| BMSetTurn | 3 | C18.cmb |

## Escape and death-check call sites

### PlayerEscapeCount

No direct aligned call in the scanned script containers.

### PlayerEscapeCheck

No direct aligned call in the scanned script containers.

### UnitEscape

- Scripts/C03.cmb scene 19, `0x2346`, arguments `[None, 0]`.
- Scripts/C04.cmb scene 3, `0xD19`, arguments `[None, 0]`.
- Scripts/C04.cmb scene 4, `0xD69`, arguments `[None, 0]`.
- Scripts/C07.cmb scene 1, `0xE66`, arguments `[None, 0]`.
- Scripts/C08.cmb scene 3, `0x170A`, arguments `[None, 0]`.
- Scripts/C08.cmb scene 4, `0x1762`, arguments `[None, 0]`.
- Scripts/C08.cmb scene 19, `0x2769`, arguments `[None, 0]`.
- Scripts/C08.cmb scene 34, `0x2F1C`, arguments `[None, 0]`.
- Scripts/C09.cmb scene 13, `0x1F61`, arguments `[None, 0]`.
- Scripts/C09.cmb scene 31, `0x32B8`, arguments `[None, 0]`.
- Scripts/C09.cmb scene 31, `0x36BC`, arguments `[None, 0]`.
- Scripts/C11.cmb scene 5, `0x1625`, arguments `[None, 0]`.
- Scripts/C12.cmb scene 6, `0x1B21`, arguments `[None, 0]`.
- Scripts/C12.cmb scene 53, `0x4B93`, arguments `[None, 0]`.
- Scripts/C12.cmb scene 53, `0x4BF8`, arguments `[None, 0]`.
- Scripts/C14.cmb scene 13, `0x14F2`, arguments `[None, 0]`.
- Scripts/C14.cmb scene 14, `0x1546`, arguments `[None, 0]`.
- Scripts/C14.cmb scene 54, `0x31CE`, arguments `[None, 0]`.
- Scripts/C14.cmb scene 54, `0x3228`, arguments `[None, 0]`.
- Scripts/C14.cmb scene 54, `0x3275`, arguments `[None, 0]`.
- Scripts/C17.cmb scene 13, `0x112A`, arguments `[None, 0]`.
- Scripts/C17.cmb scene 14, `0x1182`, arguments `[None, 0]`.
- Scripts/C18.cmb scene 82, `0x5729`, arguments `[None, 0]`.
- Scripts/C18.cmb scene 85, `0x5EA8`, arguments `[None, 0]`.
- Scripts/C18.cmb scene 86, `0x697C`, arguments `[None, 0]`.
- Scripts/C18.cmb scene 88, `0x6DF2`, arguments `[None, 0]`.
- Scripts/C18.cmb scene 89, `0x77A0`, arguments `[None, 0]`.
- Scripts/C18.cmb scene 94, `0x7D2C`, arguments `[None, 0]`.
- Scripts/C20.cmb scene 5, `0x17EF`, arguments `[None, 0]`.
- Scripts/C22.cmb scene 22, `0x18D6`, arguments `[None, 0]`.
- Scripts/C22.cmb scene 64, `0x328A`, arguments `[None, 0]`.
- Scripts/C22.cmb scene 64, `0x32A2`, arguments `[None, 0]`.
- Scripts/C23.cmb scene 9, `0x123E`, arguments `[None, 0]`.
- Scripts/C23.cmb scene 10, `0x1296`, arguments `[None, 0]`.
- Scripts/C23.cmb scene 11, `0x12EE`, arguments `[None, 0]`.
- Scripts/C23.cmb scene 12, `0x1346`, arguments `[None, 0]`.
- Scripts/C27.cmb scene 35, `0x2203`, arguments `[None, 0]`.
- Scripts/C28.cmb scene 15, `0x1132`, arguments `[None, 0]`.
- Scripts/C28.cmb scene 16, `0x118A`, arguments `[None, 0]`.
- Scripts/C28.cmb scene 40, `0x257B`, arguments `[None, 0]`.
- Scripts/C28.cmb scene 40, `0x2593`, arguments `[None, 0]`.
- Scripts/C29.cmb scene 0, `0xD13`, arguments `[None, 0]`.
- Scripts/C81.cmb scene 0, `0x8D0`, arguments `[None, 0]`.
- Scripts/C95.cmb scene 0, `0x644`, arguments `[None, 0]`.
- Scripts/startup.cmb scene 27, `0x1D02`, arguments `[None, 0]`.

### AllUnitEscape

- Scripts/C01.cmb scene 19, `0x1C70`, arguments `[]`.
- Scripts/C02.cmb scene 10, `0x1263`, arguments `[]`.
- Scripts/C02.cmb scene 10, `0x126D`, arguments `[]`.
- Scripts/C02.cmb scene 11, `0x1322`, arguments `[]`.
- Scripts/C02.cmb scene 12, `0x1731`, arguments `[]`.
- Scripts/C02.cmb scene 20, `0x1BD7`, arguments `[]`.
- Scripts/C03.cmb scene 6, `0x13D1`, arguments `[]`.
- Scripts/C03.cmb scene 6, `0x13DB`, arguments `[]`.
- Scripts/C03.cmb scene 8, `0x14A9`, arguments `[]`.
- Scripts/C03.cmb scene 9, `0x1905`, arguments `[]`.
- Scripts/C03.cmb scene 19, `0x2552`, arguments `[]`.
- Scripts/C04.cmb scene 13, `0x1211`, arguments `[]`.
- Scripts/C04.cmb scene 14, `0x1726`, arguments `[]`.
- Scripts/C04.cmb scene 22, `0x1D5D`, arguments `[]`.
- Scripts/C05.cmb scene 13, `0x1C78`, arguments `[]`.
- Scripts/C05.cmb scene 13, `0x1C82`, arguments `[]`.
- Scripts/C05.cmb scene 14, `0x2046`, arguments `[]`.
- Scripts/C05.cmb scene 15, `0x2B89`, arguments `[]`.
- Scripts/C05.cmb scene 15, `0x2BA7`, arguments `[]`.
- Scripts/C05.cmb scene 22, `0x2EF5`, arguments `[]`.
- Scripts/C06.cmb scene 10, `0x12F6`, arguments `[]`.
- Scripts/C06.cmb scene 10, `0x1300`, arguments `[]`.
- Scripts/C06.cmb scene 11, `0x1510`, arguments `[]`.
- Scripts/C06.cmb scene 11, `0x152D`, arguments `[]`.
- Scripts/C06.cmb scene 12, `0x1B75`, arguments `[]`.
- Scripts/C06.cmb scene 20, `0x1F57`, arguments `[]`.
- Scripts/C07.cmb scene 13, `0x1F6D`, arguments `[]`.
- Scripts/C07.cmb scene 13, `0x1F8D`, arguments `[]`.
- Scripts/C07.cmb scene 21, `0x2543`, arguments `[]`.
- Scripts/C08.cmb scene 15, `0x1BAF`, arguments `[]`.
- Scripts/C08.cmb scene 16, `0x2309`, arguments `[]`.
- Scripts/C08.cmb scene 35, `0x2F9B`, arguments `[]`.
- Scripts/C08.cmb scene 35, `0x4458`, arguments `[]`.
- Scripts/C08.cmb scene 37, `0x48D8`, arguments `[]`.
- Scripts/C08.cmb scene 39, `0x4F49`, arguments `[]`.
- Scripts/C08.cmb scene 40, `0x5399`, arguments `[]`.
- Scripts/C08.cmb scene 40, `0x53A3`, arguments `[]`.
- Scripts/C08.cmb scene 41, `0x549C`, arguments `[]`.
- Scripts/C09.cmb scene 12, `0x18EE`, arguments `[]`.
- Scripts/C09.cmb scene 12, `0x190F`, arguments `[]`.
- Scripts/C09.cmb scene 12, `0x1B24`, arguments `[]`.
- Scripts/C09.cmb scene 13, `0x2084`, arguments `[]`.
- Scripts/C09.cmb scene 31, `0x2E03`, arguments `[]`.
- Scripts/C09.cmb scene 31, `0x374A`, arguments `[]`.
- Scripts/C09.cmb scene 32, `0x3A17`, arguments `[]`.
- Scripts/C09.cmb scene 32, `0x3A21`, arguments `[]`.
- Scripts/C10.cmb scene 19, `0x17EA`, arguments `[]`.
- Scripts/C10.cmb scene 20, `0x18FB`, arguments `[]`.
- Scripts/C10.cmb scene 44, `0x2E87`, arguments `[]`.
- Scripts/C11.cmb scene 23, `0x1CD2`, arguments `[]`.
- Scripts/C11.cmb scene 25, `0x23AD`, arguments `[]`.
- Scripts/C11.cmb scene 57, `0x34EB`, arguments `[]`.
- Scripts/C12.cmb scene 22, `0x24B9`, arguments `[]`.
- Scripts/C12.cmb scene 22, `0x2650`, arguments `[]`.
- Scripts/C12.cmb scene 22, `0x265A`, arguments `[]`.
- Scripts/C12.cmb scene 23, `0x3801`, arguments `[]`.
- Scripts/C12.cmb scene 23, `0x380B`, arguments `[]`.
- Scripts/C12.cmb scene 53, `0x4B15`, arguments `[]`.
- Scripts/C12.cmb scene 53, `0x51FC`, arguments `[]`.
- Scripts/C13.cmb scene 10, `0x19B6`, arguments `[]`.
- Scripts/C13.cmb scene 11, `0x1AD0`, arguments `[]`.
- Scripts/C13.cmb scene 29, `0x2656`, arguments `[]`.
- Scripts/C13.cmb scene 29, `0x2673`, arguments `[]`.
- Scripts/C13.cmb scene 29, `0x2E6C`, arguments `[]`.
- Scripts/C13.cmb scene 29, `0x2E76`, arguments `[]`.
- Scripts/C14.cmb scene 20, `0x17BE`, arguments `[]`.
- Scripts/C14.cmb scene 21, `0x1D47`, arguments `[]`.
- Scripts/C14.cmb scene 21, `0x1D51`, arguments `[]`.
- Scripts/C14.cmb scene 54, `0x3372`, arguments `[]`.
- Scripts/C14.cmb scene 54, `0x3436`, arguments `[]`.
- Scripts/C14.cmb scene 54, `0x3440`, arguments `[]`.
- Scripts/C15.cmb scene 19, `0x162E`, arguments `[]`.
- Scripts/C15.cmb scene 37, `0x2507`, arguments `[]`.
- Scripts/C16.cmb scene 20, `0x179A`, arguments `[]`.
- Scripts/C16.cmb scene 21, `0x1AA2`, arguments `[]`.
- Scripts/C16.cmb scene 34, `0x25F7`, arguments `[]`.
- Scripts/C16.cmb scene 34, `0x2C2E`, arguments `[]`.
- Scripts/C17.cmb scene 20, `0x13CE`, arguments `[]`.
- Scripts/C17.cmb scene 21, `0x1626`, arguments `[]`.
- Scripts/C17.cmb scene 48, `0x21EF`, arguments `[]`.
- Scripts/C18.cmb scene 36, `0x2E21`, arguments `[]`.
- Scripts/C18.cmb scene 37, `0x333E`, arguments `[]`.
- Scripts/C18.cmb scene 37, `0x3394`, arguments `[]`.
- Scripts/C18.cmb scene 94, `0x7FD6`, arguments `[]`.
- Scripts/C18.cmb scene 94, `0x836A`, arguments `[]`.
- Scripts/C19.cmb scene 18, `0x1E8C`, arguments `[]`.
- Scripts/C19.cmb scene 19, `0x21D4`, arguments `[]`.
- Scripts/C19.cmb scene 49, `0x390E`, arguments `[]`.
- Scripts/C20.cmb scene 75, `0x26A7`, arguments `[]`.
- Scripts/C20.cmb scene 75, `0x28F2`, arguments `[]`.
- Scripts/C20.cmb scene 76, `0x2962`, arguments `[]`.
- Scripts/C20.cmb scene 105, `0x3DFC`, arguments `[]`.
- Scripts/C21.cmb scene 21, `0x19DE`, arguments `[]`.
- Scripts/C21.cmb scene 51, `0x2B07`, arguments `[]`.
- Scripts/C22.cmb scene 30, `0x1D76`, arguments `[]`.
- Scripts/C22.cmb scene 64, `0x3714`, arguments `[]`.
- Scripts/C23.cmb scene 25, `0x18C2`, arguments `[]`.
- Scripts/C23.cmb scene 26, `0x1CDB`, arguments `[]`.
- Scripts/C23.cmb scene 46, `0x2CA0`, arguments `[]`.
- Scripts/C24.cmb scene 33, `0x1992`, arguments `[]`.
- Scripts/C24.cmb scene 62, `0x2ED8`, arguments `[]`.
- Scripts/C25.cmb scene 24, `0x1F76`, arguments `[]`.
- Scripts/C25.cmb scene 24, `0x20C1`, arguments `[]`.
- Scripts/C25.cmb scene 25, `0x2523`, arguments `[]`.
- Scripts/C25.cmb scene 25, `0x2530`, arguments `[]`.
- Scripts/C25.cmb scene 56, `0x372F`, arguments `[]`.
- Scripts/C25.cmb scene 56, `0x3C9F`, arguments `[]`.
- Scripts/C26.cmb scene 38, `0x1E4E`, arguments `[]`.
- Scripts/C26.cmb scene 69, `0x303E`, arguments `[]`.
- Scripts/C26.cmb scene 69, `0x3689`, arguments `[]`.
- Scripts/C27.cmb scene 11, `0x126A`, arguments `[]`.
- Scripts/C27.cmb scene 35, `0x22FF`, arguments `[]`.
- Scripts/C28.cmb scene 26, `0x16AE`, arguments `[]`.
- Scripts/C28.cmb scene 27, `0x19BA`, arguments `[]`.
- Scripts/C28.cmb scene 27, `0x1BDA`, arguments `[]`.
- Scripts/C28.cmb scene 40, `0x292E`, arguments `[]`.
- Scripts/C29.cmb scene 6, `0xE74`, arguments `[]`.
- Scripts/C29.cmb scene 7, `0x136A`, arguments `[]`.
- Scripts/C29.cmb scene 17, `0x2980`, arguments `[]`.
- Scripts/C30.cmb scene 18, `0x161E`, arguments `[]`.
- Scripts/C30.cmb scene 19, `0x18CE`, arguments `[]`.
- Scripts/C30.cmb scene 19, `0x1A94`, arguments `[]`.
- Scripts/C30.cmb scene 41, `0x2AE2`, arguments `[]`.
- Scripts/C30.cmb scene 41, `0x2B8A`, arguments `[]`.
- Scripts/C31.cmb scene 14, `0x29E2`, arguments `[]`.
- Scripts/C31.cmb scene 15, `0x2FAE`, arguments `[]`.
- Scripts/C31.cmb scene 58, `0x55B5`, arguments `[]`.
- Scripts/C31.cmb scene 58, `0x5B4F`, arguments `[]`.
- Scripts/C31.cmb scene 58, `0x5B59`, arguments `[]`.
- Scripts/C31.cmb scene 67, `0x7DEB`, arguments `[]`.
- Scripts/C31.cmb scene 67, `0x7DF5`, arguments `[]`.
- Scripts/C31.cmb scene 67, `0x7F61`, arguments `[]`.
- Scripts/C31.cmb scene 67, `0x8202`, arguments `[]`.
- Scripts/C31.cmb scene 67, `0x820C`, arguments `[]`.
- Scripts/C31.cmb scene 67, `0x8426`, arguments `[]`.
- Scripts/C91.cmb scene 23, `0xB03`, arguments `[]`.
- Scripts/C92.cmb scene 15, `0xA5B`, arguments `[]`.
- Scripts/C93.cmb scene 16, `0xCE3`, arguments `[]`.
- Scripts/C94.cmb scene 16, `0x92B`, arguments `[]`.
- Scripts/C95.cmb scene 13, `0xBD7`, arguments `[]`.
- Scripts/C96.cmb scene 14, `0xA6B`, arguments `[]`.

### DefaultEscapeTalk

- Scripts/C07.cmb scene 1, `0xE40`, arguments `[]`.
- Scripts/C11.cmb scene 5, `0x1598`, arguments `[]`.

### PlayerDeadCheck

No direct aligned call in the scanned script containers.

### EnemyDeadCheck

No direct aligned call in the scanned script containers.

### GetDiedPlayerCount

No direct aligned call in the scanned script containers.

### UnitDead

- Scripts/C03.cmb scene 19, `0x2338`, arguments `[None]`.
- Scripts/C09.cmb scene 28, `0x2B8C`, arguments `[None]`.
- Scripts/C09.cmb scene 31, `0x36AE`, arguments `[None]`.
- Scripts/C26.cmb scene 69, `0x353C`, arguments `[None]`.
- Scripts/C26.cmb scene 69, `0x3543`, arguments `[None]`.
- Scripts/C26.cmb scene 69, `0x354A`, arguments `[None]`.
- Scripts/C26.cmb scene 69, `0x3551`, arguments `[None]`.
- Scripts/C26.cmb scene 69, `0x3558`, arguments `[None]`.

## Unresolved named calls

These names lack a recovered literal native registration. They may be imported script helpers or other resolver entries; they are not assumed missing or unused.

| Name | Call sites |
|---|---:|
| AllUnitsBreakup | 3 |
| BgmChangeEvt_MapToEvt1 | 6 |
| BgmChangeEvt_MapToEvt2 | 16 |
| BgmContEvt_EvtToMap1 | 19 |
| BgmContEvt_EvtToMap2 | 1 |
| DisposContinueSetMode | 4 |
| DisposSetMode | 106 |
| Dispos_ForEvent | 2 |
| Dispos_ForEventSenerio | 22 |
| Dispos_ForEventTiamat | 10 |
| ENVNoisyOn_WhenNotEvtSkip | 4 |
| Easy | 1 |
| FadeWait | 879 |
| FocusBetweenAB | 2 |
| ForceCheckAnyoneDead | 1 |
| InstantDisposFirstSetMode | 8 |
| InstantDisposSetMode | 33 |
| InstantUnitFocusByPID | 100 |
| InstantUnitFocusOffsetByPID | 27 |
| LocalDieTalkWithBgmChange | 22 |
| MapFree | 147 |
| MindGetItem | 76 |
| NormalOnly | 6 |
| PreLoadWait | 5 |
| RegistLocationTT | 1 |
| SoundBossTalkEnd | 256 |
| SoundBossTalkStart | 301 |
| Startup | 3 |
| TrialAddUnit | 6 |
| TutBasesCreate | 1 |
| TutBasesDelete | 1 |
| TutPadActor | 387 |
| TutSallyCreate | 1 |
| TutTalkEvent | 375 |
| TutTalkResume | 150 |
| TutWaitF | 476 |
| TutWaitForNextTaiki | 32 |
| TutWaitForNextTurnAfter | 13 |
| TutorialDialog | 50 |
| TutorialIn | 21 |
| TutorialInit | 51 |
| TutorialOut | 51 |
| TutorialResumeOut | 21 |
| Tutorial_FadeIn | 71 |
| Tutorial_FadeOut | 21 |
| UnitAnimByPID | 140 |
| UnitAnimFByPID | 53 |
| UnitCheckDeadHereByPID | 13 |
| UnitCheckExists | 4 |
| UnitCheckExistsByPID | 181 |
| UnitCheckExistsByPID2 | 6 |
| UnitCheckLinked_Breakup | 1 |
| UnitCheckLiveByPID | 447 |
| UnitDontMoveSallyByPID | 34 |
| UnitEscapeByPID | 351 |
| UnitFocusByPID | 60 |
| UnitFocusOffsetByPID | 2 |
| UnitForcedSallyByPID | 56 |
| UnitGetItemShowing | 8 |
| UnitGetItemShowingSub | 8 |
| UnitGetXByPID | 59 |
| UnitGetYByPID | 47 |
| UnitItemSendToHouseByPID | 1 |
| UnitMoveDirByPID | 411 |
| UnitMovePosByPID | 146 |
| UnitQueryJIDByPID | 1 |
| UnitRotateByPID | 672 |
| UnitRotateToPos | 20 |
| UnitRotateToPosByPID | 4 |
| UnitRotateToUnit | 6 |
| UnitRotateToUnitByPID | 78 |
| UnitSetCpTypeByPID | 9 |
| UnitSetPosDir | 41 |
| UnitSetPosDirByPID | 471 |
| UnitSetPosDirByPos | 10 |
| UnitSetWeaponAwayByPID | 4 |
| UnitTransferToForceByPID | 67 |
