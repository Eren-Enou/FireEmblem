"""Original campaign connection graph; not a certified gameplay route.

Scene declarations/local call reachability are static. Unresolved native
dispatch, chapter gates and persistence remain explicit blocked connections.
"""
import argparse
from collections import deque
import hashlib
import json
from pathlib import Path

from tools.fe9.disc import DiscReader
from tools.fe9.events import functions, calls
from tools.verify_game import DEFAULT_IMAGE
from tools.install_codes import ROOT
from tools.campaign_verify import validate

INTEREST = ('MapLoad', 'Escape', 'TransferToForce', 'Sally', 'Join', 'UnitsPush', 'UnitsPop',
            'Dead', 'Complete18', 'BMSetTurn', 'BMSetPhase', 'Save', 'Chapter')


def build(disc, ledger):
    validate(ledger)
    nodes, edges, scripts = {}, [], {}

    def node(identifier, **data): nodes[identifier] = {'id': identifier, **data}; return identifier
    def edge(source, target, kind, *, unresolved=False, **data):
        edges.append({'source': source, 'target': target, 'kind': kind,
                      'level': 'UNRESOLVED' if unresolved else 'STATICALLY VERIFIED', **data})

    rows = {r['key']: r for r in ledger['chapters']}
    for path in disc.files():
        if not path.startswith('Scripts/') or not path.endswith('.cmb'): continue
        raw = disc.read_file(path); fs = functions(raw)
        scripts[path] = {'sha256': hashlib.sha256(raw).hexdigest(), 'scenes': len(fs)}
        node(path, type='script_container', script_sha256=scripts[path]['sha256'])
        for f in fs:
            sid = f'{path}:scene:{f.index}'
            node(sid, type='scene', script=path, index=f.index, name=f.name, trigger=f.trigger(raw))
            edge(path, sid, 'declares_scene', scope='record exists; activation/order not proven')
        for call in calls(raw):
            if not any(name in call['command'] for name in INTEREST): continue
            cid = f"{path}:call:{call['offset']:X}"
            node(cid, type='call_site', script=path, scene=call['function'], offset=call['offset'],
                 command=call['command'], arguments=call['args'],
                 argument_scope=call['argument_status'])
            edge(f"{path}:scene:{call['function']}", cid, 'local_cfg_call',
                 scope='reachable in local instruction CFG, not necessarily executed')
            boundary = 'operation:' + call['command']
            if boundary not in nodes: node(boundary, type='operation_boundary', command=call['command'])
            edge(cid, boundary, 'requires_operation_effect', unresolved=True,
                 scope='native/helper effects require separate bounded model or runtime evidence')

    for key, row in rows.items():
        internal = int(key.split('.')[0]); container = f'Scripts/C{internal:02d}.cmb'
        chapter = 'chapter:' + key
        node(chapter, type='chapter_contract', key=key, title=row['title'], script=container,
             acceptance=row['checks'], lifecycle=row.get('lifecycle', {}))
        edge(chapter, container, 'identified_script_container',
             scope='internal identity only; acceptance fields are scoped, not transitive edge proof')
        # Do not link numbered chapters as if a script had called the next one.
        step = 'native_chapter_step:' + key
        node(step, type='native_transition_gate', chapter=key, reference='RESEARCH F-38/CAMP-019')
        edge(chapter, step, 'unresolved_completion_dispatch', unresolved=True,
             scope='original objective, ending activation and transition preconditions remain required')
        if internal not in (28, 31) and '.' not in key:
            target = f'Scripts/C{internal+1:02d}.cmb'
            if target in nodes:
                edge(step, target, 'conditional_native_increment_target',
                     guard='normal 0x8002E210..234 branch reached; chapter28 special path excluded',
                     scope='native current+1 arithmetic, not proof that this chapter finishes')
        else:
            unknown = 'unknown_next:' + key
            node(unknown, type='unresolved_boundary', reason='part dispatch/special chapter/ending requires independent trace')
            edge(step, unknown, 'unresolved_next_target', unresolved=True)

    for part in (1, 2, 3):
        key = '18.' + str(part)
        scene = {1: 82, 2: 85, 3: 88}[part]
        edge('chapter:' + key, f'Scripts/C18.cmb:scene:{scene}', 'original_complete18_call_site',
             scope='literal Complete18 argument identifies completion contract; event activation still unknown')
        request = f'complete18_request:{part+4}'
        node(request, type='native_sequence_request', complete18_argument=part, request_byte=part+4)
        edge(f'Scripts/C18.cmb:scene:{scene}', request, 'literal_native_request_contract',
             scope='CAMP-018; full scene/native sequence execution not inferred')
        unknown = f'unresolved_part_dispatch:{part}'
        node(unknown, type='unresolved_boundary', reason='native sequence/map/phase/ownership handoff not executed')
        edge(request, unknown, 'unresolved_part_dispatch', unresolved=True)
    for part, scene in ((2, 83), (3, 86), (4, 89)):
        edge('chapter:18.' + str(part), f'Scripts/C18.cmb:scene:{scene}', 'original_named_part_opening',
             scope='Opening18_2/3/4 metadata and bytecode; prior request dispatch remains unresolved')
    return {'schema': 1, 'nodes': nodes, 'edges': edges, 'scripts': scripts,
            'scope': 'static connections + explicit unresolved boundaries; ledger acceptance does not propagate along edges'}


def route(graph, source, target, *, allow_unresolved=False):
    if source not in graph['nodes'] or target not in graph['nodes']:
        raise ValueError('unknown graph endpoint')
    adjacency = {}
    for edge in graph['edges']:
        if not allow_unresolved and edge['level'] == 'UNRESOLVED': continue
        adjacency.setdefault(edge['source'], []).append(edge)
    pending, seen = deque([(source, [])]), {source}
    while pending:
        current, path = pending.popleft()
        if current == target:
            return {'status': 'INCONCLUSIVE' if any(e['level']=='UNRESOLVED' for e in path) else 'STATIC CONNECTION ONLY',
                    'path': path, 'scope': 'connection query, never a gameplay completion result'}
        for edge in adjacency.get(current, []):
            if edge['target'] not in seen:
                seen.add(edge['target']); pending.append((edge['target'], path+[edge]))
    return {'status': 'NO ESTABLISHED PATH', 'path': [],
            'unresolved_frontier': [e for e in graph['edges'] if e['source'] in seen and e['level']=='UNRESOLVED']}


def summary(graph):
    return {'scripts': len(graph['scripts']), 'chapter_stage_contracts': sum(n['type']=='chapter_contract' for n in graph['nodes'].values()),
            'nodes': len(graph['nodes']), 'edges': len(graph['edges']),
            'unresolved_edges': sum(e['level']=='UNRESOLVED' for e in graph['edges']), 'scope': graph['scope']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--image', type=Path, default=DEFAULT_IMAGE)
    parser.add_argument('--ledger', type=Path, default=ROOT/'campaign/verification.json')
    parser.add_argument('--out', type=Path)
    parser.add_argument('--path', nargs=2, metavar=('SOURCE','TARGET'))
    parser.add_argument('--allow-unresolved', action='store_true')
    args = parser.parse_args()
    with DiscReader(args.image) as disc: graph = build(disc, json.loads(args.ledger.read_text(encoding='utf-8')))
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open('x', encoding='utf-8') as stream: json.dump(graph, stream, indent=2)
    print(json.dumps(route(graph, *args.path, allow_unresolved=args.allow_unresolved) if args.path else summary(graph), indent=2))
