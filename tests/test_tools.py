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


class SetupPadsTests(unittest.TestCase):
    def test_set_ini_updates_and_replaces(self):
        from tools.setup_pads import PORT2_KEYBOARD, set_ini
        core = set_ini("[General]\nA = 1\n[Core]\nCPUThread = True\nSIDevice1 = 0\n[DSP]\n", "Core", {"SIDevice1": "6"})
        self.assertIn("SIDevice1 = 6\n[DSP]", core)
        self.assertIn("CPUThread = True", core)
        pads = set_ini("[GCPad1]\nDevice = X\n[GCPad2]\nDevice = old\nButtons/A = `Q`\n[GCPad3]\n", "GCPad2",
                       PORT2_KEYBOARD, replace_section=True)
        self.assertIn("[GCPad1]\nDevice = X\n[GCPad2]\nDevice = DInput/0/Keyboard Mouse\nButtons/A = `M`", pads)
        self.assertNotIn("`Q`", pads)
        for d, k in (("Up", 8), ("Down", 5), ("Left", 4), ("Right", 6)):  # keypad, not the top-row digits
            self.assertIn(f"Main Stick/{d} = `NUMPAD{k}`\n", pads)
        self.assertIn("\n[GCPad3]", pads)
        self.assertEqual(set_ini("", "Core", {"SIDevice1": "6"}), "[Core]\nSIDevice1 = 6\n")

    def test_netplay_user_folders(self):
        import tempfile
        from tools.netplay_setup import dolphin_ini, make_user
        from tools.setup_pads import PORT2_KEYBOARD
        host = dolphin_ini(Path("G:/Games"), "P1-Blue", host=True)
        for line in ("ISOPath0 = G:", "EnableCheats = True", "BackgroundInput = True", "SyncSaves = True",
                     "SyncCodes = True", "WriteSaveData = False", "HostPort = 2626"):
            self.assertIn(line, host)
        self.assertNotIn("SyncSaves", dolphin_ini(Path("G:/Games"), "P2-Yellow", host=False))
        with tempfile.TemporaryDirectory() as tmp:
            make_user(Path(tmp) / "client", Path("G:/Games"), "P2-Yellow", PORT2_KEYBOARD, None)
            pad = (Path(tmp) / "client/Config/GCPadNew.ini").read_text()
            self.assertTrue(pad.startswith("[GCPad1]\n"))  # the client's own pad 1; Netplay maps it to port 2
            self.assertIn("Main Stick/Up = `NUMPAD8`", pad)
            self.assertTrue((Path(tmp) / "client/GC/USA/Card A").is_dir())
            self.assertFalse((Path(tmp) / "client/GameSettings").exists())


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

    @staticmethod
    def _gecko_blocks(name: str) -> list[tuple[int, list[int]]]:
        """Return [(hook address, cave words incl. branch-back slot)] for every C2 block of a code."""
        from tools.install_codes import ROOT as R, parse_sections
        lines = parse_sections((R / "codes/GFEE01.ini").read_text())["Gecko"]
        i = lines.index("$" + name) + 1
        blocks = []
        while i < len(lines) and not lines[i].startswith("$"):
            op, count = lines[i].split()
            assert op.startswith("C2"), f"unexpected Gecko line {lines[i]}"
            n = int(count, 16)
            words = [int(w, 16) for line in lines[i + 1:i + 1 + n] for w in line.split()]
            blocks.append((0x80000000 | int(op[2:], 16), words))
            i += 1 + n
        return blocks

    def _gecko_c2(self, name: str, hook: int) -> list[str]:
        """Return the disassembled cave of a single-block C2 code (minus the branch-back slot)."""
        import capstone, struct
        [(addr, words)] = self._gecko_blocks(name)
        self.assertEqual(addr, hook)
        self.assertEqual(words[-1], 0)  # branch-back slot
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        code = b"".join(struct.pack(">I", w) for w in words[:-1])
        self._cave_words = words[:-1]
        return [f"{i.mnemonic} {i.op_str}".strip() for i in md.disasm(code, 0)]

    def test_exp08_gecko_hook(self):
        """EXP-08 cave: control[3] = 1 if force 3 has units else 2, then the original instruction."""
        from tools.fe9.ppc import Dol
        asm = self._gecko_c2("EXP-08 Yellow control set at each phase change (no per-frame write)", 0x8014D3B4)
        self.assertEqual(asm, [
            "lis r12, -0x7fd3", "lwz r12, -0x5d78(r12)", "cmplwi r12, 0", "li r12, 2", "beq 0x18",
            "li r12, 1", "stb r12, 0x17(r3)", "lbz r0, 0x11(r3)", "nop",
        ])
        self.assertEqual(self._cave_words[7], Dol(self.disc.read_dol()).u32(0x8014D3B4))

    def test_exp10_gecko_hook(self):
        """EXP-10 cave: human-controlled force 3 is treated as force 5 by CanGainExp."""
        from tools.fe9.ppc import Dol
        asm = self._gecko_c2("EXP-10 Human-controlled yellow units can gain EXP", 0x8003D180)
        self.assertEqual(asm, [
            "cmplwi r0, 3", "bne 0x1c", "lis r12, -0x7fcd", "lbz r12, 0x71f(r12)", "cmplwi r12, 1",
            "bne 0x1c", "li r0, 5", "cmplwi r0, 5", "nop",
        ])
        self.assertEqual(self._cave_words[7], Dol(self.disc.read_dol()).u32(0x8003D180))

    def test_exp11_gecko_hook(self):
        """EXP-11 cave: human-controlled force 3 reads its EXP byte instead of GetExp's 0xFF."""
        from tools.fe9.ppc import Dol
        asm = self._gecko_c2("EXP-11 Human-controlled yellow units show real EXP (GetExp)", 0x800386C8)
        self.assertEqual(asm, [
            "cmplwi r0, 3", "bne 0x1c", "lis r12, -0x7fcd", "lbz r12, 0x71f(r12)", "cmplwi r12, 1",
            "bne 0x1c", "li r0, 0", "cmplwi r0, 3", "nop",
        ])
        self.assertEqual(self._cave_words[7], Dol(self.disc.read_dol()).u32(0x800386C8))

    def test_exp12_gecko_hook(self):
        """EXP-12 cave: the battle write-back treats human-controlled force 3 as force 5."""
        from tools.fe9.ppc import Dol
        asm = self._gecko_c2("EXP-12 Human-controlled yellow units keep battle EXP (write-back)", 0x80034F68)
        self.assertEqual(asm, [
            "cmplwi r0, 3", "bne 0x1c", "lis r12, -0x7fcd", "lbz r12, 0x71f(r12)", "cmplwi r12, 1",
            "bne 0x1c", "li r0, 5", "cmplwi r0, 5", "nop",
        ])
        self.assertEqual(self._cave_words[7], Dol(self.disc.read_dol()).u32(0x80034F68))

    def test_exp13_gecko_hooks(self):
        """EXP-13: ten EXP-10-style caves on the force 0/5 checks of the battle-result unit pickers."""
        import capstone, struct
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        blocks = self._gecko_blocks("EXP-13 Level-up/result screens accept human-controlled yellow units")
        self.assertEqual([a for a, _ in blocks], [
            0x801B610C, 0x801B613C, 0x801B62D4, 0x801B6304, 0x801B63BC,
            0x801B63EC, 0x801B6814, 0x801B6844, 0x801B6C28, 0x801B6C58])
        for addr, words in blocks:
            self.assertEqual(words[-1], 0)
            code = b"".join(struct.pack(">I", w) for w in words[:-1])
            asm = [f"{i.mnemonic} {i.op_str}".strip() for i in md.disasm(code, 0)]
            self.assertEqual(asm, [
                "cmplwi r0, 3", "bne 0x1c", "lis r12, -0x7fcd", "lbz r12, 0x71f(r12)", "cmplwi r12, 1",
                "bne 0x1c", "li r0, 5", "cmplwi r0, 5", "nop",
            ])
            self.assertEqual(words[7], dol.u32(addr), f"{addr:08X}")
            self.assertEqual(dol.u32(addr - 0xC) >> 16, 0x8800 | (dol.u32(addr - 0xC) >> 16 & 0xFF), f"{addr:08X}")

    def test_exp14_gecko_hook(self):
        """EXP-14 cave: current-pad pointer = pad object 1 in a human yellow phase with port 2 present."""
        from tools.fe9.ppc import Dol
        asm = self._gecko_c2("EXP-14 Controller port 2 drives the human yellow phase", 0x80025B8C)
        self.assertEqual(asm, [
            "lis r12, -0x7fcd", "lbz r11, 0x719(r12)", "cmplwi r11, 3", "bne 0x34",
            "lbz r11, 0x71f(r12)", "cmplwi r11, 1", "bne 0x34",
            "lis r12, -0x7fd1", "lbz r11, -0xbe2(r12)", "cmplwi r11, 0xff", "beq 0x34",
            "addi r11, r12, -0xba4", "b 0x3c",
            "lis r12, -0x7fd1", "addi r11, r12, -0xbc8",
            "stw r11, -0x7b60(r13)", "lmw r27, 0xc(r1)",
        ])
        dol = Dol(self.disc.read_dol())
        self.assertEqual(self._cave_words[-1], dol.u32(0x80025B8C))
        # r13 (SDA base) = 0x8036EDA0, so r13-0x7B60 = 0x80367240 is the pointer the game stores pad object 0 in
        self.assertEqual((dol.u32(0x80003334), dol.u32(0x80003338)), (0x3DA08036, 0x61ADEDA0))

    def test_exp15_gecko_hooks(self):
        """EXP-15: caves calling UnitTransferToForce for PID_BOLE/PID_OSCAR (Ch1 blue phase 0->3; every chapter-end path 3->0)."""
        import capstone, struct
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        blocks = self._gecko_blocks("EXP-15 Chapter 1: Boyd and Oscar fight as the yellow army (fixed assignment)")
        self.assertEqual([a for a, _ in blocks], [0x8002E738, 0x800BA784, 0x8002E0D0, 0x80005F04])
        for (addr, words), (src, dst) in zip(blocks, [(0, 3), (3, 0), (3, 0), (3, 0)]):
            body = words[:-2] if words[-2] == 0x60000000 else words[:-1]
            self.assertEqual(words[-1], 0)
            self.assertEqual(body[-1], dol.u32(addr))  # original instruction replayed
            code = b"".join(struct.pack(">I", w) for w in body)
            self.assertIn(b"PID_BOLE\0\0\0\0PID_OSCAR\0\0\0", code)
            data = code.index(b"PID_BOLE")
            asm = [f"{i.mnemonic} {i.op_str}" for i in md.disasm(code[data + 24:], 0)]
            text = "\n".join(asm)
            self.assertIn("ori r12, r12, 0x6bdc", text)   # 0x80016BDC unit by PID
            self.assertIn("ori r12, r12, 0xca38", text)   # 0x800BCA38 UnitTransferToForce
            self.assertIn(f"cmpwi r0, {src}", text)
            self.assertIn(f"li r4, {dst}", text)
            # the bl over the strings lands right after them
            bl = body[data // 4 - 1]
            self.assertEqual(bl, 0x48000000 | (24 + 4) | 1)
        head = [f"{i.mnemonic} {i.op_str}" for i in md.disasm(
            b"".join(struct.pack(">I", w) for w in blocks[0][1][:14]), 0)]
        self.assertIn("lbz r0, 0x718(r12)", head)      # chapter id
        self.assertIn("cmpwi r0, 2", head)             # Chapter 1
        self.assertIn("lbz r0, 0x719(r12)", head)      # phase

    def test_exp16_ownership_code(self):
        """EXP-16 in the ini is exactly what tools/owner_code.py generates from its OWNERS table."""
        import capstone, struct
        from tools.fe9.ppc import Dol
        from tools import owner_code as oc
        dol = Dol(self.disc.read_dol())
        found = self._gecko_blocks(oc.CODE_NAME)
        self.assertEqual(found, oc.blocks())  # regenerate with `python -m tools.owner_code --write`
        hooks = [a for a, _ in found]
        self.assertEqual(hooks, [0x8002E738, 0x800BA784, 0x8002E0D0, 0x80005F04, 0x800BA8F8])
        table = oc.pid_table(oc.OWNERS)
        self.assertNotIn(b"PID_IKE\0", table)
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        for (addr, words), (src, dst) in zip(found, [(0, 3), (3, 0), (3, 0), (3, 0), (3, 0)]):
            body = words[:-2] if words[-2] == oc.NOP else words[:-1]
            self.assertEqual(body[-1], dol.u32(addr))  # original instruction replayed
            code = b"".join(struct.pack(">I", w) for w in body)
            self.assertIn(table, code)                 # one table, identical in every block
            start = code.index(table)
            head = [f"{i.mnemonic} {i.op_str}" for i in md.disasm(code[:start - 4], 0)]
            text = "\n".join(f"{i.mnemonic} {i.op_str}" for i in md.disasm(code[start + len(table):], 0))
            self.assertIn(f"cmpwi r0, {src}", text)
            self.assertIn(f"li r4, {dst}", text)
            self.assertIn("ori r12, r12, 0xca38", text)
            self.assertNotIn("lbz r0, 0x718(r12)", head)   # no chapter restriction any more
            self.assertEqual(addr == 0x8002E738, "lbz r0, 0x719(r12)" in head)   # apply: phase 0 only
            self.assertEqual(addr == 0x800BA8F8, "cmpw r3, r0" in text)          # escape: that unit only
            self.assertEqual(addr == 0x8002E738, "stb r0, 0x71f(r12)" in text)   # apply: control[3] = 1
        with self.assertRaises(ValueError):
            oc.pid_table({"PID_IKE": 2})

    def test_exp17_next_unit_hooks(self):
        """EXP-17: the next-unit search uses force 3 in phase 3 (auto-end + Next Unit), force 0 otherwise."""
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        name = "EXP-17 Auto-end and Next Unit use the yellow army in the yellow phase"
        blocks = self._gecko_blocks(name)
        self.assertEqual([a for a, _ in blocks], [0x800AA5F8, 0x800AA61C])
        self.assertEqual((dol.u32(0x800AA5F8), dol.u32(0x800AA61C)), (0x80840000, 0x28000000))
        pick = ["lis r12, -0x7fcd", "lbz r12, 0x719(r12)", "cmplwi r12, 3", "beq 0x14", "li r12, 0"]
        import capstone, struct
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        asm = [[f"{i.mnemonic} {i.op_str}".strip() for i in md.disasm(b"".join(struct.pack(">I", w) for w in ws[:-1]), 0)]
               for _, ws in blocks]
        self.assertEqual(asm[0], pick + ["mulli r12, r12, 0xc", "lwzx r4, r4, r12"])   # head of force r12
        self.assertEqual(asm[1], pick + ["cmplw r0, r12", "nop"])                     # start unit in force r12

    def test_exp18_base_data_hooks(self):
        """EXP-18: both force-0 unit-list walks continue into force 3 units flagged 0x400 (deployed players)."""
        import capstone, struct
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        blocks = self._gecko_blocks("EXP-18 Base Data in battle lists Player 2's yellow characters")
        self.assertEqual([a for a, _ in blocks], [0x8012E12C, 0x8012E46C])
        self.assertEqual((dol.u32(0x8012E12C), dol.u32(0x8012E46C)), (0x80840184, 0x837A0184))
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        for (addr, words), cur, dst in zip(blocks, (4, 26), (4, 27)):
            body = words[:-2] if words[-2] == 0x60000000 else words[:-1]
            asm = [f"{i.mnemonic} {i.op_str}" for i in md.disasm(b"".join(struct.pack(">I", w) for w in body), 0)]
            self.assertEqual(asm[0], f"lwz r12, 0x184(r{cur})")          # vanilla next pointer
            self.assertEqual(asm[-1], f"mr r{dst}, r12")
            for must in ("lbz r11, 0x60(r31)", "lwz r12, -0x5d78(r12)", "cmpwi r11, 3", "andi. r11, r11, 0x400"):
                self.assertIn(must, asm)
        self.assertEqual(0x802D0000 - 0x5D78, 0x802CA264 + 3 * 0xC)    # force 3 list head

    def test_exp19_death_record_hook(self):
        """EXP-19: at the death routine's force check, force 3 + flag 0x400 counts as force 0."""
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        asm = self._gecko_c2("EXP-19 Player 2 characters who die get the normal player death record", 0x8003E94C)
        self.assertEqual(asm, ["cmplwi r0, 3", "bne 0x18", "lwz r12, 0x1a0(r31)", "andi. r12, r12, 0x400",
                               "beq 0x18", "li r0, 0", "cmplwi r0, 0"])
        self.assertEqual(self._cave_words[-1], dol.u32(0x8003E94C))
        self.assertEqual(dol.u32(0x8003E968), 0x38630048)   # force 0 branch: force 6 (died list)

    def test_dbg02_yellow_hp(self):
        """DBG-02 (test aid): per-frame C0 holding force 3 units with flag 0x400 at 1 HP."""
        import capstone, struct
        from tools.install_codes import ROOT as R, parse_sections
        lines = parse_sections((R / "codes/GFEE01.ini").read_text())["Gecko"]
        i = lines.index("$DBG-02 Test aid: Player 2 deployed units have 1 HP")
        self.assertEqual(lines[i + 1], "C0000000 00000008")
        words = [int(w, 16) for line in lines[i + 2:i + 10] for w in line.split()]
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        asm = [f"{x.mnemonic} {x.op_str}".strip() for x in md.disasm(b"".join(struct.pack(">I", w) for w in words[:-1]), 0)]
        self.assertEqual(asm[:2], ["lis r12, -0x7fd3", "lwz r12, -0x5d78(r12)"])
        self.assertIn("andi. r11, r11, 0x400", asm)
        self.assertEqual(asm[-1], "blr")

    def test_coop_p4_package(self):
        """COOP-P4 is exactly COOP-P3 + EXP-17, with no hook used twice and none shared with EXP-16."""
        from tools import owner_code as oc
        parts = self._gecko_blocks("COOP-P3 Two-army co-op, port 1 blue / port 2 yellow (Phase 2 package v1)")
        parts += self._gecko_blocks("EXP-17 Auto-end and Next Unit use the yellow army in the yellow phase")
        package = self._gecko_blocks("COOP-P4 Two-army co-op with yellow auto-end and Next Unit (Phase 4 package v1)")
        self.assertEqual(package, parts)
        hooks = [a for a, _ in package]
        self.assertEqual(len(hooks), len(set(hooks)))
        self.assertFalse(set(hooks) & {a for a, _ in oc.blocks()})

    def test_coop_p5_package(self):
        """COOP-P5 is exactly COOP-P4 + EXP-18 + EXP-19, with no hook used twice and none shared with EXP-16."""
        from tools import owner_code as oc
        parts = []
        for name in ("COOP-P4 Two-army co-op with yellow auto-end and Next Unit (Phase 4 package v1)",
                     "EXP-18 Base Data in battle lists Player 2's yellow characters",
                     "EXP-19 Player 2 characters who die get the normal player death record"):
            parts += self._gecko_blocks(name)
        package = self._gecko_blocks("COOP-P5 Two-army co-op, Player 2 characters treated as player units (Phase 4 package v2)")
        self.assertEqual(package, parts)
        hooks = [a for a, _ in package]
        self.assertEqual(len(hooks), len(set(hooks)))
        self.assertFalse(set(hooks) & {a for a, _ in oc.blocks()})

    def test_dbg01_enemy_hp(self):
        """DBG-01 (test aid): per-frame C0 routine walking the force 1 list, HP byte +0x1A8 held at 1."""
        import capstone, struct
        from tools.install_codes import ROOT as R, parse_sections
        lines = parse_sections((R / "codes/GFEE01.ini").read_text())["Gecko"]
        i = lines.index("$DBG-01 Test aid: enemies have 1 HP")
        self.assertEqual(lines[i + 1], "C0000000 00000006")
        words = [int(w, 16) for line in lines[i + 2:i + 8] for w in line.split()]
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        asm = [f"{x.mnemonic} {x.op_str}".strip() for x in md.disasm(b"".join(struct.pack(">I", w) for w in words), 0)]
        self.assertEqual(asm, ["lis r12, -0x7fd3", "lwz r12, -0x5d90(r12)", "cmpwi r12, 0", "beq 0x2c",
                               "lbz r11, 0x1a8(r12)", "cmplwi r11, 1", "ble 0x24", "li r11, 1",
                               "stb r11, 0x1a8(r12)", "lwz r12, 0x184(r12)", "b 8", "blr"])
        self.assertEqual((0x802D0000 - 0x5D90), 0x802CA264 + 0xC)  # force 1 entry of the force table
        for name in lines:
            if name.startswith("$COOP-"):
                j = lines.index(name) + 1
                while j < len(lines) and not lines[j].startswith("$"):
                    self.assertFalse(lines[j].startswith("C0"), f"{name} must not contain a test aid")
                    j += 1

    def test_coop_p1_package(self):
        """COOP-P1 is exactly EXP-08 + EXP-06 + EXP-07."""
        parts = []
        for name in ("EXP-08 Yellow control set at each phase change (no per-frame write)",
                     "EXP-06 Units selectable only in their own force's phase",
                     "EXP-07 Human yellow phase does not hand leftover units to the AI"):
            parts += self._gecko_blocks(name)
        self.assertEqual(self._gecko_blocks("COOP-P1 Yellow army human-controlled (Phase 1 package v1)"), parts)

    def test_coop_p2_package(self):
        """COOP-P2 is exactly COOP-P1 + EXP-10..13, with no hook address used twice."""
        parts = []
        for name in ("COOP-P1 Yellow army human-controlled (Phase 1 package v1)",
                     "EXP-10 Human-controlled yellow units can gain EXP",
                     "EXP-11 Human-controlled yellow units show real EXP (GetExp)",
                     "EXP-12 Human-controlled yellow units keep battle EXP (write-back)",
                     "EXP-13 Level-up/result screens accept human-controlled yellow units"):
            parts += self._gecko_blocks(name)
        package = self._gecko_blocks("COOP-P2 Yellow army human-controlled with EXP (Phase 1 package v2)")
        self.assertEqual(package, parts)
        hooks = [addr for addr, _ in package]
        self.assertEqual(len(hooks), len(set(hooks)))

    def test_coop_p3_package(self):
        """COOP-P3 is exactly COOP-P2 + EXP-14, with no hook address used twice."""
        parts = (self._gecko_blocks("COOP-P2 Yellow army human-controlled with EXP (Phase 1 package v2)")
                 + self._gecko_blocks("EXP-14 Controller port 2 drives the human yellow phase"))
        package = self._gecko_blocks("COOP-P3 Two-army co-op, port 1 blue / port 2 yellow (Phase 2 package v1)")
        self.assertEqual(package, parts)
        hooks = [addr for addr, _ in package]
        self.assertEqual(len(hooks), len(set(hooks)))

    def test_exp06_gecko_hook(self):
        """EXP-06 cave disassembles as intended and replays the original instruction."""
        from tools.fe9.ppc import Dol
        asm = self._gecko_c2("EXP-06 Units selectable only in their own force's phase", 0x8002858C)
        self.assertEqual(asm, [
            "lbz r0, 0x11(r31)", "cmplw r30, r0", "beq 0x20", "li r3, 3",
            "lis r12, -0x7ffe", "ori r12, r12, 0x85a4", "mtctr r12", "bctr", "lwz r0, 0x1a0(r29)",
        ])
        self.assertEqual(self._cave_words[-1], Dol(self.disc.read_dol()).u32(0x8002858C))

    def test_exp07_gecko_hook(self):
        """EXP-07 cave: CPU yellow -> original path; otherwise jump to the handler epilogue."""
        from tools.fe9.ppc import Dol
        asm = self._gecko_c2("EXP-07 Human yellow phase does not hand leftover units to the AI", 0x8002E6DC)
        self.assertEqual(asm, [
            "lbz r12, 0x17(r31)", "cmplwi r12, 2", "beq 0x1c", "lis r12, -0x7ffe",
            "ori r12, r12, 0xe71c", "mtctr r12", "bctr", "cmplwi r3, 0", "nop",
        ])
        self.assertEqual(self._cave_words[7], Dol(self.disc.read_dol()).u32(0x8002E6DC))

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

    @unittest.skipUnless((ROOT / "work/saves/GFEE01.s08_exp07_afterEnd").exists(), "EXP-07 state not present")
    def test_exp07_leftover_waits(self):
        from tools.inspect_state import STATE, UNITS, load_mem1
        _info, m = load_mem1(ROOT / "work/saves/GFEE01.s08_exp07_afterEnd", IMAGE)
        self.assertEqual((m.u8(STATE + 0x10), m.u8(STATE + 0x11), m.u16(STATE + 0x12)), (10, 1, 1))
        pos = {}
        for i in range(1, 0xA0):
            u = UNITS + (i - 1) * 0x280
            char = m.u32(u + 0x188)
            if char:
                pos[m.cstr(m.u32(char))] = (m.u8(u + 0x19E), m.u8(u + 0x19F))
        self.assertEqual(pos["PID_MORDY"], (24, 18))  # left unacted, not moved by the AI

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
