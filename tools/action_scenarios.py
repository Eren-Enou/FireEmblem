"""Short original Rescue/combat probes, with no synthetic outcome stores."""
import json
from pathlib import Path
from tools.install_codes import ROOT,build_ini,parse_sections,validate_ini
from tools.campaign_test_pack import sha,write_json,work_destination
from tools.campaign_snapshot import capture
from tools.inspect_state import load_mem1,UNITS
from tools.verify_game import DEFAULT_IMAGE
from tools.netplay_package import fingerprint
from tools.owner_code import c2_lines
from tools.fixture_position_code import HOOK
from tools.scenario_position_code import words
from tools.fixture_relayout import replace
from tools.talk_evidence import cell

C6=ROOT/'work/fixtures/ch6_escape_native_v2'
C7=ROOT/'work/scenarios/human_v1/CH6-IKE-COMPLETE/captures/reloaded/profile'
SPECS={
 'CH6-YELLOW-RESCUE':dict(actor='PID_OSCAR',target_slot=14,positions={'PID_OSCAR':(13,24),'PID_KILROY':(14,24)},
     kind='rescue',observations=['original_rescue','p2_command','no_unexpected_behavior']),
 'CH6-YELLOW-COMBAT':dict(actor='PID_OSCAR',target_slot=13,positions={'PID_OSCAR':(15,13)},
     kind='combat',observations=['p2_original_attack','damage_observed','experience_gained','durability_consumed','no_unexpected_behavior']),
 'CH6-YELLOW-FATAL':dict(actor='PID_OSCAR',target_slot=9,positions={'PID_OSCAR':(13,26)},
     kind='fatal',observations=['p2_original_attack','fatal_combat_observed','no_unexpected_behavior']),
 'CH9-PARTNER-COMBAT':dict(actor='PID_LETHE',target_slot=30,positions={'PID_LETHE':(9,26)},
     kind='partner',observations=['p2_original_attack','damage_observed','native_partner_unassigned','no_unexpected_behavior']),
}
NAMES=tuple(SPECS)


def source(name):
    partner=name.startswith('CH9')
    state=ROOT/'work/ch9_yellow_before.s02.sav' if partner else C6/'before.s02.sav'
    ini=ROOT/'work/runtime/host/GameSettings/GFEE01.ini' if partner else C6/'accepted-config.ini'
    digest='54f141736b839b4c1c09cf8944a9fde4c08defacf91285b3b7f0ced2c82a3af5' if partner else 'a3faa84307fd86e444b10d5a6a62dea9f09c110a7a86db6bd732fa21def9a8d3'
    if sha(state)!=digest:raise ValueError('accepted original source hash mismatch')
    snap=capture(state,DEFAULT_IMAGE,ini,'offline-source')
    g=snap['game'];chapter=10 if partner else 7
    if (g['chapter'],g['phase'],g['turn'])!=(chapter,3,1) or not snap['evidence']['intended_c2_verified'] or not g['event_scripts']['complete_chain'] or g['event_scripts']['campaign_ids']!=[chapter]:
        raise ValueError('source phase/codes/original scripts rejected')
    return state,ini,snap


def prepare(name,root):
    from tools.netplay_setup import make_user
    from tools.setup_pads import PORT1_KEYBOARD,PORT2_KEYBOARD
    root=work_destination(root);spec=SPECS[name];state,ini,snap=source(name)
    g=snap['game'];_,mem=load_mem1(state,DEFAULT_IMAGE)
    target=next(u for u in g['units'] if u['slot']==spec['target_slot'])
    records=[]
    for pid,xy in spec['positions'].items():
        matches=[u for u in g['units'] if u['pid']==pid]
        if len(matches)!=1:raise ValueError('unique actor required')
        u=matches[0];grid=cell(mem,*xy)
        if grid['occupant_id'] not in (0,u['slot']) or not grid['edge_mask']&15:raise ValueError('occupied/invalid destination')
        if u['rescue_link'] or u['hp']<=0 or u['flags']&1:raise ValueError('living available unrescued actor required')
        addr=UNITS+(u['slot']-1)*0x280
        records.append(dict(pid=pid,slot=u['slot'],unit=addr,character=mem.u32(addr+0x188),force=u['force'],source_xy=u['xy'],destination_xy=xy,grid=grid))
    actor=next(u for u in g['units'] if u['pid']==spec['actor'])
    actorxy=spec['positions'][actor['pid']];targetxy=spec['positions'].get(target['pid'],target['xy'])
    if abs(actorxy[0]-targetxy[0])+abs(actorxy[1]-targetxy[1])!=1:raise ValueError('original adjacent interaction required')
    if actor['force']!=3 or actor['owned'] or actor['owner'] is not None:raise ValueError('original unassigned Yellow actor required')
    prerequisites={}
    if spec['kind']=='rescue':
        from tools.action_prerequisites import rescue
        prerequisites=rescue(mem,actor['slot'],target['slot'],actorxy,targetxy)
        if not prerequisites['all_bounded_predicates']:raise ValueError('bounded original Rescue predicate rejected')
    text=build_ini(['COOP-P6','EXP-16'],verbose=False)
    name_line='$DBG-CAMP-ACTION '+name+' original-command probe'
    body=words(g['chapter'],3,1,records)
    text+='\n[Gecko]\n'+name_line+'\n'+'\n'.join(c2_lines(HOOK,body))+'\n[Gecko_Enabled]\n'+name_line+'\n'
    text='\n'.join('['+k+']\n'+'\n'.join(v) for k,v in parse_sections(text).items())+'\n'
    size=validate_ini(text)
    cards=sorted((C7/'GC/USA/Card A').glob('*.gci'))
    if len(cards)!=1 or sha(cards[0])!='99446e1b65ed44ec60e10da9232d5ab894b48a6cc018a8e7eb6fc24445e429ca':raise ValueError('accepted disposable card copy required')
    originals={str(p):sha(p) for p in [state,ini,*[p for p in (C7/'GC').rglob('*') if p.is_file()]]}
    root.mkdir(parents=True)
    make_user(root/'User',DEFAULT_IMAGE.parent.resolve(),'PRIVATE '+name,PORT1_KEYBOARD,text,pad2=PORT2_KEYBOARD)
    for src in (C7/'GC').rglob('*'):
        if src.is_file():
            dest=root/'User/GC'/src.relative_to(C7/'GC');dest.parent.mkdir(parents=True,exist_ok=True)
            with dest.open('xb') as stream:stream.write(src.read_bytes())
    (root/'card-before').mkdir()
    for card in cards:
        with (root/'card-before'/card.name).open('xb') as stream:stream.write(card.read_bytes())
    replacement=replace(state,ini.read_text(),text,root/'seed.s02.sav')
    checked=capture(root/'seed.s02.sav',DEFAULT_IMAGE,root/'User/GameSettings/GFEE01.ini','offline-repacked')
    if checked['game']!=g or not checked['evidence']['intended_c2_verified']:raise ValueError('seed changed game data or failed live codes')
    instructions=steps(name,target)
    case=dict(id=name,title=name+' original '+spec['kind']+' interaction',captures=['before','after'],
              observations=spec['observations'],steps=instructions,classification='synthetic_original_positioning')
    write_json(root/'case.json',case)
    write_json(root/'observations.json',dict(observed=dict.fromkeys(spec['observations']),notes=''))
    write_json(root/'prerequisites.json',prerequisites)
    pins=[root/'seed.s02.sav',root/'case.json',root/'prerequisites.json',root/'User/GameSettings/GFEE01.ini',root/'User/Config/GCPadNew.ini',*sorted((root/'card-before').glob('*.gci'))]
    write_json(root/'scenario.json',dict(id=name,readiness='PREPARED_RUNTIME_UNVERIFIED',launch_type='state',
        source_hashes=originals,source_game=g,pinned={str(p.relative_to(root)):sha(p) for p in pins},
        initial_cards={p.name:sha(p) for p in cards},fingerprint=fingerprint(text),gecko_bytes=size,
        executable_sha256=sha(ROOT/'Dolphin-x64/Dolphin.exe'),
        card_identity='Private accepted GCI copy; state/card pairing and native saving OUT OF SCOPE. Do not save or Suspend.',
        setup=dict(records=records,target_slot=target['slot'],kind=spec['kind'],relayout=replacement)))
    if any(sha(Path(p))!=h for p,h in originals.items()):raise ValueError('source changed')
    return dict(scenario=name,gecko_bytes=size,fingerprint=fingerprint(text),status='NOT TESTED')


def steps(name,target):
    head=['Do not Restart Chapter, Suspend, save to memory card or advance phases. This private setup changes original positions only. All original stats, factions, items and flags are retained.',
          'Chapter6 seeds inherit an Escape action menu: use Player2 B to cancel it, then B to cancel Move. Wait at the idle map for native positioning; never confirm inherited Escape. Chapter9 starts at the idle map.',
          'Player2: set Auto End Off (map menu E > Options). Select the Yellow actor, confirm CURRENT tile. Save before.sav with the original action/forecast menu open.']
    if name=='CH6-YELLOW-RESCUE':
        return head+['Oscar is Yellow at (13,24); Rhys is Blue at (14,24). Try the original Rescue command targeting Rhys. If unavailable, save before.sav and record exact menu/eligibility result; do not force the relationship.',
          'If Rescue is offered, execute it once and save after.sav on the SAME Yellow turn, before another action. This prepares genuine carrier/passenger evidence; do not Escape yet. Carried Escape needs a separately validated follow-up fixture.']
    if name=='CH6-YELLOW-FATAL':
        return head+['DISPOSABLE FATAL probe: Oscar remains at (13,26), beside Emil (13,25), who retains original IID_AXEBASTER. Inspect the original forecast first. No HP/damage/death value was forced; a fatal result is not guaranteed.',
          'Choose original Attack once. Allow original battle/death dialogue to finish and save after.sav. If Oscar survives, record that outcome and stop; do not fight repeatedly to manufacture death.']
    actor='transformed native Yellow Lethe at (9,26)' if name.startswith('CH9') else 'Yellow Oscar at (15,13)'
    return head+[f'Use {actor}. Choose original Attack against the adjacent original Archer at {tuple(target["xy"])}. Keep the original weapon. Inspect forecast, then execute ONE attack.',
      'Let original battle/EXP finish and save after.sav on the SAME Yellow turn. Do not Wait/move again or end phase. Record damage, displayed EXP and durability where applicable. Native partner combat does not establish permanent ownership or later recruitment.']


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('name',choices=NAMES);p.add_argument('--root',type=Path,required=True)
    a=p.parse_args();print(json.dumps(prepare(a.name,a.root),indent=2))
