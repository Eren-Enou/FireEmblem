"""Build a few NEW isolated owner-operated candidates; never starts Dolphin."""
import json
from pathlib import Path
from tools.install_codes import ROOT, build_ini, validate_ini, parse_sections
from tools.campaign_test_pack import sha, write_json, work_destination
from tools.campaign_snapshot import capture
from tools.verify_game import DEFAULT_IMAGE
from tools.netplay_package import fingerprint
from tools.fixture_position_code import HOOK
from tools.owner_code import c2_lines
from tools.scenario_position_code import words
from tools.inspect_state import load_mem1, UNITS
from tools.talk_evidence import cell, CONVERSATION_KEY

NAMES=('CH10-CHAPTER-COMPLETE','CH7-PLAYER2-CONTROL')
BASE=ROOT/'work/scenarios/human_v1'
SOURCES={
 'CH10-CHAPTER-COMPLETE':(BASE/'CH10-PRISONER-ESCAPE-v2/captures/after',
   'b9a50895bf2136aace6911b3d5295545a7d2ee1826b762ee4dd504cfef2fdeca'),
 'CH7-PLAYER2-CONTROL':(BASE/'CH6-IKE-COMPLETE/captures/reloaded',
   '2d44d83b55f51a7d376fc6e6e28a6f7eed46cd236b4a4166fc32b9dbb9c5bd66')}
BLUE=('PID_TIAMAT','PID_KILROY','PID_SENERIO','PID_VOKE','PID_LETHE','PID_IKE')
YELLOW=('PID_OSCAR','PID_CHINON','PID_GATRIE')
OBS7=('original_battle','p1_cannot_command_oscar','p2_original_wait','normal_turn_cycle','no_unexpected_behavior')
OBS10=('remaining_blue_original_escapes','ike_last_blue','original_completion','expected_recruits',
       'native_save_accepted','fresh_boot_without_state','native_load_selected','no_unexpected_behavior')

REJECTED_RUNTIME_FINGERPRINTS = {
    '92f0ad0562beaef9': 'CAMP-AF: original enemy phase damages Green Brom and alarm reinforcements occupy exit6,2; this staging needs a NEW corrected trial',
}


def runtime_candidate(fingerprint_value):
    if fingerprint_value in REJECTED_RUNTIME_FINGERPRINTS:
        raise ValueError(REJECTED_RUNTIME_FINGERPRINTS[fingerprint_value])


def source(name):
    directory,digest=SOURCES[name]
    state=directory/'state.sav';ini=directory/'GFEE01.ini'
    if sha(state)!=digest: raise ValueError('accepted source hash mismatch')
    snap=capture(state,DEFAULT_IMAGE,ini,'offline-source')
    game=snap['game'];chapter=11 if name.startswith('CH10') else 8
    if not snap['evidence']['intended_c2_verified'] or not game['event_scripts']['complete_chain'] or game['event_scripts']['campaign_ids']!=[chapter]:
        raise ValueError('accepted source code/script identity mismatch')
    return directory,state,ini,snap


def positioning(game,mem):
    """Explicit original grid cells; only living active units may be positioned."""
    targets={pid:xy for pid,xy in zip(BLUE,((6,3),(7,3),(8,3),(9,3),(10,3),(9,2)))}
    targets.update(zip(YELLOW,((6,4),(7,4),(8,4))))
    reds=[u for u in game['units'] if u['force']==1]
    if len(reds)!=6: raise ValueError('expected six original Red actors')
    targets.update((u['pid']+'#'+str(u['slot']),xy) for u,xy in zip(reds,((19,18),(20,18),(19,19),(20,19),(18,18),(18,19))))
    # (19,19) is vacated by Oscar before Red positioning. All other destinations
    # must be empty. This dependency is explicit, not an occupied-tile overwrite.
    records=[];vacated={}
    ordered=[next(u for u in game['units'] if u['pid']==pid) for pid in (*BLUE,*YELLOW)]+reds
    destinations=set()
    for u in ordered:
        key=u['pid'] if u['force']!=1 else u['pid']+'#'+str(u['slot'])
        xy=targets[key];grid=cell(mem,*xy)
        if xy in destinations or not grid['edge_mask']&15: raise ValueError('invalid/duplicate staging tile')
        if grid['occupant_id'] and vacated.get(tuple(xy))!=grid['occupant_id']:
            raise ValueError('occupied staging tile: '+str(xy))
        if u['force'] not in (0,1,3) or u['hp']<=0 or u['rescue_link']: raise ValueError('invalid staging actor')
        addr=UNITS+(u['slot']-1)*0x280
        records.append(dict(pid=u['pid'],slot=u['slot'],unit=addr,character=mem.u32(addr+0x188),
                            force=u['force'],source_xy=u['xy'],destination_xy=xy,grid=grid))
        vacated[tuple(u['xy'])]=u['slot'];destinations.add(xy)
    if cell(mem,6,2)['occupant_id']: raise ValueError('original exit occupied')
    separation=min(abs(a['destination_xy'][0]-b['destination_xy'][0])+abs(a['destination_xy'][1]-b['destination_xy'][1])
                   for a in records if a['force']!=1 for b in records if b['force']==1)
    if separation<20: raise ValueError('enemy staging too close')
    return records,separation


def prepare(name,root):
    from tools.netplay_setup import make_user
    from tools.setup_pads import PORT1_KEYBOARD,PORT2_KEYBOARD
    from tools.fixture_relayout import replace
    from tools.campaign_event_model import ESCAPE_KEYS,DOOR_KEYS
    root=work_destination(root)
    directory,state,ini,snap=source(name);game=snap['game']
    native=name=='CH7-PLAYER2-CONTROL'
    text=build_ini(['COOP-P6','EXP-16'],verbose=False)
    setup={};records=[]
    if not native:
        flags=game['talk_fixture']['flags']
        k=[u for u in game['units'] if u['pid']=='PID_KEVIN']
        if len(k)!=1 or k[0]['force']!=5 or not k[0]['escaped'] or not flags.get(CONVERSATION_KEY) or not flags.get(ESCAPE_KEYS['PID_KEVIN']):
            raise ValueError('accepted original Kieran Escape required')
        if any(flags.get(DOOR_KEYS[p]) or flags.get(ESCAPE_KEYS[p]) for p in ('PID_CHAP','PID_NEPENEE')):
            raise ValueError('unexpected Brom/Nephenee prerequisites')
        _,mem=load_mem1(state,DEFAULT_IMAGE)
        records,separation=positioning(game,mem)
        body=words(11,3,1,records,queue=dict(turn=2,exit=(6,2)))
        text+='\n[Gecko]\n$DBG-CAMP-END C11 original ending staging/Blue queue\n'+'\n'.join(c2_lines(HOOK,body))+'\n[Gecko_Enabled]\n$DBG-CAMP-END C11 original ending staging/Blue queue\n'
        text='\n'.join('['+key+']\n'+'\n'.join(value) for key,value in parse_sections(text).items())+'\n'
        setup=dict(records=records,minimum_staged_manhattan_separation=separation,
                   expected_recruits=['PID_KEVIN'],unmet_recruit_conditions=['PID_CHAP','PID_NEPENEE'],
                   caveat='One original enemy phase is required; pathing, triggers and runtime positioning remain unverified. Inherited Shinon/Gatrie history is synthetic.')
    size=validate_ini(text)
    runtime_candidate(fingerprint(text))
    # Accepted immutable capture/profile only. Never copy a mutable active card.
    profile=directory/'profile'
    cards=sorted((profile/'GC/USA/Card A').glob('*.gci'))
    if not cards: raise ValueError('accepted private card missing')
    source_files=[state,ini,*[p for p in (profile/'GC').rglob('*') if p.is_file()]]
    originals={str(p):sha(p) for p in source_files}
    if native and sha(cards[0])!='99446e1b65ed44ec60e10da9232d5ab894b48a6cc018a8e7eb6fc24445e429ca':
        raise ValueError('accepted Chapter7 native card mismatch')
    root.mkdir(parents=True)
    make_user(root/'User',DEFAULT_IMAGE.parent.resolve(),'PRIVATE '+name,PORT1_KEYBOARD,text,pad2=PORT2_KEYBOARD)
    for src in (profile/'GC').rglob('*'):
        if src.is_file():
            target=root/'User/GC'/src.relative_to(profile/'GC');target.parent.mkdir(parents=True,exist_ok=True)
            with target.open('xb') as stream:stream.write(src.read_bytes())
    (root/'card-before').mkdir()
    for card in cards:
        with (root/'card-before'/card.name).open('xb') as stream:stream.write(card.read_bytes())
    if native:
        # Inspection only: the source state has old private codes and is NEVER
        # restored in this native-only scenario. Boot uses the copied GCI.
        with (root/'source.sav').open('xb') as stream:stream.write(state.read_bytes())
        with (root/'source.ini').open('x') as stream:stream.write(ini.read_text())
        setup['source_inspection_only']=True
    else:
        setup['relayout']=replace(state,ini.read_text(),text,root/'seed.s02.sav')
        check=capture(root/'seed.s02.sav',DEFAULT_IMAGE,root/'User/GameSettings/GFEE01.ini','offline-repacked')
        if check['game']!=game or not check['evidence']['intended_c2_verified']:
            raise ValueError('repacked seed changed original game state or failed C2 checks')
    case=dict(id=name,title='Chapter7 P2 control after accepted native Load' if native else 'Chapter10 original ending and permanent Kieran retention',
              classification='synthetic_history_native_boot' if native else 'synthetic_original_positioning',
              captures=['before','after'] if native else ['staged','before','after','next_prep','reloaded'],
              observations=list(OBS7 if native else OBS10),steps=steps(name))
    write_json(root/'case.json',case)
    write_json(root/'observations.json',dict(observed=dict.fromkeys(case['observations']),notes=''))
    pins=[root/'case.json',root/'User/GameSettings/GFEE01.ini',root/'User/Config/GCPadNew.ini',*sorted((root/'card-before').glob('*.gci'))]
    pins += [root/'source.sav',root/'source.ini'] if native else [root/'seed.s02.sav']
    manifest=dict(id=name,readiness='PREPARED_RUNTIME_UNVERIFIED',launch_type='native' if native else 'state',
                  source_hashes=originals,source_game=game,pinned={str(p.relative_to(root)):sha(p) for p in pins},
                  initial_cards={p.name:sha(p) for p in cards},fingerprint=fingerprint(text),gecko_bytes=size,
                  executable_sha256=sha(ROOT/'Dolphin-x64/Dolphin.exe'),setup=setup,
                  card_identity='accepted Chapter7 native card' if native else 'inherited synthetic C11 card; native save acceptance unverified')
    write_json(root/'scenario.json',manifest)
    if any(sha(Path(p))!=digest for p,digest in originals.items()): raise ValueError('source changed')
    return dict(scenario=name,gecko_bytes=size,fingerprint=fingerprint(text),status='NOT TESTED',root=str(root))


def steps(name):
    if name=='CH7-PLAYER2-CONTROL':
        return ['Native boot only: Title > Restart Chapter is the original native save-file menu. Select Ch.7: Shades of Evil on this copied card. Never load source.sav. The no-Restart warning applies to redirected state fixtures, not this native-only load.',
          'Enter Fight/Begin normally. Keep Oscar deployed. At Blue turn1 set Auto End Off and end Blue without acting or fighting.',
          'At Yellow turn1, attempt a Player1 command on Oscar: it must be refused. With Player2 select Oscar, confirm CURRENT tile and leave Wait menu open. Save before.sav.',
          'Player2 chooses original Wait. Save after.sav on the same Yellow turn. Do not move, fight, trade or advance another phase. The before capture establishes the Blue-to-Yellow cycle.']
    return ['Do not Restart Chapter. On restored Yellow turn1 the private setup stages six Blue and three owned Yellow near the exit, and moves six living Reds aside. Kieran stays legitimately escaped; no door, recruitment or completion flag is edited.',
      'Set Auto End Off (Player2 map menu E > Options). Wait for all staging, then save staged.sav BEFORE ending Yellow. If any actor is missing or not staged, stop and preserve the state.',
      'End Yellow once. Allow exactly one original enemy phase and original turn2 tutorial/story prompts. If anyone takes damage or an unexpected event blocks the queue, capture it and stop; do not play the map.',
      'On Blue turn2 the private queue puts Titania, Rhys, Soren, Volke, Lethe, then Ike at the original exit (6,2). Player1 selects CURRENT tile, chooses original Escape/Yes and allows dialogue after each. Leave Oscar/Shinon/Gatrie on map: this specifically tests original AllUnitEscape with stable ownership hand-back.',
      'When Ike reaches the exit LAST BLUE, save before.sav, then choose his original Escape. Capture after.sav at the first stable ending screen BEFORE proceeding to the next map.',
      'Continue original story to Chapter11 preparations/base before fighting. Inspect permanent roster: Kieran expected; Brom/Nephenee have unmet door/Escape conditions and should not be permanent recruits. Save next_prep.sav. Inherited Shinon/Gatrie history remains synthetic and is reviewed separately.',
      'Use an unused private native save slot only. Close Dolphin. Run this scenario with -FreshBoot and original Load (never a state), then save reloaded.sav before acting. If original saving is refused, record it; never edit card identity.']


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('name',choices=NAMES);p.add_argument('--root',type=Path,required=True)
    args=p.parse_args();print(json.dumps(prepare(args.name,args.root),indent=2))
