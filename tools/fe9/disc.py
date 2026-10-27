"""Read-only access to GameCube disc images (.iso or .ciso).

CISO layout: 'CISO' magic, u32 LE block size, then a 0x7FF8-byte map
(1 = block present, 0 = block absent/zero); present blocks follow the
0x8000-byte header in order.
GameCube disc header: 0x000 game ID (6), 0x007 revision, 0x020 internal name,
0x420 DOL offset, 0x424 FST offset, 0x428 FST size (all big endian).
"""

from __future__ import annotations

import struct
from pathlib import Path
from typing import BinaryIO

CISO_HEADER_SIZE = 0x8000


class DiscReader:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.f: BinaryIO = open(self.path, "rb")
        magic = self.f.read(4)
        self.block_map: list[int] | None = None
        if magic == b"CISO":
            (self.block_size,) = struct.unpack("<I", self.f.read(4))
            bmap = self.f.read(CISO_HEADER_SIZE - 8)
            self.block_map = []
            idx = 0
            for present in bmap:
                self.block_map.append(idx if present else -1)
                idx += 1 if present else 0
        self.f.seek(0)

    def close(self) -> None:
        self.f.close()

    def __enter__(self) -> "DiscReader":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    def read(self, offset: int, size: int) -> bytes:
        if self.block_map is None:
            self.f.seek(offset)
            return self.f.read(size)
        out = bytearray()
        while size > 0:
            block, within = divmod(offset, self.block_size)
            n = min(size, self.block_size - within)
            phys = self.block_map[block] if block < len(self.block_map) else -1
            if phys < 0:
                out += bytes(n)
            else:
                self.f.seek(CISO_HEADER_SIZE + phys * self.block_size + within)
                out += self.f.read(n)
            offset += n
            size -= n
        return bytes(out)

    # --- GameCube structures -------------------------------------------------

    def header(self) -> dict:
        h = self.read(0, 0x440)
        return {
            "game_id": h[0:6].decode("ascii"),
            "disc_number": h[6],
            "revision": h[7],
            "internal_name": h[0x20:0x60].split(b"\0")[0].decode("ascii", errors="replace"),
            "dol_offset": struct.unpack_from(">I", h, 0x420)[0],
            "fst_offset": struct.unpack_from(">I", h, 0x424)[0],
            "fst_size": struct.unpack_from(">I", h, 0x428)[0],
        }

    def read_dol(self) -> bytes:
        off = self.header()["dol_offset"]
        hdr = self.read(off, 0x100)
        offsets = struct.unpack_from(">18I", hdr, 0)
        sizes = struct.unpack_from(">18I", hdr, 0x90)
        size = max(o + s for o, s in zip(offsets, sizes))
        return self.read(off, size)

    def files(self) -> dict[str, tuple[int, int]]:
        """Return {path: (disc offset, size)} from the FST."""
        h = self.header()
        fst = self.read(h["fst_offset"], h["fst_size"])
        n = struct.unpack_from(">I", fst, 8)[0]
        names = fst[n * 12:]
        result: dict[str, tuple[int, int]] = {}
        stack: list[tuple[str, int]] = []  # (dir path, end index)

        def name_at(i: int) -> str:
            off = struct.unpack_from(">I", fst, i * 12)[0] & 0xFFFFFF
            return names[off:names.index(b"\0", off)].decode("ascii", errors="replace")

        for i in range(1, n):
            while stack and i >= stack[-1][1]:
                stack.pop()
            flags_name, a, b = struct.unpack_from(">III", fst, i * 12)
            prefix = stack[-1][0] if stack else ""
            path = prefix + name_at(i)
            if flags_name >> 24:
                stack.append((path + "/", b))
            else:
                result[path] = (a, b)
        return result

    def read_file(self, path: str) -> bytes:
        off, size = self.files()[path]
        return self.read(off, size)


def dol_sections(dol: bytes) -> list[tuple[str, int, int, int]]:
    """Return [(name, file offset, load address, size)] for non-empty DOL sections."""
    offsets = struct.unpack_from(">18I", dol, 0)
    addrs = struct.unpack_from(">18I", dol, 0x48)
    sizes = struct.unpack_from(">18I", dol, 0x90)
    out = []
    for i in range(18):
        if sizes[i]:
            name = f"text{i}" if i < 7 else f"data{i - 7}"
            out.append((name, offsets[i], addrs[i], sizes[i]))
    return out
