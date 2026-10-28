import copy
import unittest
from tools.campaign_verify import AXES,validate


def ledger():
    return {"chapters":[{"key":"7","checks":{a:{"status":"NOT TESTED"} for a in AXES}}],
            "runs":{"static":{"kind":"static","description":"parser"}}}


class EvidenceTests(unittest.TestCase):
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
