"""Generate the army-ownership Gecko code (EXP-16) from one ownership table.

Ownership is separate from the tactical force. The table below says which player owns which playable
character (by PID). The code translates that into the game's forces at the right moments, always through
the game's own script command UnitTransferToForce (0x800BCA38, F-34):

  apply   start of every player (blue) phase, any chapter: Player-2 characters in force 0 -> force 3;
          then control[3] = 1 if force 3 has units (EXP-08's rule, applied from turn 1; F-44)
  return  entry of every chapter-end path found (F-38, F-39): AllUnitEscape 0x800BA784, the turn-loop
          transition 0x8002E0D0 and the chapter sequence 0x80005F04: Player-2 characters in force 3 -> 0,
          so the vanilla cleanup and roster code sees ordinary blue units
  escape  entry of UnitEscape 0x800BA8F8(unit id): only the escaping Player-2 character, force 3 -> 0

Characters not in the table are Player 1 (blue): Ike, every newly recruited character, etc. Only units in
force 0 or 3 are ever moved, so enemies, green NPCs, scripted actors and native partners (Lethe, Mordecai)
are untouched.

The table lives in the code itself, so it is deterministic and synced to every Netplay client with the
host's codes. Nothing is written to save data (RESEARCH "Ownership storage").

Usage: python -m tools.owner_code            print the code
       python -m tools.owner_code --write    replace the $EXP-16 block in codes/GFEE01.ini
"""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CODE_NAME = "EXP-16 Army ownership table: Player 2 characters fight as the yellow army"

# PID -> owning player. Test assignment for Chapters 1-4 (user, 2026-10-27). Ike must stay Player 1.
OWNERS: dict[str, int] = {
    "PID_OSCAR": 2,
    "PID_BOLE": 2,       # Boyd
    "PID_CHINON": 2,     # Shinon (forced into the Ch3/Ch4 line-ups, F-41)
    "PID_GATRIE": 2,     # Gatrie (forced into the Ch3/Ch4 line-ups, F-41)
}
SLOT = 16                # bytes per PID in the embedded table (NUL-padded)

GET_UNIT_BY_PID = 0x80016BDC   # (PID string) -> unit* or 0
TRANSFER = 0x800BCA38          # UnitTransferToForce(unit id, force)
APPLY_HOOK = (0x8002E738, 0x9421FFF0)                       # phase-start step: stwu r1,-0x10(r1)
RETURN_HOOKS = [(0x800BA784, 0x9421FFD0),                  # AllUnitEscape: stwu r1,-0x30(r1)
                (0x8002E0D0, 0x9421FFD0),                  # chapter transition: stwu r1,-0x30(r1)
                (0x80005F04, 0x9421FFE0)]                  # chapter sequence: stwu r1,-0x20(r1)
ESCAPE_HOOK = (0x800BA8F8, 0x9421FFF0)                      # UnitEscape(id): stwu r1,-0x10(r1)


def _d(op, s, a, d): return (op << 26) | (s << 21) | (a << 16) | (d & 0xFFFF)
def stwu(s, d, a): return _d(37, s, a, d)
def stw(s, d, a): return _d(36, s, a, d)
def stb(s, d, a): return _d(38, s, a, d)
def lwz(s, d, a): return _d(32, s, a, d)
def lbz(s, d, a): return _d(34, s, a, d)
def lis(d, imm): return _d(15, d, 0, imm)
def ori(a, s, imm): return _d(24, s, a, imm)
def addi(d, a, imm): return _d(14, d, a, imm)
def li(d, imm): return _d(14, d, 0, imm)
def addic_(d, a, imm): return _d(13, d, a, imm)
def cmpwi(a, imm): return _d(11, 0, a, imm)
def cmpw(a, b): return (31 << 26) | (a << 16) | (b << 11)
def mr(a, s): return (31 << 26) | (s << 21) | (a << 16) | (s << 11) | (444 << 1)
MFLR0, MTLR0, MFLR31, MTCTR12, BCTRL, NOP = 0x7C0802A6, 0x7C0803A6, 0x7FE802A6, 0x7D8903A6, 0x4E800421, 0x60000000


class _Asm:
    def __init__(self):
        self.w: list[int] = []
        self.labels: dict[str, int] = {}
        self.fix: list[tuple[int, str, str]] = []

    def __call__(self, *ws): self.w += ws
    def label(self, n): self.labels[n] = len(self.w)
    def br(self, kind, n): self.fix.append((len(self.w), kind, n)); self.w.append(0)
    def call(self, addr): self(lis(12, addr >> 16), ori(12, 12, addr & 0xFFFF), MTCTR12, BCTRL)

    def words(self) -> list[int]:
        for i, kind, n in self.fix:
            off = (self.labels[n] - i) * 4
            self.w[i] = {"bl": (18 << 26) | (off & 0x3FFFFFC) | 1,
                         "beq": (16 << 26) | (12 << 21) | (2 << 16) | (off & 0xFFFC),
                         "bne": (16 << 26) | (4 << 21) | (2 << 16) | (off & 0xFFFC)}[kind]
        return self.w


def pid_table(owners: dict[str, int], player: int = 2) -> bytes:
    pids = [p for p, o in owners.items() if o == player]
    if "PID_IKE" in pids:
        raise ValueError("Ike must stay Player 1 (story compatibility)")
    out = b""
    for p in pids:
        raw = p.encode("ascii")
        if len(raw) >= SLOT:
            raise ValueError(f"{p} is too long for a {SLOT}-byte slot")
        out += raw + b"\0" * (SLOT - len(raw))
    return out


def cave(src: int, dst: int, original: int, table: bytes, phase: int | None = None,
         only_r3_id: bool = False, set_control: bool = False) -> list[int]:
    """C2 cave: for each PID in `table` whose unit is in force `src`, UnitTransferToForce(id, dst)."""
    n = len(table) // SLOT
    a = _Asm()
    a(stwu(1, -0x20, 1), MFLR0, stw(0, 0x24, 1), stw(3, 8, 1), stw(4, 0xC, 1), stw(31, 0x10, 1), stw(30, 0x14, 1))
    if n:
        if phase is not None:
            a(lis(12, 0x8033), lbz(0, 0x719, 12), cmpwi(0, phase)); a.br("bne", "done")   # state+0x11 phase
        a.br("bl", "past"); a.w += list(struct.unpack(f">{len(table) // 4}I", table)); a.label("past")
        a(MFLR31, li(30, n))
        a.label("loop")
        a(mr(3, 31)); a.call(GET_UNIT_BY_PID)
        a(cmpwi(3, 0)); a.br("beq", "next")
        a(lwz(4, 0x190, 3), lbz(0, 8, 4), cmpwi(0, src)); a.br("bne", "next")             # only from `src`
        a(lbz(3, 0x198, 3))
        if only_r3_id:
            a(lbz(0, 0xB, 1), cmpw(3, 0)); a.br("bne", "next")                             # saved r3 low byte
        a(li(4, dst)); a.call(TRANSFER)
        a.label("next")
        a(addi(31, 31, SLOT), addic_(30, 30, -1)); a.br("bne", "loop")
        if set_control:
            # Same rule as EXP-08 (control[3] = 1 when force 3 has units), applied right away, so the
            # COOP-P2 EXP display/gain hooks treat the yellow army as human from turn 1 (F-44).
            a(lis(12, 0x802D), lwz(12, -0x5D78, 12), cmpwi(12, 0)); a.br("beq", "done")   # force 3 head
            a(li(0, 1), lis(12, 0x8033), stb(0, 0x71F, 12))                              # control[3] = 1
    a.label("done")   # no Player-2 characters: the cave only saves and restores registers
    a(lwz(0, 0x24, 1), MTLR0, lwz(3, 8, 1), lwz(4, 0xC, 1), lwz(31, 0x10, 1), lwz(30, 0x14, 1), addi(1, 1, 0x20))
    a(original)
    w = a.words()
    return w + ([NOP, 0] if len(w) % 2 == 0 else [0])


def c2_lines(addr: int, words: list[int]) -> list[str]:
    return [f"C2{addr & 0x1FFFFFF:06X} {len(words) // 2:08X}"] + \
           [f"{words[i]:08X} {words[i + 1]:08X}" for i in range(0, len(words), 2)]


def blocks(owners: dict[str, int] = OWNERS) -> list[tuple[int, list[int]]]:
    t = pid_table(owners)
    out = [(APPLY_HOOK[0], cave(0, 3, APPLY_HOOK[1], t, phase=0, set_control=True))]
    out += [(addr, cave(3, 0, orig, t)) for addr, orig in RETURN_HOOKS]
    out.append((ESCAPE_HOOK[0], cave(3, 0, ESCAPE_HOOK[1], t, only_r3_id=True)))
    return out


def code_lines(owners: dict[str, int] = OWNERS) -> list[str]:
    lines = [f"${CODE_NAME}"]
    for addr, words in blocks(owners):
        lines += c2_lines(addr, words)
    return lines


def write_ini(path: Path, owners: dict[str, int] = OWNERS) -> None:
    """Replace the $EXP-16 code lines (header line through its last hex line) in the ini."""
    text = path.read_text()
    lines = text.split("\n")
    new = code_lines(owners)
    head = next((i for i, l in enumerate(lines) if l.startswith("$EXP-16 ")), None)
    if head is None:
        raise SystemExit(f"no $EXP-16 line in {path}; add the header and its comment block first")
    end = head + 1
    while end < len(lines) and len(lines[end].split()) == 2 and all(
            len(t) == 8 and all(c in "0123456789ABCDEF" for c in t) for t in lines[end].split()):
        end += 1
    lines[head:end] = new
    path.write_text("\n".join(lines), newline="\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="update codes/GFEE01.ini in place")
    args = ap.parse_args()
    if args.write:
        write_ini(ROOT / "codes/GFEE01.ini")
        print("updated $EXP-16 in codes/GFEE01.ini")
    else:
        print("\n".join(code_lines()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
