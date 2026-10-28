"""Small static-analysis helpers for the GameCube main.dol (PowerPC, big endian)."""

from __future__ import annotations

import struct

import capstone

from .disc import dol_sections


def direct_branch_target(address: int, word: int) -> int | None:
    """Decode PPC I-form b/bl, including AA, sign extension and 32-bit wrap.

    Conditional/indirect branches are intentionally outside this helper's scope.
    """
    if word >> 26 != 18:
        return None
    displacement = word & 0x03FFFFFC
    if displacement & 0x02000000:
        displacement -= 0x04000000
    return ((0 if word & 2 else address) + displacement) & 0xFFFFFFFF


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

    def direct_callers(self, target: int) -> list[int]:
        """Aligned text bl/bla sites only; absence says nothing about bctrl calls."""
        return [address for address, word in self.text_words()
                if word & 1 and direct_branch_target(address, word) == target]

    def disasm(self, addr: int, count: int) -> list[str]:
        off = self.addr_to_off(addr)
        code = self.data[off:off + 4 * count]
        lines = []
        for insn in self.md.disasm(code, addr):
            word = struct.unpack_from(">I", code, insn.address - addr)[0]
            lines.append(f"{insn.address:08X}  {word:08X}  {insn.mnemonic} {insn.op_str}")
        return lines
