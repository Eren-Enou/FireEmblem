import copy
import tempfile
import unittest
from pathlib import Path
from tools.save_architecture import audit_profile, compare_views, validate_native
from tools.fe9.disc import DiscReader
from tools.fe9.ppc import Dol
from tools.verify_game import DEFAULT_IMAGE
from tests.test_ch10_talk import sample


class SaveAuditTests(unittest.TestCase):
    def test_sync_does_not_imply_writeback_and_audit_preserves_profile(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'Dolphin.ini'
            raw=b'[NetPlay]\nSyncSaves=True\nSyncCodes=True\nWriteSaveData=False\n'
            path.write_bytes(raw)
            result=audit_profile(path)
            self.assertEqual(result['netplay_save_write_policy'],'DISABLED_BY_PROFILE')
            self.assertTrue(result['settings']['SyncSaves'])
            self.assertEqual(path.read_bytes(),raw)
            path.write_text('[NetPlay]\nWriteSaveData=True\n')
            self.assertEqual(audit_profile(path)['netplay_save_write_policy'],'REQUESTED_NOT_RUNTIME_VERIFIED')
            path.write_text('[NetPlay]\nWriteSaveData=perhaps\n')
            self.assertEqual(audit_profile(path)['netplay_save_write_policy'],'UNKNOWN')

    def test_selected_fields_compare_without_claiming_native_save(self):
        before,_=sample();after=copy.deepcopy(before)
        self.assertEqual(compare_views(before,after,'PID_OSCAR')['status'],'INCONCLUSIVE')
        self.assertEqual(compare_views(before,after,'PID_OSCAR')['selected_field_changes'],{})
        after['game']['units'][0]['flags'] ^= 0x60000000
        self.assertIn('flags',compare_views(before,after,'PID_OSCAR')['selected_field_changes'])
        del after['game']['units'][0]['level']
        with self.assertRaisesRegex(ValueError,'missing'): compare_views(before,after,'PID_OSCAR')

    @unittest.skipUnless(DEFAULT_IMAGE.exists(),'pinned image absent')
    def test_native_fields_are_pinned_and_wrong_width_is_rejected(self):
        with DiscReader(DEFAULT_IMAGE) as disc: dol=Dol(disc.read_dol())
        self.assertEqual(validate_native(dol)['raw_flags_width'],4)
        class Wrong:
            def u32(self,address): return 0x38800002 if address==0x8003CBC0 else dol.u32(address)
        with self.assertRaisesRegex(ValueError,'signature'): validate_native(Wrong())
