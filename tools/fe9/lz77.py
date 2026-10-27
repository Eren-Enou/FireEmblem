"""Nintendo LZ77 (type 0x10) codec as used by FE9 .cmp files.

Format (verified against zmap/bmap10/dispos.cmp of GFEE01, see docs/RESEARCH.md):
  byte 0      : 0x10
  bytes 1..3  : decompressed size, little endian
  then blocks : one flag byte (MSB first), each bit 0 = literal byte,
                1 = back-reference (2 bytes: LLLL DDDD DDDDDDDD,
                length = L + 3, distance = D + 1)
"""

from __future__ import annotations


class LZ77Error(ValueError):
    pass


def decompress(data: bytes) -> bytes:
    if len(data) < 4 or data[0] != 0x10:
        raise LZ77Error("not LZ77 type 0x10 data")
    size = data[1] | (data[2] << 8) | (data[3] << 16)
    out = bytearray()
    i = 4
    while len(out) < size:
        if i >= len(data):
            raise LZ77Error("truncated input")
        flags = data[i]
        i += 1
        for bit in range(8):
            if len(out) >= size:
                break
            if flags & (0x80 >> bit):
                if i + 1 >= len(data):
                    raise LZ77Error("truncated back-reference")
                b1, b2 = data[i], data[i + 1]
                i += 2
                length = (b1 >> 4) + 3
                dist = (((b1 & 0x0F) << 8) | b2) + 1
                if dist > len(out):
                    raise LZ77Error("back-reference before start of output")
                start = len(out) - dist
                for k in range(length):
                    out.append(out[start + k])
            else:
                out.append(data[i])
                i += 1
    return bytes(out[:size])


def compress(data: bytes) -> bytes:
    """Simple greedy compressor. Output is valid but not size-optimal."""
    if len(data) > 0xFFFFFF:
        raise LZ77Error("input too large")
    out = bytearray([0x10, len(data) & 0xFF, (len(data) >> 8) & 0xFF, (len(data) >> 16) & 0xFF])
    i = 0
    n = len(data)
    while i < n:
        flag_pos = len(out)
        out.append(0)
        flags = 0
        for bit in range(8):
            if i >= n:
                break
            best_len, best_dist = 0, 0
            max_len = min(18, n - i)
            if max_len >= 3:
                lo = max(0, i - 0x1000)
                # search window for the longest match
                j = data.rfind(data[i:i + 3], lo, i + 2)
                while j != -1 and j >= lo:
                    if j < i:
                        length = 3
                        while length < max_len and data[j + length] == data[i + length]:
                            length += 1
                        if length > best_len:
                            best_len, best_dist = length, i - j
                            if length == max_len:
                                break
                    j = data.rfind(data[i:i + 3], lo, j + 2) if j > lo else -1
            if best_len >= 3:
                flags |= 0x80 >> bit
                d = best_dist - 1
                out.append(((best_len - 3) << 4) | (d >> 8))
                out.append(d & 0xFF)
                i += best_len
            else:
                out.append(data[i])
                i += 1
        out[flag_pos] = flags
    return bytes(out)
