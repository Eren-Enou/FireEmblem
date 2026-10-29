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

### CAMP-020 — executable lifecycle fragments across roster boundaries

Original availability loop at0x8011A6F4 reads force5 head, calls transfer0 at
0x8011A708, then ORs raw0x01000000 at0x8011A710 and0xDC at0x8011A714.
All pinned. It is roster availability, NOT proof of final deployment cap,
selection or placement. Earlier forced-unit handling and later native callees
remain outside this projection. Map-start raw mask at0x8002EA10 clears0x4400
for original selected forces0/5/6/7;0x8002EA48 marks force0 with0x400 (F-43).
These writes preserve ownership bits but do not establish status/attribute
initialization in transitive calls.

Lifecycle now composes active cleanup -> force5 availability -> map-start flag
writes -> existing fixed-table ownership. Tests preserve identity/payload and
ownership while excluding disposed partners, Green NPCs, dead6 and absent7.
Explicit story transfers to enemy1/away7 take priority; only an original return
to0 allows subsequent P2 routing. Final native proof still rejects unresolved
cleanup/attribute/placement/save calls; no natural chapter boundary is claimed.

A concrete model validation defect was reproduced: individual Escape accepted
ambiguous owned PID records although bulk hand-back rejected them. A failing
regression now rejects the individual case BEFORE any mutation, matching the
existing fixed-table consistency contract. Legitimate duplicate generic NPC
PIDs remain permitted when they are not ambiguously claimed permanent owners.

### CAMP-021 — native save field pairs and read-only Netplay policy audit

Writer/loader pairs are pinned: level reads0x8003CB70/stores0x8003C950;
EXP0x8003CB7C/0x8003C95C; HP0x8003CBD4/0x8003C9B4. Full flags use writer
address0x8003CBBC, width4 at0x8003CBC0, helper call0x8003CBC4; loader address
0x8003C994, width4 at0x8003C998, helper0x8003C99C. This corroborates F-52's
raw32-bit ownership-containing word. It does NOT establish the complete UNIP
wire format, checksums, item codec, save-slot/card identity or save-mode selection.

`tools.save_architecture` validates these exact instruction pairs, compares only
known selected snapshot fields and audits a supplied Config/Dolphin.ini read-only.
Missing fields/ambiguous selected PIDs and wrong native widths fail. Matching
fields remain INCONCLUSIVE for native saving: no card I/O has been executed.
Native roster selection and chapter/global flags remain separate unknowns.

Current generated private profiles have SyncSaves=True, SyncCodes=True and
WriteSaveData=False (netplay_setup default). The audit reports Netplay write-back
DISABLED_BY_PROFILE; this setting does NOT disable standalone card saving.
True is only REQUESTED_NOT_RUNTIME_VERIFIED; missing/invalid is UNKNOWN. No
configuration or card is changed. Eventual campaign validation needs matched
private cards, original native save, session close/restart and observed host
write-back; do not enable writes on originals or infer persistence from syncing.

### CAMP-019 — campaign connection graph with unresolved transition gates

Original normal transition reads current chapter at0x8002E210, computes +1 at
0x8002E224, writes turn1 at0x8002E228 and phase0 at0x8002E230, and calls
SetChapter at0x8002E234. All pinned. This is conditional branch arithmetic,
not proof of objective completion, dispatch, native cleanup or initialization.
The special chapter28 path, internal Chapter17 parts and Endgame are NOT given
fabricated sequential links. F-38's earlier gates and rebuild remain unresolved.

`tools.campaign_graph` derives43 original CMB containers, scene declarations,
aligned relevant call sites and operation boundaries from the image. It embeds
34 chapter/stage contracts and their existing ledger evidence without promoting
those claims onto unrelated edges. Each script has its own SHA256. Local-CFG
reachability is explicitly distinct from original event activation and order.
The first graph has3409 nodes,4557 edges,1227 unresolved edges. Counts describe
static connections, not covered gameplay. Save operations without recovered
calls remain opaque boundaries rather than invented complete-looking paths.

`--path chapter:11 Scripts/C12.cmb` returns NO ESTABLISHED PATH. Adding
--allow-unresolved shows the conditional native gate and returns INCONCLUSIVE,
never PASS. Internal parts18.1..18.4, internal29 Ch27-2, Endgame31 and ending.cmb
remain separate. No C32 target or automatic endgame continuation is created.
Tests check every graph call against original aligned instruction boundaries,
special cases, unknown endpoints and non-transitive runtime classifications.

### CAMP-018 — Chapter17 bounded stage contracts and native sequence request

Original C18 SHA256 e942b11ab26ef9c6aec26fcb25d6a7110a6560629d3f531cd728a0d86f2c40f9
is pinned. Complete18 is a registered native at **0x800B6E00**, not a guessed
script helper. It selects codes5/6/7 at0x800B6E34/3C/44 for args1/2/3, reconstructs
state base at0x800B6E50 and stores byte state+0x54 at0x800B6E54. Calls at
0x800B6E58 and0x800B6E74 are unresolved native sequence/proc boundaries.
All sites pinned. This is a request encoding, NOT a current-stage discriminator.
Snapshots expose raw/matching request only for chapter18 and keep current part
UNKNOWN. Other writers, consumption and phase initialization are not inferred.

Original C18 completion scenes82/85 execute with explicit GetBattleType0 and
modeled native effects to their Complete18(1)/(2) boundary. Scene88 executes only
through turn accumulation/guard clear, stopping before SetGrid and its cutscene.
BM variable3 becomes current turn for part1 and prior accumulated+turn for2/3.
Each clears its own original clear-condition key. Red escape loops do not touch
Blue/Yellow/dead/away records in the bounded model. Full native semantics remain
limited by CAMP-016/017, not established merely by these script executions.

Original opening scenes83/86/89 each set turn1 before MapLoad(bmap18). Native
BMSetTurn0x800BCC34/38 reconstructs state base and0x800BCC3C stores the halfword
at state+0x12; all pinned. Prefix tests stop BEFORE MapLoad and do not simulate
reinforcements, original part activation, roster load, phase/controller setup or
ownership redistribution. Part4 ending is separate and unmodeled. A controlled
BMSetTurn1->2 bytecode mutation is detected by the reset expectation.

New lifecycle facets in the EXISTING verification ledger distinguish conversation,
temporary transfer, permanent recruitment, escape, cleanup, death/absence, stage,
completion, save, ownership and Netplay. Runtime facets must reuse already accepted
axis evidence (and its checked hashes); models remain MODEL VERIFIED. Missing
facets remain UNTESTED; BLOCKED requires a reason. No duplicate acceptance ledger.

### CAMP-016 — native force flags and no-rescue escape classification

**VERIFIED-STATIC + bounded instruction execution + lifecycle projection.**
Original append0x80015718 and prepend0x800157DC both mutate the unit flag word:
force0..4 clear0x18; force5 computes(flags|0x18)&~0x8; force6 ORs0x8; force7
leaves it unchanged. Pinned append sites0x80015740/6C/7C/88/98 and prepend
0x80015830/40/4C corroborate this. Setter0x8003B6D0 writes the force pointer.
The original model's force-only transfer was incorrect: a regression with
flags0x60000018 failed, then passed after applying the native masks.

An isolated executor runs original instructions0x80015740..0x800157A0 in Python
memory containing only force byte and flag word. Fragment SHA256
 a229f2f4909abd5ffcfb7686ad80ac4c6a215cc992fbe6b33d1e81739136e033
is pinned; unsupported instructions, branches/accesses and identity changes fail.
All8 forces x36 flag inputs match an independent formula. A controlled wrong-OR
mutation is rejected by identity and differs from the expected native effect.
Ownership bits0x60000000 survive this fragment. It is NOT full-function execution;
refresh0x800946F0, secondary-byte copying and other calls remain unresolved.

Escape worker0x8003DFB8 reads rescue link at0x8003DFCC; no link branches from
0x8003DFD4 to0x8003E858. Actor force loaded0x8003E864/68; branch0x8003E870
selects disposal for non-Blue. Blue calls roster prepend at0x8003E88C then ORs
escaped0x4000 at0x8003E894. Non-Blue calls uninitialize0x8003B6F0 at0x8003E8B0.
That routine directly clears character pointer0x8003B724, level0x8003B734,
EXP0x8003B738, rescue link0x8003B730, HP0x8003B75C and the whole flag word
0x8003B74C. The free-force offset0x30 and append are pinned at0x8003E8C0/C4.
Ownership bits therefore do NOT
survive disposal. AllUnitEscape's Blue-tail load0x800BA840, worker call
0x800BA84C and remaining-force call0x800BA8B4 corroborate the ordered passes.
Existing F-39/F-40 explain why EXP-16's existing hand-back is essential.

### CAMP-017 — bounded roster lifecycle integrated with original C11

`tools.unit_lifecycle` models only pinned force/status classification, no-rescue
Blue-to-roster escape versus non-Blue clearing, original active-force cleanup and
the existing fixed-PID ownership hand-back. It tracks record identity, observed
payload, disposal and unresolved native effects. Rescue paths reject BEFORE
mutation; native death/save/I/O are not simulated. Retained items/progression are
carried input data, not proof about unresolved transitive engine calls. Generic
NPCs may legitimately share PIDs: snapshot import keeps their physical slots,
never collapses them. Ambiguous permanently owned PID matches are rejected.

LifecycleWorld executes original C11 Talk -> direct prisoner Escape -> scene57
through modeled AllUnitEscape, stopping before MapFree. Directly escaped prisoners
reach force5 and remain there. Non-Maniac original open-door fallback transfers
Kieran/Brom to Blue even without Talk; Maniac does not. The synthetic closed-door
Talk-only path projects Kieran disposal, while Oscar is preserved by the existing
fixed ownership hook. The accepted post-Talk capture supplies the same local
preconditions, without modifying it. This is NOT a demonstrated runtime loss,
complete recruitment, MapFree/late-ending or native persistence result.

Mutation cases omit Yellow hand-back or wrongly assign permanent ownership to
native partners; their outcomes differ from the expected retained/disposed roster.
Dead/away lists are untouched by active cleanup. Invalid duplicate slots,
ambiguous ownership and cleared identities fail. No production code was changed.

### CAMP-015 — Jill defection directions modeled as distinct original events

**MODEL VERIFIED**, not new gameplay. C21.cmb SHA256
 d27bd04ba9fd98dbab8a355cb7ec9adab303364f34c67224b4983ca2abb7a5eb
is pinned alongside C11/startup/C07. Original scene26 is Jill->Shiharam;
scene27 is Shiharam->Jill. Both records are directed and share a consumed key.
It would be incorrect to reject reverse selection globally just because
scene26's individual reversible field is false: a separate original record exists.

64 executable cases cover both directions, starting force0/3 and explicit
Mist/Lethe PersonGetYellLevel inputs0..3. Both original event bodies transfer
Jill to force1 iff neither query equals3. With either3, force remains unchanged.
Only scene26 explicitly calls UnitSetCpAttackSeq with SEQ_ALLUNITATTACK100;
scene27 has no such explicit call. Both consume the shared conversation key.
No statement is made about the resulting native AI beyond that call distinction.

The model executes the original startup transfer helper, supplies relationship
query results and records presentation/native effects explicitly. Wrong identity,
missing actor and repeat/shared-key selection are rejected. Source game bytes
remain read-only. A Yellow Jill input is a hypothetical ownership case, not a
claim the stable fixed table assigns Jill to P2. Original event activation,
natural relationship history, native transfer/AI, next-phase ownership routing,
cleanup and save/Netplay remain unverified. No gameplay patch is justified.

### CAMP-014 — generic offline event flags and explicit unknown stages

**READ-ONLY captured-state analysis; no new native address/meaning inferred.**
The CAMP-011 pinned current 96-name table/parallel bitset decoder is now reusable
as tools.event_state. Snapshots include event_flags with completeness, known
values and explicit unknown semantics for absent names/other global banks.
Malformed pointer, unterminated name, invalid Shift-JIS or conflicting duplicate
produces values=null and an error, never a fabricated all-clear table.

Existing Ch6 native-start capture decodes36 registered names; accepted Ch10
post-Talk capture decodes64. Its generic map exactly equals the existing local
Talk map and preserves the original conversation clear->set comparison. Source
files remain unchanged. Unit escaped is an explicit view of already-pinned
flag0x4000 (CAMP-001/F-43); it adds no new offset. Battle-stage identity remains
UNKNOWN because chapter byte and loaded CMB alone cannot distinguish Ch17 parts.

Fixed comparator correctness: game-field iteration now covers the union of
both schemas. Previously a newly added field could differ while differences()
returned an empty list because only a hard-coded list was checked. Regression
injects an otherwise unknown future field and requires a missing-field finding.
Old snapshot inputs remain supported; missing fields are reported, not ignored.

The generated verification dashboard now derives STATICALLY VERIFIED, MODEL
VERIFIED, SYNTHETIC RUNTIME VERIFIED, NATURAL GAMEPLAY VERIFIED, MULTIPLAYER
VERIFIED, UNTESTED and FAILED scope labels from validated axis evidence. Blocked
manual cases and rejected fixture diagnostics are shown separately from gameplay
defects. --coverage-json emits axis/evidence/limitation records without promoting
any result. Natural history is not inferred from a native GCI or copied state.

### CAMP-013 — original prisoner cleanup predicates executed offline

**MODEL VERIFIED original bytecode; no new runtime evidence.** New
`tools.campaign_event_model` pins SHA256 of C11.cmb
153812f03aa5540589777cd8dbffc8bfd7c5494025e0ba3e905454834b94730d,
startup.cmb 2ff9182ab485b50792deb78947ab557dcb3f4be66e24b3912da0cb230e033d01,
and C07.cmb c4bb776bfc12cbcacb7bad6cebd906d1e9d88b609cd535a9d51410b20a8feacc.
No extracted script is committed. Reproduction: unittest
`tests.test_campaign_event_model`; `tools.campaign_event_model --out work/NEW.json`.

C11 scene57's prefix before AllUnitEscape has a concrete fallback: for each
Kieran/Brom/Nephenee, non-Maniac AND its original cell-door key set AND its
escape key unset AND UnitCheckExistsByPID2 returning a unit leads to transfer0.
Maniac skips this fallback. 120 combinations cover three prisoners, five forces,
difficulty, door and escape bits. A Talk key is not read by this prefix. It must
not be inferred that Talk alone, or this fallback alone, proves permanent joining.

UnitCheckExistsByPID2 is startup scene12 (lookup at script offset0x14A7), not
an opaque registered native. It calls local scene10 UnitCheckExists, whose
original comparisons accept force0/1/2/3 and reject force4/5/6/7. Thus this
specific original existence predicate accepts Yellow; no speculative patch is
justified. Startup scene24 UnitTransferToForceByPID also executes original lookup
and scene6 validity checks before its modeled native transfer. The VM now runs
local calls with isolated argument frames, shared instruction budget, depth limit
and opcode41 stack discard; unsupported reference passing fails closed.

C11 scene5 sets the matching prisoner escape key and calls its original
transfer-to-Blue helper BEFORE UnitEscape when the actor OR rescued passenger
is that prisoner. A Yellow Oscar escaping alone does not complete the map;
Ike as actor or passenger does. C07 scene1 has the same identity completion
pattern. This is bytecode order/branch evidence; UnitEscape itself is recorded,
not simulated. Carry eligibility and actual preserved roster remain runtime gaps.

C11 scenes29/30/31 match Oscar/Kieran reversible, Ike/Nephenee directed and
Ike/Brom directed. Repeated consumed-key and missing-identity tests reject calls.
Scene15 opens the original door and sets its two access keys without recruiting.
A deliberate in-memory mutation of Talk's force3 argument to force0 is caught
by the independent expected-effect assertion. Source game/state bytes stay read-only.

Strict native whitelist supplies GetStatus/GetForce from explicit model inputs,
UnitGet selector4 passenger, named flags, BM counter and presentation no-ops.
Modeled transfer preserves other fields by assumption, NOT proof about PowerPC.
Models stop before AllUnitEscape; no cleanup, native save, chapter-clear or
Netplay PASS follows. Original native evidence is CAMP-001/003/004/011/012;
this milestone introduces no new executable addresses or production patches.

### CAMP-012 — selected actor occupancy and manual Chapter10 original Talk

**VERIFIED-STATIC and captured-runtime local event effect (TESTING CAMP-N).**
The original availability routine loads the actor from menu context+0 at
**0x80078A60** (`80630000`). The adjacent collector's right-target branch reads
its neighboring occupancy ID at **0x8002B1A0** (`8863000D`) and rejects zero at
**0x8002B1A4** (`28030000`). All three instructions are pinned. This path does
not require the actor's own tile to contain its ID. The pre-Talk human capture
has Oscar at(19,19), empty own occupancy, and context actor pointer0x802B1764
(slot2); Kieran's adjacent tile still contains slot19. This does not establish
which routine cleared Oscar's occupancy or a universal rule for every menu.

Correct the fixture checker to accept an empty actor tile only when the current
context explicitly identifies the same Oscar slot. A wrong/missing actor,
occupied actor tile belonging to another unit, missing Kieran occupancy, blocked
edge, consumed key and other original gates still fail. The first redirected
report's occupancy failure was a verifier error; no gameplay/fixture code changed.

User supplied original-Talk observation and two captures: Oscar stays Yellow,
flags0x400->0x401; Kieran Green->Yellow, original conversation key clear->set.
Roster identities, positions, items and progression fields are preserved; door
and chapter flags unchanged. Both captures match all intended C2 bodies
in the3240-byte configuration and loaded C11.cmb. See CAMP-N for hashes and limits. This establishes
only the local original Talk effect from synthetic positioning, not permanent
recruitment or chapter completion. No Dolphin input sent by Codex.

### CAMP-011 — isolated Chapter10 Oscar/Kieran Talk positioning fixture

**STATIC and captured-state evidence; runtime positioning and Talk NOT TESTED.**
User separately reports original Blue->Yellow, P2 Oscar Wait and P1 lockout PASS
in the validated loader fixture. Source start SHA256c6e2ae86782fc95df14fdba33109629033bbb7e390481b7ee5c25209cf930b8e;
after-Wait f9940810bb053ba6f9b27a035d041cc86a32c63cd37970e3f6cbb80f147a4382.
Both loaded C11.cmb and matched stable+FIXTURE-LOADER C2 bodies. Not natural history.

Geometry inspected before choosing positions:
- Original dispos_c.bin places Kieran at(20,19), force2; captured slot19, HP30,
  flags0x80020, unrescued. Captured Oscar slot2, force3, HP28, flags0x400,
  unacted/unrescued at(2,19). Original Talk gate actor+0x1A5 is0.
- The grid base is **0x802CA518**, reconstructed at0x8002B0F0/0x8002B0F8
  (signed low addend). Width/height in the capture are24/23. Original Talk reads
  occupancy at base+0xD+x+64*y and edge masks at base+0x408E+2*(x+64*y),
  corroborated by CAMP-007 instructions. Right bit2 at0x8002B180 selects x+1
  at0x8002B188; left bit1 at0x8002B254. Both(19,19) and(20,19) have mask0x000F;
  the chosen Oscar tile(19,19) is empty, while(20,19) occupancy19 matches Kieran.
  This is an inside-cell floor interaction, not adjacency through a wall/door.
- Original map.bin mapbuildinst includes the door at(19,14); C11 scene15 is
  its kind5/action11 event: DoorOpen(EventGetX,EventGetY), then set F1914 and
  `扉チャップケヴィン`. Both source flags are false.
- Actual captured door object independently checked: getter0x80040844 uses
  r13-0x7AF4 => **0x803672AC** root slot. Original query0x8004721C reads count+6,
  table+0x14 at0x80047234, stride0xB4 at0x80047228; descriptor pointer+0x10
  at0x8004723C and mask+0xBC at0x80047240. Bounds+4/+6/+5/+7 read at
  0x80047260/0x80047270/0x80047280/0x80047290. InstantDoorOpen's query includes
  mask0x1000/excludes0x10 (0x8019F7FC/0x8019F800). Matching object index1 has
  bounds(19,14,19,14), descriptor mask0x1300, state byte0x80. Original open worker
  (called at0x8019F86C) reads state+2 at0x80049B94, ORs0x02 at0x80049B9C and
  stores at0x80049BA0. The captured open marker is unset; the door stays untouched.

Eligibility inspected: CAMP-007 native menu context+0x12 / +0x16 gates and
actor+0x1A5 action bits still apply. Native candidate selection needs the actual
grid edge and occupied neighbor; CAMP-004 matches Oscar/Kieran character IDs,
allows reversal and rejects consumed key. C11 scene29 has no additional door
flag conditional: original MS_11_TK02 dialogue -> Kieran force3 -> set
`オスカーケビン`. This is temporary partner membership, not permanent recruitment.
The setup never calls any of those event operations.
The context base **0x802EF4C8** is reconstructed at0x80078A2C/0x80078A34;
source mode+0x12 and flags+0x16 are both0. The pre-Talk checker requires those
original gates to remain clear; its PASS still does not prove the menu appeared.

Named flags decoded read-only: native get0x800BB04C selects state+0xB4 at
0x800BB064. Lookup reads names at0x800BDD54, bounds96 at0x800BDD74, computes
slot/8 at0x800BDD90 and bit modulo8 at0x800BDD94, and reads bitset+0x300 at
0x800BDDA0. Source conversation key, door keys, gf_complete and gf_gameover are
all clear. The new setup calls original get only as a read guard.

DBG-CAMP-TALK uses the previously pinned input hook/UnitSetPos (CAMP-005),
guarded to chapter11/turn1/humanYellow, original Oscar/Kieran positions and
factions, positive HP/no rescue, Oscar unacted, clear conversation key and empty
destination. Only Oscar is moved by original UnitSetPos to(19,19). No direct
unit-state stores or calls to faction, flag-set, DoorOpen, Talk or completion.
The original native callbacks remain responsible for whether Talk appears.
Total stable+loader+setup **3240 bytes**,8 below conservative capacity3248.
Source profile/card/states are read-only; NEW seed changes Gecko tail only.
Runtime setup/door/key/unit checks and before/after comparison are supplied;
human observation is required before a local Talk PASS. No Dolphin input sent.

### CAMP-010 — script-selection fixture hook candidate

VERIFIED-STATIC; candidate runtime NOT TESTED at introduction. Original chapter
script selection reconstructs state-block pointer at0x8002D568/0x8002D56C,
reads chapter byte at**0x8002D570** (`88630010`), then calls loader0x80166258
at0x8002D574. The loader calls descriptor lookup0x80019F04 at0x80166268.
Lookup reads row count at0x80019F04, compares each row's byte+0x3C at0x80019F18
and advances stride0x60 at0x80019F2C. Loader takes descriptor+8 script name
at0x80166278, formats `Scripts/%s.cmb` (pool0x80277976; offset construction
0x80166280) and submits it at0x80166290. All listed sites pinned.

Hypothesis: frame-polled AR missed script-selection timing during CAMP-J's
restart. A separate FIXTURE-LOADER C2 candidate intercepts0x8002D570, conditionally
changes source chapter to target before the displaced read and original loader.
It preserves r0, CR, stack and other inputs; no calls or roster/event edits.
This is fixture setup only, never a gameplay correction. All earlier source-card
initialization/history remains synthetic. Require loaded C11.cmb, actual prison
map and living prisoners before accepting the proposed Chapter10 route; later
recruitment/escape/progression must still execute originally. Production unchanged.

### CAMP-009 — independent loaded event-container chain

VERIFIED-STATIC plus captured-RAM corroboration (CAMP-K), GFEE01 rev0.
Original iterator0x80013B60 takes null to start;0x80013B68 loads r13-0x7C10.
Pinned SDA initialization (F-29) gives r13=0x8036EDA0, hence root slot
**0x80367190**.0x80013B6C reads root+0x28, then the first function pointer.
For a current function,0x80013B78 reads parent header at+8; after exhausting
its function table,0x80013B98 advances header+0x1C.0x80013BAC follows further
headers and0x80013BC8 reads the successor's function table+0x28. All pinned.

Read-only observations in existing accepted Ch6 and Ch9 captures: root points
to a `cmb\0` header named startup.cmb, linked at+0x1C to C07.cmb or C10.cmb.
The CAMP-J rejected redirect capture also links to C07.cmb while its chapter
byte is11. Thus loaded-container identity independently detects that mismatch.
The header name begins+4 (20-byte field before version+0x18), and pointer fields
are relocated big-endian in RAM, unlike little-endian offsets on disc.

tools.loaded_scripts bounds the chain, rejects invalid/misaligned/out-of-MEM1
pointers, invalid magic/names, cycles and excessive depth. Partial/missing chains
remain inconclusive. Snapshot records names and campaign IDs without assuming
they prove map geometry, event activation, story history or campaign compatibility.
state_expect rejects an observed chapter/container mismatch and can require a
specific loaded container. No RAM write, hook or production change introduced.

### CAMP-008 — chapter-byte identity can contradict the loaded scenario

VERIFIED-RUNTIME (CAMP-J): native Restart Chapter from the copied Ch6 card plus
synthetic AR source7->11 produced RAM chapter11 while the original Ch6 title,
forest/bridge map, starting positions and Emil loaded. Chapter10 prisoners were
absent; live stable C2 payloads matched. This rejects this fixture route, not
Chapter10 co-op gameplay. The previously pinned chapter field alone cannot
identify the loaded script/map. No new game addresses or correction patches.
Infer a cached/different loader source only as a hypothesis; it was not traced.
Accept later fixtures only with independent scenario/roster/event checks.

### CAMP-007 — original Talk menu and adjacent candidate chain

VERIFIED-STATIC, not a Yellow recruitment runtime result. Generated full local
instruction evidence: `python -m tools.talk_audit` -> TALK_AUDIT.md. All new
locations below have pinned instructions/data in check_signatures.

- Table0x80288960 links label callback0x800789CC; its pool offset at0x800789E0
  resolves MMM_TALK at0x8026C5DA. Table0x80288974 selects availability0x80078A24.
  That callback gates context+0x16 bit0 (0x80078A38) and context+0x12
  (0x80078A4C), calls candidate collection at0x80078A64, rejects a zero result
  count at0x80078A6C, then reads actor+0x1A5 at0x80078A90 and extracts bits4..6
  at0x80078A94 (return2 if nonzero, otherwise0). No direct faction read here.
- Candidate collection0x8002B0A4 selects callback table0x80284D40 at0x8002B0C0.
  It reads actor y/x at0x8002B0EC/0x8002B0F4, a precomputed direction mask at
  0x8002B114, then up/right/down/left occupancy IDs (first at0x8002B138),
  converts nonzero IDs to unit slots (stride at0x8002B14C), skips nulls and
  dispatches callback table+8. No force-list enumeration or faction comparison
  appears in this function. **Production of the precomputed mask is still open.**
- Table0x80284D48 links callback0x8002CD70: store target at0x8002CD8C,
  query original kind8 matcher at0x8002CD90, append x/y/unit ID on success at
  0x8002CDB4. Append increments result count at0x8002F6F8. No extra force gate.

Inference: the inspected original Talk path does not contain the suspected
force0-only candidate restriction. Context gates, precomputed mask generation,
live action-state gating, real conversation execution and subsequent prisoner
cleanup are **not verified**. No compatibility patch is justified by this static
absence. Reproduce with P2 Oscar adjacent to living Kieran in Chapter10, fresh
conversation key; execute original Talk, verify faction, key and later roster.
Original scene29 transfers Kieran to force3; that is not permanent-recruit proof.

### CAMP-006 — local symbolic samples across native state changes

VERIFIED-TOOLING (CAMP-H): treating repeated get(flag) text as one immutable
expression was unsound across an intervening set(flag). A synthetic bytecode
regression reaches a transfer with first read0 and second read1 in the concrete
mocked-native VM. The bounded tracer now assigns each opaque call an offset/visit
sample identity and invalidates explicitly passed VM-local references. This
conservatively permits additional paths; it does not model native state effects
or certify that a world-state combination can occur. Only equality of known
integer/string literals and integer branch truth are folded. No new game address
or production patch is introduced. See regenerated CAMPAIGN_EVENTS.md and CAMP-H.

### CAMP-005 — native positioning fixtures and original Yellow Escape

VERIFIED-STATIC: recovered registration UnitSetPos = 0x801A0E84, argc3
(unit ID, x, y). Entry/byte-ID gate 0x801A0E84/0x801A0E8C; staging x/y
0x801A0ED4/0x801A0EE4; original position-helper call 0x801A0EF4; position worker
0x801A0F04; map refresh 0x801A0F10; unit-display refresh 0x801A0F18 [S].
This routine is NOT assumed to enforce vacant destinations. The first synthetic
trial put Oscar on Emil's occupied exit tile; that trial was rejected without
exercising Escape. Corrected setup moves Emil alive to a vacant adjacent tile.

UnitGetByPos = 0x800BD4C0, argc2. It scans active tactical units using mask query3
at 0x800BD4E8, compares coordinates at 0x800BD550/0x800BD560, returns0 at
0x800BD584 when absent, else the unit ID at 0x800BD58C [S]. The corrected setup
requires vacant (13,25), Emil force1 at (13,26), then checks that the exit was
vacated before moving Oscar. No death, faction, Escape or completion command
is injected. Hook = existing human input entry 0x800291D8 (already pinned).
Guards: chapter7, turn1, human phase3, Oscar force3 at (14,9), alive and not
linked in a rescue pair. All volatile GPR arguments, r29..31, CR/CTR/XER/LR are preserved around
original native calls. Full debug configuration: **3168 bytes**, 80 bytes spare;
production COOP-P6/EXP-16 generators are unchanged.

Private state seed construction verifies Dolphin2609a handler SHA-256
2b2ff0716aeb9b806cc61181e559041312957f25f04c435bd7da80a78917b33b.
The GCT header is at 0x80002338, active list at 0x80002340, stable terminator at
0x80002D28, derived from the tagged handler placement (GECKO_AUDIT.md) and
confirmed in the captured state. It compares every stable code-list byte except
validated runtime branch-backs, requires a zero free tail, appends the new C2 and
terminator in a NEW state, and verifies the decoded result. All other payload
bytes remain identical. These are handler-memory addresses, pinned by handler
hash/layout and per-state code-list verification rather than original DOL words.

Inventory accessor 0x80037BD0 checks indexes; stride8 at 0x80037BE4; slots0..3
at unit+0x1CC (0x80037BE8), slots4..7 at +0x1EC (0x80037C0C), all [S]. Snapshots
now include all eight raw slots (64 bytes); item semantics beyond these records
are not fully decoded.

VERIFIED-RUNTIME, synthetic fixture only: native port2 selected Oscar at the
exit; original menu displayed Escape; original Yes confirmation and Oscar's
escape dialogue ran. After the original event and phase cycle, Oscar remains
slot2 in force5 with escaped flag0x4000, HP28/lv6/EXP28 and all64 inventory-slot
bytes unchanged. Ike remains on-map; chapter7 continues into turn2. All intended
stable AND fixture C2 bodies match both captured states. See TESTING CAMP-G.
This establishes the single-unit EXP-16 hand-back path in this fixture, not
natural traversal, carried units, Ike-last completion, cleanup, save or Netplay.

### CAMP-004 — conversation actors, direction and consumed keys

VERIFIED-STATIC: original query 0x800BF1E8 matches scene kind 8 at 0x800BF22C.
Parameter +0x1A is its key string offset (0x800BF234); +0x14/+0x16 are the
two character-name offsets (0x800BF260/0x800BF274). Character records of the
current actor/target are read from unit+0x188 (0x800BF29C/0x800BF2A0) and
compared at 0x800BF2A4/0x800BF2AC. Parameter +0x18 is read at 0x800BF2BC:
zero skips reverse matching at 0x800BF2C4; nonzero compares the reversed
identities at 0x800BF2C8/0x800BF2D0. All sites pinned [S]. This matching
routine does not read the units' tactical forces. Upstream target/menu eligibility
and real conversation activation are still separate unverified questions.

Decoded consequences (original script records, not runtime recruitment proof):

- C11 scene 29: Oscar / Kieran, reversed pairing permitted. This specifically
  exercises a stable P2-owned character as the conversation participant.
- C14 scene 37: Astrid -> Gatrie, one direction. Other Gatrie conversations have
  their own keys/effects and must not be conflated with recruitment.
- C19 scenes 21/22/23: Shinon paired with Mist/Rolf/Rhys, reversal permitted.
  Conversation alone does not establish the later battle/recruitment conditions.
- C21 scenes 26/27: Jill -> Shiharam and Shiharam -> Jill, each one direction,
  sharing one consumed key. They are alternative initiators of the same keyed
  interaction, not two unconditional sequential defections. Scene 26's relationship
  guards were decoded in CAMP-002; scene 27's effects require independent tracing.

All kind-8 metadata now appears in generated CAMPAIGN_EVENTS.md alongside local
effect predicates. tools.campaign_verify now requires explicit chapter/stage AND
axis scope per accepted evidence run, and --check-artifacts verifies local bytes
against recorded SHA-256 values. This prevents copying Prologue evidence into a
later-chapter PASS; hashes alone still do not prove semantic correctness.

### CAMP-003 — original Escape menu and tile metadata

VERIFIED-STATIC: Escape availability callback 0x80077438 is referenced by menu
table 0x8028841C; action callback 0x8007749C by 0x80288428. Label construction
resolves MMM_ESC at 0x8026C444 [S]. Availability uses action code 14 at
0x80077464, unit coordinates +0x19E/+0x19F at 0x80077468/0x8007746C, and calls
0x800BE968 at 0x80077470 [S]. The callback has a separate context+0x12 veto;
its meaning is unresolved. The callback and query contain no unit-force read.
This is not a runtime proof of Yellow menu availability or normal event execution.

The query accepts kind 5 (0x800BE9C0), compares parameters at scene+0x14/+0x16
against coordinates (0x800BE9DC/0x800BE9FC), +0x18 against action
(0x800BEA1C), and resolves +0x1A as an unsigned pool offset (0x800BEA30).
Resolver 0x800C273C/0x800C2744 reads parent ScriptInfo and its pool [S].
The query rejects a matching event if its key is already present in the chapter
event-key list; blank key lookup returns false. Key-list side effects remain open.
Decoded C07 scene 2 is Escape (13,26), empty key; C11 scenes 11/12 are Escape
(6,2)/(7,2). tools/event_report includes these tile records, beyond command strings.

tools/native_usage cross-references all 43 script containers: 24032 aligned native
calls, 327 of 406 recovered native names used. No direct aligned call names
PlayerEscapeCount, PlayerEscapeCheck, PlayerDeadCheck or GetDiedPlayerCount occur.
Native indirect dispatch/engine callers remain unresolved. This narrows the
reachability investigation; it does not establish those routines are globally unused.

### CAMP-002 — instruction-aligned VM and native registrations

VERIFIED-STATIC: dispatch at 0x80011EDC uses table 0x80283F90 and max opcode
0x41 (0x80011F18/0x80011F28). Number/string .8 operands sign-extend at
0x800127F4/0x800128F8 [S]. Decoder independently resolves all local branch
targets across 2075 scenes / 125775 instructions (43 script containers).

The 406 literal native registrations include UnitGet at 0x800BD704.
Selector 4 dispatch 0x8028D41C -> 0x800BD7C0 reads rescue link +0x194 [S].
C07 scene 1 therefore counts a carrier/passenger separately and sets completion
for escaping Ike or a carrier of Ike. Four script-model tests use mocked natives;
they do NOT establish normal event activation or roster behavior in Dolphin.

UnitGetByPID wrapper call 0x800BD5B8 and identity scan 0x80016C10 [S] show
PID resolution independent of tactical faction in this routine. Join's
0x800B7174 sets force 5 [S] for group creation; a Join command is not itself
proof that a character's recruitment conversation occurred.

Original research corroboration (format, not runtime acceptance):
https://feuniverse.us/t/fe9-and-fe10-event-script-doc-notes/6143.

### CAMP-001 details

VERIFIED-STATIC: PlayerEscapeCount at 0x801B7188 builds mask [1,0,0,0,0,1,0,0].
Sites 0x801B71B4/0x801B71C4/0x801B71CC enable forces 0/5 and exclude 3;
0x801B7224 performs the indexed mask read. PlayerEscapeCheck at 0x801B7260
does the same at 0x801B7284/0x801B7294/0x801B729C, lookup 0x801B72F4.
All eight instructions pinned [S]. Both inspect escaped flag 0x4000.
Normal Ch6 call reachability and runtime effect are unresolved; no corrective
Gecko patch is claimed necessary or working. Details: docs/CAMPAIGN_FINDINGS.md.

The campaign matrix now gets names from Mess/common.m MCTxx. Internal 29 is
Ch.27-2, 30 is Ch.28, 31 is Endgame. C18 has local Complete18 and turn resets;
suffix-map and ending-script inventories are necessary. Event calls decoded by
tools/fe9/events.py now resolve aligned local CFG calls; native semantics and scene
activation remain outside that decoder.

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
| F-05 | **Per-force control mode at `0x8033071C + force`** (state+0x14). Map init writes `{1, 2, 2, 2}`: force 0 = 1, forces 1–3 = 2. Code treats **1 as human-driven**: at `0x8002E754`, if `control[phase]==1` it starts process `0x80284AC8`. At `0x80028548` / `0x80028578`, the cursor classifier lets a **force-2/force-3 unit be selected like an own unit when `phase == force` and `control[force] == 1`**. 0 seems to mean "phase inactive" (`0x8002E6A4`). **So `0x8033071F` controls whether the yellow partner phase is CPU (2) or human (1).** | **[S]** signatures at `0x8014D960..6C`, `0x80028548`, `0x80028578`, `0x8002E754`. | **VERIFIED-RUNTIME for force 1** (EXP-04, 2026-10-27: the red army was player-controlled in its own phase). Force 3 (yellow) still needs EXP-01, which also exercises the extra classifier branch at `0x80028578`. |
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

### Unit selection and ownership (2026-10-27, from EXP-01)

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-15 | **`GetUnitSelectState(unit)` = `0x800284B4`** (callers `0x800292E0`, `0x800293BC`). Returns: 0 = no unit; 1 = blocked status (`unit+0x1A4` bits); 2 = hostile to the phase force (`0x80015648` relation==1); 3 = force 2 and not (phase==2 && control[2]==1); 4 = same for force 3; 5 = already acted (`unit+0x1A0` bit0); **6 = selectable**. It has **no check for force 0**, so blue units are selectable in any human-controlled phase. Registers at `0x8002858C`: r29 = unit, r30 = unit force id, r31 = state. | disassembly **[S]**; EXP-01 (e) observed | VERIFIED-STATIC + RUNTIME |
| F-16 | Phase-start step `0x8002E780` clears the "acted" bit (bit0 of `unit+0x1A0`) for **all units of forces 0–3** (mask query 3), not just the active force. So blue units look fresh again in the yellow phase. | disassembly; slot 7 (Ike bit0=0 after Player Phase) | VERIFIED-STATIC + RUNTIME |
| F-17 | `0x80015648(a, b)` = force relation: 0 same, 1 hostile (either is force 1), 2 allied. | disassembly | VERIFIED-STATIC |
| F-08 (upd.) | `unit+0x1A0` **bit0 = has acted this phase** (set on Ike, Mist, Lethe and Mordecai after acting in slot 8). `unit+0x18C` = class record, changes on laguz transform (Lethe `JID_BEAST_C/F` → `JID_CAT/F`). | slots 7/8 | VERIFIED-RUNTIME |

### Proc names (2026-10-27)
Proc scripts start with op `0x2003` + a name pointer. Names found: turn loop = **`E_BMapMain`** (`0x80269334`); human phase proc `0x80284AC8` = **`E_BMapPlph`**; `0x8028D138` (started by `0x8002E408`/`0x800AE3DC`) = **`E_PhaseChange`** (the phase banner, *not* AI as first guessed); others: `E_TurnToken`, `E_TurnAToken`, `E_BMapBGMCtrl`, `E_BMapBGMWaitOpening`, `E_FocusWait`. `0x800C01CC` (run under `E_TurnAToken`) scans turn/phase-triggered events (type 6, turn range, phase match). It is not the AI.

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-18 | With control[3]=1, yellow units that **haven't acted when the player ends the phase are then moved by the AI**. **Cause:** the turn-loop step `0x8002E670` (runs after `E_BMapPlph`) launches the computer-player proc **`E_CP_PhaseMain`** (`0x8028E7F8`) via `0x800FC600` (sets `0x8032B3C1 = 8`) or `0x800FC63C` (sets it to 1). Gating per phase: phase 0 → always `0x800FC600`; phases 1/2 → `0x800FC63C` only if control==2 (`0x8002E708`); **phase 3 → no control check**, and mode is chosen by `*0x8014C5A8(state) == 1` (`0x8002E6DC`). Fix = EXP-07. | EXP-06 observation; disassembly **[S]** | Behaviour VERIFIED-RUNTIME; cause VERIFIED-STATIC; **fix VERIFIED-RUNTIME** (EXP-07 A a–d: leftover units wait, phases advance, no hang; B: vanilla CPU yellow unchanged) |
| F-20 | Phase advance `0x8014D3B4` has a single caller (`0x8002E65C`, turn-loop step `0x8002E648`) and receives r3 = state. That makes it a once-per-phase-change point to enforce per-force control (used by EXP-08). The alternatives considered were rejected: map init `0x8014D920` doesn't run when a state or suspend save is loaded, and save load `0x8014C1B8` misses Dolphin save states. | disassembly **[S]** | VERIFIED-STATIC |
| F-21 | **`CanGainExp(unit)` = `0x8003D13C`**: false if `state+0x9F` bit 3 is set (special mode), if the force id isn't **0 or 5** (`0x8003D178`/`0x8003D180`), if HP == 0, or for further level checks. It has 25 callers, including the battle EXP calculation `0x80036248` (from `0x80027690`, battle copies at `0x80330EAC`) and `AddExp(unit, amount, …)` = `0x800351FC`. AddExp levels up at ≥100 and sets EXP to `0xFF` ("--") when CanGainExp fails. **So non-player partners never gain EXP in vanilla.** EXP-10 allows human-controlled force 3. | disassembly **[S]**; EXP-09 observation | VERIFIED-STATIC + RUNTIME (no EXP observed) |
| F-22 | Unit record: `+0x198` unit id, `+0x19A` level, **`+0x19B` EXP**, `+0x19C` laguz transform gauge (Lethe 0x10→0x14 and Mordecai 0→4 across one phase), `+0x19E/+0x19F` x/y, `+0x1A8` HP. Consistent with the bundled US "Quick Level Up (Ike)" code `0x802B167F` = unit 1 + 0x19B. | slots 6/7/8; Dolphin GameSettings | VERIFIED-RUNTIME |
| F-23 | **`GetExp(unit)` = `0x800386B0`** returns `0xFF` ("--") when the force id is **1, 2 or 3** (`0x800386B8`–`0x800386CC`), otherwise `unit+0x19B`. It has 30 callers, including CanGainExp (`0x8003D1A8`: `0xFF` → returns 0), AddExp (`0x80035254`: `GetExp + amount`), the battle EXP code (`0x8003629C`, `0x80036188`) and UI/status code (`0x8017C9DC`…). CanGainExp's other gates are clear for Lethe in the EXP-10 slot 4: `state+0x9F` = `00` (bit 0x08 for CanGainExp, bit 0x80 for AddExp via `0x8014DA68`) and HP 34. CanGainExp returns `min(100, cap − ((lv−1)·100 + exp))` with cap 1900 or 2000, not a boolean. **This is why EXP-10 alone failed.** Fix: EXP-11. | disassembly **[S]**; EXP-10 run (slots 4/5: exp 0 → 0, status "--") | VERIFIED-STATIC + RUNTIME (failure explained) |
| F-24 | **Battle write-back** `0x80034F40(copy)`: the battle copies live at `0x80330EAC` (Lethe's copy is there in the EXP-11 slots), and the real unit is at `copy+0x280`. Level (`+0x19A`) and EXP (`GetExp` → `SetExp` `0x8003868C`) are written back **only if the real unit's force id is 0 or 5** (`0x80034F60`/`0x80034F68`). Items, stats and HP are copied after that for every force. EXP-11 run: battle copy exp 0 → 15, gain `copy+0x2C9` = 15, an "Exp" bar was shown, but the unit stayed at 0. Fix: EXP-12. `SetExp` stores 0..100 or 0xFF and has no force check. | disassembly **[S]**; EXP-11 slots 4/5; EXP-12 slots 4/5 (exp 0 → 15 kept) | VERIFIED-STATIC + RUNTIME (EXP-12 pass) |
| F-25 | **Gecko codes and save states:** a state saved while a code list was active restores *that* code list on load. Codes installed later are not applied (EXP-11: `0x800386C8` still held the original instruction after loading the EXP-10 slot 4). Load a state saved without codes (slot 6) or boot fresh when testing new codes. | runtime (slot 8 peeks) | VERIFIED-RUNTIME |
| F-26 | **Battle-result unit pickers** `0x801B6098`, `0x801B6290`, `0x801B6348`, `0x801B67D0`, `0x801B6BE4` (called from the battle-result sequence `0x800D2DBC`/`0x800D2DA4` and the level-up screen `0x801B5F14`). Each returns battle copy A's real unit (`0x80330EAC+0x280`) if its force id is 0/5, else copy B's (`+0x560`) if 0/5, else **NULL**. `0x801B6098` gates on the level-up flag (`0x80330EAC+0xCAC` bit 0x800) and passes the unit to `0x801B32C8`. For a yellow unit it returns NULL, giving invalid reads at `0x801B5E6C` (`lwz r0,0x18C(r30)`) and `0x801B5E90` (`lbz r0,0x19A(r30)`). Fix: EXP-13 (the EXP-10 cave on all 10 `cmplwi r0,5` sites). | disassembly **[S]**; COOP-P2 level-up runs (fail without, pass with) | VERIFIED-STATIC + RUNTIME |
| F-27 | **Other force 0/5 checks not patched** (scan for `lbz rX,8(force)` → `cmplwi rX,5`): `0x80073954` (calls `0x8001C4FC`, role unknown), `0x801802E8` (float UI code), and `0x801818E0`–`0x8018234C` (8 sites that also test forces 6/7; UI/colour HYPOTHESIS). The level-up, EXP and battle runs needed none of them. Revisit if a yellow-unit screen misbehaves. | scan **[S]** | HYPOTHESIS (roles) |
| F-28 | **Next Unit (X)** cycles only through force-0 units, even in the yellow phase (cause: F-42; fix: EXP-17) (cursor jump only; EXP-06 still blocks selection). The blue action menu has **Direct** (vanilla partner-AI orders). | COOP-P2 run | VERIFIED-RUNTIME (Next Unit); Direct untested |

### Controller input (2026-10-27, Phase 2)

| Id | Finding | Evidence | Confidence |
|---|---|---|---|
| F-29 | **Pad pipeline.** SI library `0x8023A9DC`–`0x8023BB00`, PAD library `0x80211000`–`0x80212DD0` (`PADRead` = `0x80211CC0`, `PADControlMotor` = `0x80212CC0`). SDK `PADStatus[4]` at **`0x802EF408`** (stride 0xC; `+0` buttons, `+2..+5` sticks, `+0xA` err: 0 OK, 0xFF none). Per-frame update **`0x80025970`** (called from the main loop `0x80014B10`/`0x80014E1C` and the error screen `0x8005B210`) calls `PADRead(0x802EF408)` at `0x80025A48`, then refreshes four **pad objects** at **`0x802EF438`** (stride 0x24: `+0` → PADStatus, `+4` held incl. stick-direction bits at ±0x23, `+8` previous held, `+0xC`/`+0x10` pressed/repeat, `+0x1C` channel) via `0x800256CC`. Game logic reads input through the **current-pad pointer `r13-0x7B60` = `0x80367240`** (`r13` = `0x8036EDA0`, from `0x80003334`): **320 loads, one store** (`0x80025C48`, init → pad object 0). Direct `GetPad(n)` (`0x8002595C`) is only used by the error-screen OR loop (`0x8005B218`, pads 0–3) and `0x800CFE90` (pad 1's B-press, role unknown). Runtime: pointer = `0x802EF438` in vanilla battle states; = `0x802EF45C` in a human yellow phase with EXP-14 and port 2 present. With port 2 = None, PADStatus[1].err = 0xFF. | disassembly **[S]**; slot peeks (EXP-14 A/B) | VERIFIED-STATIC + RUNTIME |
| F-30 | The PAL pad address `0x802F98E8` (Ralf's codes) corresponds to US `0x802EF408` (PADStatus), consistent with the ~0xA4E0 data shift seen for the force table. | F-29 vs §1 | CORROBORATED |
| F-19 | `0x8032B3C1` = CP mode byte (8 after the player phase, 1 for AI phases). Meaning of mode 8 unknown (HYPOTHESIS: only units under forced-AI status act). | disassembly | HYPOTHESIS |

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

### Moving units between forces (2026-10-27, Phase 4)

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-34 | **The game has its own force-transfer path.** These functions handle it (r3/r4 are the arguments): <br>• Force lists are doubly linked: `unit+0x184` = next, `unit+0x180` = prev, `force+0` = head, `force+4` = tail. <br>• `0x800156A0(force, unit)` unlinks a unit. <br>• `0x80015718(force, unit)` appends it at the tail (it calls setter `0x8003B6C4`, then adjusts `unit+0x1A0` flags for forces 5/6). `0x800157DC` prepends. <br>• **`SetUnitForce(unit, index)` = `0x8003D60C`** unlinks the unit from `unit+0x190` and appends it to `0x802CA264 + 0xC*index` (`0x8003D68C` = prepend variant). For forces 0/2/3 it first calls `0x800946F0`. <br>• The script command **`UnitTransferToForce(unit id, force)` = `0x800BCA38`** (registered under that name at `0x800BB3DC` via `0x80013AE8(name, fn, argc)`) copies `+0x199` from the target force's first unit when it is nonzero (`0x8003D5FC`), calls SetUnitForce and refreshes the unit (`0x80050268`). <br>• **Unit by PID:** `0x80016BDC(PID string)` returns the unit whose `+0x188` is that character record. The unit id is at `unit+0x198` (`UnitGetByPID` `0x800BD5AC`). <br>• Other script commands found: `UnitGet`, `UnitGetNext`, `UnitGetForce`, `ForceGetFirst/Count`, `UnitGetByPos`, `Join`, `BMGetChapter`, `BMSetPhase`, `UnitBreakup`. | disassembly **[S]** (pinned) | VERIFIED-STATIC |
| F-35 | **At chapter end only force 0 joins the roster.** `0x80016C58` walks force 0 from its tail and prepends every unit to **force 5** (the roster; Ike is in force 5 at the base, F-31). It is called from the chapter-transition routine `0x8002E0D0` (which also calls `SetChapter`) and from `0x80005F04`. A player character left in force 3 would therefore not enter the roster. EXP-15 moves its yellow units back to force 0 at the entry of `0x80016C58`. Start-of-chapter deployment moves roster units into force 0 in `0x8011A694` (reached only through a table). | disassembly **[S]** | VERIFIED-STATIC; the consequence for force 3 is a HYPOTHESIS until EXP-15 |
| F-38 | **Chapter-end order (corrects F-35).**<br>• The turn-loop proc (`0x80284F88`, label 1) runs `0x801B87E8` → yield → conditional `0x13` → **`0x8002E0D0`** → `0x8002DF54`.<br>• `0x8002E0D0` exits at once when bit 0x08 of `state+0x9F` is set (`0x8002E0F8`), calling `0x80006220(0x20)`. Otherwise, for chapter id ≠ 0x1C, it runs in order: flagged roster units → force 0; the unit found by `PID_IKE` → force 0; a cleanup loop over the forces selected by mask query 4 (forces 0 and 5 only: `0x8001553C`); then `0x80016C58`; then `SetChapter`.<br>• The chapter-sequence step **`0x80005F04`** (pointer in the table at `0x802834F0`) calls `0x801ED3D4`, `0x80121414`, then **`0x801E379C`**, which leads to `0x80016628`. That routine resets all force lists and re-initialises every unit, keeping only those the loader `0x8003C830` accepts. Its own roster move (`0x80005FF0`) comes after that rebuild.<br>• **Run 1 of EXP-15** (hand-back at `0x80016C58`): after Chapter 1, unit slots 2 (Oscar) and 3 (Boyd) were empty at the Chapter 2 base (slot 4). So the units were dropped before `0x80016C58` ran, most likely by the rebuild path. EXP-15 v2 hands back at the entry of both `0x8002E0D0` and `0x80005F04`. | disassembly **[S]**; `work/ch1/host/StateSaves/GFEE01.s03..s05` | VERIFIED-STATIC (order); the drop mechanism is a HYPOTHESIS |
| F-39 | **The seize/clear event uses the script command `AllUnitEscape` (`0x800BA784`, registered at `0x800B580C`).** It works in three stages:<br>1. Breaks up rescue pairs in forces 0–3 (mask query 3, `0x80015524`).<br>2. Runs the escape worker `0x8003DFB8` over the **force 0 list only** (from its tail; force 0 units end up in force 5, the roster).<br>3. Runs `0x8003DFB8` again on every remaining unit of forces 0–3.<br>Player characters left in force 3 are therefore handled like guests and are gone afterwards.<br>**Run 2 of EXP-15** (v2, hooks confirmed patched in RAM in slots 6/7): already during the ending conversation (slot 6, chapter id 2), Ike and Titania were in force 5 and unit slots 2 and 3 were empty, so the units were dropped before `0x8002E0D0`. **v3** also hands back at `AllUnitEscape`'s entry. `UnitEscape` (`0x800BA8F8`, single unit) is not hooked yet. | disassembly **[S]**; `work/ch1/host/StateSaves/GFEE01.s06/s07` | VERIFIED-STATIC + RUNTIME (v3 hand-back at its entry kept Boyd and Oscar through the Chapter 1 → 2 transition, EXP-15) |
| F-40 | **`UnitEscape(unit id)` = `0x800BA8F8`** (script command, argc 2): looks up the unit (`unit id` in r3, `clrlwi. r3,r3,24`) and passes it to the same escape worker `0x8003DFB8` as `AllUnitEscape` (`0x800BA944`). A Player-2 character escaping alone would therefore be handled like a guest too. EXP-16 hands back only that unit at the entry. Related commands, not yet analysed (they may count force 0 only): `PlayerEscapeCheck` `0x801B7260`, `PlayerEscapeCount` `0x801B7188`, `PlayerDeadCheck` `0x801B7638`, `GetDiedPlayerCount` `0x801B7094`, `UnitDead` `0x801A094C`, `Join` `0x800B7140`, the `Sally*` deployment commands `0x800B6D20`–`0x800B6DF0`, and `UnitForcedSally` `0x800BCDF0`. | disassembly **[S]** (pinned) | VERIFIED-STATIC |
| F-41 | **Sortie and story facts seen in the EXP-16 run.**<br>• `UnitForcedSally(unit id)` (`0x800BCDF0`) sets bit `0x10000` of `unit+0x1A0` for force 0/5 units; this is the forced-deployment flag. In Ch3 (chapter id 4) the deployed four (Ike, Titania, Shinon, Gatrie) all carry it, and in Ch4 (id 5) all six deployed do (Ike, Titania, Rhys, Soren, Shinon, Gatrie). That explains why the prep screen could not change the line-up. It is set by the game's own command, which EXP-16 never calls; it has not been compared with a codes-off run.<br>• Benched characters sit in **force 7** with progression intact (Oscar and Boyd lv 4 / 82 EXP in Ch3 and Ch4). EXP-16 only acts on force 0, so benched Player 2 characters are untouched.<br>• **Marcia** has no dispos entry in Ch3 (`bmap04`, ally list: Ike, Shinon, Gatrie, Titania, Oscar, Boyd, Rhys); the Ch3 event script adds her. Her only dispos entry is Chapter 10 (`bmap11`, force 0). Leaving after talking to Ike in Ch3 is therefore consistent with the original story.<br>• Auto-end is not the phase-start scan `0x800AE3DC` (called from `0x8002E408`), which already walks the current phase's force. The auto-end check itself is not found yet. | `work/ch1/host/StateSaves/GFEE01.s02..s07`; `tools.fe9.dispos` on bmap02..bmap11; disassembly | VERIFIED-STATIC + RUNTIME (Marcia: data plus the user's observation) |
| F-42 | **Auto-end and Next Unit.**<br>• The Auto End option is **bit 0x20 of `state+0x9E` (`0x803307A6`); set = off**. Two states differing only in that option (taken by the user; backups `work/saves/GFEE01.autoend_on/off`) have the byte at 0x15 (on) and 0x35 (off). Its only readers outside the Options code (`0x801AAE14`) are at `0x80028CC4`.<br>• **`0x80028C90`** is the human-proc step run when a unit finishes acting: it sets the acted bit (`unit+0x1A0` \|= 1). If Auto End is on and **`0x800AA5F0(0)`** returns NULL, it ends the phase (`0x8018DC18`, then `0x8000C60C(proc)`).<br>• `0x800AA5F0` (next unit that can still act; also the **Next Unit** button in `0x800291D8`) is **hard-wired to force 0**: it takes the force 0 head (`0x800AA5F8`) and requires the start unit to be in force 0 (`0x800AA61C`). In the yellow phase it keeps finding unacted blue units, so auto-end never fires and Next Unit jumps to blue units (explains F-28).<br>• EXP-17 picks force 3 in phase 3 at both places. | state diff; disassembly **[S]** (pinned) | VERIFIED-STATIC + RUNTIME (option byte; EXP-17 passed: yellow auto-end, Next Unit, and Auto End off all behave) |
| F-43 | **Playable-roster classification.**<br>• The game's "player army" mask is query 4 = **forces 0 and 5** (`0x8001553C`). It is used by the chapter transition, the item-owner check `0x80193668`, the save path (`0x8014BC10`/`0x8014BEE0`, called from `0x801F690C`) and `0x80037960`. Force 3 is never part of it.<br>• **Unit lists:** `E_UnitList` (proc `0x80290EB0`), `E_UnitListWithoutFade` (`0x80290FA0`) and `E_SallyList` (`0x80291084`) all build through **`0x8012DFA8`**, whose mode byte `+0x6C` selects: 1 = force 0; 2 = force 5 (roster); 3 = force 0 + 5; 0/4 = the single force in `+0x60` (skipping flags `0x8`/`0x10`).<br>• The map menu's **Unit** command is `0x80073834`, which calls `0x8012C9FC(force 0)`, so the in-battle Base Data is force 0 only. The base screen uses mode 3 (`0x8012C964`); sortie lists use modes 2/1 (`0x8012C788`, `0x8012C7C8`).<br>• **Flag `0x400` of `unit+0x1A0` = deployed player unit this map:** step `0x8002E93C` clears bits `0x4400` on forces 0/5/6/7 and then sets `0x400` on every force 0 unit (`0x8002EA48`). Every player unit in decoded states has it (yellow ones included, since EXP-16 moves them later); Lethe, Mordecai and green NPCs never do. Gap: a character who joins mid-map and is then moved to force 3 lacks it until the next map. | disassembly **[S]** (pinned); decoded states | VERIFIED-STATIC; EXP-18 not yet run |
| F-44 | **Findings from the EXP-18 session.**<br>• `control[3]` is 2 from map init until the first phase change (EXP-08 sets it there). So at turn 1 in the blue phase, `GetExp` (EXP-11 condition `control[3]==1`) still returns 0xFF and yellow units show EXP "--". EXP-16's apply step now sets `control[3]` = 1 whenever force 3 has units, the same rule as EXP-08.<br>• A Player 2 character who dies in force 3 has its **unit slot freed** (Boyd: unit 3 present in slot 4, absent in slot 5). He then stays gone through the chapter end and the next chapter, with no revival or duplicate. Whether a blue death keeps a record (for example in force 6, which the map-start step treats as a player force) is not checked yet; that decides whether the epilogue or death record is lost.<br>• Suspend → fresh boot → resume restores phase 3, `control[3]` = 1, each unit's force and done-flags. | `work/ch1/host/StateSaves/GFEE01.s02..s07` | RUNTIME |
| F-45 | **Unit death (`0x8003E8DC`, called after combat from `0x80025FA4`, `0x80027038`, `0x800A19C0`, `0x800ADD48`).** When HP reaches 0, if the unit has attribute `0x5C` (`0x80105BC0(unit+0x1BC, 0x5C)`), it survives with flag `0x800` cleared. Otherwise it gets flag `0x8` and:<br>• **Force 0:** unlinked and **prepended to force 6 (the died list)**, with flag **`0x8000`** and the chapter id in `+0x234`. `GetDiedPlayerCount` (`0x801B7094`) counts force 6 units with `0x8000`.<br>• **Other forces:** with attribute `0x59` the unit moves to force 7 (away); otherwise it is **freed** (`0x8003B6F0`) and returned to the free pool (force 4).<br>A dead Player 2 character therefore lost its death record (Boyd, F-44). **EXP-19** treats force 3 + flag `0x400` as force 0 at the check `0x8003E94C`. **Runtime-verified** (Claude, Ch6): Oscar (EXP-16 yellow, DBG-02 1 HP) attacked a soldier and died to the counter. Afterwards he is in force 6 with flags `0x01018409` (`0x8000` set) and `+0x234` = 7 (Ch6's chapter id), the vanilla player record. Backups `work/saves/GFEE01.ch6_oscar_before/after_death_exp19`. | disassembly **[S]** (pinned); decoded states | VERIFIED-STATIC + RUNTIME |
| F-46 | **Prep screens see the vanilla roster.** In Ch6's prep (slot `work/saves/GFEE01.ch6_prep_forced`), every candidate is still force 0 (Oscar too); EXP-16 applies ownership at the first phase start. So the original "Choose Units" screen works unchanged over the shared roster. In Ch3, Ch4 and Ch6 the chapter scripts force every candidate (flag `0x10000`), so the line-up could not change; Ch6 has 5 candidates for 6 slots. A chapter whose script leaves choices open is still needed to show flexible deployment. | decoded state; in-game toggle attempts on Titania and Oscar (no effect) | RUNTIME |
| F-36 | PIDs from the decoded Chapter 2 state: Ike `PID_IKE` (unit 1), Oscar `PID_OSCAR` (2), Boyd **`PID_BOLE`** (3), Titania **`PID_TIAMAT`** (4; force 7 in Chapter 2, not deployed), Rhys `PID_KILROY`, Rolf `PID_LOFA`, Mordecai `PID_MORDY`. Chapter 1 = chapter id 2. | `inspect_state work/saves/GFEE01.s07` | RUNTIME |
| F-37 | With COOP-P3 active in the Prologue (force 3 empty), turn 1 went player phase → enemy phase with no yellow phase. This is consistent with EXP-08 setting control[3] = 2 (CPU) when force 3 is empty, and with the vanilla skip rule (F-11). | NET-00 run | RUNTIME (one observation) |

### Ownership storage (2026-10-27, design decision for EXP-16)

Ownership (which player owns a character) is kept apart from the tactical force (where the unit sits in battle). The force is translated at phase start and at chapter end (EXP-16).

| Option | Netplay-safe | Survives save/load | Risk | Status |
|---|---|---|---|---|
| **A. Table embedded in the Gecko code** (PID → player, `tools/owner_code.py`) | **Yes**: the host's codes are pushed to every client, so both run the identical table | Yes: nothing is stored in the game; the table is re-read from the code every time | None to saves. Changing the split means regenerating the code | **Chosen for now** |
| B. A spare field in the character or unit record | Yes (inside synced save data) | Yes | Needs an unused field verified across save, load and chapter transitions; none is identified yet | Open: needed for a future in-game assignment screen |
| C. A companion record (own file on the memory card) | Only if it lives on the card, which the host syncs | Yes | Needs card I/O from a code; easy to desync if written by one side only | Not started |
| D. A file outside the game (per-client) | **No**: each machine could differ | n/a | Desync | Rejected |

Two consequences of option A:
- Restoring a character to blue during chapter cleanup cannot erase the assignment, because the assignment is never stored in the unit.
- A battle save/suspend keeps the current tactical force per unit (F-13). The next player-phase start re-applies the table either way.

### Netplay runtime facts (NET-01, 2026-10-27)

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-47 | Dolphin 2609a Netplay with `netplay_setup` folders behaves as follows:<br>• The `[NetPlay]` presets appear in the dialogs.<br>• The default pad mapping gives the first player GC1 and the second GC2, which is what EXP-14 expects.<br>• "Load Host's Save Data Only" delivers the host's GCI folder to the client, and the host's card is not written.<br>• Synced Gecko codes are active on the client (yellow phase human, port routing, auto-end).<br>• **Saving** a state during Netplay is allowed; only loading is blocked (F-31). That makes per-instance desync checks by state comparison possible. | NET-01 run | RUNTIME |
| F-49 | **Dolphin 2609a Traversal, digest and disconnect (NET-02 one-PC run).**<br>• The `[NetPlay]` keys `TraversalChoice = traversal`, `TraversalServer = stun.dolphin-emu.org`, `TraversalPort = 6262` (names and defaults are strings in `Dolphin.exe`) preselect "Traversal Server" in both dialogs.<br>• A traversal host receives an 8-character **Room ID** (player-list drop-down; **Copy** puts it on the clipboard). The client field is "Host Code:".<br>• A traversal join from the same PC failed twice ("Could not communicate with host"). That is consistent with missing NAT loopback, but does not prove two networks would work.<br>• Host menu **Checksum → Current game** computes the SHA-1 per player and prints "The hashes match!". It gave `a30eca37…0309ace` for the project copy, equal to `DolphinTool verify`.<br>• Dolphin embeds its version as the NUL-terminated string `Dolphin 2609a` (used by the package launcher).<br>• When the client quits mid-game, the host chat shows "P2-Yellow has left" and **both games stop**. The room stays open. With "Load Host's Save Data Only" the host card is unchanged and the client used `GC/NetPlayTemp`. | NET-02 run (TESTING.md); strings in `Dolphin.exe` | RUNTIME (traversal join between two networks untested) |
| F-50 | **Netplay speed over the internet depends on the pad buffer.** First two-PC session (Traversal Server, ping 23–33 ms): with Buffer 5, both games were held to about 40 FPS/VPS in lockstep (stretched audio). Equal FPS on both PCs is expected in lockstep and does not identify the slow side. Buffer 26 restored 59.9 FPS/VPS; **Buffer 18 held a stable 58–60** (the recommended setting at this ping). Lower values were not tried. | user report with on-screen FPS/VPS/ping (TESTING.md NET-02) | RUNTIME (one session) |
| F-51 | **Phase-start cursor.**<br>• The turn-loop script runs **`0x8002E444`** in every phase (`.data` `0x80284EE8` and `0x80284F34`), just before the human-proc start `0x8002E738`.<br>• It acts only when **phase == 0** (`bne` at `0x8002E464`) and when bit 0x40 of `state+0x9E` is clear. That bit is probably the cursor option in Options (HYPOTHESIS).<br>• It walks the phase force's list for the first unit whose attribute bit 0 of the bit set at `unit+0x1BC` is set (`0x80105BC0`; probably the lord flag, i.e. Ike).<br>• It then moves the cursor with **`0x8014CBD8(state, f1 = x, f2 = y)`**, from `unit+0x19E/0x19F`.<br>• Next Unit (`0x800291D8`) uses the same move after `0x800AA5F0`.<br>• Vanilla therefore never moves the cursor at the start of the yellow phase; it stays where the blue phase left it (seen in NET-02). **EXP-20** takes the phase-3 path and uses `0x800AA5F0(0)` (yellow with EXP-17) instead of the lord bit. <br>• The cursor tile is stored as floats `x + 0.5` / `y + 0.5` at `state+0x524/0x528`, with copies at `+0x52C..0x538` (`0x8014CBD8`). | disassembly **[S]** (pinned); EXP-20 states | VERIFIED-STATIC + RUNTIME (EXP-20 passed; option-bit meaning HYPOTHESIS) |
| F-52 | **Save-persistent ownership storage: bits `0x20000000` / `0x40000000` of the unit flag word `unit+0x1A0`.**<br>• The card save writes each unit as a packed `UNIP` record. The writer `0x8003CA94…` and the loader `0x8003C8xx` (`0x8003C994`: `addi r5,r30,0x1a0` / `li r4,4` → `0x8017A810`) copy the 32-bit flag word **raw**. The other fields are copied byte by byte: `+0x199..0x19F`, status `+0x1A4`, HP/stats, weapon ranks `+0x1B4`, attribute set `+0x1BC`, items, `+0x20C`, `+0x214`, `+0x228`. Ike's record in the Ch. 3 file starts `0A 04 5B …` (class byte, Lv 4, 91 EXP) and appears once per save file, at 0x235A + 0x4000·k in the GCI.<br>• Across the 413 loads and stores of `+0x1A0` in the DOL, no narrow mask (andi./andis./ori/oris/rlwinm, ≤ 4 bits) within 8 instructions before or 10 after touches **bits 25–30** (`tools/draft_code.flag_bit_usage`). The known bits (0x1, 0x400, 0x8000, 0x10000, …) all show up.<br>• The flag-clearing masks keep bits 25–30: chapter transitions (`0x8002E038/E1AC/E33C`, AND `0xFF88C7FE`), map start (`0x8002EA10`, `0xFFFFBBFF`), `0x80050D1C` (`~0x241`) and `0x801D31F0` (`0xFFF77FFF`).<br>• Unit creation ORs data flags into the word (`0x8003BD0C`/`0x8003BF14`), so a new recruit starts with the bits clear (unassigned).<br>• Used as: `0x20000000` = assigned, `0x40000000` = owner Player 2 (EXP-21/EXP-22).<br>• Not yet excluded: the generic script commands at `0x800BD37C`/`0x800BD3D0` set or clear a script-supplied mask; scripts would need a literal ≥ `0x02000000`. | disassembly **[S]** (pinned); GCI vs state comparison; `test_ownership_flag_bits_unused` | VERIFIED-STATIC + RUNTIME (DRAFT-01 passed: chapter transition, save, fresh reload) |
| F-53 | **Draft input building blocks.**<br>• `0x800291D8` is the human-phase input step. The human proc `0x80284AC8` runs it every frame (label 1 loop).<br>• `0x800AA794` returns the unit under the cursor: the cursor floats → tile → map grid `0x802CA518 + x + 64·y`, byte `+0xD` = unit id.<br>• Raw per-port buttons are `PADStatus[port]` (`0x802EF408 + 12·port`, F-29), so each player's own controller can be read in any phase. L = 0x0040, R = 0x0020 (SDK layout).<br>• The sound effect `0x801475FC(0x80269070+0x138, 0x64)` is Next Unit's cursor sound (`0x800292BC`).<br>• **Prep screens** (F-46) run before ownership applies. The draft therefore happens on turn 1 of the blue phase, on the deployed units, and undeployed units cannot be drafted yet. | disassembly **[S]** | VERIFIED-STATIC |
| F-54 | **Native feedback available to the draft.**<br>• `0x801475FC(name, 0x64)` plays a sound **by name string** (`0x80269070+0x138` = `SFX_SYS_NOMOVE_UNIT_SELECT1`). The DOL holds the `SFX_SYS_*` names, e.g. `SFX_SYS_MISS1` `0x80269175`, `SFX_SYS_UNIT_SELECT1` `0x802691DF`, `SFX_SYS_UNIT_CANCEL1` `0x80269193`, `SFX_SYS_UNIT_CHANGE1` `0x802747B5`.<br>• Ring colour follows the force. Parking an unassigned unit in force 2 shows it green, and the human phase cannot select it (GetUnitSelectState returns 3, F-15).<br>• The phase banner and music come from the proc around `0x800AE6B0` (`E_PhaseChange`, `EID_PHASEPLAYER/PARTNER`), which picks both from the phase byte. Starting it mid-phase would also change the music, so the draft doesn't use it.<br>• The map cursor is the texture `etc/cursor.tpl`. What chooses its colour per phase is not yet found, so there is no "whose pick" cursor colour yet.<br>• The objective/turn windows draw message IDs from `system.cmp`/`mess/common.m` (e.g. `MD_TURN`, "Defeat boss"). Overriding them would need a hook in the message lookup (not attempted).<br>• **`0x80028C90`** (unit finished acting) sets the acted bit on `*0x802EF4C8` (the current unit) at `0x80028CBC`, then runs the auto-end check. EXP-23 unparks at `0x80028CC4`, between the two. | disassembly **[S]**; strings in the DOL | VERIFIED-STATIC |
| F-56 | **Deployment cap = sortie slots in the state block.** `SallySetByGroup` (`0x800B6D88` → `0x8014CF48`) stores 0 at `state+0x544` (`0x8014CF60`), then one (x, y) per entry of the chapter's `bmapNN_mikata_X` group at `state+0x545+2i` (`0x8014CCC0`). `SallyAddByGroup` (`0x8014CC5C`) appends. `SallyGetSurplus` returns `state+0x56` (`0x800B6DF8`). Ch6 prep runtime: `state+0x544` = 6 = the group's 6 entries. Caps per chapter and per difficulty file (`n/h/m/c`) and the forced PIDs are generated into docs/CHAPTER_AUDIT.md by `tools/chapter_audit.py`. Ch5 forces 9 PIDs (incl. Greil) with 8 entries, so entry count = cap is confirmed only where measured. | disassembly **[S]**; Ch6 prep state | VERIFIED-STATIC + RUNTIME (Ch6) |
| F-57 | **Pick Units = `E_SallyList`.**<br>• Proc `0x80291088`; steps include the shared list builder `0x8012DFA8` and the input step `0x8012D6A4`, which reads the current pad (`0x8012D6B8`).<br>• Its action callback **`0x8012C9E8` flips bit `0x80000000` of `unit+0x1A0`** (the sortie / "picked" flag); it is installed by `0x8012C9C0` (`obj+0x54`, mode `obj+0x6C` = 4).<br>• Row states come from the flags (`0x8012F060`, `0x8012F680`): `0x200000` → 3, `0x10` (away) → 0, `0x10000` (forced) → `0x13`.<br>• The map formation step is `BMapSallyProc`/`BMapSallyCursorProc`, with help messages `MESS_SALLY_HELP01…05` and `MESS_CONFIRM_EXIT_SALLY`.<br>• Bit `0x4000` is *not* a sortie flag: the escape worker sets it (`0x8003E894`).<br>• Integration plan: docs/PREP.md. | disassembly **[S]** (pinned); script-command table (406 commands, `0x80013AE8` registrations) | VERIFIED-STATIC |
| F-58 | **Pick Units at runtime (PREP-R1, Ch6 prep, Normal difficulty).**<br>• The preparations menu is: Choose Units, Reposition, View Map, Items, Conditions, Options, Save, Fight.<br>• Choose Units shows "You can select 1 more. 5/6" and the footer "A Charge On/Off · Status · B Back · Fight". All five names are drawn green (all forced in Ch6), and A on a row does nothing.<br>• **No unit has bit `0x80000000` while picked.** The flag the toggle `0x8012C9E8` flips therefore most likely means *benched* (HYPOTHESIS until a toggle is observed).<br>• **The list object is the `E_SallyList` proc instance** (here `0x802A7468`): `+0x38` column-pointer array (count `+0x6D`), `+0x3C` row records (0x24 bytes each, **unit pointer at +0**), `+0x60` force byte, `+0x61` row count, **`+0x62` highlighted row** (0 → 2 when moving Ike → Soren), `+0x6C` mode (1 in Pick Units).<br>• Cells are drawn by `0x8012EF5C` per column (column vtable `+0x4C` → `+0x1C`, mostly `0x8012F154`). r5 is a **colour index** into the text palette **`0x80296088`** (RGBA, `0x8018D900`; indices 0x13/0x14/0x22 animate): 0 grey, 1 white, 0x13 green (forced), 0x21 light blue `#6DCFF6`, 0x06 yellow `#FFFF64`.<br>• At Reposition (map formation), map start has already run: `0x4000` is cleared and `0x400` set on the force 0 units.<br>• The list's A press calls the action callback `obj+0x54` with unit = `*(obj+0x3C + obj[+0x62]·0x24)` (`0x8012DBE4…0x8012DBFC`), so `+0x62` is the absolute row. The list input range `0x8012D6A4…0x8012DFFF` tests only A, B, X, Y and Start (single-bit masks), so Z is free there. | PREP-R1 screenshots; states `work/saves/GFEE01.prepR1_s02..s04` (diffed); disassembly **[S]**; PREP-02 (EXP-25 colours correct on every data page) | RUNTIME + VERIFIED-STATIC |
| F-59 | **Gecko code space is limited, and overflow is silent.** Dolphin copies `Sys/codehandler.bin` (2880 bytes in 2609a) to `0x80001800` and writes the enabled Gecko codes after it, up to `0x80003000`. That leaves **≈ 3248 bytes** for the code list (code lines + C2 headers). Codes that don't fit are skipped with only a log message ("Too many GeckoCodes! Ran out of storage space in Game RAM. Could not write: …"; string in `Dolphin.exe`).<br>• Runtime: in PREP-03 run 1 (enabled total 4000 bytes) `0x8012D6A4` still held the original `stwu`: EXP-26, written after the others, was not installed. EXP-25, EXP-21 and EXP-22, written earlier, were.<br>• Earlier beds fit: NET-02 2536, DRAFT-01 2872, PREP-02 3016.<br>• The EXP-23 bed (3664) never fit, so DRAFT-02 couldn't have worked as installed.<br>• `install_codes`/`netplay_setup` now refuse an over-budget set and name the codes that would be lost (`test_gecko_budget`). | runtime state `work/saves/GFEE01.prep03_s02`; DRAFT-01/PREP-02 beds; Dolphin string | RUNTIME + VERIFIED-STATIC (budget ±16 bytes) |

### Event scripts (2026-10-27)

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-48 | **`.cmb` event scripts** (`Scripts/CNN.cmb`, NN = chapter id) are little-endian.<br>• Header: magic `cmb`, name, `+0x24` = string-pool start (`0x2C`), `+0x28` = a zero-terminated table of function-record offsets.<br>• The pool holds every command name the script calls and every PID it mentions.<br>• Bytecode seen: `1C xx` / `1D hh ll` push a pool string; `19 nn` pushes a small integer; **`38 hh ll nn` calls the command at pool offset `hhll` with `nn` arguments** (`1C 0A 38 00 12 01` = `UnitGetByPID("PID_IKE")` in C07).<br>• The `…ByPID` commands (`UnitEscapeByPID`, `UnitTransferToForceByPID`, `UnitForcedSallyByPID`) are not native registrations, so they are script helpers built on the native commands, and the EXP-16 hooks apply to them.<br>• `tools/chapter_audit.py` decodes every transfer call. Story transfers that touch the current Player-2 table: Ch3 and Ch4 bench Oscar and Boyd (→ 7, → 5); Ch5 → 5; Ch6, Ch8 and Ch17 send Shinon and Gatrie away (→ 7); Ch13 Gatrie → 7 → 0; **Ch18 Shinon → 7 → 0 → 1** (he can turn enemy).<br>• Other notable cases: Ch10 makes Kieran, Nephenee and Brom **temporary partners (→ 3)**; Ch20 Jill → 1; Ch22 Reyson → 6.<br>• Since EXP-16 only moves units out of force 0, story moves to 1/2/5/6/7 take priority; a story move back to 0 makes the unit yellow again at the next player phase. | `tools/chapter_audit.py` on all scripts; `test_script_transfer_decoding` | VERIFIED-STATIC (bytecode inferred from consistent call sites) |

### Starting Chapter 9 under Netplay (2026-10-27)

| ID | Finding | Evidence | Confidence |
|---|---|---|---|
| F-31 | **Netplay cannot start from a save state, and the slot 6 state cannot make a card save either.** (a) Dolphin 2609a contains the message "Loading savestates is disabled in Netplay to prevent desyncs", and three save-data modes: host's data kept, host's data discarded at session end, or no save data. (b) A *Suspend* chosen in the slot 6 state while booted on a different (empty) card was refused: "This is not the original Memory Card. Please insert the Memory Card that you used when you loaded the game." The game remembers the card it saw at boot, and that memory is inside the state. (c) The native route works: in a private user folder (`--user work/netplay/host`), a **fresh** game with EXP-05 (Easy), Prologue won, saved at the post-Prologue prompt to file 2. The title then lists **"Ch. 9: Gallia"**. A state at the base after that decodes as chapter id 10, turn 1. After a fresh boot without EXP-05, *Restart Chapter → Ch. 9* reaches the Chapter 9 base. The card is backed up in `work/saves/netplay_ch9_card/` (SHA-1 `d93a22ae…9086`). | strings in `Dolphin.exe`; screenshots; `work/netplay/host/StateSaves/GFEE01.s02` decoded | (a) VERIFIED-STATIC (runtime refusal not yet seen); (b), (c) RUNTIME |
| F-32 | Dolphin `--user <dir>` overrides `portable.txt`: the instance created and used `<dir>/Config`, `GC/USA/Card A` and `StateSaves`, and `Dolphin-x64/User` was not touched (the user's card SHA-1 is still `7afef93c…`). | file listing, hashes | RUNTIME |
| F-33 | Dolphin's DInput keyboard names the keypad keys `NUMPAD0`..`NUMPAD9` (strings in `Dolphin.exe`). The port 2 dialog loads `` `NUMPAD8` `` etc. and shows them as valid (not red) bindings. Pressing the keys has not been checked yet (computer use cannot send keypad keys). | strings; config dialog | VERIFIED-STATIC |

## 6. Open questions

1. EXP-01 runtime behaviour (see TESTING.md).
2. Which proc is `0x80284AC8` (human phase loop?), and does it hard-code force 0 anywhere (e.g. the End-turn menu, "all units moved" auto-end, phase banner)?
3. ~~Where does FE9 read controller input?~~ Answered by F-29 (current-pad pointer `0x80367240`). Still open: the role of `0x800CFE90` (reads pad 1's B press directly).
4. Is state+0x10 the chapter number? The JP warp codes write JP `0x8032E798` = JP state+0x10, which suggests yes.
5. Does the battle save or suspend data store `control[]`? If not, it is re-initialised on load (so the code must be re-applied, which a per-frame AR write does).
