"""Bounded read-only loaded CMB chain, GFEE01 rev0 (RESEARCH CAMP-009).

This identifies loaded event containers, not map geometry, activation, history,
event completion or compatibility. A missing/invalid chain is inconclusive.
"""
import re

SCRIPT_CHAIN = 0x80367190  # pinned SDA base - 0x7C10


def inspect(mem, chapter, *, root_slot=SCRIPT_CHAIN, limit=16):
    names, issues, visited = [], [], set()
    pointer = mem.u32(root_slot)
    while pointer:
        if pointer in visited:
            issues.append("script chain cycle")
            break
        if len(visited) >= limit:
            issues.append("script chain bound exceeded")
            break
        if pointer & 3 or not 0x80000000 <= pointer <= 0x817FFFD4:
            issues.append("script header outside aligned MEM1")
            break
        visited.add(pointer)
        header = mem.read(pointer, 0x2C)
        if len(header) != 0x2C or header[:4] != b"cmb\0":
            issues.append("script header magic/length mismatch")
            break
        name = header[4:0x18].split(b"\0",1)[0]
        if not re.fullmatch(rb"[A-Za-z0-9_]+\.cmb", name):
            issues.append("script header name invalid")
            break
        names.append(name.decode("ascii"))
        pointer = int.from_bytes(header[0x1C:0x20], "big")
    if not names:
        issues.append("no loaded script identified")
    ids = [int(match[1]) for name in names
           if (match := re.fullmatch(r"C([0-9]{2})\.cmb",name)) and 1 <= int(match[1]) <= 31]
    return {"names": names, "complete_chain": not issues, "issues": issues,
            "campaign_ids": ids,
            "chapter_matches": (ids == [chapter]) if ids and not issues else None,
            "scope": "loaded event containers only; no map/activation/history proof"}
