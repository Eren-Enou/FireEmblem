import copy
import hashlib
import tempfile
import unittest
from tools.campaign_verify import evidence_level
from pathlib import Path
from tools.campaign_verify import AXES,validate


def ledger():
    return {"chapters":[{"key":"7","checks":{a:{"status":"NOT TESTED"} for a in AXES}}],
            "runs":{"static":{"kind":"static","description":"parser", "chapters":["7"],"axes":["static_cfg"]}}}


class EvidenceTests(unittest.TestCase):
    def test_partner_smoke_rejects_changed_roster_and_ownership(self):
        from tools.partner_smoke import verify
        lethe={"pid":"PID_LETHE","force":3,"class":"JID_CAT/F","gauge":20,"hp":34,
               "xy":[25,18],"flags":0x80000,"owned":False,"owner":None}
        mordy={**lethe,"pid":"PID_MORDY","class":"JID_BEAST_T","hp":41,"xy":[24,18]}
        before={"evidence":{"commit":"abc","dolphin":"2609a","codes_fingerprint":"stable",
                            "intended_c2_verified":True,"debug":False,"state_sha256":"before"},
                "game":{"chapter":10,"phase":3,"turn":1,"control":[1,2,2,1],"units":[lethe,mordy]}}
        after=copy.deepcopy(before);after["evidence"]["state_sha256"]="after"
        after["game"]["units"][0]["flags"]|=1
        self.assertEqual(verify(before,after)["status"],"PASS")
        after["game"]["units"][1]["hp"]-=1
        self.assertEqual(verify(before,after)["status"],"FAIL")
        after["game"]["units"][1]["hp"]+=1
        before["game"]["units"][0]["owned"]=True
        self.assertEqual(verify(before,after)["status"],"FAIL")

    def test_evidence_cannot_be_reused_for_wrong_chapter_or_axis(self):
        data=ledger()
        data["chapters"][0]["checks"]["static_cfg"]={"status":"PASS","evidence":"static"}
        data["runs"]["static"]["chapters"]=["1"]
        with self.assertRaisesRegex(ValueError,"scope"): validate(data)
        data["runs"]["static"]["chapters"]=["7"]
        data["runs"]["static"]["axes"]=["script_model"]
        with self.assertRaisesRegex(ValueError,"scope"): validate(data)

    def test_artifact_hash_and_missing_file_rejected(self):
        from tools.campaign_verify import check_artifacts
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);artifact=root/"capture";artifact.write_bytes(b"captured bytes")
            data=ledger();data["runs"]["runtime"]={"kind":"dolphin","commit":"abc",
                "fingerprint":"stable","dolphin":"2609a","fixture_class":"synthetic",
                "chapters":["7"],"axes":["fixture"],
                "artifacts":[{"path":"capture","sha256":hashlib.sha256(artifact.read_bytes()).hexdigest()}]}
            data["chapters"][0]["checks"]["fixture"]={"status":"PASS","evidence":"runtime"}
            self.assertEqual(check_artifacts(data,root),1)
            artifact.write_bytes(b"different bytes")
            with self.assertRaisesRegex(ValueError,"hash mismatch"):check_artifacts(data,root)
            artifact.unlink()
            with self.assertRaisesRegex(ValueError,"missing"):check_artifacts(data,root)

    def test_smoke_rejects_same_state_wrong_phase_and_missing_live_hooks(self):
        from tools.prologue_smoke import verify
        before = {"evidence": {"commit":"abc", "dolphin":"2609a", "codes_fingerprint":"stable",
                               "state_sha256":"before", "intended_c2_verified":True, "debug":False},
                  "game":{"chapter":1,"turn":1,"phase":0,"units":[
                      {"pid":"PID_IKE","force":0,"hp":19,"level":1,"exp":0,"xy":[3,9]}]}}
        after = copy.deepcopy(before)
        self.assertEqual(verify(before, after)["status"], "FAIL")
        after["game"]["phase"] = 1; after["evidence"]["state_sha256"] = "after"
        self.assertEqual(verify(before, after)["status"], "PASS")
        after["evidence"]["intended_c2_verified"] = False
        self.assertEqual(verify(before, after)["status"], "FAIL")

    def test_static_pass_cannot_promote_runtime(self):
        data=ledger();data["chapters"][0]["checks"]["static_cfg"]={"status":"PASS","evidence":"static"}
        validate(data)
        data["chapters"][0]["checks"]["event_runtime"]={"status":"PASS","evidence":"static"}
        with self.assertRaisesRegex(ValueError,"static evidence"):validate(data)

    def test_file_creation_alone_does_not_establish_runnable_fixture(self):
        data=ledger();data["chapters"][0]["checks"]["fixture"]={"status":"PASS","evidence":"static"}
        with self.assertRaisesRegex(ValueError,"static evidence"):validate(data)

    def test_local_netplay_cannot_certify_two_computers(self):
        data=ledger();data["runs"]["local"]={"kind":"netplay_local"}
        data["chapters"][0]["checks"]["netplay_two_pc"]={"status":"PASS","evidence":"local"}
        with self.assertRaisesRegex(ValueError,"topology"):validate(data)

    def test_missing_provenance_and_synthetic_completion_are_rejected(self):
        data=ledger();data["runs"]["run"]={"kind":"dolphin"}
        data["chapters"][0]["checks"]["chapter_clear"]={"status":"PASS","evidence":"run"}
        with self.assertRaisesRegex(ValueError,"provenance"):validate(data)
        data["runs"]["run"].update(commit="abc",fingerprint="123",dolphin="2609a",fixture_class="synthetic",artifacts=["sha256"])
        with self.assertRaisesRegex(ValueError,"synthetic"):validate(data)


class EvidenceClassificationTests(unittest.TestCase):
    def test_lifecycle_model_stays_model_and_blocked_requires_reason(self):
        from tools.campaign_verify import coverage
        data = ledger(); data['chapters'][0]['title'] = 'Test'
        data['runs']['model'] = {'kind':'script_model', 'chapters':['7']}
        data['chapters'][0]['lifecycle'] = {
            'escape': {'status':'PASS','evidence':'model','scope':'native projection only'},
            'permanent_recruitment': {'status':'BLOCKED','scope':'MapFree/save not executed'}}
        result = coverage(data)[0]['lifecycle']
        self.assertEqual(result['escape']['level'], 'MODEL VERIFIED')
        self.assertEqual(result['permanent_recruitment']['level'], 'BLOCKED')
        self.assertEqual(result['netplay']['level'], 'UNTESTED')
        for name in ('next_chapter_initialization','native_save','native_reload'):
            self.assertEqual(result[name]['level'], 'UNTESTED')
        del data['chapters'][0]['lifecycle']['permanent_recruitment']['scope']
        with self.assertRaisesRegex(ValueError, 'scope/reason'): validate(data)

    def test_lifecycle_rejects_unaccepted_runtime_or_wrong_behavior(self):
        data = ledger()
        data['runs']['unaccepted'] = {'kind':'dolphin','chapters':['7']}
        data['chapters'][0]['lifecycle'] = {'escape': {'status':'PASS','evidence':'unaccepted','scope':'claimed'}}
        with self.assertRaisesRegex(ValueError, 'reuse accepted'): validate(data)
        data['chapters'][0]['lifecycle'] = {'invented': {'status':'NOT TESTED'}}
        with self.assertRaisesRegex(ValueError, 'unknown lifecycle'): validate(data)

    def test_independent_rescue_evidence_requires_scope_provenance_and_artifact_bytes(self):
        from tools.campaign_verify import check_artifacts,accepted_runtime_runs
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);artifact=root/'runtime.json';artifact.write_bytes(b'unit-test evidence')
            data=ledger()
            data['runs']['rescue']=dict(kind='dolphin',chapters=['7'],axes=[],lifecycle=['rescue'],
                commit='test',fingerprint='test',dolphin='test',fixture_class='synthetic',
                artifacts=[dict(path='runtime.json',sha256=hashlib.sha256(artifact.read_bytes()).hexdigest())])
            data['chapters'][0]['lifecycle']={'rescue':dict(status='PASS',evidence='rescue',scope='one original Rescue only')}
            validate(data)
            self.assertEqual(accepted_runtime_runs(data),{'rescue'})
            self.assertEqual(check_artifacts(data,root),1)
            self.assertTrue(all(c['status']=='NOT TESTED' for c in data['chapters'][0]['checks'].values()))
            for mutation in ('scope','provenance','failed'):
                bad=copy.deepcopy(data)
                if mutation=='scope':bad['runs']['rescue']['lifecycle']=['escape']
                elif mutation=='provenance':del bad['runs']['rescue']['fingerprint']
                else:bad['runs']['rescue']['status']='FAIL'
                with self.subTest(mutation=mutation),self.assertRaises(ValueError):validate(bad)
            artifact.write_bytes(b'corrupt')
            with self.assertRaisesRegex(ValueError,'hash mismatch'):check_artifacts(data,root)

    def test_scope_labels_do_not_promote_models_or_incomplete_history_to_natural(self):
        passed = {'status': 'PASS'}
        self.assertEqual(evidence_level('static_cfg', passed), 'STATICALLY VERIFIED')
        self.assertEqual(evidence_level('script_model', passed), 'MODEL VERIFIED')
        self.assertEqual(evidence_level('event_runtime', passed, {'fixture_class': 'copied_history_unknown'}),
                         'SYNTHETIC RUNTIME VERIFIED')
        self.assertEqual(evidence_level('event_runtime', passed, {'fixture_class': 'naturally_progressed'}),
                         'NATURAL GAMEPLAY VERIFIED')
        self.assertEqual(evidence_level('netplay_two_pc', passed), 'MULTIPLAYER VERIFIED')
        self.assertEqual(evidence_level('event_runtime', {'status': 'FAIL'}), 'FAILED')

    def test_machine_readable_coverage_retains_axis_evidence_and_limitation(self):
        from tools.campaign_verify import coverage
        data = ledger()
        data['chapters'][0]['title'] = 'Test chapter'
        data['chapters'][0]['checks']['static_cfg'] = {'status': 'PASS', 'evidence': 'static', 'note': 'parser only'}
        row = coverage(data)[0]['axes']
        self.assertEqual(row['static_cfg']['level'], 'STATICALLY VERIFIED')
        self.assertEqual(row['static_cfg']['evidence'], 'static')
        self.assertEqual(row['static_cfg']['limitation'], 'parser only')
        self.assertEqual(row['chapter_clear']['level'], 'UNTESTED')


if __name__=="__main__":unittest.main()
