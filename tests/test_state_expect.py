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
