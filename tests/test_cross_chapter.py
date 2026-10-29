import copy
import unittest
from tools.unit_lifecycle import Lifecycle, UnresolvedLifecycle
from tests.test_unit_lifecycle import roster


class CrossChapterProjectionTests(unittest.TestCase):
    def test_cleanup_availability_mapflags_and_fixed_ownership_sequence(self):
        source = roster(); source['DEAD']['hp'] = 0
        source['PID_OSCAR']['flags'] |= 0x60000000
        model = Lifecycle(source)
        model.all_escape(owners={'PID_OSCAR': 2})
        self.assertEqual(model.units['PID_OSCAR']['force'], 5)
        self.assertTrue(model.units['PID_OSCAR']['flags'] & 0x4000)
        model.restore_roster_availability()
        self.assertEqual(model.units['PID_OSCAR']['force'], 0)
        self.assertTrue(model.units['PID_OSCAR']['flags'] & 0x010000DC)
        model.map_start_flags(); model.apply_owned({'PID_OSCAR': 2})
        self.assertEqual(model.units['PID_OSCAR']['force'], 3)
        self.assertEqual(model.units['PID_IKE']['force'], 0)
        for pid in ('PID_OSCAR', 'PID_IKE'):
            unit = model.units[pid]
            self.assertTrue(unit['flags'] & 0x400)
            self.assertFalse(unit['flags'] & 0x4000)
            for key in ('pid','slot','hp','level','exp','inventory_slots_hex'):
                self.assertEqual(unit[key], source[pid][key])
        self.assertEqual(model.units['PID_OSCAR']['flags'] & 0x60000000, 0x60000000)
        for pid in ('DEAD','AWAY'): self.assertEqual(model.units[pid], source[pid])
        for pid in ('PID_KEVIN','NPC','ENEMY'): self.assertIsNone(model.units[pid]['pid'])
        with self.assertRaises(UnresolvedLifecycle): model.require_complete_native_proof()

    def test_story_absence_and_enemy_transfer_win_over_fixed_ownership(self):
        model = Lifecycle(roster())
        model.return_owned({'PID_OSCAR': 2}); model.transfer('PID_OSCAR', 7)
        model.restore_roster_availability(); model.map_start_flags(); model.apply_owned({'PID_OSCAR': 2})
        self.assertEqual(model.units['PID_OSCAR']['force'], 7)
        model.transfer('PID_OSCAR', 1); model.apply_owned({'PID_OSCAR': 2})
        self.assertEqual(model.units['PID_OSCAR']['force'], 1)
        # Original event must explicitly return the character before ownership applies.
        model.transfer('PID_OSCAR', 0); model.apply_owned({'PID_OSCAR': 2})
        self.assertEqual(model.units['PID_OSCAR']['force'], 3)

    def test_recruited_blue_available_unit_gets_player_flag_but_no_implicit_owner(self):
        source = roster(); source['PID_KEVIN']['force'] = 0
        model = Lifecycle(source); model.map_start_flags(); model.apply_owned({'PID_OSCAR': 2})
        self.assertEqual(model.units['PID_KEVIN']['force'], 0)
        self.assertTrue(model.units['PID_KEVIN']['flags'] & 0x400)
        self.assertFalse(model.units['PID_KEVIN']['flags'] & 0x60000000)
        self.assertEqual(model.units['NPC']['force'], 2)

    def test_wrong_mask_clearing_ownership_is_detected_against_boundary_contract(self):
        source = roster(); source['PID_OSCAR']['flags'] |= 0x60000000
        model = Lifecycle(source); model.return_owned({'PID_OSCAR':2}); model.map_start_flags()
        self.assertTrue(model.units['PID_OSCAR']['flags'] & 0x400)
        self.assertEqual(model.units['PID_OSCAR']['flags'] & 0x60000000, source['PID_OSCAR']['flags'] & 0x60000000)
        wrong = copy.deepcopy(model.units)
        wrong['PID_OSCAR']['flags'] &= 0x9FFFFFFF
        self.assertNotEqual(wrong['PID_OSCAR']['flags'] & 0x60000000, source['PID_OSCAR']['flags'] & 0x60000000)
