"""Reader for FE9 'pack' archives (the decompressed contents of .cmp files).

Layout (community notes, re-verified on bmap10/dispos.cmp):
  0x00  'pack'
  0x04  u16 file count (big endian), u16 padding
  0x08  per file, 0x10 bytes: u32 0, u32 name ptr, u32 data start, u32 length
All values big endian; pointers are absolute offsets in the pack.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass

from . import lz77


@dataclass
class PackEntry:
    name: str
    offset: int
    data: bytes


def _cstr(buf: bytes, off: int) -> str:
    end = buf.index(b"\0", off)
    return buf[off:end].decode("ascii", errors="replace")


def read_pack(raw: bytes) -> list[PackEntry]:
    if raw[:1] == b"\x10":
        raw = lz77.decompress(raw)
    if raw[:4] != b"pack":
        raise ValueError("missing 'pack' magic")
    (count,) = struct.unpack_from(">H", raw, 4)
    entries = []
    for k in range(count):
        _zero, name_ptr, start, length = struct.unpack_from(">IIII", raw, 8 + 0x10 * k)
        entries.append(PackEntry(_cstr(raw, name_ptr), start, raw[start:start + length]))
    return entries
