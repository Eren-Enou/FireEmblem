"""Bounded FE9 event-call inventory, NOT a complete CMB interpreter.

Calls are candidate 38/string-offset/argc patterns inside function code regions.
Computed arguments, branch semantics and reachability remain unresolved. Literal
suffixes are decoded conservatively; missing arguments precede the suffix.
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
        for pos in range(function.code, function.end - 3):
            if raw[pos] != 0x38:
                continue
            name = strings.get(int.from_bytes(raw[pos + 1:pos + 3], "big"))
            argc = raw[pos + 3]
            if not name or argc > 16 or not name.isascii() or not name.replace("_", "").isalnum():
                continue
            args, cursor = [], pos
            while len(args) < argc:
                if cursor - 2 >= function.code and raw[cursor - 2] in (0x19, 0x1C):
                    op, value = raw[cursor - 2:cursor]
                    args.append(value if op == 0x19 else strings.get(value))
                    cursor -= 2
                elif cursor - 3 >= function.code and raw[cursor - 3] == 0x1D:
                    args.append(strings.get(int.from_bytes(raw[cursor - 2:cursor], "big")))
                    cursor -= 3
                else:
                    break
            result.append({"offset": pos, "function": function.index, "function_name": function.name,
                           "command": name, "argc": argc,
                           "args": [None] * (argc - len(args)) + list(reversed(args)),
                           "argument_status": "literal suffix only; u8 integers",
                           "preceding_bytes": raw[max(function.code, pos - 16):pos].hex(),
                           "reachability": "unresolved"})
    return result
