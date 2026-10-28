import copy
import unittest
from tools.state_expect import verify


class FixtureExpectationTests(unittest.TestCase):
    def setUp(self):
        self.snapshot={"evidence":{"intended_c2_verified":True,"debug":False,"codes_fingerprint":"stable"},
                       "game":{"chapter":7,"phase":0,"turn":1,"control":[1,2,2,1],"units":[
                           {"pid":"PID_IKE","force":0,"hp":26,"flags":0x10400},
                           {"pid":"PID_OSCAR","force":3,"hp":28,"flags":0x10400}]}}
        self.expected={"chapter":7,"phase":0,"active_player_pids":["PID_IKE","PID_OSCAR"],
                       "absent_pids":["PID_BOLE"],"units":[{"pid":"PID_OSCAR","force":3,"flags_all":0x400}]}

    def test_lost_duplicate_or_transferred_character_fails(self):
        self.assertEqual(verify(self.snapshot,self.expected)["status"],"PASS")
        for mutation in ("lost","duplicate","transfer"):
            snapshot=copy.deepcopy(self.snapshot)
            if mutation=="lost":snapshot["game"]["units"].pop()
            elif mutation=="duplicate":snapshot["game"]["units"].append(snapshot["game"]["units"][-1].copy())
            else:snapshot["game"]["units"][-1]["force"]=6
            with self.subTest(mutation=mutation):
                self.assertEqual(verify(snapshot,self.expected)["status"],"FAIL")

    def test_unknown_fields_and_unverified_hooks_cannot_pass(self):
        with self.assertRaisesRegex(ValueError,"unknown"):
            verify(self.snapshot,{**self.expected,"chpater":7})
        self.snapshot["evidence"]["intended_c2_verified"]=False
        self.assertEqual(verify(self.snapshot,self.expected)["status"],"FAIL")

    def test_synthetic_code_requires_explicit_acceptance_and_chapter_byte_is_insufficient(self):
        self.snapshot["evidence"]["synthetic_setup"]=True
        self.assertEqual(verify(self.snapshot,self.expected)["status"],"FAIL")
        self.assertEqual(verify(self.snapshot,{**self.expected,"allow_synthetic":True})["status"],"PASS")
        import json
        from pathlib import Path
        expectation=json.loads((Path(__file__).resolve().parents[1]/"campaign/fixtures/ch10_prisoner_presence.json").read_text())
        self.snapshot["game"]["chapter"]=11
        result=verify(self.snapshot,expectation)
        self.assertEqual(result["status"],"FAIL")
        self.assertTrue(any("PID_KEVIN" in failure for failure in result["failures"]))
        self.snapshot["game"]["event_scripts"]={"complete_chain":True,"names":["C07.cmb"],"chapter_matches":False}
        result=verify(self.snapshot,{"chapter":11,"allow_synthetic":True,"units":[{"pid":"PID_IKE"}]})
        self.assertEqual(result["failures"],["loaded event script disagrees with chapter byte"])

    def test_known_setup_classification_is_not_just_debug_prefix(self):
        from tools.campaign_snapshot import configuration_flags
        for name in ("FIXTURE-REDIRECT chapter seed", "EXP-05 Redirect", "DBG-CAMP-POS setup"):
            self.assertTrue(configuration_flags([name])["synthetic_setup"])
        self.assertFalse(configuration_flags(["COOP-P6", "EXP-16"])["synthetic_setup"])
