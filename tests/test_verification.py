import copy
import hashlib
import tempfile
import unittest
from pathlib import Path
from tools.campaign_verify import AXES,validate


def ledger():
    return {"chapters":[{"key":"7","checks":{a:{"status":"NOT TESTED"} for a in AXES}}],
            "runs":{"static":{"kind":"static","description":"parser", "chapters":["7"],"axes":["static_cfg"]}}}


class EvidenceTests(unittest.TestCase):
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


if __name__=="__main__":unittest.main()
