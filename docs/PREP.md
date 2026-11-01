# Preparation-screen drafting and deployment: integration plan (PREP-01, Milestone A)

Branch `draft-ownership`. Built on the verified EXP-21 storage and EXP-22 draft (DRAFT-01 passed). EXP-23 (draft v2) is **not runtime-verified** (DRAFT-02 has no result yet), so nothing here depends on it.

Labels: **[S]** = static, from disassembly and pinned in `tools/check_signatures.py`; **[R]** = seen at runtime; **[H]** = hypothesis.

## 1. What the original game does

| # | Question | Finding | Evidence |
|---|---|---|---|
| 1 | Prep screen and roster | Preparations show the sortie list **`E_SallyList`** (proc header `0x80291088`, "Pick Units"). It uses the shared unit-list module of `window/butai_en.cmp`, the same list builder **`0x8012DFA8`** that EXP-18 already extends for Base Data. The list's per-frame input step is `0x8012D6A4`. The formation step on the map is **`BMapSallyProc` / `BMapSallyCursorProc`** (`E_SallyToken`, `RestoreSallyDisposition`, `FinalDisposition`, help messages `MESS_SALLY_HELP01…05`, confirm `MESS_CONFIRM_EXIT_SALLY`). | [S] F-57 |
| 2 | Selecting / removing a unit (**corrected by F-62:** Choose Units' A = `0x80117D80`, benched = flag group `0x010000DC`, battle start sends benched units to force 5; `0x80000000` is the per-unit animation setting) | The list's action callback **`0x8012C9E8`** flips **bit `0x80000000` of `unit+0x1A0`** (`xoris r0,r0,0x8000`) and returns 1. It is installed by `0x8012C9C0` in list mode 4 (`obj+0x54`, `obj+0x6C` = 4). So "picked for this battle" is a unit flag. It doesn't touch the ownership bits 0x20000000/0x40000000/0x10000000 (F-52). | [S] F-57 |
| 3 | Deployment cap | `SallySetByGroup(bmapNN_mikata_X)` → `0x8014CF48` sets **`state+0x544` = 0**, then stores one (x, y) slot per entry of the chapter's `mikata` group at `state+0x545 + 2·i`. Cap = slot count. At runtime, Ch6 prep has `state+0x544` = 6 = its 6 entries. `SallyGetSurplus` returns `state+0x56`. Caps per chapter and difficulty file: docs/CHAPTER_AUDIT.md. | [S] + [R] (Ch6) F-56 |
| 4 | Forced deployments | `UnitForcedSally[ByPID]` sets the `0x10000` flag (F-41). The list shows such rows in state `0x13` (`0x8012F098`). **Ch3–Ch7 force nearly everyone. From Ch8 (script C09) on, only Ike is forced**, except Ch26 (Elincia) and Ch30 (Ena, Nasir). | [S] audit |
| 5 | Unavailable characters | Away units sit in force 7 with flag `0x10` (Ch6 prep: Shinon, Gatrie). The list maps `0x10` to row state 0 and `0x200000` to state 3 (`0x8012F060`/`0x8012F680`). Story transfers (F-48) decide availability; ownership bits ride along untouched. | [S] + [R] (Ch6) |
| 6 | Prep → battle | Map start (`0x8002EA10`) clears `0x4400` and sets `0x400` on force 0 units (`0x8002EA48`). EXP-21 then moves Player-2-owned force 0 units to force 3 at the first blue-phase start (`0x8002E738`). Which list step turns the sortie bit into force 0 placement is **not traced yet**. | [S] partly |
| 7 | Input in prep | The list reads the **current-pad pointer** (`0x8012D6B8`: `lwz r4,-0x7b60(r13)`, F-29). In preparations the phase is 0, so EXP-14 keeps it on port 1, and only Player 1 drives the native list today. Raw `PADStatus[0..1]` (`0x802EF408`) are readable for both ports at any time. | [S] |
| 8 | Ownership through roster moves, chapters and saves | The flag word is saved raw (F-52). DRAFT-01 passed for a chapter transition, a save and a fresh reload. Benching = clearing `0x80000000`; it leaves the ownership bits alone. | [S] + [R] |

**Found by PREP-R1 (F-58):**
- The list object is the `E_SallyList` proc instance. Its fields: `+0x38` columns, `+0x3C` rows (unit pointer at +0, 0x24 each), `+0x61` row count, **`+0x62` highlighted row**, `+0x6C` mode.
- The cell colour is an index into the native palette `0x80296088` (0 grey, 1 white, 0x13 green, 0x21 light blue, 0x06 yellow).
- Picked units do **not** carry `0x80000000`, so it likely means *benched*.
- The campaign is on Normal difficulty (dispos file `n`).

**Still to be found:** where the sortie flag becomes force 0 placement at battle start, and which difficulty uses file `c`.

## 2. Test chapter

A genuine choice needs the roster to be bigger than the optional slots (cap − forced).
- **Ch8 (id 9): cap 7, only Ike forced.** This is the first chapter that isn't a forced line-up. Its roster may still fit the cap; that is checked when the prep screen opens (`state+0x544` against the force 0/5 units).
- **Ch10 (id 11): cap 11 (8 on file `c`)**, with Lethe and Mordecai joining. This is the first likely real bench, but the chapter also has the Kieran/Nephenee/Brom temporary partners (risk 4).

Plan: test Pick Units *mechanics* on the first reachable prep screen (Ch8), and *fairness with a bench* on the first chapter where the roster exceeds the cap. A Ch8 prep save needs Ch6 and Ch7 played from the existing Ch6 card file; DBG-01 makes that quick. **Fixture rule:** if a bench is needed earlier, a lowered cap in a save state is a test fixture only, labelled as such, never proof.

## 3. Integration plan (small steps, each with a TESTING.md entry)

| Step | What | Hook / data | Risk |
|---|---|---|---|
| 2 | **Show ownership in Pick Units**: blue / yellow / unassigned / unavailable | **EXP-25 v2, PASSED (PREP-02):** name-column colour from ownership at the cell draw `0x8012F0D4`. Light blue = Player 1 and Ike, yellow = Player 2; unassigned and grey (unavailable) unchanged. Also shows in the battle Unit list. | Low: display only |
| 3 | **Assign in prep** (**EXP-26, PASSED: PREP-03**): Z on your own pad on the highlighted row: claim on your pick, release, request a transfer (orange), the owner accepts | Hook the list input step `0x8012D6A4`. On a dedicated button (Y, or the EXP-22 L+R on the owner's own pad, read raw from PADStatus), take the row's unit (`*(*(list+0x3C) + list[+0x62]·0x24)`, F-58) and apply EXP-22's claim/release rules. **Whose pick:** shown in the list's help line (`MESS_LIST_SALLY*` / `MESS_SALLY_HELP*`), not only by sound; this needs the message lookup (F-54). **Transfer:** the owner offers (release to "offered"), the other player accepts on their own pad. A spare bit (0x08000000, unused per F-52) can mark "offered". | Medium: new input in a native menu |
| 4 | **Persist into battle and through save/reload** | Already provided by EXP-21 + F-52; verify with prep-made assignments. | Low |
| 5 | **Fair deployment under the cap** (**v0 built in EXP-27, DEPLOY-01 pending:** each player toggles only their own characters; Player 1 by the native A, Player 2 by A on their own pad; split by agreement, no quota yet) | Wrap the toggle callback `0x8012C9E8`. Count the sortie bits per owner against `state+0x544` minus forced. The press must come from the owner's own pad (raw PADStatus edge). Allow selecting only while that owner has fewer than ⌈optional / 2⌉ picked, unless the other player passes (leaves a slot, e.g. "Start on your pad to yield"). The native cap check stays authoritative; nothing raises it. | Medium |
| 6 | **Confirmation** | Before Fight: both players press Start on their own pad (a "ready" bit per player, kept in the code's data word). Until both are ready, Fight plays the refusal sound. This replaces "the draft ends at the first action". The in-battle draft (EXP-22) stays a fallback for chapters without preparations. Nothing may be left in force 2: EXP-23's parking is not used in prep. | Medium |
| 7 | **Netplay**: two instances, then two PCs | Everything is game memory + synced pads | Low (by design) |

**Input under Netplay:** Netplay syncs both pads, so reading PADStatus[1] in prep is deterministic on both machines. The native list keeps following the current pad (port 1). Player 2's actions are attributed by which raw pad pressed the button. If Player 2 must move the list cursor, the current-pad pointer can be retargeted to port 2 while it's Player 2's pick (EXP-14's mechanism). This is sequential, as the brief allows.

## 4. Risks
00. **Benched rows are grey (F-62):** the bench group includes `0x10`, so the list draws benched characters grey, and EXP-25 leaves grey unchanged. A benched character shows *benched* but not its *owner*. Step 5 should give benched owned rows a dimmed owner colour (e.g. palette `0x09` blue / `0x0D` yellow) so ownership and deployment are both visible. The drafts still let players claim benched characters (they only refuse force 7).
0. **Gecko space (F-59):** ≈ 3248 bytes for every enabled code. The prep codes must stay compact. A later package of COOP-P6 + EXP-21 + EXP-25 + EXP-26 + the deployment code needs every cave slimmed or a payload loader.
1. **Story availability:** force 7 / `0x10` units must stay unselectable whatever they own (`0x8012F060`'s order is preserved).
2. **Forced units:** owner and deployment rules count them first. A forced Player 2 unit deploys and becomes yellow (EXP-21), as in DRAFT-01.
3. **Chapters without preparations:** the in-battle draft remains for them.
4. **Ch10 temporary partners and native partners** are not in the player roster (force 3 without OWNED, F-52), so the prep list never offers them.
5. **Messages:** a whose-pick line needs a hook in the message lookup. Until then, help-line changes are out and the row states plus sounds carry the information.
6. **Suspend at prep:** prep state is in the battle save. Ready bits kept in code memory would reset on reload, which is safe: both confirm again.

## 5. Fairness, benched-owner visibility and readiness (design, 2026-11-01)

Status: DEPLOY-01 passed, so deployment by owner (Step 5 v0) works on a real Ch8 prep screen. The full package set is **3184 of 3256 bytes (72 free)**; the test aid DBG-01 takes 56 of those. Estimates below are **[H]** until built and simulated.

| Option | What it does | Hook / data | Est. bytes | Notes |
|---|---|---|---|---|
| **A. Agreement (current v0)** | Each player toggles only their own characters; the native cap ("You can select N more") limits the total; players agree on the split | EXP-27 wrapper on `0x80117D80` | 0 (built) | Verified (DEPLOY-01). Fair enough for two friends talking. The weak spot is the race: whoever deploys first fills the slots. |
| **B. Fair-slot quota** | Deploying is refused (buzz) while that owner already has ⌈(cap − forced) / 2⌉ deployed, unless the other owner has nothing left to deploy | Same wrapper; count deployed (no `0x010000DC` bits) per owner over force 0 by reusing the core's table-driven count; cap = `state+0x544`, forced = `0x10000` | 72–96 | Doesn't fit next to DBG-01; fits only without it, and only if ≤ 72. Odd cap: the extra slot goes to whoever asks first. Unassigned characters count for nobody. |
| **C. Dimmed owner colour on benched rows** | A benched owned character shows dim blue or dim yellow instead of plain grey (risk 00, seen at runtime) | EXP-25: if the chosen index is 0 (grey) and the unit is owned, use a dim index | 16–24 | Palette indices `0x09` / `0x0D` are **unverified [H]**: check the colours in `0x80296088` first. |
| **D. Readiness (PREP-06)** | Fight is refused until both players pressed Start on their own pad (one ready bit each in the EXP-27 data word; any change in Choose Units clears both) | Needs the "Begin now?" / Fight entry (**not traced yet**) + an edge reader for both pads' Start | 80–120 + 8 header | Biggest; needs research first. A reload resets the bits harmlessly (risk 6). |

**Recommendation:**
1. Keep **A** as the default. It is verified and costs nothing.
2. Build **C** next. It's small and fixes a visibility gap seen at runtime.
3. Make **B** optional: the code stays in the ini but isn't in the package, so it never uses package bytes.
4. **D** needs both research (the Fight confirm) and space.

**Making space (any of these, in order of risk):**
1. Leave DBG-01 out of every package (already the rule): 72 bytes free.
2. Compact COOP-P6 (1328 bytes). Its EXP-06 ownership caves are 13 near-identical 6-line blocks (`GetUnitSelectState` and friends). One shared routine with cross-block calls (F-60, as done for EXP-21 v3) could save about 300–400 bytes **[H]**. It is the verified release core, so it would need the full COOP regression (EXP-06/07/10–14/17/20) again.
3. Move code out of the Gecko area: Dolphin `[OnFrame]` patches or a patched DOL. Whether Netplay syncs `[OnFrame]` patches the way it syncs Gecko codes is **unknown** (research first). A patched DOL needs a distribution step for both players.
