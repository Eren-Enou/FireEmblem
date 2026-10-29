import copy
import unittest
from pathlib import Path

from tools.event_state import FLAG_TABLE, inspect, named_flags
from tools.campaign_snapshot import differences


class Memory:
    def __init__(self):
        self.names = {0x80001000: b'known_clear\0', 0x80001100: b'known_set\0'}
        self.pointers = {FLAG_TABLE: 0x80001000, FLAG_TABLE+4: 0x80001100}
        self.bits = 2

    def u32(self, address): return self.pointers.get(address, 0)
    def u8(self, address): return self.bits if address == FLAG_TABLE+0x300 else 0
    def read(self, address, size): return self.names[address].ljust(size, b'\0')[:size]


class EventStateTests(unittest.TestCase):
    def test_named_set_clear_and_absent_are_distinct(self):
        result = inspect(Memory())
        self.assertTrue(result['complete_table_read'])
        self.assertEqual(result['values'], {'known_clear': False, 'known_set': True})
        self.assertNotIn('unknown_flag', result['values'])

    def test_bad_name_pointer_duplicate_or_string_yields_unknown_not_clear(self):
        for kind in ('pointer', 'duplicate', 'unterminated', 'encoding'):
            mem = Memory()
            if kind == 'pointer': mem.pointers[FLAG_TABLE] = 0x81800000
            elif kind == 'duplicate': mem.names[0x80001100] = b'known_clear\0'
            elif kind == 'unterminated': mem.names[0x80001000] = b'x'*256
            elif kind == 'encoding': mem.names[0x80001000] = b'\x81\0'
            with self.subTest(kind=kind):
                result = inspect(mem)
                self.assertFalse(result['complete_table_read'])
                self.assertIsNone(result['values'])

    def test_comparison_detects_new_flags_and_missing_old_schema_fields(self):
        from tests.test_ch10_talk import sample
        a, b = sample()
        b = copy.deepcopy(a)
        a['game']['event_flags'] = {'complete_table_read': True, 'values': {'known': False}}
        b['game']['event_flags'] = {'complete_table_read': True, 'values': {'known': True}}
        self.assertTrue(any(line.startswith('event_flags:') for line in differences(a, b)))
        del b['game']['event_flags']
        self.assertIn('event_flags: missing from one snapshot', differences(a, b))
        a, _ = sample()
        b = copy.deepcopy(a)
        b['game']['future_unknown_field'] = {'status': 'UNKNOWN'}
        self.assertIn('future_unknown_field: missing from one snapshot', differences(a, b))

    @unittest.skipUnless(Path('work/fixtures/ch10_oscar_kieran_v1/after.s02.sav').exists(), 'private captures absent')
    def test_generic_flag_decoder_preserves_accepted_talk_evidence(self):
        from tools.campaign_snapshot import capture
        from tools.verify_game import DEFAULT_IMAGE
        from tools.talk_evidence import CONVERSATION_KEY
        root = Path('work/fixtures/ch10_oscar_kieran_v1')
        snapshots = [capture(root/name, DEFAULT_IMAGE, root/'User/GameSettings/GFEE01.ini', 'offline')
                     for name in ('before.s02.sav', 'after.s02.sav')]
        for snapshot, expected in zip(snapshots, (False, True)):
            game = snapshot['game']
            self.assertEqual(game['event_flags']['values'], game['talk_fixture']['flags'])
            self.assertEqual(game['event_flags']['values'][CONVERSATION_KEY], expected)
            self.assertEqual(game['battle_stage']['status'], 'UNKNOWN')
            for unit in game['units']:
                self.assertEqual(unit['escaped'], bool(unit['flags'] & 0x4000))
