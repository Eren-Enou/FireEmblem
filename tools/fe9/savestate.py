"""Read-only decoder for Dolphin save states (.sNN), enough to read GameCube MEM1.

Format (Dolphin Source/Core/Core/State.h/.cpp, STATE_VERSION 192, verified on a
Dolphin 2609a state):
  0x00 legacy header (24 bytes): game id[6], pad[2], u32 lzo_size (0), pad[4], f64 time
  0x18 u32 version cookie (0xBAADBABE + STATE_VERSION), u32 version string length, string
  then extended header (16 bytes): u16 header version, u16 compression (0 none, 1 LZ4),
       u32 payload offset, u64 uncompressed size
  then payload: LZ4 = repeated (s32 compressed length, LZ4 block) until uncompressed size.
All header integers are little endian (host order).

MEM1 is located inside the decompressed payload by searching for a known main.dol code
sequence, because the offset depends on the state version and video backend.
"""

from __future__ import annotations

import struct
from dataclasses import dataclass
from pathlib import Path

import lz4.block

COOKIE_BASE = 0xBAADBABE
MEM1_BASE = 0x80000000
MEM1_SIZE = 0x01800000


@dataclass
class StateInfo:
    game_id: str
    state_version: int
    dolphin_version: str
    compression: int
    uncompressed_size: int


def read_state(path: Path) -> tuple[StateInfo, bytes]:
    data = Path(path).read_bytes()
    game_id = data[0:6].decode("ascii", errors="replace")
    lzo_size = struct.unpack_from("<I", data, 8)[0]
    if lzo_size:
        raise ValueError("legacy LZO save state not supported")
    cookie, vlen = struct.unpack_from("<II", data, 0x18)
    version = data[0x20:0x20 + vlen].decode("ascii", errors="replace")
    off = 0x20 + vlen
    _hver, compression, payload_off, usize = struct.unpack_from("<HHIQ", data, off)
    off += 16 + payload_off
    info = StateInfo(game_id, cookie - COOKIE_BASE, version, compression, usize)
    if compression == 0:
        return info, data[off:off + usize]
    if compression != 1:
        raise ValueError(f"unknown compression type {compression}")
    out = bytearray()
    while len(out) < usize:
        (clen,) = struct.unpack_from("<i", data, off)
        off += 4
        if clen <= 0:
            raise ValueError("bad LZ4 chunk length")
        chunk_max = min(0x7E000000, usize - len(out))
        out += lz4.block.decompress(data[off:off + clen], uncompressed_size=chunk_max)
        off += clen
    if len(out) != usize:
        raise ValueError("payload size mismatch")
    return info, bytes(out)


def write_state(src: Path, dst: Path, payload: bytes) -> None:
    """Write a copy of state `src` with a replaced (same-size) payload, LZ4-compressed like Dolphin."""
    data = Path(src).read_bytes()
    (vlen,) = struct.unpack_from("<I", data, 0x1C)
    hdr_end = 0x20 + vlen
    _hver, _comp, payload_off, usize = struct.unpack_from("<HHIQ", data, hdr_end)
    if len(payload) != usize:
        raise ValueError("payload size must not change")
    head = bytearray(data[:hdr_end + 16 + payload_off])
    struct.pack_into("<H", head, hdr_end + 2, 1)  # LZ4
    out = bytearray(head)
    pos = 0
    while pos < len(payload):
        chunk = payload[pos:pos + 0x7E000000]
        comp = lz4.block.compress(chunk, store_size=False)
        out += struct.pack("<i", len(comp)) + comp
        pos += len(chunk)
    Path(dst).write_bytes(out)


class Mem1:
    """GameCube MEM1 view (big endian) located inside a decompressed state payload."""

    def __init__(self, payload: bytes, anchor_addr: int, anchor_bytes: bytes):
        pos = payload.find(anchor_bytes)
        if pos < 0:
            raise ValueError("anchor not found; state does not match this main.dol")
        if payload.find(anchor_bytes, pos + 1) >= 0:
            raise ValueError("anchor is ambiguous")
        self.offset = pos - (anchor_addr - MEM1_BASE)
        self.data = payload[self.offset:self.offset + MEM1_SIZE]

    def read(self, addr: int, size: int) -> bytes:
        o = addr - MEM1_BASE
        return self.data[o:o + size]

    def u8(self, addr: int) -> int:
        return self.data[addr - MEM1_BASE]

    def u16(self, addr: int) -> int:
        return struct.unpack_from(">H", self.data, addr - MEM1_BASE)[0]

    def u32(self, addr: int) -> int:
        return struct.unpack_from(">I", self.data, addr - MEM1_BASE)[0]

    def cstr(self, addr: int, limit: int = 64) -> str:
        raw = self.read(addr, limit)
        return raw.split(b"\0")[0].decode("ascii", errors="replace")
