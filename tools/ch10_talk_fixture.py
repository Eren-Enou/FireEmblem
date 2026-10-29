"""Prepare an isolated Ch10 Talk fixture or inspect user-captured evidence.

Never launches Dolphin or sends input. Never writes the source profile/card/state.
The only synthetic gameplay setup is original UnitSetPos for Oscar inside the
unchanged cell. Actual Talk execution and dialogue must be observed manually.
"""
import argparse
import hashlib
import json
from pathlib import Path
from tools.install_codes import ROOT,validate_ini
from tools.campaign_snapshot import capture
from tools.ch10_talk_code import ini,words,HOOK,OSCAR_FROM,OSCAR_TO,KIERAN_XY,KEY
from tools.talk_evidence import DOOR_KEY
from tools.netplay_package import fingerprint
from tools.netplay_setup import make_user
from tools.setup_pads import PORT1_KEYBOARD,PORT2_KEYBOARD
from tools.verify_game import DEFAULT_IMAGE


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def only_unit(snapshot,pid):
    found=[u for u in snapshot["game"]["units"] if u["pid"]==pid]
    if len(found)!=1:raise ValueError(f"requires exactly one {pid}")
    return found[0]


def preconditions(snapshot,*,positioned=False):
    """Necessary local checks only; not an assertion that Talk is available."""
    game,e=snapshot["game"],snapshot["evidence"]
    failures=[]
    expected_phase=3 if positioned else 0
    if (game["chapter"],game["phase"],game["turn"])!=(11,expected_phase,1):
        failures.append("requires Chapter10 turn1 and expected Blue/Yellow phase")
    if game["control"][3]!=1:failures.append("Yellow control must be human")
    scripts=game.get("event_scripts",{})
    if not scripts.get("complete_chain") or scripts.get("campaign_ids")!=[11] or not scripts.get("chapter_matches"):
        failures.append("loaded C11 container not verified")
    if not e.get("intended_c2_verified"):failures.append("all intended C2 bodies must match live RAM")
    codes={n.split()[0] for n in e["codes"]}
    expected={"COOP-P6","EXP-16","FIXTURE-LOADER"}
    if positioned:expected.add("DBG-CAMP-TALK")
    if codes!=expected:failures.append("unexpected code selection")
    local=game.get("talk_fixture",{})
    if local.get("map_dimensions")!=[24,23]:failures.append("unexpected prison map dimensions")
    context=local.get("menu_context",{})
    if context.get("mode12")!=0 or type(context.get("flags16")) is not int or context["flags16"]&1:
        failures.append("native Talk context gates are blocked/unverified")
    door=local.get("cell_door")
    if not door or door.get("bounds")!=[19,14,19,14] or door.get("state_byte",3)&3:
        failures.append("original closed cell-door object not verified")
    flags=local.get("flags",{})
    for name in (KEY,DOOR_KEY,"F1914","gf_complete","gf_gameover"):
        if flags.get(name) is not False:failures.append(f"required clear flag: {name}")
    for pid,force,xy in (("PID_OSCAR",3,OSCAR_TO if positioned else OSCAR_FROM),("PID_KEVIN",2,KIERAN_XY)):
        try:u=only_unit(snapshot,pid)
        except ValueError as exc:failures.append(str(exc));continue
        if u["force"]!=force or u["xy"]!=list(xy):failures.append(f"{pid}: faction/position differs")
        if u["hp"]<=0 or u["death_record"] or u.get("rescue_link")!=0:failures.append(f"{pid}: must be alive and unrescued")
        if pid=="PID_OSCAR" and (u["flags"]&1 or type(u.get("action_state_byte")) is not int or u["action_state_byte"]&0x70):
            failures.append("Oscar has acted or has a blocking native action-state gate")
    cells={tuple(c["xy"]):c for c in local.get("cells",[])}
    for xy,mask in (((19,19),2),((20,19),1)):
        if xy not in cells or not cells[xy]["edge_mask"]&mask:
            failures.append("chosen inside-cell Talk edge is blocked/unverified")
    try:
        oscar,kieran=only_unit(snapshot,"PID_OSCAR"),only_unit(snapshot,"PID_KEVIN")
        occupant=cells.get((19,19),{}).get("occupant_id")
        valid_occupancy=occupant==0 if not positioned else (
            occupant==oscar["slot"] or (occupant==0 and context.get("actor_slot")==oscar["slot"]))
        # The original Talk enumerator reads neighboring occupants, not an
        # actor entry at its own tile. In the action-menu capture Oscar is
        # selected in context while his grid entry is temporarily empty.
        if not valid_occupancy:
            failures.append("Oscar destination occupancy differs")
        if cells.get((20,19),{}).get("occupant_id")!=kieran["slot"]:
            failures.append("Kieran occupancy does not match roster identity")
    except ValueError:pass
    return failures


def create(source_root,root):
    source_root,root=source_root.resolve(),root.resolve()
    workspace=(ROOT/"work").resolve()
    if workspace not in source_root.parents or workspace not in root.parents or root.exists():
        raise ValueError("requires existing source and NEW destination inside this clone's work/")
    if source_root in root.parents or root in source_root.parents:
        raise ValueError("new fixture must be separate from source profile")
    source=source_root/"start.s02.sav"
    config=source_root/"User/GameSettings/GFEE01.ini"
    cards=sorted((source_root/"User/GC/USA/Card A").glob("*.gci"))
    if not source.is_file() or not config.is_file() or not cards:raise ValueError("source start/config/card missing")
    protected={str(p):sha(p) for p in source_root.rglob("*") if p.is_file()}
    base=config.read_text()
    snapshot=capture(source,DEFAULT_IMAGE,config,"source-user-validated")
    failures=preconditions(snapshot)
    if failures:raise ValueError("source fixture rejected: "+"; ".join(failures))
    generated,size=ini(base)
    # Every native address used here is pinned in check_signatures (CAMP-011).
    from tools.fe9.disc import DiscReader
    from tools.fe9.ppc import Dol
    from tools.fixture_position_code import ORIGINAL
    with DiscReader(DEFAULT_IMAGE) as disc:
        if Dol(disc.read_dol()).u32(HOOK)!=ORIGINAL:raise ValueError("setup hook signature differs")
    root.mkdir(parents=True,exist_ok=False)
    make_user(root/"User",DEFAULT_IMAGE.parent,"EXPERIMENTAL Ch10 Talk",PORT1_KEYBOARD,generated,pad2=PORT2_KEYBOARD)
    # Copy bindings only; do not inherit personal paths or mutate the source config.
    bindings=source_root/"User/Config/GCPadNew.ini"
    if bindings.exists():(root/"User/Config/GCPadNew.ini").write_bytes(bindings.read_bytes())
    for card in cards:
        with (root/"User/GC/USA/Card A"/card.name).open("xb") as stream:stream.write(card.read_bytes())
    with (root/"source-start.s02.sav").open("xb") as stream:stream.write(source.read_bytes())
    from tools.fixture_state import create as append
    seed=root/"seed.s02.sav"
    record=append(source,seed,base_ini=base,fixture_ini=generated,setup_hook=HOOK,setup_words=words(),
                  classification="synthetic_ch10_inside_cell_talk")
    (root/"source-snapshot.json").write_text(json.dumps(snapshot,indent=2,ensure_ascii=False),encoding="utf-8")
    changed=[p for p,h in protected.items() if sha(Path(p))!=h]
    if changed:raise ValueError("source changed concurrently: "+", ".join(changed))
    manifest={"classification":"synthetic_ch10_inside_cell_talk","setup_status":"NOT TESTED",
              "conversation_status":"NOT TESTED","gecko_bytes":size,"budget_bytes":3248,
              "fingerprint":fingerprint(generated),"source_files_sha256":protected,
              "seed_sha256":sha(seed),"source_state_sha256":sha(source),
              "positioning":{"oscar_from":OSCAR_FROM,"oscar_to":OSCAR_TO,"kieran_unchanged":KIERAN_XY},
              "door":{"xy":[19,14],"unchanged":True,"source_flags_clear":["F1914",DOOR_KEY]},
              "evidence":"source fields/geometry checked; runtime UnitSetPos and original Talk pending human test",
              "limitations":["synthetic loader and inside-cell placement skip earlier campaign, combat and door access",
                             "no Kieran force/recruitment/key/completion write or Talk invocation in setup",
                             "temporary force3 membership is not permanent recruitment or chapter cleanup proof",
                             "no clear/transition/save/reload/Netplay acceptance"]}
    (root/"fixture.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf-8")
    # User-run only. No invocation of Dolphin or UI automation occurs in this tool.
    workspace_ps=str(ROOT).replace("'","''")
    (root/"Launch.ps1").write_text(
        "$ErrorActionPreference = 'Stop'\n$workspaceRoot = '"+workspace_ps+"'\n"
        "$exe = Join-Path $workspaceRoot 'Dolphin-x64/Dolphin.exe'\n"
        "$image = Join-Path $workspaceRoot 'Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso'\n"
        "$privateUser = Join-Path $PSScriptRoot 'User'\n$seed = Join-Path $PSScriptRoot 'seed.s02.sav'\n"
        "& $exe --user $privateUser --exec $image --save_state $seed\n",encoding="utf-8")
    return manifest


def verify(before,after,observed=False):
    failures=preconditions(before,positioned=True)
    for key in ("commit","dolphin","codes_fingerprint"):
        if before["evidence"].get(key)!=after["evidence"].get(key):failures.append("evidence mismatch: "+key)
    hashes=[s["evidence"].get("state_sha256") for s in (before,after)]
    if not all(hashes) or hashes[0]==hashes[1]:failures.append("distinct captured state hashes required")
    if not after["evidence"].get("intended_c2_verified"):failures.append("after: live C2 bodies not verified")
    if before["evidence"].get("codes")!=after["evidence"].get("codes"):failures.append("after: code names differ")
    a,b=before["game"],after["game"]
    if (b["chapter"],b["phase"],b["turn"])!=(11,3,1):failures.append("after: expected same Chapter10 turn1 Yellow")
    if b["control"][3]!=1:failures.append("after: Yellow human control changed")
    if (not b.get("event_scripts",{}).get("complete_chain") or b.get("event_scripts",{}).get("campaign_ids")!=[11]
        or not b.get("event_scripts",{}).get("chapter_matches")):
        failures.append("after: loaded C11 script differs")
    flags=b.get("talk_fixture",{}).get("flags",{})
    if b.get("talk_fixture",{}).get("cell_door")!=a["talk_fixture"].get("cell_door"):
        failures.append("cell-door object changed")
    if flags.get(KEY) is not True:failures.append("original conversation key not set")
    for name in (DOOR_KEY,"F1914","gf_complete","gf_gameover"):
        if flags.get(name) is not False:failures.append("unexpected door/chapter flag: "+name)
    if sorted((u["slot"],u["pid"]) for u in a["units"])!=sorted((u["slot"],u["pid"]) for u in b["units"]):
        failures.append("roster slot/PID identities changed")
    after_slots={u["slot"]:u for u in b["units"]}
    for old in a["units"]:
        if old["pid"] in ("PID_OSCAR","PID_KEVIN"):continue
        new=after_slots.get(old["slot"],{})
        for key in ("pid","force","xy","hp","level","exp","class","inventory_slots_hex","rescue_link"):
            if old.get(key)!=new.get(key):failures.append("unrelated roster state changed: "+old["pid"]+" "+key)
    deltas=[]
    for pid in ("PID_OSCAR","PID_KEVIN"):
        try:old,new=only_unit(before,pid),only_unit(after,pid)
        except ValueError as exc:failures.append(str(exc));continue
        for key in ("slot","pid","class","hp","level","exp","xy","inventory_slots_hex","rescue_link"):
            if key not in old or old.get(key)!=new.get(key):failures.append(pid+": not preserved "+key)
        if new["force"]!=3 or new["hp"]<=0 or new["death_record"]:
            failures.append(pid+": after must be alive in Yellow force3")
        if len(old.get("inventory_slots_hex",""))!=128:failures.append(pid+": raw inventory evidence missing")
        deltas.append({"pid":pid,"before":old,"after":new})
    previous_flags=a.get("talk_fixture",{}).get("flags",{})
    changed_flags={k:[previous_flags.get(k),v] for k,v in flags.items() if previous_flags.get(k)!=v}
    return {"status":"FAIL" if failures else "PASS" if observed else "INCONCLUSIVE",
            "failures":failures,"observed_original_talk":observed,
            "classification":"synthetic_ch10_inside_cell_talk","units":deltas,"flag_changes":changed_flags,
            "scope":"original Oscar/Kieran Talk local state effect only; human observation required",
            "excludes":["door opening/access","combat traversal","permanent recruitment","chapter clear/transition","save/reload","Netplay"]}


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest="mode",required=True)
    prepare=sub.add_parser("prepare");prepare.add_argument("--source",type=Path,required=True);prepare.add_argument("--root",type=Path,required=True)
    check=sub.add_parser("check-setup");check.add_argument("state",type=Path);check.add_argument("--ini",type=Path,required=True)
    compare=sub.add_parser("compare");compare.add_argument("before",type=Path);compare.add_argument("after",type=Path)
    compare.add_argument("--ini",type=Path,required=True);compare.add_argument("--observed-original-talk",action="store_true")
    args=p.parse_args()
    if args.mode=="prepare":result=create(args.source,args.root)
    elif args.mode=="check-setup":
        snapshot=capture(args.state,DEFAULT_IMAGE,args.ini,"manual-test-analysis")
        failures=preconditions(snapshot,positioned=True)
        result={"status":"FAIL" if failures else "PASS","failures":failures,
                "scope":"synthetic placement/preconditions only; original Talk NOT TESTED"}
    else:
        before=capture(args.before,DEFAULT_IMAGE,args.ini,"manual-test-analysis")
        after=capture(args.after,DEFAULT_IMAGE,args.ini,"manual-test-analysis")
        result=verify(before,after,args.observed_original_talk)
    print(json.dumps(result,indent=2,ensure_ascii=True))
    return int(result.get("status") in ("FAIL","INCONCLUSIVE"))


if __name__=="__main__":raise SystemExit(main())
