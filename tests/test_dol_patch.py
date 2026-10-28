import struct
import unittest
from tools.fe9.dol_patch import branch,hook_plan,apply_offline
from tools.fe9.disc import dol_sections


def synthetic():
    data=bytearray(0x120)
    struct.pack_into('>I',data,0,0x100)
    struct.pack_into('>I',data,0x48,0x80004000)
    struct.pack_into('>I',data,0x90,0x20)
    struct.pack_into('>II',data,0xD8,0x80005000,0x1000)
    struct.pack_into('>I',data,0x100,0x60000000)
    return bytes(data)


class DolPatchTests(unittest.TestCase):
    def test_offline_hook_and_branch_back(self):
        source=synthetic()
        plan=hook_plan(source,0x80004000,0x60000000,[0x60000000,0],0x80008000,32)
        patched=apply_offline(source,plan)
        self.assertEqual(struct.unpack_from('>I',patched,0x100)[0],branch(0x80004000,0x80008000))
        sections=dol_sections(patched)
        self.assertEqual(sections[1][2:],(0x80008000,8))
        self.assertEqual(struct.unpack_from('>II',patched,sections[1][1]),(0x60000000,branch(0x80008004,0x80004004)))
        self.assertEqual(source,synthetic())

    def test_rejects_bss_section_signature_and_relocation_hazards(self):
        for address,original,words in [(0x80004000,0x60000000,[0x60000000,0]),
                                       (0x80005000,0x60000000,[0x60000000,0]),
                                       (0x80008000,0,[0x60000000,0]),
                                       (0x80008000,0x60000000,[0x48001001,0])]:
            with self.assertRaises(ValueError):
                hook_plan(synthetic(),0x80004000,original,words,address,32)

    def test_branch_range_and_alignment(self):
        with self.assertRaises(ValueError):branch(0x80000000,0x82000000)
        with self.assertRaises(ValueError):branch(0x80000001,0x80001000)
        self.assertEqual(branch(0x80001000,0x80000000),0x4BFFF000)


if __name__=='__main__':unittest.main()
