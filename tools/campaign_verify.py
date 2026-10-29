"""Validate and render campaign evidence; never infer gameplay from static checks."""
import argparse
import hashlib
import json
import re
from pathlib import Path

STATUSES={"PASS","FAIL","INCONCLUSIVE","NOT TESTED"}
AXES=("static_cfg","script_model","fixture","event_runtime","chapter_clear","transition","save_reload","netplay_local","netplay_two_pc")
RUNTIME={"fixture","event_runtime","chapter_clear","transition","save_reload","netplay_local","netplay_two_pc"}


def validate(ledger):
    seen=set()
    for row in ledger["chapters"]:
        if row["key"] in seen: raise ValueError("duplicate chapter/stage key")
        seen.add(row["key"])
        for axis in AXES:
            claim=row["checks"][axis]
            if claim["status"] not in STATUSES: raise ValueError("unknown status")
            if claim["status"]=="PASS":
                if not claim.get("evidence"): raise ValueError("PASS requires evidence")
                run=ledger["runs"].get(claim["evidence"])
                if not run: raise ValueError("missing evidence run")
                if axis in RUNTIME:
                    if run["kind"] not in ("dolphin","netplay_local","netplay_two_pc"):
                        raise ValueError("static evidence cannot establish gameplay")
                    if axis.startswith("netplay") and run["kind"]!=axis:
                        raise ValueError("Netplay topology does not match claim")
                    if not all(run.get(k) for k in ("commit","fingerprint","dolphin","fixture_class","artifacts")):
                        raise ValueError("runtime evidence lacks provenance")
                    if axis in ("chapter_clear","transition") and run["fixture_class"]!="naturally_progressed":
                        raise ValueError("synthetic fixture cannot certify natural campaign completion")
                    for artifact in run["artifacts"]:
                        if not isinstance(artifact,dict) or not artifact.get("path") or not re.fullmatch(r"[0-9a-fA-F]{64}",artifact.get("sha256","")):
                            raise ValueError("runtime artifact requires a path and SHA-256")
                    if axis=="netplay_two_pc" and len(set(run.get("machines",[])))<2:
                        raise ValueError("two-PC evidence requires two distinct machine declarations")
                if row["key"] not in run.get("chapters", []) or axis not in run.get("axes", []):
                    raise ValueError("evidence scope does not cover this chapter/stage and axis")
    return ledger


def check_artifacts(ledger, root):
    """Check local bytes for runtime PASS claims; hashes do not prove semantics."""
    validate(ledger)
    checked = set()
    for row in ledger["chapters"]:
        for axis in RUNTIME:
            claim = row["checks"][axis]
            if claim["status"] != "PASS":
                continue
            for artifact in ledger["runs"][claim["evidence"]]["artifacts"]:
                path = Path(artifact["path"])
                path = path if path.is_absolute() else root / path
                if not path.is_file():
                    raise ValueError(f"missing evidence artifact: {path}")
                if hashlib.sha256(path.read_bytes()).hexdigest().lower() != artifact["sha256"].lower():
                    raise ValueError(f"evidence artifact hash mismatch: {path}")
                checked.add(path.resolve())
    return len(checked)


def evidence_level(axis, claim, run=None):
    """Readable scope labels derived from accepted evidence, never a score."""
    if claim['status'] != 'PASS':
        return {'FAIL': 'FAILED', 'NOT TESTED': 'UNTESTED',
                'INCONCLUSIVE': 'UNTESTED (inconclusive)'}.get(claim['status'], 'UNTESTED')
    if axis == 'static_cfg': return 'STATICALLY VERIFIED'
    if axis == 'script_model': return 'MODEL VERIFIED'
    if axis in ('netplay_local', 'netplay_two_pc'): return 'MULTIPLAYER VERIFIED'
    if run and run.get('fixture_class') == 'naturally_progressed': return 'NATURAL GAMEPLAY VERIFIED'
    return 'SYNTHETIC RUNTIME VERIFIED'


def coverage(ledger):
    validate(ledger)
    rows = []
    for chapter in ledger['chapters']:
        entries = {}
        for axis, claim in chapter['checks'].items():
            run = ledger['runs'].get(claim.get('evidence'))
            entries[axis] = {'level': evidence_level(axis, claim, run),
                             'status': claim['status'], 'evidence': claim.get('evidence'),
                             'limitation': claim.get('note', run.get('description', '') if run else '')}
        rows.append({'key': chapter['key'], 'title': chapter['title'], 'axes': entries})
    return rows


def render(ledger):
    validate(ledger)
    out=["# Campaign verification dashboard", "",
         "PASS applies only to the named axis and evidence configuration. Parser/model passes do not imply gameplay. "
         "Old release reports remain in TESTING.md and are not promoted here. A fixture is runnable only after acceptance, "
         "not merely because a file exists. Ch17 stages share a script; stage-specific map assignment is still unresolved.", "",
         "| Chapter/stage | CFG | Script model | Fixture | Original event | Cleared | Transition | Save/reload | Netplay local | Netplay two PCs |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for row in ledger["chapters"]:
        out.append("| "+row["title"]+" | "+" | ".join(row["checks"][a]["status"] for a in AXES)+" |")
    out += ['', '## Evidence classification (scope, not campaign completion)', '',
            'STATICALLY VERIFIED = local instruction CFG; MODEL VERIFIED = original script plus explicit modeled natives. '
            'SYNTHETIC RUNTIME VERIFIED includes copied fixtures whose full natural history is unproven. '
            'NATURAL GAMEPLAY VERIFIED requires declared naturally progressed evidence. '
            'MULTIPLAYER VERIFIED applies only to the named Netplay axis/topology. '
            'No aggregate percentage is meaningful while original events, clears and transitions remain open.', '',
            '| Chapter/stage | Script semantics | Local original event | Natural clear | Two-PC |',
            '|---|---|---|---|---|']
    for row in coverage(ledger):
        axes = row['axes']
        out.append('| ' + row['title'] + ' | ' + ' | '.join(axes[a]['level'] for a in
                   ('script_model', 'event_runtime', 'chapter_clear', 'netplay_two_pc')) + ' |')
    out += ["", "## Evidence runs", ""]
    for key,run in ledger["runs"].items():
        out.append(f"- **{key}**: `{run['kind']}`; {run.get('description','')}")
    out += ["", "## Highest-priority open cases", ""]
    out += ["- "+case for case in ledger["next_cases"]]
    out += ['', '## Explicitly blocked test preparation', '',
            'These are fixture/prerequisite blockers, not confirmed production gameplay defects. '
            'See CAMPAIGN_MANUAL_TESTS.md and the generated manual pack for capture protocols.', '']
    catalog = Path(__file__).resolve().parents[1] / 'campaign/manual_cases.json'
    if catalog.exists():
        for case in json.loads(catalog.read_text(encoding='utf-8')):
            readiness = case['readiness']
            if readiness.startswith(('BLOCKED', 'NEEDS_')):
                out.append(f"- **BLOCKED {case['id']}**: {readiness}; {case['title']}")
    for key, run in ledger['runs'].items():
        if run.get('status') == 'FAIL':
            out.append(f"- **FAILED diagnostic {key}**: rejected fixture/test; do not infer a campaign defect. {run.get('description', '')}")
    return "\n".join(out)+"\n"


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ledger",type=Path,default=Path("campaign/verification.json"))
    p.add_argument("--out",type=Path,default=Path("docs/VERIFICATION.md"))
    p.add_argument("--check-artifacts",action="store_true",help="verify local runtime PASS artifact bytes")
    p.add_argument("--artifact-root",type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--coverage-json', type=Path, help='write machine-readable derived evidence classifications')
    a=p.parse_args();ledger=validate(json.loads(a.ledger.read_text()))
    if a.check_artifacts:
        print(f"verified {check_artifacts(ledger,a.artifact_root)} local runtime evidence artifacts")
    a.out.write_text(render(ledger),encoding="utf-8")
    if a.coverage_json:
        a.coverage_json.parent.mkdir(parents=True, exist_ok=True)
        a.coverage_json.write_text(json.dumps(coverage(ledger), indent=2), encoding='utf-8')
    print(f"validated {len(ledger['chapters'])} chapter/stage records")
