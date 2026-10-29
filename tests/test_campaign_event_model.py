import copy
import unittest

from tools.campaign_event_model import (World, JillWorld, load_scripts, conversation_scene,
                                       PRISONERS, ESCAPE_KEYS, DOOR_KEYS)
from tools.fe9.events import functions, calls
from tools.fe9.event_vm import execute
from tools.verify_game import DEFAULT_IMAGE


@unittest.skipUnless(DEFAULT_IMAGE.exists(), 'pinned user-owned image absent')
class OriginalCampaignModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scripts = load_scripts()

    def assert_talk_effect(self, world, pid, original):
        self.assertEqual(world.units[pid]['force'], 3)
        self.assertEqual(world.units[pid]['flags'], original[pid]['flags'])
        self.assertNotIn('gf_complete', world.flags)
        self.assertFalse(world.doors)
        for other in original:
            if other != pid: self.assertEqual(world.units[other], original[other])

    def test_original_talk_identity_reversal_and_consumed_key(self):
        raw = self.scripts['Scripts/C11.cmb']
        self.assertEqual(conversation_scene(raw, 'PID_OSCAR', 'PID_KEVIN'), [29])
        self.assertEqual(conversation_scene(raw, 'PID_KEVIN', 'PID_OSCAR'), [29])
        self.assertEqual(conversation_scene(raw, 'PID_IKE', 'PID_KEVIN'), [])
        self.assertEqual(conversation_scene(raw, 'PID_NEPENEE', 'PID_IKE'), [])
        for actor, target in [('PID_OSCAR', 'PID_KEVIN'), ('PID_IKE', 'PID_CHAP'), ('PID_IKE', 'PID_NEPENEE')]:
            for force in (0, 3):
                world = World(self.scripts)
                world.units[actor]['force'] = force
                original = copy.deepcopy(world.units)
                self.assertTrue(world.talk(actor, target))
                self.assert_talk_effect(world, target, original)
                count = len(world.calls)
                self.assertFalse(world.talk(actor, target))
                self.assertEqual(len(world.calls), count)
        world = World(self.scripts)
        del world.units['PID_KEVIN']
        self.assertFalse(world.talk('PID_OSCAR', 'PID_KEVIN'))

    def test_real_startup_exists_helper_accepts_yellow_and_green_not_roster(self):
        for force in range(8):
            world = World(self.scripts)
            world.units['PID_KEVIN']['force'] = force
            result = world.native('UnitCheckExistsByPID2', ['PID_KEVIN'])
            self.assertEqual(result, 'PID_KEVIN' if force in (0, 1, 2, 3) else 0)
        world = World(self.scripts)
        del world.units['PID_KEVIN']
        self.assertEqual(world.native('UnitCheckExistsByPID2', ['PID_KEVIN']), 0)

    def test_cleanup_predicate_truth_table_not_permanent_recruitment(self):
        for pid in PRISONERS:
            for force in (2, 3, 5, 6, 7):
                for maniac in (False, True):
                    for door in (False, True):
                        for escaped in (False, True):
                            flags = ([DOOR_KEYS[pid]] if door else []) + ([ESCAPE_KEYS[pid]] if escaped else [])
                            world = World(self.scripts, maniac=maniac, flags=flags)
                            world.units[pid]['force'] = force
                            original_flags = world.units[pid]['flags']
                            result = world.run('Scripts/C11.cmb', 57, stop_before={'AllUnitEscape'})
                            self.assertEqual(result['halted_before']['command'], 'AllUnitEscape')
                            expected = not maniac and door and not escaped and force in (2, 3)
                            self.assertEqual(world.units[pid]['force'], 0 if expected else force,
                                             (pid, force, maniac, door, escaped))
                            self.assertEqual(world.units[pid]['flags'], original_flags)
                            self.assertFalse(world.escaped)

    def test_original_escape_actor_and_carried_prisoner_handback_precedes_native_escape(self):
        for pid in PRISONERS:
            for carried in (False, True):
                world = World(self.scripts, actor='PID_OSCAR' if carried else pid,
                              passenger=pid if carried else 0)
                world.units[pid]['force'] = 3
                world.run('Scripts/C11.cmb', 5)
                self.assertIn(ESCAPE_KEYS[pid], world.flags)
                self.assertEqual(world.units[pid]['force'], 0)
                self.assertEqual(world.bm[4], 2 if carried else 1)
                self.assertNotIn('gf_complete', world.flags)
                names = [c['command'] for c in world.calls]
                self.assertLess(names.index('UnitTransferToForce'), names.index('UnitEscape'))
                self.assertEqual(len(world.escaped), 1)

    def test_ike_identity_not_yellow_membership_controls_completion_in_both_chapters(self):
        for script, scene in [('Scripts/C07.cmb', 1), ('Scripts/C11.cmb', 5)]:
            for actor, passenger, complete in [('PID_OSCAR', 0, False), ('PID_OSCAR', 'PID_KEVIN', False),
                                                ('PID_IKE', 0, True), ('PID_OSCAR', 'PID_IKE', True)]:
                world = World(self.scripts, actor=actor, passenger=passenger)
                world.run(script, scene)
                self.assertEqual('gf_complete' in world.flags, complete)
                self.assertEqual(world.bm[4], 2 if passenger else 1)

    def test_original_door_event_sets_access_keys_without_talk_or_transfer(self):
        world = World(self.scripts)
        original = copy.deepcopy(world.units)
        world.run('Scripts/C11.cmb', 15)
        self.assertEqual(world.doors, {(19, 14)})
        self.assertEqual(world.flags, {'F1914', DOOR_KEYS['PID_KEVIN']})
        self.assertEqual(world.units, original)

    def test_force_transfer_updates_native_low_status_bits(self):
        world = World(self.scripts)
        world.units['PID_KEVIN']['flags'] = 0x60000018
        world.native('UnitTransferToForce', ['PID_KEVIN', 0])
        self.assertEqual(world.units['PID_KEVIN']['flags'], 0x60000000)
        world.native('UnitTransferToForce', ['PID_KEVIN', 5])
        self.assertEqual(world.units['PID_KEVIN']['flags'], 0x60000010)

    def test_wrong_transfer_opcode_argument_is_detected_by_talk_oracle(self):
        scripts = self.scripts.copy()
        raw = bytearray(scripts['Scripts/C11.cmb'])
        transfer = next(c for c in calls(raw) if c['function'] == 29 and c['command'] == 'UnitTransferToForceByPID')
        self.assertEqual(raw[transfer['offset']-2:transfer['offset']], b'\x19\x03')
        raw[transfer['offset']-1] = 0  # deliberate incorrect force0 mutation, only in memory
        scripts['Scripts/C11.cmb'] = bytes(raw)
        world = World(scripts)
        original = copy.deepcopy(world.units)
        self.assertTrue(world.talk('PID_OSCAR', 'PID_KEVIN'))
        with self.assertRaises(AssertionError): self.assert_talk_effect(world, 'PID_KEVIN', original)

    def test_unmodeled_native_and_unreached_boundary_cannot_silently_succeed(self):
        world = World(self.scripts)
        with self.assertRaisesRegex(ValueError, 'unmodeled native'): world.native('UnknownRecruit', [])
        result = world.run('Scripts/C11.cmb', 29, stop_before={'AllUnitEscape'})
        self.assertNotIn('halted_before', result)
        result = world.run('Scripts/C11.cmb', 57, stop_before={'AllUnitEscape'})
        self.assertFalse(any(c['command'] == 'AllUnitEscape' for c in world.calls))
        self.assertEqual(result['halted_before']['command'], 'AllUnitEscape')

    def test_vm_call_arguments_and_budgets_are_checked(self):
        world = World(self.scripts)
        with self.assertRaisesRegex(ValueError, 'argument count'):
            execute(self.scripts['Scripts/startup.cmb'], world.helpers['UnitCheckExistsByPID2'], world.native)
        with self.assertRaisesRegex(ValueError, 'step bound'):
            execute(self.scripts['Scripts/startup.cmb'], world.helpers['UnitCheckExistsByPID2'], world.native,
                    max_steps=3, arguments=['PID_KEVIN'])

    def test_jill_original_relationship_truth_table_in_blue_and_yellow(self):
        for force in (0, 3):
            for mist in range(4):
                for lethe in range(4):
                    world = JillWorld(self.scripts, force=force, mist=mist, lethe=lethe)
                    original_flags = world.units['PID_JILL']['flags']
                    self.assertTrue(world.talk('PID_JILL', 'PID_SIHARAMU', 'Scripts/C21.cmb'))
                    defects = mist != 3 and lethe != 3
                    self.assertEqual(world.units['PID_JILL']['force'], 1 if defects else force,
                                     (force, mist, lethe))
                    self.assertEqual(world.units['PID_JILL']['flags'], original_flags)
                    self.assertEqual(len(world.attack_sequences), int(defects))
                    if defects:
                        self.assertEqual(world.attack_sequences, [['PID_JILL', 'SEQ_ALLUNITATTACK100']])
                    count = len(world.calls)
                    self.assertFalse(world.talk('PID_JILL', 'PID_SIHARAMU', 'Scripts/C21.cmb'))
                    self.assertEqual(len(world.calls), count)

    def test_jill_reverse_is_separate_original_event_with_shared_consumed_key(self):
        raw = self.scripts['Scripts/C21.cmb']
        self.assertEqual(conversation_scene(raw, 'PID_JILL', 'PID_SIHARAMU'), [26])
        self.assertEqual(conversation_scene(raw, 'PID_SIHARAMU', 'PID_JILL'), [27])
        for force in (0, 3):
            for mist in range(4):
                for lethe in range(4):
                    world = JillWorld(self.scripts, force=force, mist=mist, lethe=lethe)
                    self.assertTrue(world.talk('PID_SIHARAMU', 'PID_JILL', 'Scripts/C21.cmb'))
                    defects = mist != 3 and lethe != 3
                    self.assertEqual(world.units['PID_JILL']['force'], 1 if defects else force)
                    self.assertFalse(world.attack_sequences)
                    self.assertFalse(world.talk('PID_JILL', 'PID_SIHARAMU', 'Scripts/C21.cmb'))

    def test_jill_wrong_identity_or_missing_actor_rejects_selection(self):
        world = JillWorld(self.scripts)
        self.assertFalse(world.talk('PID_OSCAR', 'PID_SIHARAMU', 'Scripts/C21.cmb'))
        del world.units['PID_JILL']
        self.assertFalse(world.talk('PID_JILL', 'PID_SIHARAMU', 'Scripts/C21.cmb'))
        self.assertFalse(world.calls)
