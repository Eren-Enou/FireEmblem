"""Original call-site prerequisites versus accepted source states (read-only).

This is a gap report, not a loader or a solver. Chapter identity is necessary
but never sufficient. In particular, C18 and a request byte cannot prove a part.
"""
import hashlib
import json
from pathlib import Path
from tools.fe9.disc import DiscReader
from tools.fe9.events import functions,calls
from tools.verify_game import DEFAULT_IMAGE
from tools.campaign_test_pack import work_destination,write_json

CASES={
 'CH13-ASTRID-GATRIE':(14,('PID_STELLA','PID_GATRIE'),'Original Astrid/Ike and Astrid/Gatrie actors, conversation keys, allied ship/NPC state and original recruitment history.'),
 'CH17-STAGE-TRANSITIONS':(18,(),'Four distinct stage maps/objectives, stage-specific roster and turn/story history. C18/request5/6/7 alone is insufficient.'),
 'CH18-SHINON-REINFORCE':(19,('PID_CHINON','PID_TANIS'),'Original enemy Shinon/Rolf/Ike sequence and living Tanith with original Reinforce uses/skill. Fixed ownership cannot override enemy Shinon.'),
 'CH20-JILL-DEFECTION':(21,('PID_JILL','PID_SIHARAMU'),'Directed Jill/Shiharam event and actual support/story predicates; support query result3 versus non3 are separate branches.'),
 'CH27-2-SPECIAL':(29,('PID_IKE','PID_MIST'),'Original special encounter map, transition from Ch27/internal28, eligible Ike/Mist and special enemy/objective state.'),
 'ENDGAME-ENDING':(31,('PID_IKE',),'Original final map, difficulty/story-specific boss phase, eligible damage/forced deployment and complete ending/roster history.'),
}


def report(snapshots):
    sources=[]
    for path in snapshots:
        snap=json.loads(path.read_text(encoding='utf-8'));g=snap['game']
        sources.append(dict(path=str(path),state_sha256=snap['evidence']['state_sha256'],chapter=g['chapter'],
                            scripts=g.get('event_scripts',{}),units=g['units']))
    rows=[]
    with DiscReader(DEFAULT_IMAGE) as disc:
        for name,(chapter,actors,requirements) in CASES.items():
            path=f'Scripts/C{chapter:02d}.cmb';raw=disc.read_file(path);fs=functions(raw);cs=calls(raw)
            selected={c['function'] for c in cs if any(a in c['args'] for a in actors)}
            if chapter==18:selected|={82,85,88}
            relevant=[dict(scene=c['function'],offset=c['offset'],command=c['command'],arguments=c['args']) for c in cs
                      if c['function'] in selected and (c['command'].startswith(('Unit','BM','Complete','Map','Join')) or c['command'] in ('get','set','PersonGetYellLevel','Maniac'))]
            maps=[dict(scene=c['function'],command=c['command'],arguments=c['args']) for c in cs if c['command']=='MapLoad']
            matches=[s['path'] for s in sources if s['chapter']==chapter and s['scripts'].get('complete_chain') and s['scripts'].get('campaign_ids')==[chapter]]
            rows.append(dict(scenario=name,chapter_internal=chapter,script=path,script_sha256=hashlib.sha256(raw).hexdigest(),
                status='BLOCKED',runnable=False,matching_source_candidates=matches,
                reason='No accepted original chapter/map/history source in the selected evidence set.' if not matches else 'Chapter match requires independent map, actor, flag and original history validation.',
                required_history=requirements,original_map_calls=maps,
                directed_conversations=[dict(scene=f.index,**f.trigger(raw)['conversation_event']) for f in fs if 'conversation_event' in f.trigger(raw)],
                original_relevant_calls=relevant,
                scope='Original instruction-aligned call sites/condition inputs; execution/activation and native side effects are unresolved. No chapter byte, recruitment or outcome is edited.'))
    return dict(status='BLOCKED',sources=[{k:v for k,v in s.items() if k!='units'} for s in sources],cases=rows)


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('snapshots',type=Path,nargs='+');p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();out=work_destination(a.out);out.parent.mkdir(parents=True,exist_ok=True)
    data=report(a.snapshots);write_json(out,data)
    print(json.dumps(dict(written=str(out),cases=[dict(scenario=r['scenario'],status=r['status'],original_call_sites=len(r['original_relevant_calls'])) for r in data['cases']]),indent=2))
