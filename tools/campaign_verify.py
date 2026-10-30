"""Validate and render campaign evidence; never infer gameplay from static checks."""
import argparse
import hashlib
import json
import re
from pathlib import Path

STATUSES={"PASS","FAIL","INCONCLUSIVE","NOT TESTED"}
AXES=("static_cfg","script_model","fixture","event_runtime","chapter_clear","transition","save_reload","netplay_local","netplay_two_pc")
RUNTIME={"fixture","event_runtime","chapter_clear","transition","save_reload","netplay_local","netplay_two_pc"}
LIFECYCLE=('conversation','temporary_transfer','permanent_recruitment','rescue','combat','escape','roster_cleanup',
           'death_absence','stage_transition','chapter_completion','next_chapter_initialization',
           'save_reload','native_save','native_reload','ownership','netplay')


def runtime_provenance(run):
    if run.get('status') == 'FAIL': raise ValueError('failed diagnostic cannot establish runtime PASS')
    if not all(run.get(k) for k in ('commit','fingerprint','dolphin','fixture_class','artifacts')):
        raise ValueError('runtime evidence lacks provenance')
    for artifact in run['artifacts']:
        if not isinstance(artifact,dict) or not artifact.get('path') or not re.fullmatch(r'[0-9a-fA-F]{64}',artifact.get('sha256','')):
            raise ValueError('runtime artifact requires a path and SHA-256')
    if run['kind']=='netplay_two_pc' and len(set(run.get('machines',[])))<2:
        raise ValueError('two-PC evidence requires two distinct machine declarations')


def accepted_runtime_runs(ledger):
    """Named accepted axes AND explicitly scoped lifecycle-only runs."""
    return {claim['evidence'] for row in ledger['chapters']
            for claim in [*row['checks'].values(),*row.get('lifecycle',{}).values()]
            if claim['status']=='PASS' and
            ledger['runs'][claim['evidence']]['kind'] in ('dolphin','netplay_local','netplay_two_pc')}


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
                    if axis in ("chapter_clear","transition") and run.get('fixture_class') and run['fixture_class']!="naturally_progressed":
                        raise ValueError("synthetic fixture cannot certify natural campaign completion")
                    runtime_provenance(run)
                if row["key"] not in run.get("chapters", []) or axis not in run.get("axes", []):
                    raise ValueError("evidence scope does not cover this chapter/stage and axis")
        for behavior, claim in row.get('lifecycle', {}).items():
            if behavior not in LIFECYCLE or claim['status'] not in STATUSES | {'BLOCKED'}:
                raise ValueError('unknown lifecycle behavior/status')
            if claim['status'] == 'BLOCKED' and not claim.get('scope'):
                raise ValueError('blocked lifecycle requires precise scope/reason')
            if claim['status'] == 'PASS':
                run = ledger['runs'].get(claim.get('evidence'))
                if not run or row['key'] not in run.get('chapters', []) or not claim.get('scope'):
                    raise ValueError('lifecycle PASS requires scoped chapter evidence')
                if run['kind'] not in ('static','script_model','dolphin','netplay_local','netplay_two_pc'):
                    raise ValueError('unknown lifecycle evidence kind')
                if run['kind'] in ('dolphin','netplay_local','netplay_two_pc') and not any(
                        c['status']=='PASS' and c.get('evidence')==claim['evidence'] for c in row['checks'].values()):
                    if behavior not in run.get('lifecycle',[]):
                        raise ValueError('runtime lifecycle must reuse accepted/hash-validated axis evidence or declare exact lifecycle scope')
                    runtime_provenance(run)
    return ledger


def check_artifacts(ledger, root):
    """Check local bytes for runtime PASS claims; hashes do not prove semantics."""
    validate(ledger)
    checked = set()
    for run_id in accepted_runtime_runs(ledger):
        for artifact in ledger['runs'][run_id]['artifacts']:
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
        behaviors = {}
        for name in LIFECYCLE:
            claim = chapter.get('lifecycle', {}).get(name, {'status': 'NOT TESTED'})
            run = ledger['runs'].get(claim.get('evidence'))
            if claim['status'] == 'BLOCKED': level = 'BLOCKED'
            elif claim['status'] != 'PASS': level = evidence_level('event_runtime', claim)
            elif run['kind'] == 'static': level = 'STATICALLY VERIFIED'
            elif run['kind'] == 'script_model': level = 'MODEL VERIFIED'
            else: level = evidence_level('netplay_two_pc' if run['kind'].startswith('netplay') else 'event_runtime', claim, run)
            behaviors[name] = {'level': level, 'evidence': claim.get('evidence'), 'scope': claim.get('scope', '')}
        rows.append({'key': chapter['key'], 'title': chapter['title'], 'axes': entries, 'lifecycle': behaviors})
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
    out += ['', '## Lifecycle evidence (independent of whole-chapter acceptance)', '',
            'Unlisted behaviors/chapters are UNTESTED. MODEL VERIFIED never establishes native persistence. '
            'BLOCKED identifies unavailable evidence/setup, not a reproduced gameplay defect.', '',
            '| Chapter/stage | Behavior | Level | Evidence | Exact scope or blocker |', '|---|---|---|---|---|']
    for row in coverage(ledger):
        for name, claim in row['lifecycle'].items():
            if claim['level'] != 'UNTESTED':
                out.append(f"| {row['title']} | {name} | {claim['level']} | {claim['evidence'] or '-'} | {claim['scope']} |")
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
