import struct
import unittest
import json
import copy
from pathlib import Path

import capstone
from tools.fixture_position_code import words,ini,HOOK,ORIGINAL
from tools.install_codes import validate_ini


class PrivateFixtureCodeTests(unittest.TestCase):
    def test_escape_evidence_rejects_loss_faction_or_inventory_damage(self):
        from tools.escape_smoke import verify
        unit={"pid":"PID_OSCAR","slot":2,"force":3,"class":"JID_SOCIALKNIGHT_L",
              "hp":28,"level":6,"exp":28,"xy":[13,26],"flags":0x10400,
              "death_record":False,"inventory_slots_hex":"a1"*64}
        before={"evidence":{"commit":"abc","dolphin":"2609a","codes_fingerprint":"fixture",
                 "state_sha256":"before","intended_c2_verified":True,"codes":["COOP-P6","EXP-16","DBG-CAMP-POS"]},
                "game":{"chapter":7,"phase":3,"turn":1,"units":[unit,
                    {"pid":"PID_IKE","force":0},{"pid":"PID_EMAKOU","force":1,"hp":32}]}}
        after=copy.deepcopy(before);after["evidence"]["state_sha256"]="after"
        after["game"].update(phase=0,turn=2)
        after["game"]["units"][0].update(force=5,flags=0x14411,xy=[13,29])
        self.assertEqual(verify(before,after)["status"],"PASS")
        for mutation in ("lost","faction","inventory","missing_hash"):
            bad=copy.deepcopy(after)
            if mutation=="lost":bad["game"]["units"].pop(0)
            elif mutation=="faction":bad["game"]["units"][0]["force"]=3
            elif mutation=="inventory":bad["game"]["units"][0]["inventory_slots_hex"]="00"*64
            else:bad["evidence"].pop("state_sha256")
            with self.subTest(mutation=mutation):
                self.assertEqual(verify(before,bad)["status"],"FAIL")

    def test_append_prefix_checks_body_and_correct_runtime_return(self):
        from tools.fixture_state import validate_prefix
        text="[Gecko]\n$test\nC2001000 00000001\n60000000 00000000\n[Gecko_Enabled]\n$test\n"
        base=0x80002500
        branch=0x48000000|((0x80001004-(base+12))&0x3FFFFFC)
        actual=struct.pack(">4I",0xC2001000,1,0x60000000,branch)
        validate_prefix(actual,base,text)
        with self.assertRaisesRegex(ValueError,"branch-back"):
            validate_prefix(actual[:-4]+bytes(4),base,text)
        with self.assertRaisesRegex(ValueError,"differs"):
            validate_prefix(actual[:8]+bytes(4)+actual[12:],base,text)

    @unittest.skipUnless(Path("work/fixtures/ch6_escape_native_v2/seed.s02.sav.json").exists(),"private seed absent")
    def test_captured_seed_changes_only_documented_gecko_storage(self):
        from tools.fe9.savestate import read_state,MEM1_BASE
        from tools.inspect_state import load_mem1
        from tools.verify_game import DEFAULT_IMAGE
        seed=Path("work/fixtures/ch6_escape_native_v2/seed.s02.sav")
        record=json.loads(Path(str(seed)+".json").read_text())
        source=Path(record["source"])
        _,a=read_state(source);_,b=read_state(seed)
        _,m=load_mem1(source,DEFAULT_IMAGE)
        start=m.offset+int(record["edit_address"],16)-MEM1_BASE
        end=start+record["edit_bytes"]
        self.assertEqual(a[:start],b[:start]);self.assertEqual(a[end:],b[end:])
        self.assertEqual(len(a),len(b))
        self.assertNotEqual(a[start:end],b[start:end])

    def test_complete_fixture_fits_and_preserves_native_hook(self):
        text,size=ini()
        self.assertLessEqual(size,3248)
        self.assertGreater(size,2536)
        code=words()
        self.assertEqual(code[-1],0)
        self.assertIn(ORIGINAL,code[-3:])
        self.assertIn(f"C2{HOOK&0x1FFFFFF:06X}",text)
        self.assertIn("DBG-CAMP-POS",text)
        raw=struct.pack(f">{len(code)}I",*code)
        self.assertIn(b"PID_OSCAR\0",raw)
        # Check both save/restore forms of each special register, and native
        # ABI argument saves. Native call execution still requires Dolphin.
        for word in (0x7C000026,0x7C0FF120,0x7C0902A6,0x7C0903A6,0x7C0102A6,0x7C0103A6):
            self.assertIn(word,code)
        md=capstone.Cs(capstone.CS_ARCH_PPC,capstone.CS_MODE_32|capstone.CS_MODE_BIG_ENDIAN)
        for word in (0x7C000026,0x7C0FF120,0x7C0902A6,0x7C0903A6,0x7C0102A6,0x7C0103A6):
            self.assertEqual(len(list(md.disasm(word.to_bytes(4,"big"),0))),1)

    def test_actual_enabled_ini_rejects_truncated_conflicting_and_overbudget_codes(self):
        def source(lines,names="test"):
            return "[Gecko]\n$test\n"+lines+"\n[Gecko_Enabled]\n$"+names+"\n"
        with self.assertRaisesRegex(ValueError,"truncated"):
            validate_ini(source("C20291D8 00000002\n60000000 00000000"))
        with self.assertRaisesRegex(ValueError,"empty"):
            validate_ini(source(""))
        with self.assertRaisesRegex(ValueError,"placeholder"):
            validate_ini(source("C20291D8 00000001\n60000000 60000000"))
        with self.assertRaisesRegex(ValueError,"undefined"):
            validate_ini(source("04000000 00000000",names="missing"))
        with self.assertRaisesRegex(ValueError,"space"):
            validate_ini(source("04000000 00000000\n"*407))
        with self.assertRaisesRegex(ValueError,"conflict"):
            validate_ini(source("C20291D8 00000001\n60000000 00000000\n$other\nC20291D8 00000001\n60000000 00000000",names="test\n$other"))
