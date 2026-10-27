# Research Log — FE9 (Path of Radiance) Two-Army Co-op

Reverse-engineering findings, with source and confidence for each.
All addresses are for **GFEE01 rev 0** (NTSC-U) with `main.dol` SHA-1
`9d00d7d407750b82cb1cfccc56f8aa8a89cc8851` unless marked otherwise.
`python -m tools.check_signatures` re-checks every static claim marked **[S]**.

Confidence labels:
- **VERIFIED-STATIC**: read directly from our own disassembly or data dump (reproducible by script).
- **VERIFIED-RUNTIME**: observed in Dolphin with a recorded test (see TESTING.md).
- **CORROBORATED**: an independent community source agrees with our static reading.
- **HYPOTHESIS**: an inference that is not yet tested.

---

## 0. Environment facts

| Item | Value | Confidence |
|---|---|---|
| Image | `Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso` | VERIFIED |
| Game ID / revision | GFEE01 / rev 0, internal name `FIRE EMBLEM GC US`, region NTSC-U | VERIFIED (DolphinTool `header` and `tools/verify_game.py`) |
| Image file (.ciso as stored) | size 1304461888, CRC32 `0b60d750`, MD5 `f9d17c23af18cf41ac2de80c1459b31f`, SHA-1 `dcb8af21a5708bd890cffa26c961e58da7cb31e4` | VERIFIED |
| DolphinTool `verify` (logical disc data) | CRC32 `f2b3410f`, SHA-1 `a30eca376ab9b2b4dd8b1a9136772a62c0309ace`; "format does not store disc size" (low severity) | VERIFIED |
| main.dol | 2776512 bytes, SHA-1 `9d00d7d407750b82cb1cfccc56f8aa8a89cc8851`, CRC32 `99623932` | VERIFIED |
| Redump match | **Cannot be checked.** CISO drops unused blocks (including the disc's junk padding), so the full-disc Redump hash cannot be rebuilt. `main.dol` is our build anchor. | — |
| Dolphin | Portable build (`portable.txt` present), binary built 2026-10-07, string `Dolphin 2609a` in exe. `User/` is created on first launch. | VERIFIED (version string: confirm via Help > About) |
| Python | 3.12.6; `capstone` 5.0.7 in `.venv` | VERIFIED |

## 1. What each community resource actually demonstrates

| Resource | What it demonstrates | What it does NOT do |
|---|---|---|
| [FE9 Character Editor & Randomizer](https://github.com/jespoketheepic/FE9-Character-Editor-and-Randomizer) (Java) | Edits `system.cmp` character data and `zmap/*/dispos.cmp` classes/items. Documents the dispos entry size (0x6C) and offsets of PID/JID/items/coords. Its `resources/Dispos.txt` shows Lethe and Mordecai in `bmap10`. | No faction, AI or runtime work. Nothing about multiplayer. |
| [fe9-game-data-patcher](https://github.com/emilybrooks/fe9-game-data-patcher) (Python + C) | `pack` archive reader/writer, LZ77 (type 0x10) codec, `FE8Data.bin` tables (units 0x54, classes, items, skills). | Data only. Nothing about control or turns. |
| [Serenes Forest AR thread](https://forums.serenesforest.net/topic/96167-fe9-about-ar-codes-and-memory-editing/) | **Not read.** The server returned HTTP 403 to automated fetches. | Needs a manual read (see PROGRESS.md blockers). |
| [FEU "FE9 file structure notes"](https://feuniverse.us/t/fe9-file-structure-notes/5020) | pack and dispos container layout, character table layout. | Says outright that the dispos "entry type" bytes are not decoded. |
| [gc-forever PAL code thread](https://www.gc-forever.com/forums/viewtopic.php?t=2203) (Ralf) | PAL (GFEP01) "Transform unit into player-controlled" and "Unit Control Roller". Our decoding: they hook PAL `0x80029824` (`lwz r3,0x190(r3)`), then rewrite `unit+0x190` to one of 4 force structs at PAL `0x802D4744 + 0xC*n`, using `force+8` as the index. Pad state at PAL `0x802F98E8` (held) and `0x802F9926` (pressed). | Changes *who a unit belongs to*. It does not add a separately controlled army. The author warns it can break missions. |
| [WiiRd GFEE01 thread](https://wiird.gamehacking.org/forum/index.php?topic=4593.0) (Crapulecorp ports) | "Make everyone player-controlled": writes byte `force+8` for forces 1..3 through a pointer. "Enemies player-controlled but not on your team": writes the phase byte (PAL `0x8033A719`). | The ports reuse the **PAL** pad address `0x802F98E8`, so they are probably not true US codes. Not verified on our build. |
| Dolphin `GameSettings/GFEE01.ini` (bundled) | US Ike stat codes at `0x802B168C..` (HP etc.). | Stat cheats only. |
| [Dolphin NetPlayClient.cpp](https://github.com/dolphin-emu/dolphin/blob/master/Source/Core/Core/NetPlayClient.cpp) | Netplay is lock-step input sharing; see section 5. | — |

No FE9 decompilation or symbol map was found.

## 2. Data formats (VERIFIED-STATIC)

- **.cmp** = Nintendo LZ77 type 0x10 (`10 <size24 LE>` + flag-byte blocks) wrapping a `pack` archive.
  Implementation: `tools/fe9/lz77.py`, `tools/fe9/pack.py` (round-trip tested on a real file).
- **pack**: `'pack'`, u16 count, then 0x10-byte records `(0, name ptr, start, length)`, big endian.
- **dispos_X.bin** (one per difficulty variant: `c` common, `h`, `m`, `n`) is a relocatable data file:
  `u32 size, u32 data size, u32 reloc count, u32 symbol count`, data at 0x20 (pointers relative to 0x20),
  then the reloc table, the symbol table `(offset, name offset)`, and names.
  Each symbol except `*_date_*` is a **unit group**: `u8 count, u8[3] unknown`, then 0x6C-byte entries.
  Parser: `tools/fe9/dispos.py`; CLI: `python -m tools.dump_dispos <dispos.cmp> --variant n --raw`.
- **Dispos entry** (0x6C): 0x00 PID, 0x04 JID, 0x0C..0x28 4 weapons + 4 items (IID pointers),
  0x4C..0x58 four AI pointers (observed names `SEQ_*` ×3 then `MTYPE_*`), 0x5C start XY, 0x5E end XY,
  **0x60 = level? (HYPOTHESIS)**, **0x61 = force index (VERIFIED-STATIC, see F-02)**.

## 3. Chapter 9 ("Gallia") = `zmap/bmap10`

`dispos_n.bin`, group `bmap10_m01_n`: **PID_MORDY** (JID_BEAST_T) at (23,18) and **PID_LETHE**
(JID_BEAST_C/F) at (22,18). AI = `SEQ_ALLUNITATTACK100, SEQ_NEARESTUNITMOVE, SEQ_NOHEAL, MTYPE_NORMAL`.
The same two units appear in the `c`/`h` variants (group `m05` in `c`).
The `c` file also has green NPC/event units: Mist, Rhys/Lofa, Marcia, and `*_EV` event actors.

## 4. Faction model (the core of Phase 1)

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-01 | **Unit table** at `0x802B14E4`, stride `0x280`, unit ids 1..0x9F (159). `unit+0x188 != 0` means the slot is in use. | Loops at `0x800295C4`, `0x800162DC` **[S]**. Consistent with the bundled US Ike HP code `0x802B168C` = unit1 + 0x1A8. | VERIFIED-STATIC |
| F-02 | **Force index comes from the dispos entry byte +0x61.** Ike, Oscar, etc. = 0. Every Daein enemy = 1. Mist, Marcia and event actors = 2. **Lethe and Mordecai = 3.** | `tools.dump_dispos` on all variants of bmap10. `tests/test_tools.py::test_chapter9_partner_units`. | VERIFIED-STATIC (data). The link to the runtime index is HYPOTHESIS: the loader reads a byte through `0x8017A9DC` (a byte-stream reader) and uses it as the force index at `0x8003C894`. |
| F-03 | **Force table** at `0x802CA264`, 0xC bytes per force. `force+0` = head of a unit linked list (next = `unit+0x184`), `force+8` = force id byte. The loader sets `unit->force = 0x802CA264 + 0xC*index` via setter `0x8003B6C4` (`stw r4,0x190(r3)`). | `0x8003C88C..0x8003C8A8` **[S]**. Structure matches Ralf's PAL roller (`0x802D4744 + 0xC*n`, id at +8). | VERIFIED-STATIC + CORROBORATED |
| F-04 | **Battle-map state block** at `0x80330708`. `+0x10` = chapter? (HYPOTHESIS). **`+0x11` = current phase (force id)**. `+0x12` (u16) = turn number. | Map init `0x8014D920` writes phase=0, turn=1 **[S]**. The phase is used as the force index across turn code (`0x8002E5E8`, `0x800AE3F8`). Crapulecorp's PAL code writes `0x8033A719` = PAL state+0x11. | VERIFIED-STATIC + CORROBORATED |
| F-05 | **Per-force control mode at `0x8033071C + force`** (state+0x14). Map init writes `{1, 2, 2, 2}`: force 0 = 1, forces 1–3 = 2. Code treats **1 as human-driven**: at `0x8002E754`, if `control[phase]==1` it starts process `0x80284AC8`. At `0x80028548` / `0x80028578`, the cursor classifier lets a **force-2/force-3 unit be selected like an own unit when `phase == force` and `control[force] == 1`**. 0 seems to mean "phase inactive" (`0x8002E6A4`). **So `0x8033071F` controls whether the yellow partner phase is CPU (2) or human (1).** | **[S]** signatures at `0x8014D960..6C`, `0x80028548`, `0x80028578`, `0x8002E754`. | VERIFIED-STATIC. Runtime effect untested (EXP-01). |
| F-06 | **Force relations** (`0x80015320`, mask builder): same force = 0. Any pair involving force 1 = hostile (1). Forces 0, 2 and 3 are mutual allies (2). Query 0 = current phase force only; query 3 = forces 0–3. | Disassembly of `0x80015320`. | VERIFIED-STATIC |
| F-07 | Cursor/unit-info classification (`0x80029664`) writes a code to `0x80330C25` (state+0x51D): force 0 → 3, force 1 → 5/6, force 2 → 8, force 3 → 7. This is the US counterpart of Ralf's PAL hook site `0x80029824` (US `0x80029684`). | **[S]** | VERIFIED-STATIC |
| F-08 | `unit+0x1A0` = status flags. bit0 is checked in the selection classifier. Bit 0x4 is checked by `0x800AE3DC` while scanning for units that have not acted (HYPOTHESIS: "has moved/acted"). `unit+0x19E/0x19F` = map X/Y (HYPOTHESIS, used as coords in cursor code). | Disassembly. | HYPOTHESIS for the meanings |

### Runtime confirmation (2026-10-27, Prologue save state, decoded with `tools/inspect_state.py`)
- Control bytes `01 02 02 02`, phase 0, turn 1 → F-04/F-05 initial values **VERIFIED-RUNTIME**.
- Force table: `force+8` = 0..7 for forces 0..7. `force+0` = first unit, `force+4` = last unit (HYPOTHESIS: list tail). Every unit's `+0x190` points at the right force → F-03 **VERIFIED-RUNTIME**.
- Unit table decodes: `unit+0x188` → character record whose first word is a PID string pointer. `unit+0x18C` → class record (first word = JID pointer). `+0x19E/+0x19F` = x/y and `+0x1A8` = current HP are consistent with the scene (Ike HP 19 at (3,9)). → F-01 **VERIFIED-RUNTIME**; F-08 x/y **VERIFIED-RUNTIME**.
- `state+0x10` = 1 in the Prologue. This matches the JP chapter numbering (Prologue 0x01, Ch9 0x0A) → "chapter id" upgraded to **CORROBORATED**. Its role as next-chapter source is tested by EXP-03.
- Dolphin save-state format (State.h, v192): see `tools/fe9/savestate.py`. MEM1 sits at payload offset `0x8B8353` in this Dolphin 2609a state, found by code-anchor search, so we don't depend on a fixed offset.

### Turn loop and chapters (2026-10-27)

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-09 | **Phase order 0 → 3 → 1 → 2 → 0** (turn+1 when wrapping from 2). The partner phase directly follows the player phase. | `0x8014D3B4` **[S]** | VERIFIED-STATIC |
| F-10 | The turn loop is a bytecode "proc" script in `.data` around `0x80284E40`. Ops look like `(u16 arg, u16 op)`: `0x200F` = call function (pointer follows), `0x2012` = call with yield, `0x1001` = label, `0x100C` = goto, `0x100A` = yield, `0x120B`/`0x1206` = conditionals (semantics HYPOTHESIS). Steps include `0x8002E738` (control[phase]==1 → start human proc `0x80284AC8`) **[S]**, `0x8002E670` (phase end), `0x8002E648` (advance phase). | data dump, xrefs | Layout HYPOTHESIS; handler roles VERIFIED-STATIC |
| F-11 | Some rule skips a phase. In the Prologue the green phase never appeared even with control[2]=1 (slot 5: turn reached 2). The rule isn't decoded; likely candidates are the proc conditionals or "no unit able to act". | EXP-02 | HYPOTHESIS |
| F-12 | **Chapter id = `state+0x10`; id N loads `zmap/bmap0N`** (Prologue = 1, Chapter 2 = 3, so Chapter 9 = 10). `SetChapter` = `0x8014D2B0` (old id → `state+0x51E`) **[S]**, called from `0x80005F6C`, `0x8002E234`, `0x8002E3B8`, `0x800AA0E8` (script library), `0x801D8804`, `0x801F8994`. Changing the id mid-battle does not choose the next chapter (EXP-03 failed). | slot 1 (id 1), slot 7 (id 3, bmap03 units, prev 2) | VERIFIED-RUNTIME (mapping) |
| F-13 | The state block is serialised in save data: `0x8014C1B8` reads chapter, phase, turn and **all four control bytes** from the save stream. A battle save can therefore carry a human-controlled yellow army across save/load, which helps Phase 4. | disassembly | VERIFIED-STATIC |
| F-14 | Script-library accessors (likely `.cmb` commands): `0x800BCC04` get phase, `0x800BCC14` set phase, `0x800BCC24` get turn, `0x800BCC34` set turn. | disassembly | VERIFIED-STATIC (role as script commands: HYPOTHESIS) |

### Implication

FE9 already models four forces with an explicit per-force **human/CPU control byte**. The selection code already contains the branches that let a non-player force be driven by a human during its own phase. The smallest Phase 1 lever is therefore one byte, not new selection or menu code: `0x8033071F := 1`.
Whether the rest of the turn loop (action menu, "End" command, phase transitions, combat forecast) respects it is unknown. EXP-01 tests exactly that.

## 5. Dolphin input and Netplay architecture (from source, `NetPlayClient.cpp`, master)

- **Lock-step input sharing**: each client polls its local pads (`PollLocalPad`) and sends `PadData`. Every client blocks in `GetNetPads()` until it has every port's input for the frame. Emulation must be deterministic. Nothing but inputs is exchanged during play (plus a timebase sync every 60 frames).
- **Port ownership**: the host's `pad_map` assigns each GameCube port to one player. `InGamePadToLocalPad` maps a player's local controller to their assigned port(s). So **player 2 can own port 2** while player 1 owns port 1. The game must then read port 2 for the yellow army, which FE9 does not do natively (Phase 2 work).
- **Codes**: the host's AR/Gecko codes are pushed to clients (`SyncCodes`, `NotifyGecko`/`NotifyAR`), so our patch can ship as host-side codes. Both sides must run the identical game build.
- **Saves**: GC memory cards/GCI folders are synced from host (`SyncSaveData*`). With "load"/"write" options.
- **Desync**: the client handles `DesyncDetected(frame, player)` from the server. The hashing mechanism is not in this file (TODO: read `NetPlayServer.cpp`).
- **Host input authority / Golf mode**: only the "golfer" drives inputs, and control can pass between players. This is a possible no-code fallback for strictly alternating turns (HYPOTHESIS, untested).

## 6. Open questions

1. EXP-01 runtime behaviour (see TESTING.md).
2. Which proc is `0x80284AC8` (human phase loop?), and does it hard-code force 0 anywhere (e.g. the End-turn menu, "all units moved" auto-end, phase banner)?
3. Where does FE9 read controller input (US equivalent of PAL `0x802F98E8`)? Needed for Phase 2. Plan: Dolphin memory search for the button halfword, or Dolphin's built-in SDK signature DB to name `PADRead`.
4. Is state+0x10 the chapter number? The JP warp codes write JP `0x8032E798` = JP state+0x10, which suggests yes.
5. Does the battle save or suspend data store `control[]`? If not, it is re-initialised on load (so the code must be re-applied, which a per-frame AR write does).
