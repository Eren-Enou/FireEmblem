import struct
import unittest
from tools.fe9.ppc import Dol, direct_branch_target
from tests.test_dol_patch import synthetic


class BranchReferencesTests(unittest.TestCase):
    def test_relative_absolute_signed_and_linked_branches(self):
        self.assertEqual(direct_branch_target(0x80001000, 0x4BFFF001), 0x80000000)
        self.assertEqual(direct_branch_target(0x80001000, 0x48001003), 0x1000)
        self.assertEqual(direct_branch_target(0x80001000, 0x4BFFFFFE), 0xFFFFFFFC)
        self.assertEqual(direct_branch_target(0xFFFFFFFC, 0x48000008), 4)
        self.assertIsNone(direct_branch_target(0x80001000, 0x4E800421))
        raw=bytearray(synthetic())
        struct.pack_into(">4I", raw, 0x100, 0x48000011, 0x4800000C, 0x48004013, 0x4E800421)
        self.assertEqual(Dol(bytes(raw)).direct_callers(0x80004010), [0x80004000])
        self.assertEqual(Dol(bytes(raw)).direct_callers(0x4010), [0x80004008])
