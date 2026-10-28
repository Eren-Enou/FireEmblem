"""Offline C2-to-DOL placement proof, not a safe FE9 runtime memory allocator.

Callers must supply a reserved region. Section/BSS checks alone do NOT establish
heap exclusion or overlay lifetime. No CLI emits a runnable patched game here.
"""
import struct
from tools.fe9.disc import dol_sections


def branch(source: int, target: int) -> int:
    delta = target - source
    if source % 4 or target % 4 or not -(1 << 25) <= delta < (1 << 25):
        raise ValueError("branch requires aligned addresses within signed 26-bit displacement")
    return 0x48000000 | (delta & 0x3FFFFFC)


def hook_plan(dol: bytes, hook: int, original: int, words: list[int], payload: int,
              reserved_size: int) -> dict:
    if len(dol) < 0x100 or not words or words[-1] != 0:
        raise ValueError("DOL header or C2 branch-back terminator missing")
    size = len(words) * 4
    if payload % 32 or reserved_size < size or not 0x80003100 <= payload < payload + size <= 0x81800000:
        raise ValueError("payload outside aligned reserved MEM1 region")
    sections = dol_sections(dol)
    for _, _, base, length in sections:
        if payload < base + length and base < payload + size:
            raise ValueError("payload overlaps a loaded section")
    bss, bss_size = struct.unpack_from(">II", dol, 0xD8)
    if bss_size and payload < bss + bss_size and bss < payload + size:
        raise ValueError("payload overlaps BSS range")
    location = next((off + hook - base for _, off, base, length in sections if base <= hook < base + length), None)
    if location is None or struct.unpack_from(">I", dol, location)[0] != original:
        raise ValueError("unexpected or unmapped original hook instruction")
    slot = next((i for i in range(7) if struct.unpack_from(">I", dol, 0x90 + 4 * i)[0] == 0), None)
    if slot is None:
        raise ValueError("no free text section slot")
    # All internal relative branches keep their displacement. External relative
    # branches require explicit relocation and are rejected in this small proof.
    for i, word in enumerate(words[:-1]):
        op = word >> 26
        if op in (16, 18) and not word & 2:
            bits = 16 if op == 16 else 26
            mask = 0xFFFC if op == 16 else 0x3FFFFFC
            disp = word & mask
            if disp & (1 << (bits - 1)):
                disp -= 1 << bits
            target = i * 4 + disp
            if not 0 <= target < size:
                raise ValueError("external relative branch needs relocation")
    body = words[:-1] + [branch(payload + size - 4, hook + 4)]
    return {"slot": slot, "payload": payload, "size": size, "hook": hook, "hook_offset": location,
            "hook_word": branch(hook, payload), "body": body,
            "runtime_status": "NOT TESTED; caller must prove allocation exclusion and lifetime"}


def apply_offline(dol: bytes, plan: dict) -> bytes:
    """Pure offline transform; only synthetic-DOL tests use this in this milestone."""
    out = bytearray(dol)
    offset = (len(out) + 31) & ~31
    out.extend(bytes(offset - len(out)))
    out.extend(struct.pack(f">{len(plan['body'])}I", *plan["body"]))
    slot = plan["slot"]
    for table, value in ((0, offset), (0x48, plan["payload"]), (0x90, plan["size"])):
        struct.pack_into(">I", out, table + slot * 4, value)
    struct.pack_into(">I", out, plan["hook_offset"], plan["hook_word"])
    return bytes(out)
