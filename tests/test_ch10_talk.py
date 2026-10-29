import copy
import json
import struct
import unittest
from pathlib import Path
from tools.ch10_talk_fixture import preconditions,verify
from tools.ch10_talk_code import words,GET_FLAG,KEY,HOOK
from tools.fixture_position_code import GET_UNIT_BY_PID,UNIT_GET_BY_POS,UNIT_SET_POS
from tools.talk_evidence import DOOR_KEY


def sample():
    units=[]
    for slot,pid,force,xy in ((2,'PID_OSCAR',3,[19,19]),(19,'PID_KEVIN',2,[20,19])):
        units.append({'slot':slot,'pid':pid,'force':force,'xy':xy,'hp':28,'level':6,'exp':28,
                      'class':'fixture_class','flags':0x400 if slot==2 else 0x80020,
                      'rescue_link':0,'action_state_byte':0,'death_record':False,'inventory_slots_hex':'ab'*64})
    before={'evidence':{'commit':'same','dolphin':'2609a','codes_fingerprint':'fixture','state_sha256':'before',
                       'intended_c2_verified':True,'codes':['COOP-P6','EXP-16','FIXTURE-LOADER','DBG-CAMP-TALK']},
            'game':{'chapter':11,'phase':3,'turn':1,'control':[1,2,2,1],
                    'event_scripts':{'complete_chain':True,'campaign_ids':[11],'chapter_matches':True},'units':units,
                    'talk_fixture':{'map_dimensions':[24,23],
                                    'menu_context':{'mode12':0,'flags16':0},
                                    'cell_door':{'bounds':[19,14,19,14],'state_byte':128},
                                    'cells':[{'xy':[19,19],'occupant_id':2,'edge_mask':15},
                                             {'xy':[20,19],'occupant_id':19,'edge_mask':15}],
                                    'flags':{KEY:False,DOOR_KEY:False,'F1914':False,'gf_complete':False,'gf_gameover':False}}}}
    after=copy.deepcopy(before);after['evidence']['state_sha256']='after'
    after['game']['units'][1]['force']=3
    after['game']['units'][0]['flags']|=1
    after['game']['talk_fixture']['flags'][KEY]=True
    return before,after


class Ch10TalkTests(unittest.TestCase):
    @unittest.skipUnless(Path('work/fixtures/ch10_oscar_kieran_v1/after.s02.sav').exists(),'private Talk captures not present')
    def test_captured_original_talk_preserves_identity_and_requires_observation(self):
        from tools.campaign_snapshot import capture
        from tools.verify_game import DEFAULT_IMAGE
        root=Path('work/fixtures/ch10_oscar_kieran_v1')
        ini=root/'User/GameSettings/GFEE01.ini'
        before=capture(root/'before.s02.sav',DEFAULT_IMAGE,ini,'regression')
        after=capture(root/'after.s02.sav',DEFAULT_IMAGE,ini,'regression')
        result=verify(before,after,observed=True)
        self.assertEqual(result['failures'],[])
        self.assertEqual(result['status'],'PASS')
        self.assertEqual(verify(before,after)['status'],'INCONCLUSIVE')
        self.assertEqual(before['game']['talk_fixture']['menu_context']['actor_slot'],2)
        self.assertEqual(result['flag_changes'],{KEY:[False,True]})

    def test_selected_actor_can_be_absent_from_occupancy_without_relaxing_target_checks(self):
        before,after=sample()
        before['game']['talk_fixture']['cells'][0]['occupant_id']=0
        context=before['game']['talk_fixture']['menu_context']
        context['actor_slot']=2
        self.assertEqual(verify(before,after,observed=True)['status'],'PASS')
        for actor in (None,19):
            context['actor_slot']=actor
            self.assertEqual(verify(before,after,observed=True)['status'],'FAIL')
        context['actor_slot']=2
        before['game']['talk_fixture']['cells'][1]['occupant_id']=0
        self.assertEqual(verify(before,after,observed=True)['status'],'FAIL')

    def test_original_ui_observation_is_required_for_event_pass(self):
        before,after=sample()
        self.assertEqual(preconditions(before,positioned=True),[])
        self.assertEqual(verify(before,after)['status'],'INCONCLUSIVE')
        result=verify(before,after,observed=True)
        self.assertEqual(result['status'],'PASS')
        self.assertEqual(result['flag_changes'],{KEY:[False,True]})
        self.assertEqual(len(result['units']),2)

    def test_faction_identity_inventory_door_or_key_damage_rejects_claim(self):
        for mutation in ('force','lost','inventory','door','key','same_file','control','script'):
            before,after=sample()
            if mutation=='force':after['game']['units'][1]['force']=0
            if mutation=='lost':after['game']['units'].pop()
            if mutation=='inventory':after['game']['units'][0]['inventory_slots_hex']='00'*64
            if mutation=='door':after['game']['talk_fixture']['cell_door']['state_byte']|=2
            if mutation=='key':after['game']['talk_fixture']['flags'][KEY]=False
            if mutation=='same_file':after['evidence']['state_sha256']='before'
            if mutation=='control':after['game']['control'][3]=2
            if mutation=='script':after['game']['event_scripts']['campaign_ids']=[7]
            with self.subTest(mutation=mutation):self.assertEqual(verify(before,after,True)['status'],'FAIL')

    def test_adjacency_does_not_override_blocking_state_or_consumed_key(self):
        for mutation in ('wall','occupied','consumed','door_open','acted','action_state','missing_action','rescue'):
            before,_=sample()
            if mutation=='wall':before['game']['talk_fixture']['cells'][0]['edge_mask']&=~2
            if mutation=='occupied':before['game']['talk_fixture']['cells'][0]['occupant_id']=19
            if mutation=='consumed':before['game']['talk_fixture']['flags'][KEY]=True
            if mutation=='door_open':before['game']['talk_fixture']['flags'][DOOR_KEY]=True
            if mutation=='acted':before['game']['units'][0]['flags']|=1
            if mutation=='action_state':before['game']['units'][0]['action_state_byte']=16
            if mutation=='missing_action':before['game']['units'][0].pop('action_state_byte')
            if mutation=='rescue':before['game']['units'][1]['rescue_link']=0x80001000
            with self.subTest(mutation=mutation):self.assertTrue(preconditions(before,positioned=True))

    def test_setup_native_calls_and_direct_writes_are_restricted(self):
        code=words()
        jump=next(i for i,w in enumerate(code) if w>>26==18 and w&1)
        target=jump+(code[jump]&0x3FFFFFC)//4
        instructions=code[:jump+1]+code[target:]
        calls=[]
        for i,w in enumerate(instructions[:-3]):
            if w&0xFFFF0000==0x3D800000 and instructions[i+1]&0xFFFF0000==0x618C0000:
                self.assertEqual(instructions[i+2:i+4],[0x7D8903A6,0x4E800421])
                calls.append(((w&65535)<<16)|(instructions[i+1]&65535))
        self.assertEqual(calls,[GET_FLAG,GET_UNIT_BY_PID,GET_UNIT_BY_PID,UNIT_GET_BY_POS,UNIT_SET_POS])
        # In particular: no UnitTransferToForce, set, DoorOpen or Talk call.
        for w in instructions:
            if w>>26 in (36,37,38,39,44,45,47):
                self.assertIn(w>>26,(36,37))
                self.assertEqual((w>>16)&31,1,'setup direct stores must target its stack only')
        raw=struct.pack('>'+str(len(code))+'I',*code)
        self.assertIn(KEY.encode('shift_jis')+b'\0',raw)

    @unittest.skipUnless(Path('work/fixtures/ch10_oscar_kieran_v1/seed.s02.sav.json').exists(),'private fixture not present')
    def test_seed_changes_only_gecko_tail_and_preserves_source_profile(self):
        import hashlib
        from tools.fe9.savestate import read_state,MEM1_BASE
        from tools.inspect_state import load_mem1
        from tools.verify_game import DEFAULT_IMAGE
        from tools.install_codes import validate_ini
        root=Path('work/fixtures/ch10_oscar_kieran_v1')
        record=json.loads((root/'seed.s02.sav.json').read_text())
        source=Path(record['source']);_,a=read_state(source);_,b=read_state(root/'seed.s02.sav')
        _,mem=load_mem1(source,DEFAULT_IMAGE)
        start=mem.offset+int(record['edit_address'],16)-MEM1_BASE;end=start+record['edit_bytes']
        self.assertEqual(a[:start],b[:start]);self.assertEqual(a[end:],b[end:])
        self.assertEqual(len(a),len(b));self.assertNotEqual(a[start:end],b[start:end])
        self.assertEqual(validate_ini((root/'User/GameSettings/GFEE01.ini').read_text()),3240)
        manifest=json.loads((root/'fixture.json').read_text(encoding='utf-8'))
        for path,expected in manifest['source_files_sha256'].items():
            self.assertEqual(hashlib.sha256(Path(path).read_bytes()).hexdigest(),expected)
