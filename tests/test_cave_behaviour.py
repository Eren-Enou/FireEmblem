"""Behavioural tests: run the generated caves (EXP-21/22/25/26) in tools/fe9/ppc_sim against a synthetic world.

These check what the code *does* (claims, alternating picks, transfers, refusals, force moves), complementing
the disassembly tests in test_tools. They need no game image and no Dolphin.
"""

from __future__ import annotations

import unittest

from tests.sim_world import (OFFER, OWNED, P2, PLAY_SE, STATE, World, unit_addr)
from tools import draft_code as dc, prep_code as pc
from tools.fe9.ppc_sim import SimError

IKE, TITANIA, SOREN, RHYS, OSCAR, SHINON, LETHE = 1, 4, 24, 14, 2, 5, 23
Z, LR = 0x0010, 0x0060
LIST = 0x80A00000                 # synthetic E_SallyList proc / list object
ROWS = 0x80A10000                 # synthetic row records (0x24 each, unit pointer at +0)


def prep_world(order=(IKE, TITANIA, SOREN, RHYS, OSCAR), away=(SHINON,)) -> World:
    w = World(phase=0, turn=1)
    for uid in order:
        w.add_unit(uid, 0, lord=(uid == IKE))
    for uid in away:
        w.add_unit(uid, 7, flags=0x10)
    w.ww(LIST + 0x14, pc.SALLY_LIST_NAME)
    w.ww(LIST + 0x3C, ROWS)
    for i, uid in enumerate(list(order) + list(away)):
        w.ww(ROWS + 0x24 * i, unit_addr(uid))
    w.load(pc.prep_draft_cave())
    w.rows = list(order) + list(away)
    return w


def prep_press(w: World, port: int, uid: int) -> None:
    """Highlight `uid`, then one frame with Z held on `port`, then one frame released."""
    w.wb(LIST + 0x62, w.rows.index(uid))
    w.r[3] = LIST
    w.press(port, Z); w.run()
    w.release_all(); w.r[3] = LIST; w.run()


class PrepDraftBehaviour(unittest.TestCase):
    """EXP-26 in Choose Units (PREP-03's steps, executed)."""

    def test_claims_alternate_and_refusals_buzz(self):
        w = prep_world()
        prep_press(w, 0, TITANIA)
        self.assertEqual(w.flags(TITANIA), OWNED)
        prep_press(w, 0, SOREN)                                   # not Player 1's pick
        self.assertEqual(w.flags(SOREN), 0)
        self.assertEqual(w.sounds[-1], pc.SE26["miss"])
        prep_press(w, 1, SOREN)
        self.assertEqual(w.flags(SOREN), OWNED | P2)
        prep_press(w, 1, IKE)                                     # Ike stays Player 1
        self.assertEqual(w.flags(IKE), 0)
        self.assertEqual(w.sounds[-1], pc.SE26["miss"])
        prep_press(w, 0, SHINON)                                  # away (force 7): unavailable
        self.assertEqual(w.flags(SHINON), 0x10)
        self.assertEqual(w.sounds[-1], pc.SE26["miss"])
        self.assertEqual(w.transfers, [])                         # prep never changes forces
        self.assertEqual(w.sounds[:3], [pc.SE26["p1"], pc.SE26["miss"], pc.SE26["p2"]])

    def test_transfer_needs_both_players(self):
        w = prep_world()
        prep_press(w, 0, TITANIA); prep_press(w, 1, SOREN)
        prep_press(w, 1, TITANIA)                                 # Player 2 requests
        self.assertEqual(w.flags(TITANIA), OWNED | OFFER)
        self.assertEqual(w.sounds[-1], pc.SE26["request"])
        prep_press(w, 1, TITANIA)                                 # ... and cancels
        self.assertEqual(w.flags(TITANIA), OWNED)
        prep_press(w, 1, TITANIA); prep_press(w, 0, TITANIA)       # request, owner accepts
        self.assertEqual(w.flags(TITANIA), OWNED | P2)
        self.assertEqual(w.sounds[-1], pc.SE26["transfer"])

    def test_one_request_at_a_time_and_release(self):
        w = prep_world()
        prep_press(w, 0, TITANIA); prep_press(w, 1, SOREN); prep_press(w, 0, RHYS)
        prep_press(w, 1, TITANIA); prep_press(w, 1, RHYS)          # a second request replaces the first
        self.assertEqual((w.flags(TITANIA) & OFFER, w.flags(RHYS) & OFFER), (0, OFFER))
        prep_press(w, 1, SOREN)                                   # owner releases
        self.assertEqual(w.flags(SOREN), 0)
        self.assertEqual(w.sounds[-1], pc.SE26["release"])

    def test_edge_only_and_other_lists_ignored(self):
        w = prep_world()
        w.wb(LIST + 0x62, 1); w.press(0, Z)
        for _ in range(3):                                        # Z held for three frames = one claim
            w.r[3] = LIST; w.run()
        self.assertEqual(w.sounds, [pc.SE26["p1"]])
        w.release_all(); w.r[3] = LIST; w.run()
        w.ww(LIST + 0x14, 0x80275AED)                             # E_UnitList (Base Data): not the prep list
        w.press(0, Z); w.wb(LIST + 0x62, 2); w.r[3] = LIST; w.run()
        self.assertEqual(w.flags(SOREN), 0)

    def test_registers_preserved(self):
        w = prep_world()
        w.wb(LIST + 0x62, 1); w.press(0, Z)
        w.r[3], w.r[4], w.r[28], w.r[29], w.r[30], w.r[31] = LIST, 0x1234, 28, 29, 30, 31
        sp = w.r[1]; w.run()
        self.assertEqual((w.r[3], w.r[4], w.r[28], w.r[29], w.r[30], w.r[31]), (LIST, 0x1234, 28, 29, 30, 31))
        self.assertEqual(w.r[1], sp - 0x30)                       # only the replayed stwu r1,-0x30(r1) remains


def battle_world(phase=0, turn=1) -> World:
    w = World(phase=phase, turn=turn)
    for uid in (IKE, TITANIA, SOREN, RHYS):
        w.add_unit(uid, 0, flags=0x400, lord=(uid == IKE))
    w.add_unit(LETHE, 3)                                          # native partner (no OWNED)
    w.load(dc.draft_cave())
    return w


def battle_press(w: World, port: int, uid: int) -> None:
    w.cursor_unit = unit_addr(uid)
    w.press(port, LR); w.run()
    w.release_all(); w.run()


class BattleDraftBehaviour(unittest.TestCase):
    """EXP-22 (DRAFT-01's steps, executed)."""

    def test_draft_flow(self):
        w = battle_world()
        battle_press(w, 0, TITANIA)
        self.assertEqual((w.flags(TITANIA) & (OWNED | P2), w.force_of(TITANIA)), (OWNED, 0))
        battle_press(w, 0, SOREN)                                 # Player 2's pick: nothing
        self.assertEqual(w.flags(SOREN) & OWNED, 0)
        battle_press(w, 1, SOREN)
        self.assertEqual((w.flags(SOREN) & (OWNED | P2), w.force_of(SOREN), w.control(3)), (OWNED | P2, 3, 1))
        battle_press(w, 1, IKE)                                   # lord refused
        self.assertEqual(w.flags(IKE) & OWNED, 0)
        battle_press(w, 1, LETHE)                                 # native partner refused
        self.assertEqual(w.flags(LETHE), 0)
        battle_press(w, 1, SOREN)                                 # release: back to blue
        self.assertEqual((w.flags(SOREN) & (OWNED | P2), w.force_of(SOREN)), (0, 0))
        battle_press(w, 1, SOREN)
        self.assertEqual(w.force_of(SOREN), 3)

    def test_only_turn1_blue_phase(self):
        for phase, turn in ((3, 1), (0, 2)):
            w = battle_world(phase, turn)
            battle_press(w, 0, TITANIA)
            self.assertEqual(w.flags(TITANIA) & OWNED, 0, (phase, turn))
            self.assertEqual(w.sounds, [])


class OwnershipForcesBehaviour(unittest.TestCase):
    """EXP-21: apply at the blue-phase start, return at chapter end, single-unit escape."""

    def _world(self, phase=0):
        w = World(phase=phase)
        w.add_unit(IKE, 0, lord=True)
        w.add_unit(TITANIA, 0, flags=OWNED | P2)
        w.add_unit(RHYS, 0, flags=OWNED)
        w.add_unit(SOREN, 0, flags=OWNED | P2)
        w.add_unit(LETHE, 3)
        return w

    def test_apply_moves_player2_units_only(self):
        apply_, *rest = dc.blocks21()
        w = self._world(); w.run(apply_[1])
        self.assertEqual(w.members(0), [IKE, RHYS])
        self.assertEqual(sorted(w.members(3)), sorted([LETHE, TITANIA, SOREN]))
        self.assertEqual(w.control(3), 1)
        w2 = self._world(phase=3); w2.run(apply_[1])
        self.assertEqual(w2.transfers, [])

    def test_return_and_escape(self):
        blocks = dc.blocks21()
        w = self._world(); w.run(blocks[0][1])
        w.run(blocks[1][1])                                       # AllUnitEscape entry
        self.assertEqual(sorted(w.members(0)), sorted([IKE, RHYS, TITANIA, SOREN]))
        self.assertEqual(w.members(3), [LETHE])                   # the native partner stays
        w = self._world(); w.run(blocks[0][1])
        w.r[3] = SOREN; w.run(blocks[4][1])                       # UnitEscape(Soren)
        self.assertEqual((w.force_of(SOREN), w.force_of(TITANIA)), (0, 3))


class ListColourBehaviour(unittest.TestCase):
    """EXP-25: the colour index chosen for a data cell."""

    def _colour(self, flags=0, uid=TITANIA, r5=1, data_column=True):
        w = World()
        w.add_unit(uid, 0, flags=flags)
        col, vt = 0x80B00000, 0x80B10000
        w.ww(col + 0x4C, vt); w.ww(vt + 0x1C, pc.DATA_CELL_DRAW if data_column else 0x80130D34)
        w.ww(LIST + 0x3C, ROWS); w.ww(ROWS, unit_addr(uid))
        w.r[24], w.r[25], w.r[29], w.r[5] = col, LIST, 0, r5
        w.run(pc.blocks()[0][1])
        return w.r[5]

    def test_colours(self):
        self.assertEqual(self._colour(OWNED), pc.COLOUR_P1)
        self.assertEqual(self._colour(OWNED | P2), pc.COLOUR_P2)
        self.assertEqual(self._colour(OWNED | OFFER), 0x10)
        self.assertEqual(self._colour(0, uid=IKE), pc.COLOUR_P1)
        self.assertEqual(self._colour(0), 1)                      # unassigned unchanged
        self.assertEqual(self._colour(0, r5=0x13), 0x13)          # forced green unchanged
        self.assertEqual(self._colour(OWNED | P2, r5=0), 0)       # unavailable grey wins
        self.assertEqual(self._colour(OWNED | P2, data_column=False), 1)   # name column untouched


class SimulatorGuards(unittest.TestCase):
    def test_unstubbed_call_is_an_error(self):
        w = World()
        w.stubs.pop(PLAY_SE)
        w2 = prep_world(); w2.stubs.pop(PLAY_SE)
        w2.wb(LIST + 0x62, 1); w2.press(0, Z); w2.r[3] = LIST
        with self.assertRaises(SimError):
            w2.run()


if __name__ == "__main__":
    unittest.main()
