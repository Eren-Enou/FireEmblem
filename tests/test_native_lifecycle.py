import unittest
from tools.native_lifecycle import force_flags, execute_flag_fragment, FLAG_START
from tools.fe9.ppc import Dol
from tools.fe9.disc import DiscReader
from tools.verify_game import DEFAULT_IMAGE


@unittest.skipUnless(DEFAULT_IMAGE.exists(), 'pinned image absent')
class NativeFlagTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with DiscReader(DEFAULT_IMAGE) as disc: cls.dol = Dol(disc.read_dol())

    def test_original_instruction_fragment_matches_projection_for_all_forces_and_bits(self):
        values = [0, 0x18, 0xFFFFFFFF, 0x60000400] + [1 << bit for bit in range(32)]
        for force in range(8):
            for flags in values:
                self.assertEqual(execute_flag_fragment(self.dol, force, flags), force_flags(flags, force))
                self.assertEqual(force_flags(flags, force) & 0x60000000, flags & 0x60000000)

    def test_wrong_roster_bit_mutation_is_detected_by_independent_expected_effect(self):
        original = self.dol
        class Mutated:
            def u32(self, address):
                return 0x60000000 if address == 0x8001577C else original.u32(address)
        with self.assertRaisesRegex(ValueError, 'identity'): execute_flag_fragment(Mutated(), 5, 0)
        # Deliberately bypass identity only inside the mutation test, never production.
        self.assertNotEqual(execute_flag_fragment(Mutated(), 5, 0, verify_identity=False), force_flags(0, 5))

    def test_invalid_force_and_unknown_instruction_are_rejected(self):
        with self.assertRaises(ValueError): force_flags(0, 8)
        class Unknown:
            def u32(self, address): return 0
        with self.assertRaisesRegex(ValueError, 'unsupported'):
            execute_flag_fragment(Unknown(), 0, 0, verify_identity=False)
