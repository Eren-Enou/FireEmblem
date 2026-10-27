"""Parser for FE9 dispos_*.bin unit-placement files (inside zmap/<map>/dispos.cmp).

Container layout (verified on GFEE01 zmap/bmap10/dispos_c.bin, see docs/RESEARCH.md):
  0x00 u32 file size
  0x04 u32 data size          (data section starts at 0x20)
  0x08 u32 relocation count   (table of u32 data offsets follows the data)
  0x0C u32 symbol count       (table of (u32 data offset, u32 name offset) follows relocs,
                               then the symbol-name string table)
  0x20 data section; all pointers in it are offsets relative to 0x20.

Each symbol except *_date_* names a unit group:
  +0x00 u8  unit count
  +0x01 u8[3] unknown (hypothesis: group type / faction flags -- UNVERIFIED)
  +0x04 entries, 0x6C bytes each:
        0x00 PID ptr, 0x04 JID ptr, 0x08 u32 (0 so far),
        0x0C 4x weapon IID ptr, 0x1C 4x item IID ptr,
        0x2C..0x4B unknown,
        0x4C..0x58 four AI/move pointers (SEQ_* x3, MTYPE_* x1) -- names observed, meaning unverified
        0x5C start (x, y), 0x5E final (x, y), 0x60.. unknown bytes
"""

from __future__ import annotations

import struct
from dataclasses import dataclass, field

DATA_BASE = 0x20
ENTRY_SIZE = 0x6C


@dataclass
class DisposUnit:
    offset: int  # offset within the dispos_*.bin file
    pid: str
    jid: str
    weapons: list[str]
    items: list[str]
    ai: list[str]
    start: tuple[int, int]
    end: tuple[int, int]
    raw: bytes


@dataclass
class DisposGroup:
    name: str
    offset: int
    header: bytes
    units: list[DisposUnit] = field(default_factory=list)


def _cstr(buf: bytes, off: int) -> str:
    return buf[off:buf.index(b"\0", off)].decode("ascii", errors="replace")


def _ptr_str(buf: bytes, ptr: int) -> str:
    return _cstr(buf, DATA_BASE + ptr) if ptr else ""


def parse(buf: bytes) -> tuple[str, list[DisposGroup]]:
    _size, data_size, nreloc, nsym = struct.unpack_from(">IIII", buf, 0)
    sym_table = DATA_BASE + data_size + 4 * nreloc
    str_table = sym_table + 8 * nsym
    symbols = []
    for k in range(nsym):
        off, name_off = struct.unpack_from(">II", buf, sym_table + 8 * k)
        symbols.append((_cstr(buf, str_table + name_off), off))

    date = ""
    groups = []
    for name, off in symbols:
        base = DATA_BASE + off
        if "_date" in name:
            date = _ptr_str(buf, struct.unpack_from(">I", buf, base)[0])
            continue
        count = buf[base]
        group = DisposGroup(name, base, buf[base:base + 4])
        for i in range(count):
            e = base + 4 + ENTRY_SIZE * i
            ptrs = struct.unpack_from(">IIIIIIIIIII", buf, e)
            ai_ptrs = struct.unpack_from(">IIII", buf, e + 0x4C)
            group.units.append(DisposUnit(
                offset=e,
                pid=_ptr_str(buf, ptrs[0]),
                jid=_ptr_str(buf, ptrs[1]),
                weapons=[_ptr_str(buf, p) for p in ptrs[3:7]],
                items=[_ptr_str(buf, p) for p in ptrs[7:11]],
                ai=[_ptr_str(buf, p) for p in ai_ptrs],
                start=(buf[e + 0x5C], buf[e + 0x5D]),
                end=(buf[e + 0x5E], buf[e + 0x5F]),
                raw=buf[e:e + ENTRY_SIZE],
            ))
        groups.append(group)
    return date, groups
