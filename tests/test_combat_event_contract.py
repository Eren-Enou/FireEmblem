import copy
import unittest
from tools.verify_game import DEFAULT_IMAGE
from tools.combat_event_contract import DISCOVERY,BOSS_TALK,discovery_scene,boss_scene,event_effect


@unittest.skipUnless(DEFAULT_IMAGE.exists(),'pinned user-owned original script unavailable')
class OriginalCombatFlagTests(unittest.TestCase):
    def test_generic_boss_scene_excludes_ike_and_uses_target_in_red_phase(self):
        for phase,actor,target,talk in ((3,'oscar','emil',True),(0,'ike','emil',False),
                                       (1,'emil','oscar',True),(1,'emil','ike',False)):
            with self.subTest(phase=phase,actor=actor,target=target):
                model=boss_scene(phase,{BOSS_TALK:False},actor=actor,target=target)
                self.assertEqual(model['values'][BOSS_TALK],talk)
                self.assertEqual(any(e['command']=='TalkEvent' for e in model['trace']['events']),talk)

    def test_only_emil_probe_admits_original_boss_and_discovery_effects(self):
        before=dict(complete_table_read=True,values={DISCOVERY:False,BOSS_TALK:False,'gf_complete':False})
        after=copy.deepcopy(before);after['values'].update({DISCOVERY:True,BOSS_TALK:True})
        valid,effect=event_effect('CH6-YELLOW-FATAL',before,after,3)
        self.assertTrue(valid);self.assertEqual(effect['scenes'],[17,19])
        for case in ('CH6-YELLOW-COMBAT','CH6-YELLOW-RESCUE','CH9-PARTNER-COMBAT'):
            self.assertFalse(event_effect(case,before,after,3)[0])
        self.assertFalse(event_effect('CH6-YELLOW-FATAL',after,before,3)[0])
        after['values']['gf_complete']=True
        self.assertFalse(event_effect('CH6-YELLOW-FATAL',before,after,3)[0])
        with self.assertRaisesRegex(ValueError,'unmodeled'):
            boss_scene(3,{})

    def test_original_scene_handles_blue_red_and_yellow_without_force_zero_gate(self):
        for phase,who in ((0,'actor'),(1,'target'),(3,'actor')):
            with self.subTest(phase=phase):
                result=discovery_scene(phase,{DISCOVERY:False,'gf_complete':False})
                self.assertEqual(result['bm'],{1:who})
                self.assertEqual(result['values'],{DISCOVERY:True,'gf_complete':False})
                self.assertEqual(result['trace']['return'],0)

    def test_only_registered_forward_discovery_effect_in_c06_combat_is_admitted(self):
        before=dict(complete_table_read=True,values={DISCOVERY:False,'gf_complete':False})
        after=copy.deepcopy(before);after['values'][DISCOVERY]=True
        for case in ('CH6-YELLOW-COMBAT','CH6-YELLOW-FATAL'):
            self.assertTrue(event_effect(case,before,after,3)[0])
        self.assertFalse(event_effect('CH6-YELLOW-RESCUE',before,after,3)[0])
        self.assertFalse(event_effect('CH9-PARTNER-COMBAT',before,after,3)[0])
        self.assertFalse(event_effect('CH6-YELLOW-COMBAT',after,before,3)[0])
        after['values']['gf_complete']=True
        self.assertFalse(event_effect('CH6-YELLOW-COMBAT',before,after,3)[0])
        with self.assertRaisesRegex(ValueError,'unmodeled'):
            discovery_scene(3,{'gf_complete':False})
