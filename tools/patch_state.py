"""Write a NEW save state that is a copy of an existing one with some MEM1 bytes changed.

The source state is only read. The output must not exist yet (no overwrites).

Usage:
  python -m tools.patch_state SRC.sNN DST.sNN --set 80330718=09 [--set ADDR=HEXBYTES ...]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from tools.fe9.savestate import MEM1_BASE, MEM1_SIZE, read_state, write_state
from tools.inspect_state import load_mem1
from tools.verify_game import DEFAULT_IMAGE


def apply_edits(payload: bytes, mem1_offset: int, specifications: list[str]):
    """Validate every edit before changing a copy of a complete MEM1 payload.

    Dolphin state payloads include non-RAM emulator state. Negative slices and
    out-of-range writes must never redirect a MEM1 edit into those other fields.
    Overlapping edits are rejected so each recorded old value is unambiguous.
    """
    if mem1_offset < 0 or mem1_offset + MEM1_SIZE > len(payload):
        raise ValueError("state payload does not contain a complete MEM1 range")
    edits = []
    for item in specifications:
        try:
            address, hexbytes = item.split("=", 1)
            address, value = int(address, 16), bytes.fromhex(hexbytes)
        except ValueError as exc:
            raise ValueError(f"invalid MEM1 edit: {item!r}") from exc
        if not value or address < MEM1_BASE or address + len(value) > MEM1_BASE + MEM1_SIZE:
            raise ValueError(f"edit outside MEM1 or empty: {item!r}")
        if any(address < a + len(v) and a < address + len(value) for a, _, v in edits):
            raise ValueError("overlapping MEM1 edits")
        pos = mem1_offset + address - MEM1_BASE
        edits.append((address, payload[pos:pos + len(value)], value))
    result = bytearray(payload)
    for address, _, value in edits:
        pos = mem1_offset + address - MEM1_BASE
        result[pos:pos + len(value)] = value
    return bytes(result), edits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src", type=Path)
    ap.add_argument("dst", type=Path)
    ap.add_argument("--set", action="append", required=True, metavar="ADDR=HEX")
    ap.add_argument("--image", type=Path, default=DEFAULT_IMAGE)
    args = ap.parse_args()

    if args.dst.exists():
        print(f"refusing to overwrite {args.dst}", file=sys.stderr)
        return 1
    if args.dst.resolve() == args.src.resolve():
        print("dst must differ from src", file=sys.stderr)
        return 1
    manifest = Path(str(args.dst) + ".json")
    if manifest.exists():
        print(f"refusing to overwrite fixture manifest {manifest}", file=sys.stderr)
        return 1

    info, m = load_mem1(args.src, args.image)
    _info, payload = read_state(args.src)
    try:
        payload, edits = apply_edits(payload, m.offset, args.set)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    args.dst.parent.mkdir(parents=True, exist_ok=True)
    write_state(args.src, args.dst, payload)

    # verify by decoding the written file
    _info, m2 = load_mem1(args.dst, args.image)
    for addr, old, val in edits:
        got = m2.read(addr, len(val))
        status = "OK" if got == val else "FAILED"
        print(f"{status} {addr:08X}: {old.hex()} -> {got.hex()}")
        if got != val:
            return 1
    with manifest.open("x", encoding="utf-8") as stream:
        json.dump({"classification": "synthetic_state_edit", "source": str(args.src.resolve()),
                   "source_sha256": hashlib.sha256(args.src.read_bytes()).hexdigest(),
                   "output_sha256": hashlib.sha256(args.dst.read_bytes()).hexdigest(),
                   "game_id": info.game_id, "dolphin": info.dolphin_version,
                   "edits": [{"address": f"{a:08X}", "old": old.hex(), "new": new.hex()}
                             for a, old, new in edits],
                   "acceptance": "NOT TESTED",
                   "limitations": ["RAM edits do not establish original story flags or roster history",
                                   "a chapter redirect does not reproduce natural progression",
                                   "state-carried executable hooks may differ from profile INI"]}, stream, indent=2)
    print(f"wrote {args.dst} and {manifest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
