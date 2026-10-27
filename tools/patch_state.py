"""Write a NEW save state that is a copy of an existing one with some MEM1 bytes changed.

The source state is only read. The output must not exist yet (no overwrites).

Usage:
  python -m tools.patch_state SRC.sNN DST.sNN --set 80330718=09 [--set ADDR=HEXBYTES ...]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tools.fe9.savestate import MEM1_BASE, read_state, write_state
from tools.inspect_state import load_mem1
from tools.verify_game import DEFAULT_IMAGE


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

    _info, m = load_mem1(args.src, args.image)
    _info, payload = read_state(args.src)
    payload = bytearray(payload)
    edits = []
    for item in args.set:
        addr_s, val_s = item.split("=")
        addr, val = int(addr_s, 16), bytes.fromhex(val_s)
        pos = m.offset + addr - MEM1_BASE
        old = bytes(payload[pos:pos + len(val)])
        payload[pos:pos + len(val)] = val
        edits.append((addr, old, val))

    args.dst.parent.mkdir(parents=True, exist_ok=True)
    write_state(args.src, args.dst, bytes(payload))

    # verify by decoding the written file
    _info, m2 = load_mem1(args.dst, args.image)
    for addr, old, val in edits:
        got = m2.read(addr, len(val))
        status = "OK" if got == val else "FAILED"
        print(f"{status} {addr:08X}: {old.hex()} -> {got.hex()}")
        if got != val:
            return 1
    print(f"wrote {args.dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
