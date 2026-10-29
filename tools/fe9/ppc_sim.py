"""A tiny PowerPC interpreter for behavioural tests of the generated Gecko caves (no Dolphin needed).

It runs one C2 cave as Dolphin would: the cave is placed at CAVE_BASE, execution starts at its first word, and
reaching the final 0x00000000 slot (Gecko's branch back to hook+4) ends the run. Calls through `mtctr/bctrl`
to game functions are answered by Python stubs. Any other call target, or any instruction outside the subset
the generators emit, raises SimError, so a test can't silently pass over unmodelled behaviour.

Memory is sparse big-endian (unwritten bytes read as 0). Only the integer subset is modelled.
"""

from __future__ import annotations

import struct
from typing import Callable

CAVE_BASE = 0x81700000
STACK_TOP = 0x817F0000


class SimError(Exception):
    pass


class Machine:
    def __init__(self):
        self.mem: dict[int, int] = {}
        self.r = [0] * 32
        self.r[1] = STACK_TOP
        self.cr0 = (False, False, False)          # lt, gt, eq
        self.lr = 0
        self.ctr = 0
        self.stubs: dict[int, Callable[["Machine"], None]] = {}
        self.calls: list[tuple[int, tuple[int, ...]]] = []   # (target, (r3, r4, r5)) of every stubbed call
        self.steps = 0

    # --- memory ---
    def rb(self, a: int) -> int: return self.mem.get(a & 0xFFFFFFFF, 0)
    def wb(self, a: int, v: int) -> None: self.mem[a & 0xFFFFFFFF] = v & 0xFF
    def rh(self, a: int) -> int: return (self.rb(a) << 8) | self.rb(a + 1)
    def wh(self, a: int, v: int) -> None: self.wb(a, v >> 8); self.wb(a + 1, v)
    def rw(self, a: int) -> int: return (self.rh(a) << 16) | self.rh(a + 2)
    def ww(self, a: int, v: int) -> None: self.wh(a, (v >> 16) & 0xFFFF); self.wh(a + 2, v & 0xFFFF)
    def write_bytes(self, a: int, data: bytes) -> None:
        for i, b in enumerate(data):
            self.wb(a + i, b)

    # --- load once, run many times (like Dolphin: data words inside a cave persist between runs) ---
    def load(self, words: list[int]) -> None:
        if words[-1] != 0:
            raise SimError("cave must end with the 0x00000000 branch-back slot")
        for i, w in enumerate(words):
            self.ww(CAVE_BASE + 4 * i, w)
        self._end = CAVE_BASE + 4 * (len(words) - 1)

    def load_code(self, blocks: list[tuple[int, list[int]]]) -> list[int]:
        """Lay out a whole Gecko code (several C2 blocks) as Dolphin writes it: each block is an 8-byte C2
        header followed by its cave. Returns each cave's start; run_block(i) then runs block i."""
        self._blocks, addr = [], CAVE_BASE
        for _hook, words in blocks:
            if words[-1] != 0:
                raise SimError("cave must end with the 0x00000000 branch-back slot")
            addr += 8                                             # the C2 header line
            for i, w in enumerate(words):
                self.ww(addr + 4 * i, w)
            self._blocks.append((addr, addr + 4 * (len(words) - 1)))
            addr += 4 * len(words)
        self._region = (CAVE_BASE, addr)
        return [s for s, _e in self._blocks]

    EXIT_LR = 0x81FFFFF0          # sentinel return address: a blr to it means "returned to the caller"

    def run_block(self, i: int, max_steps: int = 200000) -> bool:
        """Run block i. Returns True if it left through the normal branch-back slot, False if it returned
        straight to its caller with blr (e.g. a hook that refuses and returns a value itself)."""
        start, end = self._blocks[i]
        self.lr = self.EXIT_LR
        return self._exec(start, end, self._region, max_steps)

    def run(self, words: list[int] | None = None, max_steps: int = 200000) -> None:
        if words is not None:
            self.load(words)
        self._exec(CAVE_BASE, self._end, (CAVE_BASE, self._end), max_steps)

    def _exec(self, pc: int, end: int, region: tuple[int, int], max_steps: int) -> bool:
        while pc != end:
            if pc == self.EXIT_LR:
                return False
            self.steps += 1
            if self.steps > max_steps:
                raise SimError("step limit (infinite loop?)")
            if not region[0] <= pc < region[1]:
                raise SimError(f"pc left the code: {pc:08X}")
            pc = self._step(pc, self.rw(pc))
        return True

    # --- helpers ---
    def _set_cr0(self, a: int, b: int, signed: bool = True) -> None:
        if signed:
            a = a - (1 << 32) if a & 0x80000000 else a
            b = b - (1 << 32) if b & 0x80000000 else b
        self.cr0 = (a < b, a > b, a == b)

    def _rec(self, v: int) -> None:
        self._set_cr0(v & 0xFFFFFFFF, 0)

    def _cond(self, bo: int, bi: int) -> bool:
        if bi > 2:
            raise SimError(f"condition bit {bi} not modelled")
        if bo == 20:
            return True
        if bo == 12:
            return self.cr0[bi]
        if bo == 4:
            return not self.cr0[bi]
        raise SimError(f"BO {bo} not modelled")

    def _call(self, target: int) -> None:
        stub = self.stubs.get(target)
        if stub is None:
            raise SimError(f"call to unstubbed {target:08X}")
        self.calls.append((target, (self.r[3], self.r[4], self.r[5])))
        stub(self)
        for v in (0, 5, 6, 7, 8, 9, 10, 11, 12):       # volatile registers are not preserved by callees
            self.r[v] = 0xDEAD0000 + v

    def _step(self, pc: int, w: int) -> int:
        r = self.r
        op = w >> 26
        d, a, b = (w >> 21) & 31, (w >> 16) & 31, (w >> 11) & 31
        uimm = w & 0xFFFF
        simm = uimm - 0x10000 if uimm & 0x8000 else uimm
        ra0 = r[a] if a else 0
        ea = (ra0 + simm) & 0xFFFFFFFF
        M = 0xFFFFFFFF
        if op == 14: r[d] = (ra0 + simm) & M                               # addi / li
        elif op == 15: r[d] = (ra0 + (simm << 16)) & M                     # addis / lis
        elif op == 24: r[a] = r[d] | uimm                                  # ori (rs in d)
        elif op == 25: r[a] = r[d] | (uimm << 16)                          # oris
        elif op == 26: r[a] = r[d] ^ uimm                                  # xori
        elif op == 27: r[a] = r[d] ^ (uimm << 16)                          # xoris
        elif op == 28: r[a] = r[d] & uimm; self._rec(r[a])                 # andi.
        elif op == 29: r[a] = r[d] & (uimm << 16); self._rec(r[a])         # andis.
        elif op == 7: r[d] = (_s(r[a]) * simm) & M                         # mulli (rA = r0 is r0, not 0)
        elif op == 8: r[d] = (simm - _s(r[a])) & M                         # subfic
        elif op == 11: self._set_cr0(r[a], simm & M)                       # cmpwi (crf 0 only)
        elif op == 10: self._set_cr0(r[a], uimm, signed=False)             # cmplwi
        elif op == 32: r[d] = self.rw(ea)                                  # lwz
        elif op == 34: r[d] = self.rb(ea)                                  # lbz
        elif op == 40: r[d] = self.rh(ea)                                  # lhz
        elif op == 42: h = self.rh(ea); r[d] = (h - 0x10000 if h & 0x8000 else h) & M   # lha
        elif op == 36: self.ww(ea, r[d])                                   # stw
        elif op == 37: self.ww(ea, r[d]); r[a] = ea                        # stwu
        elif op == 38: self.wb(ea, r[d])                                   # stb
        elif op == 44: self.wh(ea, r[d])                                   # sth
        elif op == 47:                                                      # stmw
            for k in range(d, 32): self.ww(ea + 4 * (k - d), r[k])
        elif op == 46:                                                      # lmw
            for k in range(d, 32): r[k] = self.rw(ea + 4 * (k - d))
        elif op == 21:                                                      # rlwinm[.]
            sh, mb, me = b, (w >> 6) & 31, (w >> 1) & 31
            v = ((r[d] << sh) | (r[d] >> (32 - sh))) & M if sh else r[d]
            r[a] = v & _mask(mb, me)
            if w & 1: self._rec(r[a])
        elif op == 18:                                                      # b / bl
            off = w & 0x3FFFFFC
            off = off - 0x4000000 if off & 0x2000000 else off
            if w & 2: raise SimError("absolute branch")
            if w & 1: self.lr = pc + 4
            return (pc + off) & M
        elif op == 16:                                                      # bc
            off = w & 0xFFFC
            off = off - 0x10000 if off & 0x8000 else off
            if w & 3: raise SimError("bc with AA/LK not modelled")
            return (pc + off) & M if self._cond(d, a) else pc + 4
        elif op == 19:
            xo = (w >> 1) & 0x3FF
            if xo == 528 and d == 20:                                       # bctr / bctrl
                if w & 1:
                    self._call(self.ctr)
                    return pc + 4
                raise SimError(f"bctr to {self.ctr:08X} (tail jump out of the cave)")
            if xo == 16 and d == 20 and not (w & 1):                        # blr (return from a local routine)
                return self.lr
            raise SimError(f"op19 xo {xo}")
        elif op == 31:
            xo = (w >> 1) & 0x3FF
            if xo == 444: r[a] = r[d] | r[b]                               # or / mr
            elif xo == 28: r[a] = r[d] & r[b]; (w & 1) and self._rec(r[a])  # and
            elif xo == 40: r[d] = (r[b] - r[a]) & M                        # subf
            elif xo == 266: r[d] = (r[a] + r[b]) & M                       # add
            elif xo == 954: v = r[d] & 0xFF; r[a] = (v - 0x100 if v & 0x80 else v) & M   # extsb
            elif xo == 0: self._set_cr0(r[a], r[b])                        # cmpw
            elif xo == 32: self._set_cr0(r[a], r[b], signed=False)         # cmplw
            elif xo == 23: r[d] = self.rw((ra0 + r[b]) & M)                # lwzx
            elif xo == 87: r[d] = self.rb((ra0 + r[b]) & M)                # lbzx
            elif xo == 279: r[d] = self.rh((ra0 + r[b]) & M)               # lhzx
            elif xo == 215: self.wb((ra0 + r[b]) & M, r[d])                # stbx
            elif xo == 339 and ((w >> 11) & 0x3FF) == 0x100: r[d] = self.lr   # mflr
            elif xo == 467 and ((w >> 11) & 0x3FF) == 0x100: self.lr = r[d]   # mtlr
            elif xo == 467 and ((w >> 11) & 0x3FF) == 0x120: self.ctr = r[d]  # mtctr
            else: raise SimError(f"op31 xo {xo} at {pc:08X}")
        elif w == 0x60000000:
            pass
        else:
            raise SimError(f"instruction {w:08X} at {pc:08X} not modelled")
        return pc + 4


def _s(v: int) -> int:
    return v - (1 << 32) if v & 0x80000000 else v


def _mask(mb: int, me: int) -> int:
    m, i = 0, mb
    while True:
        m |= 1 << (31 - i)
        if i == me:
            return m
        i = (i + 1) % 32


def words_be(data: bytes) -> list[int]:
    return list(struct.unpack(f">{len(data) // 4}I", data))
