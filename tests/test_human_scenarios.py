import copy
import json
import struct
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.fixture_cpu import CACHE, CACHE_SIZE, SPR, guard_and_invalidate, locate
from tools.fe9.savestate import StateInfo
from tools.escape_position_code import words
from tools.fixture_position_code import ORIGINAL
from tools.test_scenario import PACKAGE, configuration, observe, check, scenario_dir


def cpu_blob():
    info = StateInfo('GFEE01',192,'Dolphin 2609a',1,0)
    offset = 12
    payload = bytearray(offset+CACHE+2*CACHE_SIZE)
    payload[:12]=struct.pack('<III',0x42,0x42,0x42)
    struct.pack_into('<I',payload,offset+4,0x80010000)
    struct.pack_into('<II',payload,offset+128,0x80020000,0x80020004)
    struct.pack_into('<I',payload,offset+SPR+287*4,0x83214)
    return info,payload,offset


class Mem:
    def __init__(self,words=None): self.words=words or {}
    def u32(self,address): return self.words.get(address,0)


class HumanScenarioTests(unittest.TestCase):
    def test_ch6_completion_rejects_loss_wrong_exit_and_native_payload_damage(self):
        from tools.scenario_verdicts import ch6_completion
        snapshots={}
        pids=('PID_IKE','PID_OSCAR','PID_TIAMAT','PID_KILROY','PID_SENERIO','PID_CHINON','PID_GATRIE')
        labels=('before_queue','before','after','next_prep','reloaded')
        for label in labels:
            units=[];chapter=7 if label in labels[:3] else 8
            for index,pid in enumerate(pids):
                force=7 if index>=5 else 5 if label=='after' or (label=='before' and pid!='PID_IKE') or (label=='before_queue' and pid=='PID_OSCAR') else 0
                units.append({'slot':index+1,'pid':pid,'class':'test','force':force,'hp':28,
                    'level':6,'exp':28,'rescue_link':0,'death_record':False,'escaped':force==5,
                    'flags':0x4000 if force==5 else 0,'xy':[13,26],'inventory_slots_hex':'ab'*64})
            snapshots[label]={'evidence':{'state_sha256':label,'intended_c2_verified':True,
                'codes_fingerprint':'e60e83a81d994e3b'},'game':{'chapter':chapter,'phase':0,'turn':2 if chapter==7 else 1,
                'control':[1,2,2,1],'event_scripts':{'complete_chain':True,'campaign_ids':[chapter],'chapter_matches':True},
                'event_flags':{'complete_table_read':True},'units':units}}
        observed=dict.fromkeys(('remaining_blue_original_escapes','ike_last','original_completion','oscar_present_next_chapter','fresh_native_load'),True)
        self.assertEqual(ch6_completion(snapshots,observed,True)['status'],'PASS')
        self.assertEqual(ch6_completion(snapshots,observed,False)['status'],'INCONCLUSIVE')
        incomplete=copy.deepcopy(snapshots);incomplete.pop('reloaded')
        self.assertEqual(ch6_completion(incomplete,observed,True)['status'],'INCONCLUSIVE')
        for change in ('lost','duplicate','oscar_items','oscar_exp','ike_exit','ike_order','away','script','hooks','human'):
            bad=copy.deepcopy(snapshots);obs=dict(observed)
            if change=='lost':bad['reloaded']['game']['units'].pop(1)
            elif change=='duplicate':bad['reloaded']['game']['units'].append(copy.deepcopy(bad['reloaded']['game']['units'][1]))
            elif change=='oscar_items':bad['reloaded']['game']['units'][1]['inventory_slots_hex']='changed'
            elif change=='oscar_exp':bad['next_prep']['game']['units'][1]['exp']=0
            elif change=='ike_exit':bad['before']['game']['units'][0]['xy']=[1,1]
            elif change=='ike_order':bad['before']['game']['units'][0]['force']=5
            elif change=='away':bad['reloaded']['game']['units'][5]['force']=0
            elif change=='script':bad['reloaded']['game']['event_scripts']['campaign_ids']=[7]
            elif change=='hooks':bad['after']['evidence']['intended_c2_verified']=False
            else:obs['fresh_native_load']=False
            with self.subTest(change=change):self.assertEqual(ch6_completion(bad,obs,True)['status'],'FAIL')

    @unittest.skipUnless((PACKAGE/'CH6-IKE-COMPLETE/captures/reloaded/snapshot.json').exists(),'private native-load evidence unavailable')
    def test_human_ch6_native_load_bundle_verifies_without_requiring_enemy_slots(self):
        from tools.campaign_test_pack import review
        result=review(PACKAGE/'CH6-IKE-COMPLETE')
        self.assertEqual(result['status'],'PASS')
        self.assertTrue(result['private_card_write_verified'])
        self.assertIn('enemy slot reconstruction/whole-engine equivalence',result['excludes'])

    def test_native_resume_requires_human_fresh_load_card_write_and_retained_records(self):
        from tests.test_campaign_test_pack import wait_pair
        from tools.scenario_verdicts import native_resume
        before,_=wait_pair()
        before['game']['event_flags']={'complete_table_read':True,'values':{'gf_complete':False}}
        after=copy.deepcopy(before);after['evidence']['state_sha256']='after'
        observed=dict.fromkeys(('native_suspend_accepted','fresh_boot_without_state',
            'native_resume_selected','same_roster_and_progression','no_unexpected_behavior'),True)
        self.assertEqual(native_resume(before,after,observed,True)['status'],'PASS')
        self.assertEqual(native_resume(before,after,observed,False)['status'],'INCONCLUSIVE')
        self.assertEqual(native_resume(before,after,{},True)['status'],'INCONCLUSIVE')
        for change in ('items','force','hp','acted','lost','duplicate','script','hooks','key','flags','same_state','human'):
            bad=copy.deepcopy(after);obs=dict(observed)
            if change=='items':bad['game']['units'][0]['inventory_slots_hex']='changed'
            elif change=='force':bad['game']['units'][1]['force']=2
            elif change=='hp':bad['game']['units'][0]['hp']-=1
            elif change=='acted':bad['game']['units'][0]['flags']^=1
            elif change=='lost':bad['game']['units'].pop()
            elif change=='duplicate':bad['game']['units'].append(copy.deepcopy(bad['game']['units'][1]))
            elif change=='script':bad['game']['event_scripts']['campaign_ids']=[7]
            elif change=='hooks':bad['evidence']['intended_c2_verified']=False
            elif change=='key':bad['game']['talk_fixture']['flags'].clear()
            elif change=='flags':bad['game'].pop('event_flags')
            elif change=='same_state':bad['evidence']['state_sha256']=before['evidence']['state_sha256']
            else:obs['fresh_boot_without_state']=False
            with self.subTest(change=change):self.assertEqual(native_resume(before,bad,obs,True)['status'],'FAIL')

    def test_native_resume_allows_ui_context_reset_without_claiming_whole_engine_equality(self):
        from tests.test_campaign_test_pack import wait_pair
        from tools.scenario_verdicts import native_resume
        before,_=wait_pair()
        before['game']['event_flags']={'complete_table_read':True,'values':{'gf_complete':False}}
        before['game']['units'].append({'slot':11,'pid':'ENEMY','force':1,'flags':0x80000})
        after=copy.deepcopy(before);after['evidence']['state_sha256']='after'
        after['game']['units'][-1]['flags']|=0x20
        after['game']['talk_fixture']['menu_context']={'actor_slot':None,'flags16':0}
        observed=dict.fromkeys(('native_suspend_accepted','fresh_boot_without_state',
            'native_resume_selected','same_roster_and_progression','no_unexpected_behavior'),True)
        verdict=native_resume(before,after,observed,True)
        self.assertEqual(verdict['status'],'PASS')
        self.assertIn('enemy transient flag interpretation',verdict['excludes'])

    def test_generated_queue_executes_guards_order_and_register_restoration(self):
        from tests.fixture_executor import run
        from tools.escape_scenarios import SPECS
        for spec in SPECS.values():
            code=words(spec['chapter'],spec['phase'],spec['turn'],spec['force'],spec['actors'],spec['exit'],156)
            actors={pid:{'xy':xy,'force':spec['force']} for pid,xy in spec['actors']}
            for index,pid in enumerate(actors):
                moves,gpr,spr,_=run(code,spec,actors)
                self.assertEqual(moves,[(index+1,*spec['exit'])]);self.assertTrue(gpr);self.assertTrue(spr)
                actors[pid].update(force=5,flags=0x4000)
            self.assertEqual(run(code,spec,actors)[0],[])
            actors={pid:{'xy':xy,'force':spec['force']} for pid,xy in spec['actors']}
            self.assertEqual(run(code,spec,actors,occupied=True)[0],[])
            self.assertEqual(run(code,spec,actors,chapter=99)[0],[])
            first=next(iter(actors))
            for mutation,value in [('force',1),('flags',1),('hp',0),('rescue',123),('xy',(0,0))]:
                changed=copy.deepcopy(actors);changed[first][mutation]=value
                with self.subTest(mutation=mutation):self.assertEqual(run(code,spec,changed)[0],[])

    def test_cpu_framing_requires_unique_supported_schema(self):
        info,payload,offset=cpu_blob()
        self.assertEqual(locate(payload,info)[0],offset)
        with self.assertRaises(ValueError): locate(payload+payload,info)
        for field,value in [('game_id','GFEJ01'),('state_version',191),('dolphin_version','other')]:
            bad=copy.copy(info);setattr(bad,field,value)
            with self.subTest(field=field),self.assertRaises(ValueError):locate(payload,bad)

    def test_replacement_rejects_active_register_and_stack_returns(self):
        for location in ('gpr','lr','ctr','stack','cycle'):
            info,payload,offset=cpu_blob();mem=Mem()
            if location=='gpr':struct.pack_into('<I',payload,offset+3*4,0x80002900)
            elif location in ('lr','ctr'):struct.pack_into('<I',payload,offset+SPR+(8 if location=='lr' else 9)*4,0x80002900)
            elif location=='stack':mem=Mem({0x80010004:0x80002900})
            else:mem=Mem({0x80010000:0x80010000})
            with self.subTest(location=location),self.assertRaises(ValueError):guard_and_invalidate(payload,info,mem,0x80002D00,632)

    def test_only_overlapping_clean_cache_valid_bit_is_cleared(self):
        info,payload,offset=cpu_blob()
        cache=offset+CACHE; cache_set=(0x2D00>>5)&127
        payload[cache+0x8080+cache_set]=3
        struct.pack_into('<II',payload,cache+0x8100+cache_set*8*4,0x2D00,0x3D00)
        result,report=guard_and_invalidate(payload,info,Mem(),0x80002D00,32)
        self.assertEqual(len(report['invalidated']),1)
        self.assertEqual(result[cache+0x8080+cache_set],2)
        changes=[i for i,(a,b) in enumerate(zip(payload,result)) if a!=b]
        self.assertEqual(changes,[cache+0x8080+cache_set])
        payload[cache+0x9100+cache_set]=1
        with self.assertRaisesRegex(ValueError,'dirty'):guard_and_invalidate(payload,info,Mem(),0x80002D00,32)

    def test_stack_zero_and_native_bottom_sentinel_accepted(self):
        info,payload,_=cpu_blob()
        for end in (0,0xFFFFFFFF):
            _,report=guard_and_invalidate(payload,info,Mem({0x80010000:end}),0x80002D00,32)
            self.assertEqual(report['stack_frames'],[0x80010000])

    def test_generated_setup_fits_and_only_stores_to_own_stack(self):
        from tools.escape_scenarios import SPECS
        from tools.owner_code import GET_UNIT_BY_PID
        from tools.fixture_position_code import UNIT_SET_POS,UNIT_GET_BY_POS
        for spec in SPECS.values():
            code=words(spec['chapter'],spec['phase'],spec['turn'],spec['force'],spec['actors'],spec['exit'],156)
            self.assertEqual(len(code),156);self.assertEqual(code[-2:],[ORIGINAL,0])
            jump=next(i for i,w in enumerate(code) if w>>26==18 and w&1)
            end=jump+(code[jump]&0x3FFFFFC)//4
            instructions=code[:jump+1]+code[end:]
            calls=[]
            for i,w in enumerate(instructions[:-3]):
                if w&0xFFFF0000==0x3D800000 and instructions[i+1]&0xFFFF0000==0x618C0000:
                    calls.append(((w&65535)<<16)|(instructions[i+1]&65535))
            self.assertEqual(calls,[GET_UNIT_BY_PID,UNIT_GET_BY_POS,UNIT_SET_POS])
            for w in instructions:
                if w>>26 in (36,37,38,39,44,45,47):
                    self.assertIn(w>>26,(36,37));self.assertEqual((w>>16)&31,1)
            with self.assertRaises(ValueError):words(spec['chapter'],spec['phase'],spec['turn'],spec['force'],spec['actors'],spec['exit'],10)

    def test_card_overrides_rejected_but_normal_dolphin_exit_settings_allowed(self):
        with tempfile.TemporaryDirectory() as temp:
            profile=Path(temp);(profile/'Config').mkdir()
            path=profile/'Config/Dolphin.ini'
            base='[Core]\nEnableCheats=True\nSIDevice0=6\nSIDevice1=6\nCPUCore=1\n'
            path.write_text(base);configuration(profile)
            path.write_text(base+'SlotA=8\nSlotB=255\nMemcardAPath=\nGCIFolderAPath=\nOverrideRegionSettings=False\n')
            configuration(profile)
            for key in ('MemcardAPath','GCIPathA','EXIDevice0','OverrideRegionSettings'):
                path.write_text(base+key+'=C:/personal/card\n')
                with self.subTest(key=key),self.assertRaises(ValueError):configuration(profile)
            path.write_text(base+'SlotA=1\n')
            with self.assertRaises(ValueError):configuration(profile)

    def test_prisoner_escape_verdict_requires_ui_and_preserved_original_character(self):
        from tests.test_campaign_test_pack import wait_pair
        from tools.scenario_verdicts import prisoner_escape
        a,_=wait_pair()
        a['evidence']['codes']=['COOP-P6','EXP-16','FIXTURE-LOADER','DBG-CAMP-EXIT']
        a['evidence']['codes_fingerprint']='efc52ab6c1471602'
        a['game']['units'][1].update(xy=[6,2],escaped=False,death_record=False,rescue_link=0)
        a['game']['units'].append({'pid':'PID_IKE','force':0})
        b=copy.deepcopy(a);b['evidence']['state_sha256']='after'
        b['game']['units'][1].update(force=5,escaped=True,flags=0x84000)
        observed=dict.fromkeys(('original_escape','p2_command','no_unexpected_behavior'),True)
        self.assertEqual(prisoner_escape(a,b,{})['status'],'INCONCLUSIVE')
        self.assertEqual(prisoner_escape(a,b,observed)['status'],'PASS')
        for change in ('lost','wrong_force','no_escape','items','oscar','fingerprint','no_ui'):
            bad=copy.deepcopy(b);obs=dict(observed)
            if change=='lost':bad['game']['units'].pop(1)
            elif change=='wrong_force':bad['game']['units'][1]['force']=3
            elif change=='no_escape':bad['game']['units'][1]['escaped']=False
            elif change=='items':bad['game']['units'][1]['inventory_slots_hex']='changed'
            elif change=='oscar':bad['game']['units'][0]['hp']-=1
            elif change=='fingerprint':bad['evidence']['codes_fingerprint']='stale'
            else:obs['original_escape']=False
            with self.subTest(change=change):self.assertEqual(prisoner_escape(a,bad,obs)['status'],'FAIL')

    def test_native_card_refusal_is_inconclusive_even_without_after_capture(self):
        from tools.campaign_test_pack import review
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)
            (dest/'case.json').write_text(json.dumps({'id':'CH10-NATIVE-RESUME','captures':['before','after'],
                'observations':['native_suspend_accepted','no_unexpected_behavior']}))
            (dest/'observations.json').write_text(json.dumps({'observed':{'native_suspend_accepted':False},'notes':'not original card'}))
            self.assertEqual(review(dest)['status'],'INCONCLUSIVE')

    def test_observations_require_explicit_valid_names_and_keep_history(self):
        with tempfile.TemporaryDirectory() as temp:
            dest=Path(temp)
            (dest/'case.json').write_text('{"observations":["original_escape"]}')
            (dest/'observations.json').write_text('{"observed":{"original_escape":null},"notes":""}')
            self.assertTrue(observe(dest,['original_escape'],[],'human declaration')['observed']['original_escape'])
            self.assertFalse(observe(dest,[],['original_escape'],'correction')['observed']['original_escape'])
            self.assertEqual(len(list((dest/'observation-history').glob('*.json'))),2)
            with self.assertRaises(ValueError):observe(dest,['invented'],[],'')
            with self.assertRaises(ValueError):observe(dest,['original_escape'],['original_escape'],'')

    @unittest.skipUnless((PACKAGE/'CH6-IKE-COMPLETE/scenario.json').exists(),'private candidates unavailable')
    def test_private_seed_payload_deltas_and_source_hashes_are_bounded(self):
        from tools.campaign_test_pack import sha
        from tools.fe9.savestate import read_state
        from tools.inspect_state import load_mem1
        from tools.verify_game import DEFAULT_IMAGE
        for name in ('CH10-PRISONER-ESCAPE','CH6-IKE-COMPLETE'):
            dest=scenario_dir(name)
            record=json.loads((dest/'scenario.json').read_text(encoding='utf-8'))
            for src,digest in record['source_hashes'].items():self.assertEqual(sha(Path(src)),digest)
            source=next(Path(p) for p in record['source_hashes'] if p.endswith('after.s02.sav'))
            _,a=read_state(source);_,b=read_state(dest/'seed.s02.sav')
            _,mem=load_mem1(source,DEFAULT_IMAGE)
            setup=record['setup'];start=mem.offset+setup['address']-0x80000000
            ranges=[(start,start+setup['bytes'])]
            cpu=setup['cpu_safety']
            for item in cpu['invalidated']:
                off=cpu['cpu_offset']+CACHE+item['cache']*CACHE_SIZE+0x8080+item['set']
                ranges.append((off,off+1))
            cursor=0
            for left,right in sorted(ranges):
                self.assertEqual(a[cursor:left],b[cursor:left]);cursor=right
            self.assertEqual(a[cursor:],b[cursor:]);self.assertEqual(len(a),len(b))
            changed_card=any(sha(dest/'User/GC/USA/Card A'/filename)!=digest
                             for filename,digest in record['initial_cards'].items())
            if changed_card:
                with self.assertRaisesRegex(ValueError,'card changed'):check(name)
            else:
                self.assertEqual(check(name)['readiness'],'PREPARED_RUNTIME_UNVERIFIED')
            if name=='CH6-IKE-COMPLETE':self.assertNotIn('--save_state',check(name,True)['arguments'])

    def test_blocked_and_unknown_scenarios_refuse_launch(self):
        for name in ('CH17-STAGE-TRANSITIONS','CH10-PRISONER-CLEANUP','unknown'):
            with self.subTest(name=name),self.assertRaises(ValueError):check(name)
