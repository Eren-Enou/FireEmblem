"""Instruction-aligned FE9 scene CFGs, NOT a complete game/event interpreter.

Signed operands, local branches and literal argument suffixes are decoded.
Native effects and scene activation remain unresolved. Unknown operations and
branches into operands fail closed instead of becoming command-string guesses.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass


def message_table(raw: bytes) -> dict[str, str]:
    """FE9 relocatable message container; values remain raw control-code text."""
    _, size, relocations, count = struct.unpack_from(">4I", raw)
    table = 0x20 + size + 4 * relocations
    names = table + 8 * count
    def string(offset):
        return raw[offset:raw.index(b"\0", offset)].decode("latin1")
    return {string(names + name): string(0x20 + value)
            for value, name in (struct.unpack_from(">II", raw, table + 8 * i) for i in range(count))}


@dataclass
class Function:
    index: int
    record: int
    code: int
    end: int
    name: str
    metadata: list[int]

    def trigger(self, raw: bytes) -> dict:
        """Raw scene kind/parameters; only turn kinds 3/6 have corroborated meaning."""
        kind, argc, count = raw[self.record + 12:self.record + 15]
        limit = self.record + 20 + count * 2
        if limit > self.code:
            return {"kind": kind, "error": "parameter range exceeds header"}
        parameters = list(struct.unpack_from(f"<{count}h", raw, self.record + 20))
        result = {"kind": kind, "argc": argc, "parameters": parameters}
        if kind in (3, 6) and len(parameters) >= 3:
            result["inferred_turn_trigger"] = dict(zip(("first_turn", "last_turn", "phase"), parameters))
        return result


# FE9 VM dispatch at 0x80011EDC / table 0x80283F90. Corroborated by StanH's
# original notes: https://feuniverse.us/t/fe9-and-fe10-event-script-doc-notes/6143
# Widths are operands only; FE10's extended local-call instruction is NOT used.
WIDTHS = {0: 0, **{i: 1 if i % 2 else 2 for i in range(1, 25)},
          0x19: 1, 0x1A: 2, 0x1B: 4, 0x1C: 1, 0x1D: 2, 0x1E: 4,
          **{i: 0 for i in range(0x1F, 0x37)}, 0x37: 1, 0x38: 3, 0x39: 0,
          **{i: 2 for i in range(0x3A, 0x3F)}, 0x3F: 0, 0x40: 4, 0x41: 1}


def instructions(raw: bytes, function: Function) -> list[dict]:
    """Decode instruction boundaries and branch targets; reject unknown/truncated opcodes."""
    decoded, pending = {}, [function.code]
    while pending:
        pos = pending.pop()
        if pos in decoded:
            continue
        if not function.code <= pos < function.end:
            raise ValueError(f"branch outside function at {pos:X}")
        op = raw[pos]
        if op not in WIDTHS:
            raise ValueError(f"unknown FE9 opcode {op:02X} at {pos:X}")
        width = WIDTHS[op]
        if pos + 1 + width > function.end:
            raise ValueError(f"truncated operand at {pos:X}")
        operand = raw[pos + 1:pos + 1 + width]
        value = int.from_bytes(operand, "big", signed=True) if operand else None
        target = pos + 1 + value if 0x3A <= op <= 0x3E else None
        nxt = pos + 1 + width
        decoded[pos] = {"offset": pos, "opcode": op, "operand": value,
                        "raw_operand": operand.hex(), "next": nxt, "target": target}
        if target is not None:
            pending.append(target)
        if op not in (0x39, 0x3A):
            pending.append(nxt)
    ordered = sorted(decoded.values(), key=lambda i: i["offset"])
    for left, right in zip(ordered, ordered[1:]):
        if left["next"] > right["offset"]:
            raise ValueError(f"branch enters operand at {right['offset']:X}")
    return ordered


def functions(raw: bytes) -> list[Function]:
    if raw[:4] != b"cmb\0":
        raise ValueError("not a CMB script")
    table = struct.unpack_from("<I", raw, 0x28)[0]
    pointers = []
    while table + 4 <= len(raw):
        pointer = struct.unpack_from("<I", raw, table)[0]
        table += 4
        if pointer == 0:
            break
        if pointer >= len(raw) - 20:
            raise ValueError("invalid function record")
        pointers.append(pointer)
    if pointers != sorted(set(pointers)):
        raise ValueError("unordered/duplicate function records")
    result = []
    for i, record in enumerate(pointers):
        name_ptr, code, *metadata = struct.unpack_from("<5I", raw, record)
        end = pointers[i + 1] if i + 1 < len(pointers) else len(raw)
        if not record + 20 <= code <= end:
            raise ValueError("code outside function record")
        name = raw[name_ptr:raw.index(b"\0", name_ptr)].decode("shift_jis", "replace") if name_ptr else f"function_{i}"
        result.append(Function(i, record, code, end, name, metadata))
    return result


def calls(raw: bytes) -> list[dict]:
    from tools.chapter_audit import script_strings
    strings = script_strings(raw)
    result = []
    for function in functions(raw):
        code = instructions(raw, function)
        for index, insn in enumerate(code):
            if insn["opcode"] != 0x38:
                continue
            pos = insn["offset"]
            name = strings.get(int.from_bytes(raw[pos + 1:pos + 3], "big"))
            argc = raw[pos + 3]
            if name is None:
                raise ValueError(f"call name missing at {pos:X}")
            args, cursor, previous = [], pos, index - 1
            while len(args) < argc and previous >= 0:
                prev = code[previous]
                if prev["next"] != cursor:
                    break
                if prev["opcode"] in (0x19, 0x1A, 0x1B):
                    args.append(prev["operand"])
                elif prev["opcode"] in (0x1C, 0x1D, 0x1E):
                    args.append(strings.get(prev["operand"]))
                else:
                    break
                cursor, previous = prev["offset"], previous - 1
            result.append({"offset": pos, "function": function.index, "function_name": function.name,
                           "command": name, "argc": argc,
                           "args": [None] * (argc - len(args)) + list(reversed(args)),
                           "argument_status": "aligned literal suffix; signed FE9 operands",
                           "preceding_bytes": raw[max(function.code, pos - 16):pos].hex(),
                           "reachability": "reachable in local CFG; external event activation unresolved"})
    return result
