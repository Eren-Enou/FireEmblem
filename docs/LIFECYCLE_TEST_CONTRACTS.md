# Native lifecycle and stage verification contracts

Offline checkpoint only. No new Dolphin execution is claimed. The existing
Oscar/Kieran Talk captures remain accepted; escape, cleanup, recruitment and
save/reload are separate questions. No new exit fixture was generated because
rescue behavior, geometry and combined Gecko allocation have not been established.

## Expected transitions and limits

| Original operation | Evidence-backed result | Remaining uncertainty |
|---|---|---|
| Force-list append/prepend to0..4 | clear low flags0x18 | surrounding refresh/secondary-byte effects |
| Append/prepend to5 | set0x10, clear0x8 | permanent joining/save history |
| Append/prepend to6 | set0x8 | original death worker and0x8000 marking are separate |
| No-rescue Blue Escape | move to5, escaped0x4000 | map detach, transitive native effects |
| No-rescue non-Blue Escape | uninitialize identity/flags/level/EXP/HP, append free4 | item-clear worker details |
| Fixed-owned Yellow Escape/cleanup | existing EXP-16 first returns matching force3 to0 | carried partner and full native cleanup |
| Temporary Yellow or Green at active cleanup | remaining non-Blue disposal in projection | original script must recruit/retain it first |
| C11 prisoner direct Escape | original script sets escape key, transfers0 before native worker | original menu/route and full ending/save |
| C11 closed-door Talk without Escape | force3/key changes alone do not satisfy fallback | projected disposal is not a reproduced runtime defect |
| C11 non-Maniac opened-door/unescaped fallback | original helper accepts Green/Yellow, transfer0 before cleanup | later ending/permanent roster/native reload |
| C11 Maniac fallback | skipped; separate escape path matters | original runtime objective/cleanup |
| C18 part1/2 completion prefix | turn accumulation and own guard clear; Complete18 arg1/2 | native sequence/phase/map/ownership handoff |
| C18 part3 completion prefix | accumulation/guard clear only | remaining cutscene and request invocation unmodeled |
| C18 openings2/3/4 | turn1 before MapLoad(bmap18) | actual map/roster/reinforcement initialization |
| Complete18(1/2/3) | request byte5/6/7 at state+0x54 | request is NOT current-stage identity |

Native fragments are pinned in RESEARCH CAMP-016..018. Ownership bits survive
the force-list flag fragment but are cleared by disposal. Inventory/progression
retention inside the projection means input payload was carried through the
model; it does not prove every unexecuted native callee preserves it.
Generic NPCs may share a PID; compare physical slot/PID pairs. Never collapse
all records into a PID-only dictionary or treat every Yellow unit as permanently owned.

## Offline reproduction

From the isolated campaign clone, using its existing interpreter:

```powershell
$py = '..\FireEmblemTwoHouses\.venv\Scripts\python.exe'
& $py -B -m unittest tests.test_native_lifecycle tests.test_unit_lifecycle tests.test_ch17_stage_model
& $py -B -m tools.ch17_stage_model --out work/NEW_ch17_prefix.json
& $py -B -m tools.campaign_verify --check-artifacts --coverage-json work/NEW_lifecycle_coverage.json
```

The original-PPC executor covers only the isolated flag fragment. Rescue/native
death/MapLoad/save operations cannot be silently substituted by successful mocks.
Lifecycle.require_complete_native_proof always rejects while opaque callees remain.

## Future manual cases (preparation only; no test requested now)

Use the existing pack and a suitable private **natural** chapter save for
continuity. Synthetic local-event results cannot certify natural history.
All runs use new captures and disposable card slots; no original card/state is overwritten.
The previous weak-army inside-cell profile is not an exit/continuity fixture.

**CH10-ESCAPE, direct branch:** Start with the original prisoner present, a
documented difficulty/door/Talk history, an unacted living recruit at the genuine
exit(6,2) or(7,2), and Ike still available. Capture `before` just before original
Escape. Perform Escape/confirmation/dialogue; capture `after` on the same map.
Expected local state: matching prisoner identity remains in roster5 with escaped
bit0x4000; no duplication, death or unrelated progression/item changes. Oscar
retains fixed ownership. Finish with Ike last; capture `cleanup` after original
ending and `reloaded` after a fresh native boot into the next roster. A force5
capture alone is not acceptance of permanent recruitment.

**CH10-ESCAPE, carried branch:** Requires an independently valid original Rescue
pair and reachable exit; use a separate case/run from direct Escape. Capture
carrier/passenger IDs, factions, rescue links and flags before the original
action; record both identities afterward and at cleanup/reload. The offline
native projection deliberately rejects this path. Do not infer passenger
retention from the original script's transfer-to-Blue call alone.

**CH10 permanent recruitment:** Record each prisoner's actual door/Talk/escape
history. After original ending, save to an unused private slot, close Dolphin,
fresh boot without a savestate and inspect the next roster/preparations.
Kieran/Brom/Nephenee are not in the stable fixed P2 table; do not require them
to remain Yellow after permanent recruitment or assign ownership automatically.
Failure signatures: missing/duplicate living recruits, unexpected death,
progression/items reset, inconsistent native reload or control ownership.

**CH6 carried/Ike-last:** Use the existing CH6-CARRIED-ESCAPE contract with a
natural or separately geometry-checked exit state. Capture original Escape for
both carrier/passenger factions separately; keep Ike last for completion and
record Chapter7 roster plus native reload. A model identity check that permits
carried Ike is not proof the original Rescue eligibility allows that scenario.

**CH17-STAGES:** Separate runs for1->2,2->3,3->4 and part4's final clear. Capture
before completion, first stable next-part map, and any offered native save/reload.
Record part number by original map/dialogue/objective, not C18.cmb alone. Check
turn1, accumulated turn bookkeeping, new reinforcements, living/dead/away roster,
ownership, items/HP/EXP and phase controls. Preserve the raw request byte as
diagnostic evidence only. No independent per-part save is assumed available.

For each case use the existing collector (all paths are examples to substitute):

```powershell
$case = 'work/manual_campaign_v1/CH10-ESCAPE'
$ini = 'work/YOUR_DISPOSABLE_PROFILE/User/GameSettings/GFEE01.ini'
& $py -B -m tools.campaign_test_pack capture $case before "$case/before.sav" --ini $ini
& $py -B -m tools.campaign_test_pack capture $case after "$case/after.sav" --ini $ini
# Collect cleanup/reloaded using their declared labels too.
& $py -B -m tools.campaign_test_pack review $case
```

Generic review remains INCONCLUSIVE pending original-event/native analysis;
missing captures are not PASS. For a repeat/branch generate a NEW pack with
`tools.campaign_test_pack prepare --root work/NEW_manual_campaign`.
The existing VERIFICATION dashboard now reports lifecycle behavior and precise
evidence levels separately from whole-chapter acceptance.

## Campaign graph and native persistence audit

```powershell
& $py -B -m tools.campaign_graph --path chapter:11 Scripts/C12.cmb
& $py -B -m tools.campaign_graph --path chapter:11 Scripts/C12.cmb --allow-unresolved
& $py -B -m tools.campaign_graph --out work/NEW_campaign_graph.json
& $py -B -m tools.save_architecture --profile work/YOUR_PRIVATE_PROFILE/User/Config/Dolphin.ini
```

Graph scene/call connections are static, not event activation. An unresolved
path query cannot certify a chapter clear. Native field-pair presence does not
certify roster enumeration, card identity, wire format or persistent saving.

For the future native ownership-save test, start from a disposable naturally
progressed native card/profile with a living P2-owned character. Record intended
codes/fingerprint, unit PID, faction, flags, level/EXP, items and chapter/turn.
Capture before original Suspend/save, then fresh boot the same matched private
card WITHOUT savestate loading and capture after original reload before actions.
Preserve all item/progression/owner evidence and record any original-card refusal.
Do not infer failure of production saving from an inherited synthetic card mismatch.

For Netplay additionally record host/client machines and the save-data mode.
Current WriteSaveData=False means this setup does not request persistent Netplay
write-back; it does not disable standalone local card saving. Any future True
setting belongs only in a NEW disposable profile and remains unverified until
native save, session end and a new synced session from the host card are observed.
No policy changes, card writers or manual tests were performed in this initiative.

A pair of separately collected campaign snapshot JSONs can be inspected with:

```powershell
& $py -B -m tools.save_architecture --compare work/BEFORE_snapshot.json work/AFTER_snapshot.json --pid PID_OSCAR
```

The result deliberately stays INCONCLUSIVE for native save/reload even when
selected native-backed fields match. Inventory, save slots and global flags
require their own evidence. Ledger facets native_save, native_reload and
next_chapter_initialization remain independent of event/model passes.
