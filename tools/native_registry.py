"""Recover literal native script registrations from GFEE01 DOL basic blocks.

Only known literal lis/addi/ori argument construction is accepted. This is not
whole-program data flow. Unknown/clobbered values are discarded conservatively.
"""
from tools.fe9.ppc import Dol
from tools.fe9.disc import DiscReader
from tools.verify_game import DEFAULT_IMAGE
import json
from pathlib import Path


def registrations(dol: Dol) -> list[dict]:
    registers, result, block = {}, [], []
    for address, word in dol.text_words():
        op, rd, ra = word >> 26, (word >> 21) & 31, (word >> 16) & 31
        signed = (word & 0xFFFF) - (0x10000 if word & 0x8000 else 0)
        block.append((address, word))
        if op == 15:
            registers[rd] = ((registers.get(ra, 0) if ra else 0) + (signed << 16)) & 0xFFFFFFFF if not ra or registers.get(ra) is not None else None
        elif op == 14:
            registers[rd] = ((registers.get(ra, 0) if ra else 0) + signed) & 0xFFFFFFFF if not ra or registers.get(ra) is not None else None
        elif op == 24:
            registers[ra] = registers[rd] | (word & 0xFFFF) if registers.get(rd) is not None else None
        elif op in (18, 16) or (op==19 and ((word>>1)&0x3FF) in (16,528)):
            if op == 18 and word & 1:
                displacement = (word & 0x3FFFFFC) - (0x4000000 if word & 0x2000000 else 0)
                if address + displacement == 0x80013AE8:
                    name, fn, argc = (registers.get(i) for i in (3, 4, 5))
                    off = dol.addr_to_off(name) if name is not None else None
                    if off is not None and fn is not None and argc is not None:
                        raw = dol.data[off:off + 128].split(b"\0")[0]
                        if raw and all(32 <= c < 127 for c in raw):
                            result.append({"name": raw.decode(), "function": fn, "argc": argc,
                                           "registration": address,
                                           "signature": [{"address": a, "word": w} for a, w in block[-10:]]})
            registers, block = {}, []
        else:
            # Writes not modeled must not leave stale argument constants behind.
            if op in (32, 34, 40, 42, 12, 13, 7, 8, 10, 11):
                registers.pop(rd, None)
            elif op == 31:
                registers.clear()
        if len(block) > 32:
            block = block[-32:]
    return result


if __name__ == "__main__":
    with DiscReader(DEFAULT_IMAGE) as disc:
        data = registrations(Dol(disc.read_dol()))
    Path("work/native_registry.json").write_text(json.dumps(data, indent=2))
    print(f"{len(data)} literal registrations recovered")
    for r in data:
        if r["name"] in ("UnitGet", "Join", "UnitEscape", "AllUnitEscape", "UnitTransferToForce"):
            print(r["name"], hex(r["function"]), r["argc"])
