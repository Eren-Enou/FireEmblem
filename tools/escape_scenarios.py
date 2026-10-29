"""Prepare NEW short original-Escape candidates; never start Dolphin."""
import json
from pathlib import Path

from tools.install_codes import ROOT, parse_sections, validate_ini
from tools.netplay_package import enabled_codes, fingerprint
from tools.campaign_test_pack import sha, write_json, work_destination
from tools.campaign_snapshot import capture
from tools.inspect_state import load_mem1
from tools.fe9.savestate import read_state, write_state
from tools.fixture_state import HEADER, TERMINATOR, HANDLER_SHA256, validate_prefix
from tools.fixture_cpu import guard_and_invalidate
from tools.fixture_position_code import HOOK
from tools.escape_position_code import words
from tools.owner_code import c2_lines
from tools.patch_state import apply_edits
from tools.talk_evidence import cell, CONVERSATION_KEY
from tools.verify_game import DEFAULT_IMAGE

SPECS = {
    'CH10-PRISONER-ESCAPE': dict(source='ch10_oscar_kieran_v1', ini='User/GameSettings/GFEE01.ini',
        chapter=11, phase=3, turn=1, force=3, exit=(6,2),
        actors=[('PID_KEVIN',(20,19))], old='DBG-CAMP-TALK',
        title='Kieran original Escape after accepted Oscar Talk', captures=['before','after'],
        observations=['original_escape','p2_command','no_unexpected_behavior'],
        steps=['Kieran is moved synthetically to the original exit (6,2) when map input resumes. Oscar and the original closed cell door remain unchanged.',
               'Player2: numpad8/5/4/6 move cursor; M confirms, N cancels. Set Auto End Off using map menu E > Options. Select Kieran and confirm his CURRENT tile.',
               'Save before.sav with the original Escape menu open. Choose Escape, confirm Yes if offered, and allow original dialogue to finish. Save after.sav without ending the phase.',
               'If the command is absent or Kieran disappears, capture it and record the exact result. This tests local original Escape, not permanent recruitment or chapter cleanup.']),
    'CH6-IKE-COMPLETE': dict(source='ch6_escape_native_v2', ini='accepted-config.ini',
        chapter=7, phase=0, turn=2, force=0, exit=(13,26),
        actors=[('PID_TIAMAT',(12,9)),('PID_KILROY',(14,8)),('PID_SENERIO',(13,8)),('PID_IKE',(13,9))],
        old='DBG-CAMP-POS', title='Chapter6 remaining Blue Escape queue, Ike LAST',
        captures=['before_queue','before','after','next_prep','reloaded'],
        observations=['remaining_blue_original_escapes','ike_last','original_completion','oscar_present_next_chapter','fresh_native_load'],
        steps=['Oscar has already escaped through the accepted original event. Three other Blue allies remain, so Ike cannot honestly be presented as the last escape yet.',
               'Player1: arrows move cursor, X confirms, Z cancels; D map menu. Set Auto End Off. The setup moves Titania, then Rhys, then Soren, then Ike individually to the original exit when it is vacant.',
               'Save before_queue.sav. Select each waiting ally at the exit, confirm CURRENT tile, choose original Escape and Yes, and allow dialogue to finish. Repeat three times; no battle traversal is needed.',
               'When Ike reaches the exit, save before.sav with Escape available. Choose his original Escape last. Let the original ending run; capture after.sav at the first stable completion screen.',
               'Continue original story to Chapter7 and capture next_prep.sav. Save only if a new unused disposable slot is offered. If the inherited card is refused, record the refusal; do not alter card identity.',
               'For a native reload use -FreshBoot on this SAME scenario after closing Dolphin completely. Load using the original game menu, capture reloaded.sav before acting. If no legitimate save is available, leave that capture absent.']),
}


def geometry(mem, spec):
    """Original kind5/action14 record plus actual bounded occupancy/edge grid."""
    from tools.fe9.disc import DiscReader
    from tools.fe9.events import functions
    with DiscReader(DEFAULT_IMAGE) as disc:
        raw=disc.read_file(f"Scripts/C{spec['chapter']:02d}.cmb")
    matching=[]
    for function in functions(raw):
        tile=function.trigger(raw).get('tile_event',{})
        if (tile.get('x'),tile.get('y'),tile.get('action_code')) == (*spec['exit'],14):
            matching.append({'scene':function.index,**tile})
    if len(matching)!=1 or matching[0]['key']!='':
        raise ValueError('expected original unkeyed Escape record missing')
    grid=cell(mem,*spec['exit'])
    if grid['occupant_id'] or not grid['edge_mask']:
        raise ValueError('original exit occupied or invalid')
    return {'grid':grid,'original_event':matching[0],
            'limit':'Synthetic teleport skips route/doors/combat. Original Escape menu context and event must still be exercised.'}


def replace(source, old_ini, new_ini, body, destination):
    handler = ROOT / 'Dolphin-x64/Sys/codehandler.bin'
    if sha(handler) != HANDLER_SHA256:
        raise ValueError('handler mismatch')
    info, mem = load_mem1(source, DEFAULT_IMAGE)
    header = 0x80001800 + handler.stat().st_size - 8
    size = validate_ini(old_ini)
    if validate_ini(new_ini) != size or mem.read(header,8) != HEADER or mem.read(header+8+size,8) != TERMINATOR:
        raise ValueError('same-sized known Gecko layout required')
    start = header + 8
    validate_prefix(mem.read(start,size),start,old_ini)
    blocks = [bytes.fromhex(''.join(lines)) for kind,_,lines in enabled_codes(old_ini) if kind == 'Gecko']
    address = start + sum(map(len,blocks[:-1]))
    addition = bytes.fromhex(''.join(c2_lines(HOOK,body)))
    if len(addition) != len(blocks[-1]) or addition[:8] != blocks[-1][:8]:
        raise ValueError('replacement must preserve last C2 header and size')
    # Preserve the installed return branch, whose target validate_prefix checked.
    addition = addition[:-4] + mem.read(address+len(addition)-4,4)
    state_info,payload = read_state(source)
    guarded,cpu = guard_and_invalidate(payload,state_info,mem,address,len(addition))
    patched,_ = apply_edits(guarded,mem.offset,[f'{address:X}={addition.hex()}'])
    # All CPU/roster/script data untouched, except documented clean cache valid bits.
    write_state(source,destination,patched)
    _,out = load_mem1(destination,DEFAULT_IMAGE)
    validate_prefix(out.read(start,size),start,new_ini)
    if out.read(HOOK,4) != mem.read(HOOK,4):
        raise ValueError('installed hook changed unexpectedly')
    return {'address':address,'bytes':len(addition),'cpu_safety':cpu,
            'source_sha256':sha(source),'state_sha256':sha(destination)}


def prepare(name, root):
    from tools.netplay_setup import make_user
    from tools.setup_pads import PORT1_KEYBOARD, PORT2_KEYBOARD
    spec = SPECS[name]
    root = work_destination(root)
    src = ROOT / 'work/fixtures' / spec['source']
    state, config = src/'after.s02.sav', src/spec['ini']
    text = config.read_text()
    snap = capture(state,DEFAULT_IMAGE,config,'offline-fixture')
    game = snap['game']
    if not snap['evidence']['intended_c2_verified'] or (game['chapter'],game['phase'],game['turn']) != (spec['chapter'],spec['phase'],spec['turn']):
        raise ValueError('source identity or patches rejected')
    if not game['event_scripts']['complete_chain'] or game['event_scripts']['campaign_ids'] != [spec['chapter']]:
        raise ValueError('loaded original scripts rejected')
    for pid,xy in spec['actors']:
        matches = [u for u in game['units'] if u['pid']==pid]
        if len(matches)!=1 or matches[0]['force']!=spec['force'] or matches[0]['xy']!=list(xy) or matches[0]['flags']&1 or matches[0]['hp']<=0 or matches[0]['rescue_link']:
            raise ValueError('actor source conditions rejected: '+pid)
    oscar = next(u for u in game['units'] if u['pid']=='PID_OSCAR')
    if name.startswith('CH10'):
        if game['talk_fixture']['flags'][CONVERSATION_KEY] is not True or oscar['force']!=3:
            raise ValueError('accepted original Talk outcome required')
    elif oscar['force']!=5 or not oscar['escaped']:
        raise ValueError('accepted Oscar original Escape required')
    _,mem = load_mem1(state,DEFAULT_IMAGE)
    geometry_record = geometry(mem,spec)
    codes = enabled_codes(text)
    if codes[-1][1].split()[0] != spec['old']:
        raise ValueError('only expected last private setup can be replaced')
    old_words = len(bytes.fromhex(''.join(codes[-1][2])))//4-2
    body = words(spec['chapter'],spec['phase'],spec['turn'],spec['force'],spec['actors'],spec['exit'],old_words)
    sections = parse_sections(text)
    old_name = '$'+codes[-1][1]
    lines = sections['Gecko']; index = lines.index(old_name)
    new_name = '$DBG-CAMP-EXIT '+name+' synthetic original-position queue'
    sections['Gecko'] = lines[:index]+[new_name,*c2_lines(HOOK,body)]
    sections['Gecko_Enabled'] = [new_name if line==old_name else line for line in sections['Gecko_Enabled']]
    new_ini = '\n'.join('['+key+']\n'+'\n'.join(value) for key,value in sections.items())+'\n'
    size = validate_ini(new_ini)
    cards = sorted((src/'User/GC/USA/Card A').glob('*.gci'))
    if not cards: raise ValueError('private source card missing')
    originals = {str(p):sha(p) for p in [state,config,*cards]}
    root.mkdir(parents=True)
    make_user(root/'User',DEFAULT_IMAGE.parent.resolve(),name,PORT1_KEYBOARD,new_ini,pad2=PORT2_KEYBOARD)
    (root/'card-before').mkdir()
    for card in cards:
        for target in [root/'User/GC/USA/Card A'/card.name,root/'card-before'/card.name]:
            with target.open('xb') as stream:stream.write(card.read_bytes())
    replacement = replace(state,text,new_ini,body,root/'seed.s02.sav')
    # Offline setup changes neither a single roster field nor original event flags.
    after = capture(root/'seed.s02.sav',DEFAULT_IMAGE,root/'User/GameSettings/GFEE01.ini','offline-fixture')
    if after['game'] != game or not after['evidence']['intended_c2_verified']:
        raise ValueError('new seed changed game state or failed live code checks')
    pinned = {str(p.relative_to(root)):sha(p) for p in [root/'seed.s02.sav',
        root/'User/GameSettings/GFEE01.ini',root/'User/Config/GCPadNew.ini',*sorted((root/'card-before').glob('*.gci'))]}
    write_json(root/'case.json',{'id':name,'title':spec['title'],'captures':spec['captures'],
        'observations':spec['observations'],'steps':spec['steps'],'classification':'synthetic_original_positioning'})
    write_json(root/'observations.json',{'observed':{k:None for k in spec['observations']},'notes':''})
    record = {'id':name,'readiness':'PREPARED_RUNTIME_UNVERIFIED','source_hashes':originals,
        'pinned':pinned,'initial_cards':{p.name:sha(p) for p in cards},'fingerprint':fingerprint(new_ini),
        'gecko_bytes':size,'card_identity':'UNVERIFIED inherited history','source_game':game,
        'geometry':geometry_record,'setup':replacement,
        'limits':'Only last private C2 storage and overlapping clean cache valid bits changed. Original UnitSetPos has NOT run. Escape/completion must be performed by owner.'}
    write_json(root/'scenario.json',record)
    if any(sha(Path(p))!=digest for p,digest in originals.items()):raise ValueError('source changed')
    return {'scenario':name,'gecko_bytes':size,'replacement':replacement,'status':'NOT TESTED'}


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('name',choices=SPECS);p.add_argument('--root',type=Path,required=True)
    args=p.parse_args()
    print(json.dumps(prepare(args.name,args.root),indent=2))
