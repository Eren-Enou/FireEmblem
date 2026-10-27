"""Small static-analysis helpers for the GameCube main.dol (PowerPC, big endian)."""

from __future__ import annotations

import struct

import capstone

from .disc import dol_sections


class Dol:
    def __init__(self, data: bytes):
        self.data = data
        self.sections = dol_sections(data)
        self.md = capstone.Cs(capstone.CS_ARCH_PPC, capstone.CS_MODE_32 | capstone.CS_MODE_BIG_ENDIAN)

    def addr_to_off(self, addr: int) -> int | None:
        for _name, off, base, size in self.sections:
            if base <= addr < base + size:
                return off + addr - base
        return None

    def text_words(self):
        """Yield (address, instruction word) for every word in text sections."""
        for name, off, base, size in self.sections:
            if not name.startswith("text"):
                continue
            for k in range(0, size, 4):
                yield base + k, struct.unpack_from(">I", self.data, off + k)[0]

    def u32(self, addr: int) -> int:
        return struct.unpack_from(">I", self.data, self.addr_to_off(addr))[0]

    def disasm(self, addr: int, count: int) -> list[str]:
        off = self.addr_to_off(addr)
        code = self.data[off:off + 4 * count]
        lines = []
        for insn in self.md.disasm(code, addr):
            word = struct.unpack_from(">I", code, insn.address - addr)[0]
            lines.append(f"{insn.address:08X}  {word:08X}  {insn.mnemonic} {insn.op_str}")
        return lines
