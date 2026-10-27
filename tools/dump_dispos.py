"""Print the unit groups of an FE9 dispos.cmp (read-only).

Usage: python -m tools.dump_dispos <path/to/dispos.cmp> [--variant c|h|m|n] [--raw]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from tools.fe9 import dispos, pack


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", type=Path)
    ap.add_argument("--variant", default="c", help="dispos_<variant>.bin to dump (c=common, h/m/n=difficulty)")
    ap.add_argument("--raw", action="store_true", help="also print unknown bytes 0x2C-0x4B and 0x60-0x6B")
    args = ap.parse_args()

    files = {e.name: e.data for e in pack.read_pack(args.path.read_bytes())}
    name = f"dispos_{args.variant}.bin"
    date, groups = dispos.parse(files[name])
    print(f"{args.path} :: {name}  (build date {date})")
    for g in groups:
        print(f"\n[{g.name}] @0x{g.offset:04X} header={g.header.hex(' ')} units={len(g.units)}")
        for u in g.units:
            weapons = ",".join(w for w in u.weapons + u.items if w)
            ai = ",".join(a for a in u.ai if a)
            print(f"  @0x{u.offset:04X} {u.pid:<18} {u.jid:<22} start={u.start} end={u.end} ai=[{ai}] items=[{weapons}]")
            if args.raw:
                print(f"      2C:{u.raw[0x2C:0x4C].hex(' ')}  60:{u.raw[0x60:0x6C].hex(' ')}")


if __name__ == "__main__":
    main()
