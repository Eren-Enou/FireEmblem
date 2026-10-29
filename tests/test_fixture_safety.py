import struct
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.fe9.savestate import MEM1_SIZE, write_state, read_state
from tools.patch_state import apply_edits


class FixtureSafetyTests(unittest.TestCase):
    def test_loader_hook_profile_excludes_ar_and_fits_budget(self):
        from tools.fixture_bootstrap import create
        from tools.install_codes import parse_sections
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);card=root/"source.gci";card.write_bytes(b"GFEE01"+bytes(58))
            with patch("tools.fixture_bootstrap.ROOT",root):
                destination=root/"work/loader"
                result=create(destination,11,source_chapter=7,card=card,redirect_kind="loader-hook")
                sections=parse_sections((destination/"User/GameSettings/GFEE01.ini").read_text())
                self.assertEqual(result["gecko_bytes"],2608)
                self.assertFalse(sections.get("ActionReplay_Enabled"))
                self.assertEqual(len(sections["Gecko_Enabled"]),3)
                self.assertEqual(card.read_bytes(),b"GFEE01"+bytes(58))

    def test_native_card_source_is_copied_and_hashed_without_mutation(self):
        import hashlib
        from tools.fixture_bootstrap import create
        from tools.install_codes import parse_sections
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/"source.gci"
            original=b"GFEE01"+bytes(58)+b"synthetic test content"
            source.write_bytes(original)
            with patch("tools.fixture_bootstrap.ROOT",root):
                target=root/"work/ch10"
                result=create(target,11,source_chapter=7,card=source)
                sections=parse_sections((target/"User/GameSettings/GFEE01.ini").read_text())
                self.assertIn("08330718 00000007",sections["ActionReplay"])
                self.assertIn("00330718 0000000B",sections["ActionReplay"])
                self.assertEqual((target/"User/GC/USA/Card A/source.gci").read_bytes(),original)
                self.assertEqual(source.read_bytes(),original)
                self.assertEqual(result["card"]["sha256"],hashlib.sha256(original).hexdigest())
                self.assertEqual(result["internal_source"],7)
                self.assertEqual(result["status"],"NOT TESTED")

    def test_invalid_source_route_and_budget_fail_before_profile_creation(self):
        from tools.fixture_bootstrap import create
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/"bad.gci";source.write_bytes(b"other game")
            with patch("tools.fixture_bootstrap.ROOT",root):
                target=root/"work/new"
                for args in ({"source_chapter":7},{"source_chapter":11},
                             {"source_chapter":0},{"source_chapter":7,"card":source}):
                    with self.assertRaises(ValueError):create(target,11,**args)
                    self.assertFalse(target.exists())
                with patch("tools.fixture_bootstrap.validate_ini",side_effect=ValueError("budget")):
                    with self.assertRaisesRegex(ValueError,"budget"):create(target,11)
                self.assertFalse(target.exists())

    def test_bootstrap_is_private_new_and_keeps_only_intended_codes_enabled(self):
        from tools.fixture_bootstrap import create
        from tools.install_codes import parse_sections
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch("tools.fixture_bootstrap.ROOT", root):
                # build_ini still reads the repository's definitions; only the
                # fixture destination boundary is redirected to this temp area.
                target = root / "work/ch6"
                result = create(target, 7)
                self.assertEqual(result["classification"], "synthetic_chapter_redirect")
                self.assertEqual(result["gecko_bytes"], 2536)
                sections = parse_sections((target/"User/GameSettings/GFEE01.ini").read_text())
                self.assertEqual(len(sections["ActionReplay_Enabled"]), 1)
                self.assertEqual(len(sections["Gecko_Enabled"]), 2)
                self.assertIn("00330718 00000007", sections["ActionReplay"])
                self.assertFalse(list((target/"User/GC/USA/Card A").iterdir()))
                (target/"preserve").write_text("sentinel")
                with self.assertRaisesRegex(ValueError, "replace"):
                    create(target, 7)
                self.assertEqual((target/"preserve").read_text(), "sentinel")
                with self.assertRaisesRegex(ValueError, "inside"):
                    create(root/"outside", 7)
                with self.assertRaisesRegex(ValueError, "3..31"):
                    create(root/"work/invalid", 32)

    def test_existing_manifest_rejected_before_loading_game_or_state(self):
        from tools.patch_state import main
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp)/"original", Path(tmp)/"new"
            src.write_bytes(b"original sentinel")
            manifest = Path(str(dst)+".json")
            manifest.write_text("keep existing provenance")
            with patch("sys.argv", ["patch_state", str(src), str(dst), "--set", "80000000=01"]), \
                 patch("tools.patch_state.load_mem1") as load:
                self.assertEqual(main(), 1)
                load.assert_not_called()
            self.assertFalse(dst.exists())
            self.assertEqual(src.read_bytes(), b"original sentinel")
            self.assertEqual(manifest.read_text(), "keep existing provenance")

    def test_mem1_bounds_and_overlap_fail_before_mutation(self):
        payload = b"prefix" + bytes(MEM1_SIZE) + b"suffix"
        for edits in (["7FFFFFFF=01"], ["817FFFFF=0102"], ["81800000=01"],
                      ["80000000="], ["80000000=XX"],
                      ["80000000=0102", "80000001=03"]):
            with self.subTest(edits=edits), self.assertRaises(ValueError):
                apply_edits(payload, 6, edits)
        for offset in (-1, 100):
            with self.assertRaisesRegex(ValueError, "complete MEM1"):
                apply_edits(payload, offset, ["80000000=01"])
        changed, edits = apply_edits(payload, 6, ["80000000=01", "817FFFFF=02"])
        self.assertEqual(changed[:6], b"prefix")
        self.assertEqual(changed[-6:], b"suffix")
        self.assertEqual((changed[6], changed[-7]), (1, 2))
        self.assertEqual(len(changed), len(payload))
        self.assertEqual(edits, [(0x80000000, b"\0", b"\1"), (0x817FFFFF, b"\0", b"\2")])

    def test_writer_refuses_existing_destination_and_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp)/"source", Path(tmp)/"copy"
            header = bytearray(0x30)
            header[:6] = b"GFEE01"
            struct.pack_into("<II", header, 0x18, 0xBAADBABE+1, 0)
            struct.pack_into("<HHIQ", header, 0x20, 1, 0, 0, 4)
            src.write_bytes(header+b"old!")
            write_state(src, dst, b"new!")
            self.assertEqual(read_state(dst)[1], b"new!")
            original = src.read_bytes()
            for target in (src, dst):
                before = target.read_bytes()
                with self.assertRaises(FileExistsError):
                    write_state(src, target, b"bad!")
                self.assertEqual(target.read_bytes(), before)
            self.assertEqual(src.read_bytes(), original)
