"""Create a NEW private profile for a synthetic later-chapter start.

Generalizes EXP-05's conditional Prologue->Ch9 redirect (TESTING.md). Other
destinations are unverified. This never constructs a roster or story flags and
never certifies natural progression. Optional native GCI input is copied into a
new private profile, never opened for writing. No savestate is imported.
"""
import argparse
import hashlib
import json
from pathlib import Path

from tools.install_codes import ROOT, build_ini, parse_sections, validate_ini
from tools.netplay_setup import make_user
from tools.setup_pads import PORT1_KEYBOARD, keyboard_layout, _KEYS


def create(root: Path, chapter: int, *, dolphin: Path = ROOT / "Dolphin-x64",
           source_chapter: int = 2, card: Path | None = None, redirect_kind: str = "ar"):
    if not 3 <= chapter <= 31:
        raise ValueError("target internal chapter must be 3..31 (Prologue=1)")
    root = root.resolve()
    workspace = (ROOT / "work").resolve()
    if workspace not in root.parents:
        raise ValueError("fixture profile must be a new directory inside this clone's work/")
    if root.exists():
        raise ValueError("refusing to replace existing fixture directory")
    if not 2 <= source_chapter <= 31 or source_chapter == chapter:
        raise ValueError("source internal chapter must be 2..31 and differ from target")
    if source_chapter != 2 and card is None:
        raise ValueError("a copied native GCI card is required for a non-default source")
    if redirect_kind not in ("ar","loader-hook"):
        raise ValueError("unknown redirect kind")
    card_bytes = None
    if card is not None:
        if not card.is_file() or card.suffix.lower() != ".gci":
            raise ValueError("source must be a readable FE9 GCI file")
        card_bytes = card.read_bytes()
        if len(card_bytes) < 64 or card_bytes[:6] != b"GFEE01":
            raise ValueError("source GCI must have GFEE01 directory identity")
    codes = ["COOP-P6", "EXP-16"]
    sections = parse_sections(build_ini(codes, verbose=False, dolphin=dolphin))
    if redirect_kind == "ar":
        name = f"FIXTURE-REDIRECT synthetic internal chapter {source_chapter} to {chapter}"
        sections.setdefault("ActionReplay", []).extend([
            "$" + name, f"08330718 {source_chapter:08X}", f"00330718 {chapter:08X}"])
        sections.setdefault("ActionReplay_Enabled", []).append("$" + name)
    else:
        from tools.fixture_loader_code import HOOK,ORIGINAL,words
        from tools.owner_code import c2_lines
        from tools.fe9.disc import DiscReader
        from tools.fe9.ppc import Dol
        from tools.verify_game import DEFAULT_IMAGE
        with DiscReader(DEFAULT_IMAGE) as disc:
            if Dol(disc.read_dol()).u32(HOOK) != ORIGINAL:
                raise ValueError("original chapter-loader hook signature mismatch")
        name = f"FIXTURE-LOADER synthetic internal chapter {source_chapter} to {chapter}"
        sections.setdefault("Gecko",[]).extend(["$"+name,*c2_lines(HOOK,words(source_chapter,chapter))])
        sections.setdefault("Gecko_Enabled",[]).append("$"+name)
    text = "# Synthetic fixture bootstrap only; never a production configuration.\n"
    text += "\n".join("[" + k + "]\n" + "\n".join(v) for k, v in sections.items()) + "\n"
    size = validate_ini(text, dolphin=dolphin)
    # Exclusive directory reservation; no force option. Card input is read-only.
    root.mkdir(parents=True, exist_ok=False)
    make_user(root / "User", (dolphin / "Games").resolve(), "Synthetic fixture",
              PORT1_KEYBOARD, text, pad2=keyboard_layout(_KEYS))
    if card_bytes is not None:
        with (root / "User/GC/USA/Card A" / card.name).open("xb") as stream:
            stream.write(card_bytes)
    entry = ("Boot this private profile and load Restart Chapter from its copied card"
             if card_bytes is not None else
             "Boot this private profile, choose New Game and finish the original Prologue")
    manifest = {"classification": "synthetic_chapter_redirect", "internal_target": chapter,
                "internal_source": source_chapter,
                "redirect_kind": redirect_kind,
                "status": "NOT TESTED", "gecko_bytes": size,
                "card": None if card_bytes is None else {
                    "source": str(card.resolve()), "sha256": hashlib.sha256(card_bytes).hexdigest(),
                    "size": len(card_bytes), "history": "not certified; supplied source chapter is unverified",
                    "validation": "GFEE01 directory identity only; no checksum or content rewriting"},
                "source": ("EXP-05 / TESTING.md; original state+0x10 chapter field (F-12)"
                           if redirect_kind == "ar" else "CAMP-010 original chapter-script selection hook; candidate only"),
                "procedure": [entry,
                              f"The conditional {redirect_kind} seed redirects internal chapter {source_chapter} to the target",
                              "Save only to this disposable private card if the original game permits",
                              "Capture state and snapshot; inspect map, roster, flags and live hooks",
                              "Disable the FIXTURE setup code in this private INI before further progression",
                              "Test the target event through original gameplay; do not set its completion flag"],
                "limitations": ["No natural roster, recruitment, inventory, supports or story history",
                                "Target cutscenes may softlock or lack mandatory characters/items",
                                "Only source2->destination10 has historical redirect evidence; every new route is NOT TESTED",
                                "A mid-battle chapter-byte write is not a valid loader redirect (EXP-03)",
                                "Cannot certify natural chapter completion, transition or Netplay"]}
    (root / "fixture.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, required=True)
    p.add_argument("--target", type=int, required=True, help="internal ID; Ch6=7, Ch10=11, Ch17=18, Endgame=31")
    p.add_argument("--source-chapter", type=int, default=2, help="internal source ID; requires --card unless 2")
    p.add_argument("--card", type=Path, help="read-only native GCI input to COPY into the new profile")
    p.add_argument("--redirect-kind",choices=("ar","loader-hook"),default="ar",
                   help="loader-hook is an unverified candidate at original script selection; AR restart7->11 failed")
    a = p.parse_args()
    result = create(a.root, a.target, source_chapter=a.source_chapter, card=a.card,redirect_kind=a.redirect_kind)
    print(f"created {a.root}; target {a.target}; {result['gecko_bytes']} Gecko bytes; NOT TESTED")
