"""A body match alone must never certify a C2 hook that cannot return safely."""
import unittest
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
from tools.campaign_snapshot import observe_hooks
from tools.fixture_relayout import branch
from tools.install_codes import ROOT,build_ini
from tools.netplay_package import fingerprint

TEXT='''[Gecko]
$TEST Integrity regression
C2010000 00000002
60000000 60000000
9421FFF0 00000000
[Gecko_Enabled]
$TEST Integrity regression
'''
HOOK=0x80010000
CAVE=0x80002800
ORIGINAL=0x9421FFF0


class Memory:
    def __init__(self):self.data={}
    def put(self,address,data):self.data.update((address+i,b) for i,b in enumerate(data))
    def read(self,address,size):return bytes(self.data.get(address+i,0) for i in range(size))
    def u32(self,address):return int.from_bytes(self.read(address,4),'big')


class Dol:
    def u32(self,address):
        if address!=HOOK:raise AssertionError('unexpected hook')
        return ORIGINAL


def fixture(cave=CAVE):
    mem=Memory();mem.put(HOOK,branch(HOOK,cave))
    mem.put(cave,bytes.fromhex('60000000600000009421FFF0')+branch(cave+12,HOOK+4))
    return mem


class HookIntegrityTests(unittest.TestCase):
    def test_relative_entry_and_dynamic_return_are_both_verified(self):
        row=observe_hooks(fixture(),Dol(),TEXT)[0]
        self.assertEqual(row['status'],'intended C2 body matched')
        self.assertTrue(row['return_verified'])
        self.assertEqual(row['return_target'],HOOK+4)

    def test_matching_body_with_bad_return_never_passes(self):
        for kind in ('zero','wrong_target','absolute','link','not_branch'):
            mem=fixture()
            value=int.from_bytes(branch(CAVE+12,HOOK+4),'big')
            if kind=='zero':value=0
            elif kind=='wrong_target':value=int.from_bytes(branch(CAVE+12,HOOK+8),'big')
            elif kind=='absolute':value|=2
            elif kind=='link':value|=1
            else:value=0x4E800020  # blr cannot replace the known continuation.
            mem.put(CAVE+12,value.to_bytes(4,'big'))
            with self.subTest(kind=kind):
                row=observe_hooks(mem,Dol(),TEXT)[0]
                self.assertNotEqual(row['status'],'intended C2 body matched')
                self.assertFalse(row['return_verified'])

    def test_entry_link_absolute_body_corruption_and_overflow_are_rejected(self):
        for kind in ('link','absolute','body','overflow','original'):
            mem=fixture(CAVE if kind!='overflow' else 0x80002FF8)
            if kind in ('link','absolute'):mem.put(HOOK,(mem.u32(HOOK)|(1 if kind=='link' else 2)).to_bytes(4,'big'))
            elif kind=='body':mem.put(CAVE,b'\x00')
            elif kind=='original':mem.put(HOOK,ORIGINAL.to_bytes(4,'big'))
            with self.subTest(kind=kind):self.assertNotEqual(observe_hooks(mem,Dol(),TEXT)[0]['status'],'intended C2 body matched')

    def test_malformed_zero_or_truncated_payload_is_not_accepted(self):
        for text in (TEXT.replace('00000002','00000000'),TEXT.replace('9421FFF0 00000000',''),TEXT.replace('9421FFF0 00000000','9421FFF0 60000000')):
            self.assertNotEqual(observe_hooks(fixture(),Dol(),text)[0]['status'],'intended C2 body matched')

    @unittest.skipUnless((ROOT/'work/scenarios/human_v1/CH10-PRISONER-ESCAPE-v2/captures/after/state.sav').is_file(),'accepted private source unavailable')
    def test_raw_state_reaudit_detects_corrupt_return_without_changing_source(self):
        from tools.next_scenarios import source
        from tools.campaign_snapshot import verify_live_hooks
        from tools.campaign_test_pack import sha
        from tools.fe9.savestate import read_state,write_state
        from tools.inspect_state import load_mem1
        from tools.patch_state import apply_edits
        _,state,ini,_=source('CH10-CHAPTER-COMPLETE')
        digest=sha(state);text=ini.read_text()
        original=verify_live_hooks(state,text)
        self.assertEqual(original['status'],'PASS')
        address=original['hooks'][0]['return_address']
        _,mem=load_mem1(state,Path('Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso'))
        _,payload=read_state(state)
        changed,_=apply_edits(payload,mem.offset,[f'{address:X}=00000000'])
        with tempfile.TemporaryDirectory(dir=ROOT/'work') as directory:
            target=Path(directory)/'deliberately_invalid_do_not_launch.sav'
            self.assertIn((ROOT/'work').resolve(),target.resolve().parents)
            write_state(state,target,changed)
            bad=verify_live_hooks(target,text)
            self.assertEqual(bad['status'],'FAIL')
            self.assertTrue(any('invalid return branch' in error for error in bad['failures']))
        self.assertEqual(sha(state),digest)


class CampaignIntegrityTests(unittest.TestCase):
    def test_rejected_candidate_does_not_hide_independent_integrity_or_runtime_results(self):
        from tools.campaign_integrity import candidates
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            config=root/'safe/User/GameSettings/GFEE01.ini'
            config.parent.mkdir(parents=True);config.write_text(TEXT)
            with patch('tools.test_scenario.NEXT',('rejected','safe')), \
                 patch('tools.test_scenario.scenario_dir',side_effect=lambda name,root:root/name), \
                 patch('tools.test_scenario.review',side_effect=[dict(status='FAIL'),dict(status='PASS')]), \
                 patch('tools.test_scenario.check',side_effect=[ValueError('runtime fixture interference'),dict(gecko_bytes=2536)]), \
                 patch('tools.campaign_integrity.verify_live_hooks',return_value=dict(status='PASS')):
                rows=candidates(root)
            self.assertEqual(len(rows),2)
            self.assertEqual(rows[0]['status'],'INCONCLUSIVE')
            self.assertTrue(rows[0]['launch_refused'])
            self.assertEqual(rows[0]['runtime'],'FAIL')
            self.assertEqual((rows[1]['status'],rows[1]['runtime']),('PASS','PASS'))

    def test_review_cannot_reuse_cached_true_when_raw_hook_check_fails(self):
        from tools.campaign_test_pack import review,sha
        with tempfile.TemporaryDirectory() as directory:
            case=Path(directory)
            (case/'case.json').write_text(json.dumps(dict(id='CH10-PARTNER-WAIT',captures=['before','after'],observations=[])))
            (case/'observations.json').write_text(json.dumps(dict(observed={})))
            for label in ('before','after'):
                dest=case/'captures'/label;dest.mkdir(parents=True)
                (dest/'state.sav').write_bytes(b'mocked raw decoding')
                (dest/'GFEE01.ini').write_text(TEXT)
                snapshot=dict(evidence=dict(state_sha256=sha(dest/'state.sav'),intended_c2_verified=True))
                (dest/'snapshot.json').write_text(json.dumps(snapshot))
                (dest/'manifest.json').write_text(json.dumps(dict(state_sha256=sha(dest/'state.sav'),
                    ini_sha256=sha(dest/'GFEE01.ini'),snapshot_sha256=sha(dest/'snapshot.json'))))
            with patch('tools.campaign_snapshot.verify_live_hooks',return_value=dict(status='FAIL',failures=['invalid return branch'])),patch('tools.campaign_test_pack.verify_partner_wait',return_value=dict(status='PASS')) as gameplay_verdict:
                verdict=review(case)
                self.assertEqual(verdict['status'],'FAIL')
                self.assertTrue(any('invalid return branch' in e for e in verdict['failures']))
                gameplay_verdict.assert_not_called()

    def test_configuration_requires_exact_declared_fingerprint(self):
        from tools.campaign_integrity import configurations
        stable=build_ini(['COOP-P6','EXP-16'],verbose=False)
        with tempfile.TemporaryDirectory() as directory:
            state=Path(directory)/'state.sav'
            text,label=configurations(state,fingerprint(stable))
            self.assertEqual(text,stable)
            self.assertTrue(label.startswith('generated unchanged stable'))
            self.assertEqual(configurations(state,'missing-configuration'),(None,None))
            ini=state.parent/'GFEE01.ini';ini.write_text(TEXT)
            self.assertEqual(configurations(state,fingerprint(TEXT)),(TEXT,str(ini)))

    def ledger(self,path):
        from tools.campaign_verify import AXES
        from tools.campaign_test_pack import sha
        checks={axis:dict(status='NOT TESTED') for axis in AXES}
        checks['fixture']=dict(status='PASS',evidence='test-run')
        return dict(chapters=[dict(key='11',checks=checks)],runs={'test-run':dict(kind='dolphin',commit='unit-test',
                    fingerprint='unavailable-config',dolphin='unit-test',fixture_class='synthetic',chapters=['11'],axes=['fixture'],
                    artifacts=[dict(path=str(path),sha256=sha(path))])})

    def test_missing_config_is_inconclusive_and_artifact_damage_is_refused(self):
        from tools.campaign_integrity import accepted
        with tempfile.TemporaryDirectory() as directory:
            state=Path(directory)/'state.sav';state.write_bytes(b'unit-test sentinel, never an emulator state')
            ledger=self.ledger(state)
            with patch('tools.campaign_integrity.verify_live_hooks') as raw_check:
                report=accepted(ledger)
                raw_check.assert_not_called()
            self.assertEqual(report['status'],'INCONCLUSIVE')
            self.assertEqual(len(report['raw_states']),1)
            state.write_bytes(b'changed')
            with self.assertRaisesRegex(ValueError,'hash mismatch'):accepted(ledger)
