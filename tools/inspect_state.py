"""Decode an FE9 Dolphin save state and print battle-map state, forces and units (read-only).

Usage: python -m tools.inspect_state <state.sNN> [--image path.ciso]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from tools.fe9.disc import DiscReader
from tools.fe9.ppc import Dol
from tools.fe9.savestate import Mem1, read_state
from tools.verify_game import DEFAULT_IMAGE

# Addresses: docs/RESEARCH.md section 4 (GFEE01 rev 0)
STATE = 0x80330708        # battle-map state block
FORCES = 0x802CA264       # force table, 0xC per force
UNITS = 0x802B14E4        # unit table, 0x280 per unit, ids 1..0x9F
ANCHOR = 0x8014D920       # main.dol code used to locate MEM1 inside the state payload
FORCE_NAMES = {0: "blue/player", 1: "red/enemy", 2: "green/other", 3: "yellow/partner"}
CONTROL_NAMES = {0: "none", 1: "human", 2: "CPU"}


def load_mem1(state_path: Path, image: Path) -> tuple[object, Mem1]:
    info, payload = read_state(state_path)
    with DiscReader(image) as disc:
        dol = Dol(disc.read_dol())
    off = dol.addr_to_off(ANCHOR)
    return info, Mem1(payload, ANCHOR, dol.data[off:off + 0x60])


def describe(m: Mem1) -> list[str]:
    def s(ptr: int) -> str:
        return m.cstr(ptr) if 0x80000000 <= ptr < 0x81800000 else "?"

    lines = [
        f"chapter id (state+0x10, hypothesis) : {m.u8(STATE + 0x10)}",
        f"phase (state+0x11)                  : {m.u8(STATE + 0x11)}",
        f"turn (state+0x12)                   : {m.u16(STATE + 0x12)}",
        "control (0x8033071C..F)             : "
        + ", ".join(f"f{f}={v}({CONTROL_NAMES.get(v, '?')})" for f, v in enumerate(m.read(STATE + 0x14, 4))),
        "forces:",
    ]
    for f in range(8):
        base = FORCES + 0xC * f
        lines.append(f"  force {f} @{base:08X} first={m.u32(base):08X} id={m.u8(base + 8)}")
    lines.append("units (id, force, PID, JID, x,y, hp, flags@1A0):")
    for i in range(1, 0xA0):
        u = UNITS + (i - 1) * 0x280
        char = m.u32(u + 0x188)
        if not char:
            continue
        force_ptr = m.u32(u + 0x190)
        fid = m.u8(force_ptr + 8) if force_ptr else -1
        jptr = m.u32(u + 0x18C)
        lines.append(
            f"  {i:3d} {FORCE_NAMES.get(fid, fid)!s:<15} {s(m.u32(char)):<20} "
            f"{s(m.u32(jptr)) if jptr else '':<20} ({m.u8(u + 0x19E)},{m.u8(u + 0x19F)}) "
            f"hp={m.u8(u + 0x1A8)} flags={m.u32(u + 0x1A0):08X}"
        )
    return lines


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("state", type=Path)
    ap.add_argument("--image", type=Path, default=DEFAULT_IMAGE)
    args = ap.parse_args()
    info, m = load_mem1(args.state, args.image)
    print(f"{args.state}: {info.game_id}, state v{info.state_version}, {info.dolphin_version}, "
          f"MEM1 at payload+0x{m.offset:X}")
    print("\n".join(describe(m)))


if __name__ == "__main__":
    main()
