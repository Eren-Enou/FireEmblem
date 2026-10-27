"""Identify and checksum a Fire Emblem: Path of Radiance disc image (read-only).

Prints game ID, revision, internal name, file size and hashes of
  * the image file as stored (.ciso hashes are format-specific), and
  * main.dol (format-independent, the anchor for every code/address in docs/RESEARCH.md).
Exit code is non-zero if the image is not GFEE01 rev 0 or the main.dol SHA-1 differs
from the reference recorded in docs/RESEARCH.md.

Usage: python -m tools.verify_game [path] [--skip-file-hash]
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import zlib
from pathlib import Path

from tools.fe9.disc import DiscReader

DEFAULT_IMAGE = Path("Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso")
EXPECTED_ID = "GFEE01"
EXPECTED_REVISION = 0
# Reference main.dol SHA-1 for GFEE01 rev 0 (recorded 2026-10-26, see docs/RESEARCH.md).
EXPECTED_DOL_SHA1 = "9d00d7d407750b82cb1cfccc56f8aa8a89cc8851"


def hash_file(path: Path) -> dict[str, str]:
    md5, sha1, crc = hashlib.md5(), hashlib.sha1(), 0
    with open(path, "rb") as f:
        while chunk := f.read(1 << 22):
            md5.update(chunk)
            sha1.update(chunk)
            crc = zlib.crc32(chunk, crc)
    return {"crc32": f"{crc:08x}", "md5": md5.hexdigest(), "sha1": sha1.hexdigest()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("image", nargs="?", type=Path, default=DEFAULT_IMAGE)
    ap.add_argument("--skip-file-hash", action="store_true", help="skip hashing the whole image file")
    args = ap.parse_args()

    ok = True
    with DiscReader(args.image) as disc:
        h = disc.header()
        dol = disc.read_dol()
        fmt = "CISO" if disc.block_map is not None else "ISO"
    dol_sha1 = hashlib.sha1(dol).hexdigest()

    print(f"image          : {args.image}")
    print(f"format         : {fmt}")
    print(f"file size      : {args.image.stat().st_size}")
    print(f"game id        : {h['game_id']}")
    print(f"revision       : {h['revision']}")
    print(f"internal name  : {h['internal_name']}")
    print(f"main.dol size  : {len(dol)}")
    print(f"main.dol sha1  : {dol_sha1}")
    print(f"main.dol crc32 : {zlib.crc32(dol):08x}")
    if not args.skip_file_hash:
        for k, v in hash_file(args.image).items():
            print(f"file {k:<9} : {v}")

    if h["game_id"] != EXPECTED_ID or h["revision"] != EXPECTED_REVISION:
        print(f"MISMATCH: expected {EXPECTED_ID} rev {EXPECTED_REVISION}", file=sys.stderr)
        ok = False
    if EXPECTED_DOL_SHA1 and dol_sha1 != EXPECTED_DOL_SHA1:
        print("MISMATCH: main.dol differs from the reference build; addresses in docs may not apply",
              file=sys.stderr)
        ok = False
    print("RESULT         :", "OK" if ok else "MISMATCH")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
