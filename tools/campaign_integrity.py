"""Re-audit saved Gecko hook paths without launching Dolphin or editing evidence.

Hash-valid evidence may predate stricter hook checks. This independently decodes
accepted raw states, using the run's declared configuration fingerprint. Missing
configuration is INCONCLUSIVE; no successful campaign result is inferred.
"""
import argparse
import json
import re
import struct
from pathlib import Path
from tools.install_codes import ROOT,build_ini,validate_ini
from tools.campaign_verify import validate,check_artifacts,RUNTIME
from tools.campaign_snapshot import verify_live_hooks
from tools.campaign_test_pack import sha,write_json,work_destination
from tools.netplay_package import fingerprint


def configurations(state,expected):
    """Only exact recorded fingerprint matches; never guess a near-enough INI."""
    paths=(state.parent/'GFEE01.ini',state.parent/'accepted-config.ini',
           state.parent/'User/GameSettings/GFEE01.ini')
    for path in paths:
        if path.is_file():
            text=path.read_text()
            if fingerprint(text)==expected:
                return text,str(path)
    stable=build_ini(['COOP-P6','EXP-16'],verbose=False)
    if fingerprint(stable)==expected:return stable,'generated unchanged stable COOP-P6 + EXP-16'
    return None,None


def accepted(ledger,root=ROOT):
    validate(ledger)
    count=check_artifacts(ledger,root)
    runs={claim['evidence'] for row in ledger['chapters'] for axis,claim in row['checks'].items()
          if axis in RUNTIME and claim['status']=='PASS'}
    states={}
    for run_id in sorted(runs):
        run=ledger['runs'][run_id]
        for artifact in run['artifacts']:
            path=Path(artifact['path']);path=path if path.is_absolute() else root/path
            if path.suffix.lower()!='.sav' and not re.fullmatch(r'\.s\d{2}',path.suffix.lower()):continue
            key=(path.resolve(),run['fingerprint'])
            if key not in states:states[key]=dict(path=path,expected=run['fingerprint'],sha256=artifact['sha256'],runs=[])
            states[key]['runs'].append(run_id)
    results=[]
    for row in states.values():
        text,source=configurations(row['path'],row['expected'])
        if text is None:
            result=dict(status='INCONCLUSIVE',failures=[],reason='No exact recorded configuration fingerprint available')
        else:
            size=validate_ini(text)
            result=verify_live_hooks(row['path'],text)
            result.update(configuration_source=source,gecko_bytes=size)
        if sha(row['path']).lower()!=row['sha256'].lower():raise ValueError('evidence changed during audit')
        results.append(dict(path=str(row['path']),state_sha256=row['sha256'],fingerprint=row['expected'],runs=row['runs'],**result))
    return dict(accepted_artifacts_hash_verified=count,raw_states=results,
                status='FAIL' if any(r['status']=='FAIL' for r in results) else 'INCONCLUSIVE' if not results or any(r['status']!='PASS' for r in results) else 'PASS',
                scope='Accepted saved C2 entry/body/return integrity only; existing gameplay scope unchanged; full campaign remains unverified')


def candidates(root):
    from tools.test_scenario import NEXT,scenario_dir,check,review
    result=[]
    for name in NEXT:
        dest=scenario_dir(name,root)
        verdict=review(dest)
        try:
            plan=check(name,root=root)
        except ValueError as exc:
            result.append(dict(scenario=name,status='INCONCLUSIVE',launch_refused=True,
                               reason=str(exc),runtime=verdict['status']))
            continue
        native=name=='CH7-PLAYER2-CONTROL'
        state=dest/('source.sav' if native else 'seed.s02.sav')
        ini=dest/'source.ini' if native else dest/'User/GameSettings/GFEE01.ini'
        record=verify_live_hooks(state,ini.read_text())
        result.append(dict(scenario=name,launch_gecko_bytes=plan['gecko_bytes'],
                           inspection_only=native,runtime=verdict['status'],**record))
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ledger',type=Path,default=ROOT/'campaign/verification.json')
    p.add_argument('--include-candidates',action='store_true')
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    try:
        out=work_destination(args.out)
        result=accepted(json.loads(args.ledger.read_text(encoding='utf-8')))
        if args.include_candidates:
            result['candidates']=candidates(ROOT/'work/scenarios/human_v1')
            if any(r['status']=='FAIL' for r in result['candidates']):result['status']='FAIL'
            elif any(r['status']!='PASS' for r in result['candidates']):result['status']='INCONCLUSIVE'
        out.parent.mkdir(parents=True,exist_ok=True);write_json(out,result)
        summary=dict(status=result['status'],accepted_artifacts=result['accepted_artifacts_hash_verified'],
                     raw_states=len(result['raw_states']),hooks=sum(len(r.get('hooks',[])) for r in result['raw_states']),
                     candidates=len(result.get('candidates',[])),written=str(out),scope=result['scope'])
        print(json.dumps(summary,indent=2))
        return int(result['status']=='FAIL')
    except (ValueError,OSError,KeyError,struct.error,RuntimeError) as exc:
        print(json.dumps(dict(status='REFUSED',reason=str(exc))));return 1


if __name__=='__main__':raise SystemExit(main())
