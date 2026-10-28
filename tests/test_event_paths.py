import struct
import unittest
from tools.fe9.event_paths import trace,binary
from tools.fe9.event_vm import execute


def script(code,pool=b"get\0set\0FLAG\0UnitTransferToForce\0"):
    raw=bytearray(0x84+len(code))
    raw[:4]=b"cmb\0";raw[0x2C:0x2C+len(pool)]=pool
    struct.pack_into("<II",raw,0x24,0x2C,0x60)
    struct.pack_into("<II",raw,0x60,0x70,0)
    struct.pack_into("<5I",raw,0x70,0,0x84,0,0,0)
    raw[0x84:]=code
    return bytes(raw)


class OpaqueStateTests(unittest.TestCase):
    def test_query_after_native_mutation_is_not_the_previous_sample(self):
        code=bytearray.fromhex("1C08 38000001 3B0000 1C08 38000401 20 1C08 38000001 3D0000 1901 1903 38000D02 20 39")
        for branch in (6,22):struct.pack_into(">h",code,branch+1,len(code)-1-(branch+1))
        raw=script(code);result=trace(raw,0)
        queries=[e for e in result["events"] if e["command"]=="get"]
        transfers=[e for e in result["events"] if e["command"]=="UnitTransferToForce"]
        self.assertTrue(result["complete_local_trace"])
        self.assertEqual(len(transfers),1)
        self.assertEqual(len(queries),2)
        self.assertNotEqual(queries[0]["result"],queries[1]["result"])
        self.assertIn(queries[0]["result"]+" == 0",transfers[0]["conditions"])
        self.assertIn(queries[1]["result"]+" != 0",transfers[0]["conditions"])
        world={"flag":0,"transfers":[]}
        def native(name,args):
            if name=="get":return world["flag"]
            if name=="set":world["flag"]=1
            if name=="UnitTransferToForce":world["transfers"].append(args)
            return 0
        execute(raw,0,native)
        self.assertEqual(world["transfers"],[[1,3]])

    def test_literal_equality_and_nonboolean_constant_branch(self):
        self.assertEqual(binary("0","0",0x2F),"1")
        self.assertEqual(binary("'PID_IKE'","'PID_OSCAR'",0x35),"0")
        # A branch on literal 2 is true; its false arm must not be explored.
        raw=script(bytes.fromhex("1902 3B0004 1900 39"))
        self.assertTrue(trace(raw,0)["complete_local_trace"])

    def test_native_reference_argument_invalidates_local_value(self):
        # v1=0; opaque set(&v1); if (v1) transfer(1,3). The call may write v1.
        code=bytearray.fromhex("0701 1900 21 20 0701 38000401 20 0101 3D0000 1901 1903 38000D02 20 39")
        branch=15
        struct.pack_into(">h",code,branch+1,len(code)-1-(branch+1))
        result=trace(script(code),0)
        transfers=[e for e in result["events"] if e["command"]=="UnitTransferToForce"]
        self.assertTrue(result["complete_local_trace"])
        self.assertEqual(len(transfers),1)
        self.assertIn("v1@0x8C#1 != 0",transfers[0]["conditions"])
