import json
import re
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.install_codes import ROOT, build_ini
from tools.fe9.events import calls, functions


class BuildSafetyTests(unittest.TestCase):
    def test_skipped_large_code_does_not_consume_space_for_later_small_code(self):
        from tools.install_codes import check_budget
        lost = check_budget(["COOP-P6", "EXP-21", "EXP-23", "DBG-01"])
        self.assertEqual([n.split()[0] for n in lost], ["EXP-23"])

    def test_library_rejects_overflow_and_unknown_selection(self):
        with self.assertRaisesRegex(ValueError, "Gecko space"):
            build_ini(["COOP-P6", "EXP-21", "EXP-23", "DBG-01"], verbose=False)
        with self.assertRaisesRegex(ValueError, "unknown code"):
            build_ini(["EXP-TYPO"], verbose=False)

    def test_library_rejects_shared_hooks(self):
        with self.assertRaisesRegex(ValueError, "hook conflict"):
            build_ini(["EXP-16", "EXP-21"], verbose=False)
        with self.assertRaisesRegex(ValueError, "hook conflict"):
            build_ini(["COOP-P6", "EXP-06"], verbose=False)

    def test_package_cannot_bypass_budget(self):
        from tools import netplay_package
        with patch.object(netplay_package, "PACKAGE_CODES", ["COOP-P6", "EXP-21", "EXP-23"]):
            with self.assertRaisesRegex(ValueError, "Gecko space"):
                netplay_package.contents()

    def test_force_setup_rejects_before_removing_existing_card(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            sentinel = root / "host/GC/USA/Card A/preserve.gci"
            sentinel.parent.mkdir(parents=True)
            sentinel.write_bytes(b"test card must survive rejected configuration")
            result = subprocess.run([sys.executable, "-B", "-m", "tools.netplay_setup", "--root", str(root),
                                     "--force", "--enable", "COOP-P6", "--enable", "EXP-21",
                                     "--enable", "EXP-23"], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Gecko space", result.stderr)
            self.assertEqual(sentinel.read_bytes(), b"test card must survive rejected configuration")

    def test_installer_rejects_before_destination_or_backup_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            ini = Path(tmp) / "GameSettings/GFEE01.ini"
            ini.parent.mkdir()
            ini.write_text("sentinel")
            result = subprocess.run([sys.executable, "-B", "-m", "tools.install_codes", "--user", tmp,
                                     "--enable", "COOP-P6", "--enable", "EXP-21", "--enable", "EXP-23"],
                                    cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(ini.read_text(), "sentinel")
            self.assertFalse(ini.with_suffix(".ini.bak").exists())


class EventDecoderTests(unittest.TestCase):
    def test_unknown_argument_is_prefix_not_suffix_and_pool_is_not_code(self):
        raw = bytearray(160)
        raw[:4] = b"cmb\0"
        struct.pack_into("<II", raw, 0x24, 0x2C, 0x50)
        raw[0x2C:0x31] = b"Test\0"
        # A fake call in the pool must not be counted.
        raw[0x35:0x39] = b"\x38\x00\x00\x02"
        struct.pack_into("<II", raw, 0x50, 0x60, 0)
        struct.pack_into("<5I", raw, 0x60, 0, 0x74, 0, 0, 0)
        raw[0x74:0x7D] = b"\x01\x00\x19\x03\x38\x00\x00\x02\x39"
        found = calls(bytes(raw))
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["args"], [None, 3])
        self.assertEqual(found[0]["offset"], 0x78)


IMAGE = ROOT / "Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso"


@unittest.skipUnless(IMAGE.exists(), "game image unavailable")
class CampaignDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tools.fe9.disc import DiscReader
        from tools.campaign_audit import inventory
        cls.disc = DiscReader(IMAGE)
        cls.data = inventory(cls.disc)

    @classmethod
    def tearDownClass(cls):
        cls.disc.close()

    def test_all_scripts_and_special_maps_are_inventoried(self):
        rows = self.data["chapters"]
        self.assertEqual(len(rows), 31)
        self.assertIn("Ch.27-2", rows[28]["title"])
        self.assertIn("Ch.28", rows[29]["title"])
        self.assertTrue(rows[30]["title"].startswith("Endgame"))
        self.assertEqual({m["path"] for m in rows[17]["maps"]},
                         {"zmap/bmap18/dispos.cmp", "zmap/bmap18_3/dispos.cmp"})
        self.assertIn("Scripts/ending.cmb", self.data["scripts"])
        self.assertIn("Scripts/C80.cmb", self.data["scripts"])

    def test_event_order_and_computed_transfer_argument(self):
        found = self.data["scripts"]["Scripts/C11.cmb"]["calls"]
        self.assertEqual([c["offset"] for c in found], sorted(c["offset"] for c in found))
        self.assertTrue(any(c["command"] == "UnitTransferToForce" and c["args"] == [None, 0] for c in found))
        self.assertTrue(any(c["command"] == "UnitTransferToForceByPID" and c["args"] == ["PID_KEVIN", 3] for c in found))

    def test_inventory_never_promotes_static_to_gameplay(self):
        for r in self.data["chapters"]:
            for k in ("runtime_current", "cleared_current", "transition_current", "netplay_current"):
                self.assertNotIn(k, r)  # runtime status belongs only to the validated evidence ledger

    def test_escape_routine_force_mask_is_blue_and_roster_only(self):
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        # Native routines explicitly construct [1,0,0,0,0,1,0,0]. No gameplay assertion.
        for base in (0x801B71BC, 0x801B728C):
            self.assertEqual([dol.u32(base + i * 4) for i in range(7)],
                             [0x38800000, 0x38A00000, 0x38C00000, 0x38E00000,
                              0x39000001, 0x39200000, 0x39400000])

    def test_every_script_has_valid_local_instruction_boundaries(self):
        from tools.fe9.events import instructions
        count = 0
        for path in self.data["scripts"]:
            raw = self.disc.read_file(path)
            for f in functions(raw):
                code = instructions(raw, f)
                bounds = {i["offset"] for i in code}
                for i in code:
                    if i["target"] is not None:
                        self.assertIn(i["target"], bounds)
                count += 1
        self.assertEqual(count, 2075)

    def test_jill_defection_has_relationship_guards(self):
        from tools.fe9.event_paths import trace
        result = trace(self.disc.read_file("Scripts/C21.cmb"), 26)
        self.assertTrue(result["complete_local_trace"])
        transfers = [e for e in result["events"] if e["command"] == "UnitTransferToForceByPID"]
        self.assertEqual(len(transfers), 1)
        self.assertEqual(transfers[0]["args"], ["'PID_JILL'", "1"])
        conditions=[re.sub(r"@0x[0-9A-F]+#[0-9]+","",c) for c in transfers[0]["conditions"]]
        self.assertEqual(conditions, [
            "(PersonGetYellLevel('PID_JILL', 'PID_MIST') == 3) == 0",
            "(PersonGetYellLevel('PID_JILL', 'PID_LETHE') == 3) == 0"])

    def test_reyson_transfer_is_guarded_by_empty_roster_setup(self):
        from tools.fe9.event_paths import trace
        result = trace(self.disc.read_file("Scripts/C23.cmb"), 25)
        transfers = [e for e in result["events"] if e["command"] == "UnitTransferToForceByPID"]
        self.assertTrue(transfers)
        for event in transfers:
            self.assertEqual(event["args"], ["'PID_RIEUSION'", "6"])
            conditions=[re.sub(r"@0x[0-9A-F]+#[0-9]+","",c) for c in event["conditions"]]
            self.assertIn("(ForceGetCount(5) == 0) != 0", conditions)
            self.assertIn("Normal() != 0", conditions)

    def test_ch6_original_escape_script_counts_carried_units_and_ike(self):
        from tools.fe9.event_vm import execute
        raw = self.disc.read_file("Scripts/C07.cmb")
        for actor, passenger, expected_count, complete in [(2,0,1,False),(2,3,2,False),
                                                          (1,0,1,True),(2,1,2,True)]:
            world = {"count":0,"complete":False,"escaped":[]}
            def native(name,args):
                if name=="MindGetMe": return actor
                if name=="UnitGetByPID": return 1
                if name=="UnitGet":
                    self.assertEqual(args,[actor,4]);return passenger
                if name=="BMGetValue": return world["count"]
                if name=="BMSetValue": world["count"]=args[1]
                if name=="UnitEscape": world["escaped"].append(args[0])
                if name=="set" and args==["gf_complete"]: world["complete"]=True
                return 0
            execute(raw,1,native)
            self.assertEqual(world,{"count":expected_count,"complete":complete,"escaped":[actor]})

    def test_original_escape_tile_metadata_and_no_literal_escape_counter_calls(self):
        from tools.native_usage import analyze
        data = analyze(self.disc)
        self.assertEqual(len(data["scripts"]), 43)
        self.assertEqual(len(data["registrations"]), 406)
        for name in ("PlayerEscapeCount", "PlayerEscapeCheck", "PlayerDeadCheck", "GetDiedPlayerCount"):
            self.assertEqual(data["sites"][name], [])
        self.assertEqual(len(data["sites"]["UnitEscape"]), 45)
        raw = self.disc.read_file("Scripts/C07.cmb")
        tile = functions(raw)[2].trigger(raw)["tile_event"]
        self.assertEqual(tile, {"x": 13, "y": 26, "action_code": 14,
                                "key_pool_offset": 191, "key": "", "action": "Escape"})
        raw = self.disc.read_file("Scripts/C11.cmb")
        escape_tiles = [f.trigger(raw)["tile_event"] for f in functions(raw)
                        if f.trigger(raw).get("tile_event", {}).get("action") == "Escape"]
        self.assertEqual([(e["x"], e["y"]) for e in escape_tiles], [(6,2),(7,2)])

    def test_conversation_pairs_direction_and_shared_jill_key(self):
        raw = self.disc.read_file("Scripts/C11.cmb")
        event = functions(raw)[29].trigger(raw)["conversation_event"]
        self.assertEqual((event["actor"],event["target"],event["reversible"]),
                         ("PID_OSCAR","PID_KEVIN",True))
        raw = self.disc.read_file("Scripts/C14.cmb")
        event = functions(raw)[37].trigger(raw)["conversation_event"]
        self.assertEqual((event["actor"],event["target"],event["reversible"]),
                         ("PID_STELLA","PID_GATRIE",False))
        raw = self.disc.read_file("Scripts/C21.cmb")
        first, second = [functions(raw)[i].trigger(raw)["conversation_event"] for i in (26,27)]
        self.assertEqual((first["actor"],first["target"]),("PID_JILL","PID_SIHARAMU"))
        self.assertEqual((second["actor"],second["target"]),(first["target"],first["actor"]))
        self.assertEqual(first["key"],second["key"])
        self.assertFalse(first["reversible"] or second["reversible"])

    def test_original_talk_menu_dispatch_reaches_identity_matcher(self):
        from tools.fe9.ppc import Dol
        from tools.talk_audit import analyze
        data=analyze(Dol(self.disc.read_dol()))
        self.assertEqual(data["table"], {"menu_availability":0x80078A24,
                                        "target_callback":0x8002CD70})
        self.assertIn((0x80078A64,0x8002B0A4),data["Talk availability"]["calls"])
        self.assertIn((0x8002CD90,0x800BF1E8),data["Conversation target callback"]["calls"])
        self.assertEqual(data["matcher_direct_callers"],
                         [0x8002CD90,0x800F88B4,0x800F8EE4,0x801032BC])

    def test_native_registration_recovery_and_rescue_selector(self):
        from tools.native_registry import registrations
        from tools.fe9.ppc import Dol
        dol=Dol(self.disc.read_dol())
        found=registrations(dol)
        self.assertEqual(len(found),406)
        symbols={r["name"]:r for r in found}
        self.assertEqual((symbols["UnitGet"]["function"],symbols["UnitGet"]["argc"]),(0x800BD704,2))
        self.assertEqual(dol.u32(0x8028D41C),0x800BD7C0)
        self.assertEqual(dol.u32(0x800BD7C0),0x807F0194)


class MovieBuilderTests(unittest.TestCase):
    def test_binary_records_and_overwrite_refusal(self):
        from tools.dtm_script import movie,build
        data=movie([{"polls":2,"buttons":["A"]}])
        self.assertEqual(data[:4],b"DTM\x1A")
        self.assertEqual(len(data),272)
        self.assertEqual(data[256:264],b"\x02\x40\0\0\x80\x80\x80\x80")
        with tempfile.TemporaryDirectory() as tmp:
            state=Path(tmp)/"fixture";state.write_bytes(b"original fixture")
            out=Path(tmp)/"test.dtm"
            template=bytearray(data[:256]);template[137]=1
            build(state,[{"polls":1}],out,bytes(template))
            self.assertEqual(Path(str(out)+".sav").read_bytes(),state.read_bytes())
            with self.assertRaisesRegex(ValueError,"refusing"):
                build(state,[{"polls":1}],out,bytes(template))


class SnapshotTests(unittest.TestCase):
    @unittest.skipUnless((ROOT / "work/saves/2026-10-27_baseline/GFEE01.s01").exists() and IMAGE.exists(),
                         "copied baseline fixture unavailable")
    def test_capture_decodes_real_baseline_without_asserting_active_ini(self):
        from tools.campaign_snapshot import capture
        with tempfile.TemporaryDirectory() as tmp:
            ini = Path(tmp) / "codes.ini"
            ini.write_text(build_ini(["COOP-P6", "EXP-16"], verbose=False))
            data = capture(ROOT / "work/saves/2026-10-27_baseline/GFEE01.s01", IMAGE, ini, "fixture")
        self.assertEqual((data["game"]["chapter"], data["game"]["phase"], data["game"]["turn"]), (1, 0, 1))
        ike = next(u for u in data["game"]["units"] if u["pid"] == "PID_IKE")
        self.assertEqual((ike["force"], ike["hp"], ike["owner"]), (0, 19, None))
        self.assertIn("intended configuration", data["evidence"]["warning"])
        self.assertFalse(data["evidence"]["intended_c2_verified"])

    def test_same_fields_with_different_files_match_but_config_mismatch_fails(self):
        from tools.campaign_snapshot import differences
        a = {"evidence": {"commit": "x", "dolphin": "2609a", "codes_fingerprint": "a", "state_sha256": "one"},
             "game": {"chapter": 7, "phase": 3, "turn": 2, "control": [1, 2, 2, 1], "units": []}}
        b = json.loads(json.dumps(a))
        b["evidence"]["state_sha256"] = "two"
        self.assertEqual(differences(a, b), [])
        b["evidence"]["codes_fingerprint"] = "b"
        self.assertIn("configuration mismatch", differences(a, b)[0])


if __name__ == "__main__":
    unittest.main()
