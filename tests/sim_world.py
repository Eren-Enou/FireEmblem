"""A small FE9 world for running generated caves in tools/fe9/ppc_sim (unit table, force lists, state, pads).

Layout follows RESEARCH.md: unit table 0x802B14E4 (0x280 per unit, id at +0x198, next +0x184, force object
pointer +0x190, flags +0x1A0, attributes +0x1BC), force objects 0x802CA264 + 0xC*f (head +0, id byte +8),
state block 0x80330708 (phase +0x11, turn +0x12, control +0x14+f), PADStatus 0x802EF408 (+12 per port).
"""

from __future__ import annotations

from tools.fe9.ppc_sim import Machine

UNIT_TABLE, FORCES, STATE, PADS = 0x802B14E4, 0x802CA264, 0x80330708, 0x802EF408
TRANSFER, HAS_ATTR, PLAY_SE, CURSOR_UNIT = 0x800BCA38, 0x80105BC0, 0x801475FC, 0x800AA794
OWNED, P2, PARKED, OFFER = 0x20000000, 0x40000000, 0x10000000, 0x08000000


def unit_addr(uid: int) -> int:
    return UNIT_TABLE + (uid - 1) * 0x280


class World(Machine):
    def __init__(self, phase: int = 0, turn: int = 1):
        super().__init__()
        self.lords: set[int] = set()
        self.cursor_unit = 0
        self.sounds: list[int] = []
        self.transfers: list[tuple[int, int]] = []
        for f in range(8):
            self.wb(FORCES + 0xC * f + 8, f)
        self.wb(STATE + 0x11, phase)
        self.wh(STATE + 0x12, turn)
        for f, c in enumerate((1, 2, 2, 2)):
            self.wb(STATE + 0x14 + f, c)
        self.stubs[TRANSFER] = self._transfer
        self.stubs[HAS_ATTR] = self._has_attr
        self.stubs[PLAY_SE] = lambda m: m.sounds.append(m.r[3])
        self.stubs[CURSOR_UNIT] = lambda m: m.r.__setitem__(3, m.cursor_unit)

    # --- units and force lists ---
    def add_unit(self, uid: int, force: int, flags: int = 0, lord: bool = False) -> int:
        u = unit_addr(uid)
        self.wb(u + 0x198, uid)
        self.ww(u + 0x1A0, flags)
        if lord:
            self.lords.add(uid)
        self._link(u, force)
        return u

    def _link(self, u: int, force: int) -> None:
        head = FORCES + 0xC * force
        tail, nxt = 0, self.rw(head)
        while nxt:
            tail, nxt = nxt, self.rw(nxt + 0x184)
        if tail:
            self.ww(tail + 0x184, u)
        else:
            self.ww(head, u)
        self.ww(u + 0x184, 0)
        self.ww(u + 0x190, head)

    def _unlink(self, u: int) -> None:
        head = self.rw(u + 0x190)
        prev, cur = 0, self.rw(head)
        while cur and cur != u:
            prev, cur = cur, self.rw(cur + 0x184)
        if cur:
            nxt = self.rw(u + 0x184)
            if prev:
                self.ww(prev + 0x184, nxt)
            else:
                self.ww(head, nxt)

    def _has_attr(self, m: "World") -> None:
        """0x80105BC0(unit+0x1BC, index): attribute 0 = the lord (Ike) in this model."""
        is_lord = (m.r[3] - 0x1BC) & 0xFFFFFFFF in {unit_addr(u) for u in m.lords}
        m.r[3] = 1 if is_lord and m.r[4] == 0 else 0

    def _transfer(self, m: "World") -> None:
        uid, force = m.r[3] & 0xFF, m.r[4]
        u = unit_addr(uid)
        self.transfers.append((uid, force))
        self._unlink(u)
        self._link(u, force)

    def force_of(self, uid: int) -> int:
        return self.rb(self.rw(unit_addr(uid) + 0x190) + 8)

    def flags(self, uid: int) -> int:
        return self.rw(unit_addr(uid) + 0x1A0)

    def members(self, force: int) -> list[int]:
        out, cur = [], self.rw(FORCES + 0xC * force)
        while cur:
            out.append(self.rb(cur + 0x198))
            cur = self.rw(cur + 0x184)
        return out

    # --- input and state ---
    def press(self, port: int, buttons: int) -> None:
        self.wh(PADS + 12 * port, buttons)

    def release_all(self) -> None:
        for p in range(4):
            self.wh(PADS + 12 * p, 0)

    def control(self, force: int) -> int:
        return self.rb(STATE + 0x14 + force)
