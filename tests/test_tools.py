"""Tests for the inspection tools. Game-dependent tests skip when the image is absent."""

from __future__ import annotations

import random
import unittest
from pathlib import Path

from tools.fe9 import dispos, lz77, pack

ROOT = Path(__file__).resolve().parents[1]
IMAGE = ROOT / "Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso"


class LZ77Tests(unittest.TestCase):
    def test_roundtrip(self):
        rng = random.Random(9)
        samples = [b"", b"a", b"abcabcabcabcabcabc" * 50, bytes(rng.randrange(4) for _ in range(5000))]
        for s in samples:
            self.assertEqual(lz77.decompress(lz77.compress(s)), s)

    def test_rejects_bad_magic(self):
        with self.assertRaises(lz77.LZ77Error):
            lz77.decompress(b"\x11\x00\x00\x00")


@unittest.skipUnless(IMAGE.exists(), "game image not present")
class GameTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from tools.fe9.disc import DiscReader
        cls.disc = DiscReader(IMAGE)

    @classmethod
    def tearDownClass(cls):
        cls.disc.close()

    def test_header(self):
        h = self.disc.header()
        self.assertEqual(h["game_id"], "GFEE01")
        self.assertEqual(h["revision"], 0)

    def test_dol_hash(self):
        import hashlib
        from tools.verify_game import EXPECTED_DOL_SHA1
        self.assertEqual(hashlib.sha1(self.disc.read_dol()).hexdigest(), EXPECTED_DOL_SHA1)

    def test_signatures(self):
        from tools.check_signatures import SIGNATURES
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        for addr, word, meaning in SIGNATURES:
            self.assertEqual(dol.u32(addr), word, f"{addr:08X} {meaning}")

    def test_exp06_gecko_hook(self):
        """EXP-06 cave disassembles as intended and replays the original instruction."""
        import capstone, struct
        from tools.fe9.ppc import Dol
        from tools.install_codes import ROOT as R, parse_sections
        lines = parse_sections((R / "codes/GFEE01.ini").read_text())["Gecko"]
        start = lines.index("$EXP-06 Units selectable only in their own force's phase")
        header, *body = lines[start + 1:start + 7]
        self.assertEqual(header, "C202858C 00000005")
        words = [int(w, 16) for line in body for w in line.split()]
        self.assertEqual(words[-1], 0)  # branch-back slot
        dol = Dol(self.disc.read_dol())
        self.assertEqual(words[-2], dol.u32(0x8002858C))  # original instruction replayed
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        code = b"".join(struct.pack(">I", w) for w in words[:-1])
        asm = [f"{i.mnemonic} {i.op_str}".strip() for i in md.disasm(code, 0)]
        self.assertEqual(asm, [
            "lbz r0, 0x11(r31)", "cmplw r30, r0", "beq 0x20", "li r3, 3",
            "lis r12, -0x7ffe", "ori r12, r12, 0x85a4", "mtctr r12", "bctr", "lwz r0, 0x1a0(r29)",
        ])

    def test_chapter9_partner_units(self):
        files = {e.name: e.data for e in pack.read_pack(self.disc.read_file("zmap/bmap10/dispos.cmp"))}
        _date, groups = dispos.parse(files["dispos_n.bin"])
        units = {u.pid: u for g in groups for u in g.units}
        # force index byte (+0x61): Lethe/Mordecai = 3, Ike = 0, enemies = 1
        self.assertEqual(units["PID_LETHE"].raw[0x61], 3)
        self.assertEqual(units["PID_MORDY"].raw[0x61], 3)
        self.assertEqual(units["PID_IKE"].raw[0x61], 0)
        self.assertEqual(units["PID_KOTAHU"].raw[0x61], 1)

    def test_lz77_recompress_real_file(self):
        raw = self.disc.read_file("zmap/bmap10/dispos.cmp")
        plain = lz77.decompress(raw)
        self.assertEqual(lz77.decompress(lz77.compress(plain)), plain)


BASELINE_STATE = ROOT / "work/saves/2026-10-27_baseline/GFEE01.s01"


@unittest.skipUnless(IMAGE.exists() and BASELINE_STATE.exists(), "baseline save state not present")
class SaveStateTests(unittest.TestCase):
    def test_baseline_runtime_matches_static_model(self):
        from tools.inspect_state import FORCES, STATE, load_mem1
        info, m = load_mem1(BASELINE_STATE, IMAGE)
        self.assertEqual((info.game_id, info.state_version), ("GFEE01", 192))
        self.assertEqual(list(m.read(STATE + 0x14, 4)), [1, 2, 2, 2])  # F-05 control modes
        self.assertEqual([m.u8(FORCES + 0xC * f + 8) for f in range(8)], list(range(8)))  # F-03
        self.assertEqual(m.u8(STATE + 0x11), 0)  # phase
        self.assertEqual(m.u16(STATE + 0x12), 1)  # turn

    @unittest.skipUnless((ROOT / "work/saves/GFEE01.s04_exp04").exists(), "EXP-04 state not present")
    def test_exp04_enemy_phase_snapshot(self):
        from tools.inspect_state import STATE, load_mem1
        _info, m = load_mem1(ROOT / "work/saves/GFEE01.s04_exp04", IMAGE)
        self.assertEqual(m.u8(STATE + 0x10), 1)  # Prologue
        self.assertEqual(m.u8(STATE + 0x11), 1)  # enemy phase
        self.assertEqual(list(m.read(STATE + 0x14, 4)), [1, 1, 2, 2])  # red army human-controlled

    @unittest.skipUnless((ROOT / "work/saves/GFEE01.s06_ch9_fixture").exists(), "Ch9 fixture not present")
    def test_ch9_fixture(self):
        from tools.inspect_state import FORCES, STATE, UNITS, load_mem1
        _info, m = load_mem1(ROOT / "work/saves/GFEE01.s06_ch9_fixture", IMAGE)
        self.assertEqual((m.u8(STATE + 0x10), m.u8(STATE + 0x11), m.u16(STATE + 0x12)), (10, 0, 1))
        self.assertEqual(list(m.read(STATE + 0x14, 4)), [1, 2, 2, 2])
        yellow = {}
        for i in range(1, 0xA0):
            u = UNITS + (i - 1) * 0x280
            char = m.u32(u + 0x188)
            if char and m.u32(u + 0x190) == FORCES + 0xC * 3:
                yellow[m.cstr(m.u32(char))] = (m.u8(u + 0x19E), m.u8(u + 0x19F))
        self.assertEqual(yellow, {"PID_LETHE": (25, 18), "PID_MORDY": (24, 18)})

    @unittest.skipUnless((ROOT / "work/saves/GFEE01.s06_exp06_turn2").exists(), "EXP-06 state not present")
    def test_exp06_turn2_snapshot(self):
        from tools.inspect_state import STATE, load_mem1
        _info, m = load_mem1(ROOT / "work/saves/GFEE01.s06_exp06_turn2", IMAGE)
        self.assertEqual((m.u8(STATE + 0x10), m.u8(STATE + 0x11), m.u16(STATE + 0x12)), (10, 3, 2))
        self.assertEqual(list(m.read(STATE + 0x14, 4)), [1, 2, 2, 1])

    def test_write_state_roundtrip(self):
        import tempfile
        from tools.fe9.savestate import read_state, write_state
        _info, payload = read_state(BASELINE_STATE)
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "copy.s09"
            write_state(BASELINE_STATE, out, payload)
            _info2, payload2 = read_state(out)
        self.assertEqual(payload, payload2)


if __name__ == "__main__":
    unittest.main()
