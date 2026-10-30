"""Offline fixture safety and verdict regressions; native calls are mocked."""
import copy
import tempfile
import unittest
from pathlib import Path
from tools.scenario_position_code import words
from tests.fixture_executor import run
from tools.install_codes import ROOT


class PositionTests(unittest.TestCase):
    def rows(self):
        actors={'a':dict(xy=(2,3),force=0),'b':dict(xy=(4,5),force=1),'c':dict(xy=(8,8),force=3)}
        rows=[dict(unit=0x81200000+i*0x280,character=0x81400000+i*4,force=u['force'],source_xy=u['xy'],destination_xy=(6+i,3)) for i,u in enumerate(actors.values())]
        return actors,rows

    def test_staging_abi_native_calls_and_no_false_moves(self):
        actors,rows=self.rows();spec=dict(chapter=11,phase=3,turn=1,force=0)
        code=words(11,3,1,rows,queue=dict(turn=2,exit=(6,2)))
        moves,gprs,sprs,_=run(code,spec,actors)
        self.assertEqual(moves,[(1,6,3),(2,7,3),(3,8,3)])
        self.assertTrue(gprs and sprs)
        self.assertEqual(run(code,spec,actors,occupied=True)[0],[])
        self.assertEqual(run(code,spec,actors,chapter=12)[0],[])
        for field,value in (('rescue',1),('hp',0),('force',2),('character',0x81400080)):
            bad=copy.deepcopy(actors);bad['a'][field]=value
            self.assertEqual(run(code,spec,bad)[0],[])
        for unit in actors.values(): unit['xy']=(1,1)
        self.assertEqual(run(code,spec,actors)[0],[])

    def test_queue_skips_red_yellow_escaped_and_stops_after_one_blue(self):
        actors,rows=self.rows()
        # Add a second Blue to demonstrate that only one is queued each call.
        actors['d']=dict(xy=(9,3),force=0)
        rows.append(dict(unit=0x81200780,character=0x8140000C,force=0,source_xy=(9,9),destination_xy=(9,3)))
        for unit,row in zip(actors.values(),rows): unit['xy']=row['destination_xy']
        code=words(11,3,1,rows,queue=dict(turn=2,exit=(6,2)))
        spec=dict(chapter=11,phase=0,turn=2,force=0)
        self.assertEqual(run(code,spec,actors)[0],[(1,6,2)])
        actors['a'].update(force=5,flags=0x4000)
        self.assertEqual(run(code,spec,actors)[0],[(4,6,2)])
        actors['a']['flags']=0
        self.assertEqual(run(code,spec,actors)[0],[])
        actors['a'].update(force=0,flags=1)
        self.assertEqual(run(code,spec,actors)[0],[])
        spec['turn']=3
        self.assertEqual(run(code,spec,actors)[0],[])

    def test_budget_rejects_oversize_and_unaligned_identity(self):
        _,rows=self.rows()
        with self.assertRaises(ValueError): words(11,3,1,rows,total_words=4)
        with self.assertRaises(ValueError): words(11,3,1,[])
        rows[0]['character']|=1
        with self.assertRaises(ValueError): words(11,3,1,rows)

    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH10-PRISONER-ESCAPE-v2/captures/after/state.sav').is_file(),'accepted private source unavailable')
    def test_actual_source_relayout_preserves_all_game_fields_and_stable_hooks(self):
        from tools.next_scenarios import source,positioning
        from tools.inspect_state import load_mem1
        from tools.verify_game import DEFAULT_IMAGE
        from tools.install_codes import build_ini,parse_sections,validate_ini
        from tools.owner_code import c2_lines
        from tools.fixture_position_code import HOOK
        from tools.fixture_relayout import replace
        from tools.campaign_snapshot import capture
        _,state,ini,snap=source('CH10-CHAPTER-COMPLETE')
        _,mem=load_mem1(state,DEFAULT_IMAGE)
        rows,distance=positioning(snap['game'],mem)
        self.assertEqual(distance,23)
        body=words(11,3,1,rows,queue=dict(turn=2,exit=(6,2)))
        text=build_ini(['COOP-P6','EXP-16'],verbose=False)
        text+='\n[Gecko]\n$DBG-CAMP-END test\n'+'\n'.join(c2_lines(HOOK,body))+'\n[Gecko_Enabled]\n$DBG-CAMP-END test\n'
        text='\n'.join('['+key+']\n'+'\n'.join(value) for key,value in parse_sections(text).items())+'\n'
        self.assertEqual(validate_ini(text),3216)
        with tempfile.TemporaryDirectory(dir=ROOT/'work') as folder:
            target=Path(folder)/'new.sav'
            result=replace(state,ini.read_text(),text,target)
            self.assertEqual(len(result['edit_spans']),3)
            config=Path(folder)/'config.ini';config.write_text(text)
            out=capture(target,DEFAULT_IMAGE,config,'offline-test')
            self.assertEqual(out['game'],snap['game'])
            self.assertTrue(out['evidence']['intended_c2_verified'])
            with self.assertRaises(ValueError): replace(state,ini.read_text(),text,target)
            from tools.netplay_package import enabled_codes
            sections=parse_sections(text);lines=sections['Gecko']
            first=lines.index('$'+enabled_codes(text)[0][1])+2
            lines[first]=f'{int(lines[first][:8],16)^1:08X}'+lines[first][8:]
            unsafe='\n'.join('['+k+']\n'+'\n'.join(v) for k,v in sections.items())+'\n'
            with self.assertRaisesRegex(ValueError,'stable gameplay prefix'):
                replace(state,ini.read_text(),unsafe,Path(folder)/'unsafe.sav')


class NewVerdictTests(unittest.TestCase):
    def ch7_pair(self):
        from tests.test_human_scenarios import PACKAGE
        original=json_load(PACKAGE/'CH6-IKE-COMPLETE/captures/reloaded/snapshot.json')['game']
        g=copy.deepcopy(original);g.update(phase=3,turn=1)
        g['control'][3]=1
        actor=next(u for u in g['units'] if u['pid']=='PID_OSCAR');actor['force']=3;actor['flags']&=~1
        evidence=dict(intended_c2_verified=True,codes_fingerprint='8609ae9f49fd879f',state_sha256='before')
        before=dict(game=g,evidence=evidence);after=copy.deepcopy(before)
        after['evidence']['state_sha256']='after';next(u for u in after['game']['units'] if u['pid']=='PID_OSCAR')['flags']|=1
        return original,dict(before=before,after=after)

    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH6-IKE-COMPLETE/captures/reloaded/snapshot.json').is_file(),'private source unavailable')
    def test_ch7_wait_requires_ownership_progression_original_script_and_human(self):
        from tools.next_verdicts import ch7_wait
        from tools.next_scenarios import OBS7
        original,pair=self.ch7_pair();obs=dict.fromkeys(OBS7,True)
        self.assertEqual(ch7_wait(pair,obs,original)['status'],'PASS')
        self.assertEqual(ch7_wait(pair,{},original)['status'],'INCONCLUSIVE')
        for mutation in ('force','hp','exp','items','script','phase','acted','hooks','human'):
            bad=copy.deepcopy(pair);o=dict(obs);actor=next(u for u in bad['after']['game']['units'] if u['pid']=='PID_OSCAR')
            if mutation=='force':actor['force']=0
            elif mutation=='hp':actor['hp']-=1
            elif mutation=='exp':actor['exp']+=1
            elif mutation=='items':actor['inventory_slots_hex']='00'*64
            elif mutation=='script':bad['after']['game']['event_scripts']['campaign_ids']=[9]
            elif mutation=='phase':bad['after']['game']['phase']=1
            elif mutation=='acted':actor['flags']&=~1
            elif mutation=='hooks':bad['after']['evidence']['intended_c2_verified']=False
            else:o['p1_cannot_command_oscar']=False
            with self.subTest(mutation=mutation):self.assertEqual(ch7_wait(bad,o,original)['status'],'FAIL')

    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH10-CHAPTER-COMPLETE/scenario.json').is_file(),'new private fixture unavailable')
    def test_ch10_retention_rejects_wrong_prisoner_history_loss_and_unproved_native_load(self):
        from tools.next_scenarios import source,BLUE,YELLOW,OBS10
        from tools.next_verdicts import ch10_completion
        from tools.campaign_event_model import ESCAPE_KEYS
        _,_,_,original=source('CH10-CHAPTER-COMPLETE')
        setup=json_load(ROOT/'work/scenarios/human_v1/CH10-CHAPTER-COMPLETE/scenario.json')['setup']
        src=original['game'];snaps={}
        for label in ('staged','before','after','next_prep','reloaded'):
            g=copy.deepcopy(src)
            for row in setup['records']:next(u for u in g['units'] if u['slot']==row['slot'])['xy']=list(row['destination_xy'])
            if label!='staged':g.update(phase=0,turn=2)
            for u in g['units']:
                if label=='before' and u['pid'] in BLUE and u['pid']!='PID_IKE':u.update(force=5,escaped=True)
                if label=='before' and u['pid']=='PID_IKE':u['xy']=[6,2]
                if label in ('after','next_prep','reloaded'):
                    if u['pid'] in (*BLUE,*YELLOW,'PID_KEVIN','PID_MORDY'):u['force']=5 if label=='after' else 0
                    elif u['pid'] in ('PID_CHAP','PID_NEPENEE'):u['force']=4
            if label=='after':g['event_flags']['values']['gf_complete']=True
            if label in ('next_prep','reloaded'):
                g['chapter']=12;g['turn']=1;g['event_scripts'].update(campaign_ids=[12],chapter_matches=True)
            snaps[label]=dict(game=g,evidence=dict(state_sha256=label,intended_c2_verified=True,codes_fingerprint='92f0ad0562beaef9'))
        obs=dict.fromkeys(OBS10,True)
        self.assertEqual(ch10_completion(snaps,obs,src,setup,True)['status'],'PASS')
        self.assertEqual(ch10_completion(snaps,obs,src,setup,False)['status'],'INCONCLUSIVE')
        self.assertEqual(ch10_completion(snaps,{},src,setup,True)['status'],'INCONCLUSIVE')
        for mutation in ('kieran_lost','brom_retained','history','early_ike','items','native','flag','hooks','staging'):
            bad=copy.deepcopy(snaps)
            if mutation=='kieran_lost':bad['reloaded']['game']['units']=[u for u in bad['reloaded']['game']['units'] if u['pid']!='PID_KEVIN']
            elif mutation=='brom_retained':next(u for u in bad['next_prep']['game']['units'] if u['pid']=='PID_CHAP')['force']=0
            elif mutation=='history':bad['before']['game']['event_flags']['values'][ESCAPE_KEYS['PID_KEVIN']]=False
            elif mutation=='early_ike':next(u for u in bad['before']['game']['units'] if u['pid']=='PID_TIAMAT')['force']=0
            elif mutation=='items':next(u for u in bad['next_prep']['game']['units'] if u['pid']=='PID_OSCAR')['inventory_slots_hex']='00'*64
            elif mutation=='native':next(u for u in bad['reloaded']['game']['units'] if u['pid']=='PID_KEVIN')['exp']=1
            elif mutation=='flag':bad['after']['game']['event_flags']['values']['gf_complete']=False
            elif mutation=='hooks':bad['after']['evidence']['intended_c2_verified']=False
            else:bad['staged']['game']['units'][0]['hp']-=1
            with self.subTest(mutation=mutation):self.assertEqual(ch10_completion(bad,obs,src,setup,True)['status'],'FAIL')


def json_load(path):
    import json
    return json.loads(path.read_text(encoding='utf-8'))


class ActionVerdictTests(unittest.TestCase):
    def pair(self,name):
        from tools.action_scenarios import source
        _,_,snap=source(name);src=snap['game']
        manifest=json_load(ROOT/'work/scenarios/human_v1'/name/'scenario.json')
        before=copy.deepcopy(snap)
        before['evidence'].update(codes_fingerprint=manifest['fingerprint'],state_sha256='before')
        for row in manifest['setup']['records']:
            next(u for u in before['game']['units'] if u['slot']==row['slot'])['xy']=list(row['destination_xy'])
        after=copy.deepcopy(before);after['evidence']['state_sha256']='after'
        return src,manifest,dict(before=before,after=after)

    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH6-YELLOW-RESCUE/scenario.json').is_file(),'private candidate unavailable')
    def test_rescue_requires_reciprocal_links_role_bits_identity_and_human_action(self):
        from tools.action_verdicts import verify
        from tools.action_scenarios import SPECS
        from tools.inspect_state import UNITS
        name='CH6-YELLOW-RESCUE';src,m,s=self.pair(name)
        a=next(u for u in s['after']['game']['units'] if u['pid']=='PID_OSCAR')
        b=next(u for u in s['after']['game']['units'] if u['pid']=='PID_KILROY')
        a['rescue_link']=UNITS+(b['slot']-1)*0x280;b['rescue_link']=UNITS+(a['slot']-1)*0x280
        a['flags']|=2;b['flags']|=4;b['xy']=list(a['xy'])
        obs=dict.fromkeys(SPECS[name]['observations'],True)
        self.assertEqual(verify(name,s,obs,src,m['setup'],m['fingerprint'])['status'],'PASS')
        self.assertEqual(verify(name,s,{},src,m['setup'],m['fingerprint'])['status'],'INCONCLUSIVE')
        screen=copy.deepcopy(s)
        for label in ('before','after'):
            next(u for u in screen[label]['game']['units'] if u['slot']==10)['flags']^=0x20
        next(u for u in screen['after']['game']['units'] if u['slot']==16)['flags']^=0x20
        rendered=verify(name,screen,obs,src,m['setup'],m['fingerprint'])
        self.assertEqual(rendered['status'],'PASS')
        self.assertTrue(rendered['render_cache_changes']['setup'])
        self.assertTrue(rendered['render_cache_changes']['action'])
        for bit in (1,2,4,0x400,0x4000,0x8000,0x10000,0x20000000,0x40000000):
            bad=copy.deepcopy(screen)
            next(u for u in bad['after']['game']['units'] if u['slot']==16)['flags']^=bit
            with self.subTest(unrelated_bit=hex(bit)):
                self.assertEqual(verify(name,bad,obs,src,m['setup'],m['fingerprint'])['status'],'FAIL')
        for mutation in ('link','role','force','hp','items','ownership','xy','extra_flags'):
            bad=copy.deepcopy(s);p=next(u for u in bad['after']['game']['units'] if u['pid']=='PID_KILROY')
            if mutation=='link':p['rescue_link']=0
            elif mutation=='role':p['flags']&=~4
            elif mutation=='force':p['force']=3
            elif mutation=='hp':p['hp']=0
            elif mutation=='items':p['inventory_slots_hex']='00'*64
            elif mutation=='ownership':p['owned']=True
            elif mutation=='extra_flags':p['flags']|=0x4000
            else:p['xy']=[1,1]
            with self.subTest(mutation=mutation):self.assertEqual(verify(name,bad,obs,src,m['setup'],m['fingerprint'])['status'],'FAIL')

    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH6-YELLOW-COMBAT/scenario.json').is_file(),'private candidate unavailable')
    def test_combat_requires_actual_damage_exp_and_original_weapon_use_decrease(self):
        from tools.action_verdicts import verify
        from tools.action_scenarios import SPECS
        name='CH6-YELLOW-COMBAT';src,m,s=self.pair(name)
        a=next(u for u in s['after']['game']['units'] if u['pid']=='PID_OSCAR');a['exp']+=10
        raw=bytearray.fromhex(a['inventory_slots_hex']);raw[4]-=1;a['inventory_slots_hex']=raw.hex()
        next(u for u in s['after']['game']['units'] if u['slot']==13)['hp']-=10
        obs=dict.fromkeys(SPECS[name]['observations'],True)
        self.assertEqual(verify(name,s,obs,src,m['setup'],m['fingerprint'])['status'],'PASS')
        for mutation in ('exp','uses','damage','death','flags'):
            bad=copy.deepcopy(s);a=next(u for u in bad['after']['game']['units'] if u['pid']=='PID_OSCAR')
            original=next(u for u in bad['before']['game']['units'] if u['pid']=='PID_OSCAR')
            if mutation=='exp':a['exp']=original['exp']
            elif mutation=='uses':a['inventory_slots_hex']=original['inventory_slots_hex']
            elif mutation=='damage':next(u for u in bad['after']['game']['units'] if u['slot']==13)['hp']+=10
            elif mutation=='death':a['hp']=0
            else:bad['after']['game']['event_flags']['values']['gf_complete']=True
            with self.subTest(mutation=mutation):self.assertEqual(verify(name,bad,obs,src,m['setup'],m['fingerprint'])['status'],'FAIL')

    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH6-YELLOW-FATAL/scenario.json').is_file(),'private candidate unavailable')
    def test_fatal_probe_cannot_pass_from_survival_or_unmarked_hp_zero(self):
        from tools.action_verdicts import verify
        from tools.action_scenarios import SPECS
        name='CH6-YELLOW-FATAL';src,m,s=self.pair(name);obs=dict.fromkeys(SPECS[name]['observations'],True)
        self.assertEqual(verify(name,s,obs,src,m['setup'],m['fingerprint'])['status'],'INCONCLUSIVE')
        a=next(u for u in s['after']['game']['units'] if u['pid']=='PID_OSCAR');a['hp']=0
        self.assertEqual(verify(name,s,obs,src,m['setup'],m['fingerprint'])['status'],'INCONCLUSIVE')
        a.update(death_record=True,death_chapter=7,force=6)
        self.assertEqual(verify(name,s,obs,src,m['setup'],m['fingerprint'])['status'],'PASS')
        a['force']=7
        self.assertEqual(verify(name,s,obs,src,m['setup'],m['fingerprint'])['status'],'FAIL')

    @unittest.skipUnless((ROOT/'work/fixtures/ch6_escape_native_v2/before.s02.sav').is_file(),'private source unavailable')
    def test_original_rescue_bounded_predicates_admit_yellow_blue_but_not_reversed_capacity(self):
        from tools.action_scenarios import source
        from tools.action_prerequisites import rescue
        from tools.inspect_state import load_mem1
        from tools.verify_game import DEFAULT_IMAGE
        p,_,_=source('CH6-YELLOW-RESCUE');_,mem=load_mem1(p,DEFAULT_IMAGE)
        r=rescue(mem,2,14,(13,24),(14,24))
        self.assertEqual((r['carrier_capacity_stat'],r['passenger_capacity_stat'],r['force_relation']),(33,8,2))
        self.assertTrue(r['all_bounded_predicates'])
        r=rescue(mem,14,2,(14,24),(13,24))
        self.assertFalse(r['static_predicates']['capacity'])
        self.assertFalse(r['all_bounded_predicates'])


class LauncherTests(unittest.TestCase):
    def test_runtime_rejected_staging_cannot_be_relaunched_or_rebuilt(self):
        from tools.next_scenarios import runtime_candidate
        with self.assertRaisesRegex(ValueError,'Green Brom'):
            runtime_candidate('92f0ad0562beaef9')
        runtime_candidate('8609ae9f49fd879f')

    def test_accepted_runtime_stays_visible_when_current_card_blocks_seed_launch(self):
        import json
        from unittest.mock import patch
        from tools.test_scenario import listing
        with tempfile.TemporaryDirectory(dir=ROOT/'work') as folder:
            d=Path(folder);(d/'verified').mkdir();(d/'verified/scenario.json').write_text('{}')
            with patch('tools.test_scenario.known',return_value=('verified','missing')),patch('tools.test_scenario.BLOCKED',{}),patch('tools.test_scenario.review',return_value=dict(status='PASS')),patch('tools.test_scenario.check',side_effect=ValueError('private card changed')):
                rows=listing(d)
            self.assertEqual(rows[0]['readiness'],'HUMAN_VERIFIED')
            self.assertEqual(rows[0]['offline_validation'],'REFUSED')
            self.assertEqual(rows[1]['readiness'],'MISSING_PREREQUISITES')
    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH7-PLAYER2-CONTROL/scenario.json').is_file(),'private candidate unavailable')
    def test_candidate_checks_do_not_change_observations_and_reject_known_runtime_failure(self):
        from tools.test_scenario import check,NEXT,scenario_dir
        for name in NEXT:
            with self.subTest(name=name):
                obs_path=scenario_dir(name)/'observations.json'
                before=obs_path.read_bytes()
                if name=='CH10-CHAPTER-COMPLETE':
                    with self.assertRaisesRegex(ValueError,'CAMP-AF'):check(name)
                    self.assertEqual(obs_path.read_bytes(),before)
                    continue
                p=check(name)
                self.assertLessEqual(p['gecko_bytes'],3248)
                self.assertEqual('--save_state' in p['arguments'],name!='CH7-PLAYER2-CONTROL')
                self.assertEqual(obs_path.read_bytes(),before)

    def test_collect_refuses_changed_raw_and_keeps_existing_evidence(self):
        import json
        from unittest.mock import patch
        from tools.test_scenario import collect_all
        from tools.campaign_test_pack import sha
        with tempfile.TemporaryDirectory(dir=ROOT/'work') as folder:
            d=Path(folder);(d/'captures/before').mkdir(parents=True);(d/'User').mkdir()
            (d/'case.json').write_text(json.dumps(dict(captures=['before','after'])))
            raw=d/'before.sav';raw.write_bytes(b'original')
            (d/'captures/before/manifest.json').write_text(json.dumps(dict(state_sha256=sha(raw))))
            with patch('tools.test_scenario.configuration'),patch('tools.test_scenario.review',return_value=dict(status='INCONCLUSIVE')):
                r=collect_all(d);self.assertEqual(r['retained'],['before']);self.assertEqual(r['missing_raw_states'],['after'])
                raw.write_bytes(b'changed')
                with self.assertRaisesRegex(ValueError,'differs from immutable'):collect_all(d)
            self.assertFalse((d/'captures/after').exists())

    @unittest.skipUnless((ROOT/'Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso').is_file(),'original image unavailable')
    def test_later_gap_report_uses_original_commands_and_never_promotes_a_chapter_number(self):
        from tools.scenario_prerequisites import report
        data=report([])
        self.assertEqual(len(data['cases']),6)
        self.assertTrue(all(r['status']=='BLOCKED' and not r['runnable'] for r in data['cases']))
        jill=next(r for r in data['cases'] if r['scenario']=='CH20-JILL-DEFECTION')
        self.assertTrue(any(c['command']=='PersonGetYellLevel' for c in jill['original_relevant_calls']))
        self.assertTrue(any(c['actor']=='PID_JILL' and c['target']=='PID_SIHARAMU' for c in jill['directed_conversations']))
        self.assertEqual(next(r for r in data['cases'] if r['scenario']=='CH27-2-SPECIAL')['chapter_internal'],29)
