"""Tests for the inspection tools. Game-dependent tests skip when the image is absent."""

from __future__ import annotations

import random
import unittest
from pathlib import Path

from tools.fe9 import dispos, lz77, pack

ROOT = Path(__file__).resolve().parents[1]
IMAGE = ROOT / "Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso"


class NetplayPackageTests(unittest.TestCase):
    """The shareable Player 2 ZIP (NET-02): exact contents, matching codes, reproducible bytes."""

    def test_build_verifies_and_is_reproducible(self):
        import hashlib, tempfile, zipfile
        from tools import netplay_package as npk
        with tempfile.TemporaryDirectory() as d:
            a, b = npk.build(Path(d) / "a.zip"), npk.build(Path(d) / "b.zip")
            self.assertEqual(npk.verify(a), [])
            self.assertEqual(a.read_bytes(), b.read_bytes())
            self.assertLess(a.stat().st_size, 64 * 1024)
            with zipfile.ZipFile(a) as z:
                names = z.namelist()
                ini = z.read(f"{npk.TOP}/User/Config/Dolphin.ini").decode()
            self.assertFalse(any(n.lower().endswith((".gci", ".iso", ".ciso", ".sav", ".dol")) for n in names))
            # No Dolphin binaries or launcher scripts: the friend starts their own Dolphin (README step 2).
            self.assertFalse(any(n.lower().endswith((".exe", ".dll", ".bat", ".cmd", ".ps1")) for n in names))
            with zipfile.ZipFile(a) as z:
                readme = z.read(f"{npk.TOP}/README.txt").decode()
                codes_sha = hashlib.sha256(z.read(f"{npk.TOP}/User/GameSettings/GFEE01.ini")).hexdigest().upper()
            self.assertIn(codes_sha, readme)    # the Get-FileHash check in README step 4
            self.assertIn("--user", readme)
            self.assertIn("TraversalChoice = traversal", ini)
            self.assertNotIn("ISOPath", ini)

    def test_verify_rejects_save_data_and_other_codes(self):
        import tempfile, zipfile
        from tools import netplay_package as npk
        from tools.install_codes import build_ini
        with tempfile.TemporaryDirectory() as d:
            good = npk.build(Path(d) / "good.zip")
            bad = Path(d) / "bad.zip"
            with zipfile.ZipFile(good) as src, zipfile.ZipFile(bad, "w") as dst:
                for i in src.infolist():
                    data = src.read(i)
                    if i.filename.endswith("GameSettings/GFEE01.ini"):
                        data = build_ini(npk.PACKAGE_CODES + ["DBG-01"], verbose=False).encode()
                    dst.writestr(i, data)
                dst.writestr(f"{npk.TOP}/User/GC/USA/Card A/01-GFEE-FIREEMBLEM8J.gci", b"x")
                dst.writestr(f"{npk.TOP}/Start-FE9-Coop.bat", b"@echo off")
            problems = " ".join(npk.verify(bad))
            self.assertIn("forbidden entry", problems)
            self.assertIn("code fingerprint", problems)
            self.assertIn("MANIFEST hash mismatch", problems)

    def test_fingerprint_rules(self):
        from tools import netplay_package as npk
        from tools.install_codes import build_ini
        text = build_ini(npk.PACKAGE_CODES, verbose=False)
        fp = npk.fingerprint(text)
        spaced = "\r\n".join(l.replace(" ", "\t ").lower() if not l.startswith(("$", "[")) else l
                             for l in text.split("\n"))   # line endings and code-line spacing/case only
        self.assertEqual(npk.fingerprint(spaced), fp)
        self.assertEqual([n.split()[0] for _k, n, _c in npk.enabled_codes(text)], ["EXP-16", "COOP-P6"])  # definition order
        self.assertNotEqual(npk.fingerprint(build_ini(npk.PACKAGE_CODES + ["DBG-01"], verbose=False)), fp)
        self.assertNotEqual(npk.fingerprint(build_ini(["COOP-P5"], verbose=False)), fp)

    def test_netplay_setup_traversal_host_keeps_net01_defaults(self):
        from tools.netplay_setup import dolphin_ini
        net01 = dolphin_ini(Path("G"), "P1-Blue", True)
        self.assertIn("TraversalChoice = direct", net01)
        self.assertIn("BackgroundInput = True", net01)
        net02 = dolphin_ini(Path("G"), "P1-Blue", True, traversal=True)
        for need in ("TraversalChoice = traversal", "TraversalServer = stun.dolphin-emu.org",
                     "BackgroundInput = False", "SyncCodes = True", "WriteSaveData = False", "SIDevice1 = 6"):
            self.assertIn(need, net02)


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

    @staticmethod
    def _asm(words: list[int]) -> list[str]:
        """Disassemble a cave, skipping embedded data words (capstone stops at them)."""
        import capstone, struct
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        raw, out, off = b"".join(struct.pack(">I", w) for w in words), [], 0
        while off < len(raw):
            n = len(out)
            for i in md.disasm(raw[off:], off):
                out.append(f"{i.mnemonic} {i.op_str}".strip()); off = i.address + 4
            if len(out) == n:
                out.append(".word"); off += 4
        return out

    def test_ownership_flag_bits_unused(self):
        """F-52: bits 25-30 of unit+0x1A0 are never in a narrow mask near any flag access, the chapter
        transition / map start masks keep them, and the card save reads and writes the word raw."""
        from tools.fe9.ppc import Dol
        from tools import draft_code as dc
        dol = Dol(self.disc.read_dol())
        bits = dc.flag_bit_usage(dol)
        self.assertEqual([bits[b] for b in range(25, 31)], [0] * 6)
        self.assertGreater(bits[10], 0)                       # 0x400 (deployed) is found, so the scan works
        transition = ((dol.u32(0x8002E038) & 0xFFFF) << 16) + ((dol.u32(0x8002E040) & 0xFFFF) - 0x10000)
        self.assertEqual(transition & 0xFFFFFFFF, 0xFF88C7FE)
        for mask in (0xFF88C7FE, 0xFFFFBBFF, 0xFFFFFDBF, 0xFFF77FFF):   # 0x8002E0xx, 0x8002EA10, 0x80050D1C, 0x801D31F0
            self.assertEqual(mask & (dc.OWNED | dc.P2), dc.OWNED | dc.P2)
        self.assertEqual((dol.u32(0x8003C994), dol.u32(0x8003C998)), (0x38BE01A0, 0x38800004))   # load 4 raw bytes
        self.assertEqual(dol.u32(0x8003CBBC), 0x38BE01A0)                                          # save them

    def test_exp21_flag_ownership_code(self):
        """EXP-21 in the ini is what tools/draft_code.py generates; same hooks as EXP-16, keyed on the P2 bit."""
        from tools.fe9.ppc import Dol
        from tools import draft_code as dc, owner_code as oc
        dol = Dol(self.disc.read_dol())
        found = self._gecko_blocks(dc.NAMES[21])
        self.assertEqual(found, dc.blocks21())   # regenerate with `python -m tools.draft_code --write`
        self.assertEqual([a for a, _ in found], [a for a, _ in oc.blocks()])   # never enable with EXP-16
        for (addr, words), (src, dst) in zip(found, [(0, 3), (3, 0), (3, 0), (3, 0), (3, 0)]):
            body = words[:-2] if words[-2] == oc.NOP else words[:-1]
            self.assertEqual(body[-1], dol.u32(addr))         # original instruction replayed
            asm = self._asm(body)
            head = {0: "lwz r31, -0x5d9c(r12)", 3: "lwz r31, -0x5d78(r12)"}[src]
            self.assertIn(head, asm)
            self.assertIn("andis. r0, r0, 0x4000", asm)       # only Player 2 units move
            self.assertIn(f"li r4, {dst}", asm)
            self.assertIn("lwz r30, 0x184(r31)", asm)         # next read before the transfer unlinks
            self.assertEqual(addr == 0x8002E738, "lbz r0, 0x719(r12)" in asm)
            self.assertEqual(addr == 0x800BA8F8, "cmpw r3, r0" in asm)
            self.assertEqual(addr == 0x8002E738, "stb r0, 0x71f(r12)" in asm)

    def test_exp23_draft_v2_code(self):
        """EXP-23: green parking at turn 1, unpark on first action and phase advance, four named sounds."""
        from tools.fe9.ppc import Dol
        from tools import draft_code as dc
        dol = Dol(self.disc.read_dol())
        found = self._gecko_blocks(dc.NAMES[23])
        self.assertEqual(found, dc.blocks23())   # regenerate with `python -m tools.draft_code --write`
        self.assertEqual([a for a, _ in found], [0x800291D8, 0x8002E73C, 0x80028CC4, 0x8002E65C])
        self.assertEqual(found[0][0], self._gecko_blocks(dc.NAMES[22])[0][0])   # replaces EXP-22: never both
        for addr, orig in (dc.INPUT_HOOK, dc.PARK_HOOK, dc.ACTED_HOOK, dc.ADVANCE_CALL):
            self.assertEqual(dol.u32(addr), orig)
        for key, name in (("p1", "SFX_SYS_UNIT_SELECT1"), ("p2", "SFX_SYS_UNIT_CHANGE1"),
                          ("release", "SFX_SYS_UNIT_CANCEL1"), ("miss", "SFX_SYS_MISS1")):
            off = dol.addr_to_off(dc.SE[key])
            self.assertEqual(dol.data[off:off + len(name) + 1], name.encode() + b"\0")
        inp, park, acted, adv = (self._asm(w[:-1]) for _, w in found)
        for need in ["andi. r0, r0, 1", "andis. r12, r11, 0x1000", "oris r11, r11, 0x1000", "li r4, 2",
                     "rlwinm r11, r11, 0, 4, 2", "oris r11, r11, 0x6000", "ori r3, r3, 0x9175"]:
            self.assertIn(need, inp)
        self.assertIn("stwu r1, -0x30(r1)", inp[-2:])                              # original replayed
        for need in ["lha r0, 0x71a(r12)", "andi. r12, r0, 0x400", "andis. r12, r0, 0x2000",
                     "oris r0, r0, 0x1000", "li r4, 2", "ori r12, r12, 0x5bc0"]:
            self.assertIn(need, park)
        self.assertEqual(park[-1], "mflr r0")                                     # original replayed
        for asm in (acted, adv):
            self.assertIn("lwz r31, -0x5d84(r12)", asm)                          # force 2 head
            self.assertIn("andis. r12, r0, 0x1000", asm)                         # only PARKED units
            self.assertIn("rlwinm r0, r0, 0, 4, 2", asm)
            self.assertIn("li r4, 0", asm)
        self.assertEqual(acted[-1], "lbz r0, 0x9e(r3)")
        self.assertEqual(adv[-5:], ["lis r12, -0x7fec", "ori r12, r12, 0xd3b4", "mtctr r12", "bctrl", "nop"])
        self.assertEqual((dol.u32(0x80028CBC), dol.u32(0x80028CC0)), (0x60000001, 0x900501A0))   # acted bit set before

    def test_exp22_draft_code(self):
        """EXP-22: turn 1 blue phase, L+R edge per port, cursor unit, lord/partner refusal, alternating picks."""
        from tools.fe9.ppc import Dol
        from tools import draft_code as dc
        dol = Dol(self.disc.read_dol())
        [(addr, words)] = self._gecko_blocks(dc.NAMES[22])
        self.assertEqual((addr, words), (dc.INPUT_HOOK[0], dc.draft_cave()))
        self.assertEqual(dol.u32(addr), dc.INPUT_HOOK[1])
        asm = self._asm(words[:-1])
        for need in ["lbz r0, 0x719(r12)", "lha r0, 0x71a(r12)", "cmpwi r0, 1",      # phase 0, turn 1
                     "ori r12, r12, 0xf408", "mulli r0, r30, 0xc", "andi. r0, r0, 0x60",  # PADStatus[port], L+R
                     "ori r12, r12, 0xa794", "ori r12, r12, 0x5bc0", "ori r12, r12, 0xca38",
                     "ori r12, r12, 0x75fc", "andis. r12, r11, 0x2000", "oris r11, r11, 0x6000",
                     "oris r11, r11, 0x2000", "rlwinm r11, r11, 0, 3, 0", "cmpw r0, r30", "cmpwi r30, 2"]:
            self.assertIn(need, asm)
        for head in ("-0x5d9c", "-0x5d78", "-0x5d60", "-0x5d48"):                    # count forces 0/3/5/7
            self.assertIn(f"lwz r12, {head}(r12)", asm)
        self.assertEqual(asm[-1], "stwu r1, -0x30(r1)" if words[-2] != 0x60000000 else "nop")
        self.assertIn("stwu r1, -0x30(r1)", asm)                                     # original replayed
        self.assertEqual((dol.u32(0x800292BC), dol.u32(0x800292C0)), (0x3C608027, 0x38800064))  # Next Unit's SE args

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

    def test_exp20_yellow_cursor_hook(self):
        """EXP-20: in a human yellow phase the phase-start cursor step moves the cursor to 0x800AA5F0(0)."""
        import capstone, struct
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        [(addr, words)] = self._gecko_blocks("EXP-20 Yellow phase starts with the cursor on a yellow unit")
        self.assertEqual(addr, 0x8002E464)
        self.assertEqual(dol.u32(0x8002E464), 0x40820098)          # bne 0x8002E4FC (phase != 0)
        md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)
        asm = [f"{i.mnemonic} {i.op_str}".strip()
               for i in md.disasm(b"".join(struct.pack(">I", w) for w in words[:-1]), 0)]
        self.assertEqual(asm, [
            "beq 0x64", "cmplwi r4, 3", "bne 0x54",
            "lbz r0, 0x17(r3)", "cmplwi r0, 1", "bne 0x54",
            "lbz r0, 0x9e(r3)", "rlwinm. r0, r0, 0x1a, 0x1f, 0x1f", "bne 0x54",
            "li r3, 0", "lis r12, -0x7ff6", "ori r12, r12, 0xa5f0", "mtctr r12", "bctrl",
            "cmplwi r3, 0", "beq 0x54",
            "mr r31, r3", "lis r12, -0x7ffe", "ori r12, r12, 0xe4b0", "mtctr r12", "bctr",
            "lis r12, -0x7ffe", "ori r12, r12, 0xe4fc", "mtctr r12", "bctr",
            "nop", "nop"])
        self.assertEqual(words[-1], 0)                             # branch back to 0x8002E468
        # the jump targets are the vanilla cursor move (unit in r31) and the epilogue
        self.assertEqual((dol.u32(0x8002E4B0), dol.u32(0x8002E4FC)), (0x887F019E, 0x80010024))

    def test_coop_p6_package(self):
        """COOP-P6 is exactly COOP-P5 + EXP-20, with no hook used twice."""
        p5 = self._gecko_blocks("COOP-P5 Two-army co-op, Player 2 characters treated as player units (Phase 4 package v2)")
        e20 = self._gecko_blocks("EXP-20 Yellow phase starts with the cursor on a yellow unit")
        p6 = self._gecko_blocks("COOP-P6 Two-army co-op, cursor cue for the yellow phase (Phase 4 package v3)")
        self.assertEqual(p6, p5 + e20)
        hooks = [a for a, _ in p6]
        self.assertEqual(len(hooks), len(set(hooks)))

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

    def test_script_transfer_decoding(self):
        """chapter_audit decodes (PID, force) of UnitTransferToForceByPID calls from .cmb bytecode (F-48)."""
        from tools.chapter_audit import script_strings, script_transfers
        ch3 = self.disc.read_file("Scripts/C04.cmb")
        self.assertIn(("PID_OSCAR", 7), script_transfers(ch3))      # Ch3 benches Oscar (force 7)
        self.assertIn(("PID_BOLE", 5), script_transfers(ch3))       # ... and returns Boyd to the roster
        ch18 = script_transfers(self.disc.read_file("Scripts/C19.cmb"))
        self.assertIn(("PID_CHINON", 1), ch18)                      # Shinon turns enemy in Ch18
        self.assertIn(("PID_CHINON", 0), ch18)
        self.assertEqual(script_strings(self.disc.read_file("Scripts/C07.cmb"))[0x0A], "PID_IKE")

    def test_sortie_caps_and_forced_units(self):
        """chapter_audit: sortie cap = mikata entries (F-56); forced units decoded from UnitForcedSally* calls."""
        from tools.chapter_audit import script_calls, sortie_caps
        forced = lambda cid: [a[0] for _n, a in script_calls(self.disc.read_file(f"Scripts/C{cid:02d}.cmb"),
                                                             ("UnitForcedSallyByPID", "UnitForcedSally"))]
        self.assertEqual(forced(9), ["PID_IKE"])                                   # Ch8: only Ike is forced
        self.assertEqual(set(forced(7)), {"PID_IKE", "PID_TIAMAT", "PID_OSCAR", "PID_BOLE", "PID_KILROY", "PID_SENERIO"})
        self.assertEqual(sortie_caps(self.disc, 7), {"c": 6, "h": 6, "m": 6, "n": 6})   # = runtime state+0x544 at Ch6 prep
        self.assertEqual(sortie_caps(self.disc, 9)["n"], 7)
        self.assertEqual(sortie_caps(self.disc, 11), {"c": 8, "h": 11, "m": 11, "n": 11})

    def test_prep_sortie_toggle(self):
        """F-57: Pick Units (E_SallyList) toggles bit 0x80000000 of unit+0x1A0 through its list callback."""
        from tools.fe9.ppc import Dol
        dol = Dol(self.disc.read_dol())
        self.assertEqual([dol.u32(a) for a in (0x8012C9E8, 0x8012C9EC, 0x8012C9F0, 0x8012C9F4, 0x8012C9F8)],
                         [0x800401A0, 0x38600001, 0x6C008000, 0x900401A0, 0x4E800020])
        self.assertEqual((dol.u32(0x8012C9C8), dol.u32(0x8012C9D0)), (0x3884C9E8, 0x90830054))   # callback -> obj+0x54
        self.assertEqual([dol.u32(a) for a in (0x80291088, 0x802910B4, 0x802910C0)],
                         [0x80275B0E, 0x8012DFA8, 0x8012D6A4])                        # E_SallyList proc steps
        off = dol.addr_to_off(0x80275B0E)
        self.assertEqual(dol.data[off:off + 12], b"E_SallyList\0")

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
