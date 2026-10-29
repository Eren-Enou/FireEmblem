import copy
import unittest
from pathlib import Path
from tools.unit_lifecycle import Lifecycle, UnresolvedLifecycle, from_snapshot
from tools.campaign_event_model import LifecycleWorld, load_scripts, PRISONERS
from tools.verify_game import DEFAULT_IMAGE


def roster():
    return {pid: {'pid': pid, 'slot': slot, 'force': force, 'flags': flags,
                  'level': 6, 'exp': 28, 'hp': 28, 'inventory_slots_hex': 'ab'*64,
                  'rescue_link': 0}
            for slot, (pid, force, flags) in enumerate([
                ('PID_IKE', 0, 0x400), ('PID_OSCAR', 3, 0x400), ('PID_KEVIN', 3, 0x80000),
                ('NPC', 2, 0), ('ENEMY', 1, 0), ('AWAY', 7, 0x10), ('DEAD', 6, 0x8008)], 1)}


class LifecycleTests(unittest.TestCase):
    def test_owned_yellow_return_is_distinct_from_native_temporary_partner(self):
        original = roster(); model = Lifecycle(original)
        model.all_escape(owners={'PID_OSCAR': 2})
        for pid in ('PID_IKE', 'PID_OSCAR'):
            actual = model.units[pid]
            self.assertEqual(actual['force'], 5)
            self.assertEqual(actual['flags'], original[pid]['flags'] | 0x4010)
            for key in ('pid', 'slot', 'level', 'exp', 'hp', 'inventory_slots_hex'):
                self.assertEqual(actual[key], original[pid][key])
        for pid in ('PID_KEVIN', 'NPC', 'ENEMY'):
            self.assertEqual(model.units[pid]['force'], 4)
            self.assertIsNone(model.units[pid]['pid'])
            self.assertEqual(model.units[pid]['flags'], 0)
        for pid in ('AWAY', 'DEAD'): self.assertEqual(model.units[pid], original[pid])
        self.assertEqual(original, roster())

    def test_mutated_blue_only_handback_loses_yellow_and_blanket_yellow_retains_guest(self):
        missing = Lifecycle(roster()); missing.all_escape()  # omit existing EXP-16 hand-back
        self.assertIsNone(missing.units['PID_OSCAR']['pid'])
        blanket = Lifecycle(roster())
        blanket.all_escape(owners={'PID_OSCAR': 2, 'PID_KEVIN': 2})  # deliberately wrong ownership
        self.assertEqual(blanket.units['PID_KEVIN']['force'], 5)
        correct = Lifecycle(roster()); correct.all_escape(owners={'PID_OSCAR': 2})
        self.assertNotEqual(blanket.units['PID_KEVIN'], correct.units['PID_KEVIN'])

    def test_flag_ownership_does_not_silently_change_fixed_table_contract(self):
        units = roster(); units['PID_KEVIN']['flags'] |= 0x60000000
        model = Lifecycle(units); model.all_escape(owners={'PID_OSCAR': 2})
        self.assertIsNone(model.units['PID_KEVIN']['pid'])
        model = Lifecycle(units); model.transfer('PID_OSCAR', 1)
        model.return_owned({'PID_OSCAR': 2})
        self.assertEqual(model.units['PID_OSCAR']['force'], 1)  # story enemy transfer wins

    def test_rescue_path_rejects_before_mutating_roster_or_ownership(self):
        units = roster(); units['PID_OSCAR']['rescue_link'] = 123
        model = Lifecycle(units)
        with self.assertRaises(UnresolvedLifecycle): model.all_escape(owners={'PID_OSCAR': 2})
        self.assertEqual(model.units, units)
        with self.assertRaises(UnresolvedLifecycle): model.escape('DEAD')
        with self.assertRaises(UnresolvedLifecycle): model.require_complete_native_proof()

    def test_duplicate_slots_and_ambiguous_owned_identity_are_invalid(self):
        units = roster(); units['NPC']['slot'] = units['PID_IKE']['slot']
        with self.assertRaisesRegex(ValueError, 'duplicate'): Lifecycle(units)
        units = roster(); units['NPC']['pid'] = 'PID_IKE'
        model = Lifecycle(units)
        units = roster(); units['NPC']['pid'] = 'PID_OSCAR'; units['NPC']['force'] = 3
        model = Lifecycle(units)
        with self.assertRaisesRegex(ValueError, 'ambiguous'): model.return_owned({'PID_OSCAR': 2})


@unittest.skipUnless(DEFAULT_IMAGE.exists(), 'pinned image absent')
class PrisonerLifecycleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.scripts = load_scripts()

    def world(self, **kwargs):
        return LifecycleWorld(self.scripts, owners={'PID_OSCAR': 2}, **kwargs)

    def test_talk_then_original_direct_escape_then_cleanup_prefix(self):
        for pid, actor in [('PID_KEVIN', 'PID_OSCAR'), ('PID_CHAP', 'PID_IKE'), ('PID_NEPENEE', 'PID_IKE')]:
            world = self.world(actor=pid)
            self.assertTrue(world.talk(actor, pid))
            self.assertEqual(world.units[pid]['force'], 3)
            world.run('Scripts/C11.cmb', 5)
            self.assertEqual(world.units[pid]['force'], 5)
            self.assertEqual(world.units[pid]['pid'] if 'pid' in world.units[pid] else pid, pid)
            self.assertTrue(world.units[pid]['flags'] & 0x4000)
            result = world.run('Scripts/C11.cmb', 57, stop_before={'MapFree'})
            self.assertEqual(result['halted_before']['command'], 'MapFree')
            self.assertEqual(world.units[pid]['force'], 5)
            self.assertEqual(world.units['PID_OSCAR']['force'], 5)
            with self.assertRaises(UnresolvedLifecycle): world.lifecycle.require_complete_native_proof()

    def test_closed_door_talk_alone_is_insufficient_in_projection(self):
        world = self.world()
        world.talk('PID_OSCAR', 'PID_KEVIN')
        world.run('Scripts/C11.cmb', 57, stop_before={'MapFree'})
        self.assertIsNone(world.units['PID_KEVIN']['pid'])
        self.assertEqual(world.units['PID_OSCAR']['force'], 5)

    def test_original_open_door_fallback_differs_on_maniac(self):
        for maniac in (False, True):
            world = self.world(maniac=maniac)
            world.run('Scripts/C11.cmb', 15)
            world.run('Scripts/C11.cmb', 57, stop_before={'MapFree'})
            for pid in ('PID_KEVIN', 'PID_CHAP'):
                self.assertEqual(world.units[pid]['force'], 4 if maniac else 5)
            self.assertEqual(world.units['PID_NEPENEE']['force'], 4)

    @unittest.skipUnless(Path('work/fixtures/ch10_oscar_kieran_v1/after.s02.sav').exists(), 'private state absent')
    def test_projection_from_accepted_talk_capture_is_read_only(self):
        from tools.campaign_snapshot import capture
        root = Path('work/fixtures/ch10_oscar_kieran_v1')
        snapshot = capture(root/'after.s02.sav', DEFAULT_IMAGE, root/'User/GameSettings/GFEE01.ini', 'offline')
        original = copy.deepcopy(snapshot)
        model = from_snapshot(snapshot)
        self.assertEqual(model.units['PID_KEVIN']['force'], 3)
        self.assertFalse(model.units['PID_KEVIN']['flags'] & 0x400)
        model.all_escape(owners={'PID_OSCAR': 2})
        self.assertIsNone(model.units['PID_KEVIN']['pid'])
        self.assertEqual(model.units['PID_OSCAR']['force'], 5)
        self.assertEqual(snapshot, original)
