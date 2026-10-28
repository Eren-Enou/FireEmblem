import unittest
from pathlib import Path
from tools.loaded_scripts import inspect


class Memory:
    def __init__(self):
        self.data=bytearray(0x400)
        self.data[:4]=(0x80000100).to_bytes(4,'big')
        for offset,name,nxt in ((0x100,b'startup.cmb',0x80000200),(0x200,b'C07.cmb',0)):
            self.data[offset:offset+4]=b'cmb\0'
            self.data[offset+4:offset+4+len(name)]=name
            self.data[offset+0x1C:offset+0x20]=nxt.to_bytes(4,'big')
    def read(self,address,size):return bytes(self.data[address-0x80000000:address-0x80000000+size])
    def u32(self,address):return int.from_bytes(self.read(address,4),'big')


class LoadedScriptTests(unittest.TestCase):
    @unittest.skipUnless(all(Path(path).exists() for path in (
        'work/ch6_native_start.s02.sav','work/ch9_yellow_before.s02.sav',
        'work/bootstrap/ch10_from_ch6/diagnostic.s02.sav')), 'private captured states unavailable')
    def test_captured_states_identify_real_container_and_reject_redirect(self):
        from tools.inspect_state import load_mem1
        from tools.verify_game import DEFAULT_IMAGE
        for path,chapter,script,match in (
            ('work/ch6_native_start.s02.sav',7,'C07.cmb',True),
            ('work/ch9_yellow_before.s02.sav',10,'C10.cmb',True),
            ('work/bootstrap/ch10_from_ch6/diagnostic.s02.sav',11,'C07.cmb',False)):
            with self.subTest(path=path):
                _,memory=load_mem1(Path(path),DEFAULT_IMAGE)
                result=inspect(memory,chapter)
                self.assertTrue(result['complete_chain'])
                self.assertEqual(result['names'],['startup.cmb',script])
                self.assertEqual(result['chapter_matches'],match)

    def test_independent_container_identity_detects_wrong_chapter(self):
        memory=Memory()
        accepted=inspect(memory,7,root_slot=0x80000000)
        self.assertEqual(accepted['names'],['startup.cmb','C07.cmb'])
        self.assertTrue(accepted['chapter_matches'])
        self.assertFalse(inspect(memory,11,root_slot=0x80000000)['chapter_matches'])

    def test_cycle_bad_pointer_header_and_bound_are_inconclusive(self):
        for mutation in ('cycle','outside','magic','bound','empty'):
            memory=Memory();limit=16
            if mutation=='cycle':memory.data[0x21C:0x220]=(0x80000100).to_bytes(4,'big')
            if mutation=='outside':memory.data[:4]=(0x70000000).to_bytes(4,'big')
            if mutation=='magic':memory.data[0x200:0x204]=b'nope'
            if mutation=='bound':limit=1
            if mutation=='empty':memory.data[:4]=bytes(4)
            with self.subTest(mutation=mutation):
                result=inspect(memory,7,root_slot=0x80000000,limit=limit)
                self.assertFalse(result['complete_chain'])
                self.assertIsNone(result['chapter_matches'])
