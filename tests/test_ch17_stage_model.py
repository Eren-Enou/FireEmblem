import copy
import unittest
from tools.ch17_stage_model import StageWorld, load, complete18_request, SCRIPT
from tools.fe9.events import calls, functions
from tools.verify_game import DEFAULT_IMAGE


@unittest.skipUnless(DEFAULT_IMAGE.exists(), 'pinned image absent')
class Chapter17ModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.scripts = load()

    def test_original_completion_prefix_accumulates_turns_and_clears_only_its_guard(self):
        for stage in (1, 2, 3):
            world = StageWorld(self.scripts, turn=9, previous_turns=7)
            result = world.completion_prefix(stage)
            self.assertEqual(world.bm[3], 9 if stage == 1 else 16)
            self.assertNotIn('クリア条件' + '１２３'[stage-1], world.flags)
            self.assertEqual(len(world.flags), 2)
            self.assertEqual(result['halted_before']['command'], 'SetGrid' if stage == 3 else 'Complete18')

    def test_original_openings_reset_turn_before_mapload_not_roster_or_phase(self):
        for stage in (2, 3, 4):
            world = StageWorld(self.scripts, turn=29)
            original = copy.deepcopy(world.units)
            result = world.opening_prefix(stage)
            self.assertEqual(world.turn, 1)
            self.assertEqual(world.units, original)
            self.assertEqual(result['halted_before']['command'], 'MapLoad')
            with self.assertRaises(ValueError): world.native('MapLoad', ['bmap18'])

    def test_all_three_literal_request_sites_and_native_codes_are_distinct(self):
        sites = [c for c in calls(self.scripts[SCRIPT]) if c['command'] == 'Complete18']
        self.assertEqual([(c['function'], c['args']) for c in sites], [(82, [1]), (85, [2]), (88, [3])])
        self.assertEqual([complete18_request(n) for n in (1, 2, 3)], [5, 6, 7])
        with self.assertRaises(ValueError): complete18_request(4)

    def test_wrong_turn_reset_mutation_is_caught(self):
        scripts = self.scripts.copy(); raw = bytearray(scripts[SCRIPT])
        call = next(c for c in calls(raw) if c['function'] == 83 and c['command'] == 'BMSetTurn')
        self.assertEqual(raw[call['offset']-2:call['offset']], b'\x19\x01')
        raw[call['offset']-1] = 2
        scripts[SCRIPT] = bytes(raw)
        world = StageWorld(scripts); world.opening_prefix(2)
        self.assertNotEqual(world.turn, 1)

    def test_red_cleanup_does_not_consume_owned_yellow_or_revive_dead(self):
        world = StageWorld(self.scripts)
        world.units['RED'] = {'force': 1, 'flags': 0}
        world.units['DEAD'] = {'force': 6, 'flags': 0x8008}
        world.units['AWAY'] = {'force': 7, 'flags': 0x10}
        original = copy.deepcopy(world.units)
        world.completion_prefix(1)
        self.assertEqual(world.units['RED']['force'], 4)
        for pid in ('PID_OSCAR', 'DEAD', 'AWAY'): self.assertEqual(world.units[pid], original[pid])
