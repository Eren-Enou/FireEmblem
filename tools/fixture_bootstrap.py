"""Create a NEW private profile for a synthetic later-chapter start.

Generalizes EXP-05's conditional Prologue->Ch9 redirect (TESTING.md). Other
destinations are unverified. This never constructs a roster or story flags and
never certifies natural progression. No card/state is imported or overwritten.
"""
import argparse
import json
from pathlib import Path

from tools.install_codes import ROOT, build_ini, parse_sections, gecko_sizes
from tools.netplay_setup import make_user
from tools.setup_pads import PORT1_KEYBOARD, keyboard_layout, _KEYS


def create(root: Path, chapter: int, *, dolphin: Path = ROOT / "Dolphin-x64"):
    if not 3 <= chapter <= 31:
        raise ValueError("target internal chapter must be 3..31 (Prologue=1)")
    root = root.resolve()
    workspace = (ROOT / "work").resolve()
    if workspace not in root.parents:
        raise ValueError("fixture profile must be a new directory inside this clone's work/")
    if root.exists():
        raise ValueError("refusing to replace existing fixture directory")
    codes = ["COOP-P6", "EXP-16"]
    sections = parse_sections(build_ini(codes, verbose=False, dolphin=dolphin))
    name = f"FIXTURE-REDIRECT synthetic internal chapter 2 to {chapter}"
    sections.setdefault("ActionReplay", []).extend([
        "$" + name, "08330718 00000002", f"00330718 {chapter:08X}"])
    sections.setdefault("ActionReplay_Enabled", []).append("$" + name)
    text = "# Synthetic fixture bootstrap only; never a production configuration.\n"
    text += "\n".join("[" + k + "]\n" + "\n".join(v) for k, v in sections.items()) + "\n"
    # Exclusive directory reservation; no force option and no personal card copy.
    root.mkdir(parents=True, exist_ok=False)
    make_user(root / "User", (dolphin / "Games").resolve(), "Synthetic fixture",
              PORT1_KEYBOARD, text, pad2=keyboard_layout(_KEYS))
    manifest = {"classification": "synthetic_chapter_redirect", "internal_target": chapter,
                "status": "NOT TESTED", "gecko_bytes": sum(n for _, n in gecko_sizes(codes)),
                "source": "EXP-05 / TESTING.md; original state+0x10 chapter field (F-12)",
                "procedure": ["Boot this private profile, choose New Game and finish the original Prologue",
                              "The conditional AR seed redirects the first internal chapter 2 to the target",
                              "Save only to this initially empty private card if the original game permits",
                              "Capture state and snapshot; inspect map, roster, flags and live hooks",
                              "Disable FIXTURE-REDIRECT in this private INI before further progression",
                              "Test the target event through original gameplay; do not set its completion flag"],
                "limitations": ["No natural roster, recruitment, inventory, supports or story history",
                                "Target cutscenes may softlock or lack mandatory characters/items",
                                "Only destination 10 has historical redirect evidence; no new runtime acceptance",
                                "Cannot certify natural chapter completion, transition or Netplay"]}
    (root / "fixture.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--target", type=int, required=True, help="internal ID; Ch6=7, Ch10=11, Ch17=18, Endgame=31")
    a = p.parse_args()
    result = create(a.root, a.target)
    print(f"created {a.root}; target {a.target}; {result['gecko_bytes']} Gecko bytes; NOT TESTED")
