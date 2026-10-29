"""Conservative Dolphin2609a serialized CPU/cache checks for private C2 replacement.

Schema evidence: docs/RESEARCH.md CAMP-022. No CPU register is modified.
Reject ambiguous framing, active Gecko return paths and dirty overlapping cache.
"""
import struct

MARKER = struct.pack('<III', 0x42, 0x42, 0x42)
SPR = 0x31C
CACHE = 0x252A
CACHE_SIZE = 0x9180


def locate(payload, info):
    if info.game_id != 'GFEE01' or info.state_version != 192 or info.dolphin_version != 'Dolphin 2609a':
        raise ValueError('CPU schema supports GFEE01/Dolphin2609a/version192 only')
    candidates = []
    start = 0
    while True:
        pos = payload.find(MARKER, start)
        if pos < 0:
            break
        start = pos + 1
        offset = pos + len(MARKER)
        if offset + CACHE + 2 * CACHE_SIZE > len(payload):
            continue
        regs = struct.unpack_from('<34I', payload, offset)
        pvr = struct.unpack_from('<I', payload, offset + SPR + 287 * 4)[0]
        if pvr == 0x83214 and 0x80003000 <= regs[32] < 0x81800000 and regs[32] % 4 == 0 and 0x80003000 <= regs[1] < 0x81800000 and regs[1] % 8 == 0:
            candidates.append((offset, regs))
    if len(candidates) != 1:
        raise ValueError('CPU serialization framing ambiguous or unsupported')
    return candidates[0]


def guard_and_invalidate(payload, info, mem, address, length):
    offset, regs = locate(payload, info)
    sprs = struct.unpack_from('<1024I', payload, offset + SPR)
    # Native calls may currently be outside a cave with LR/CTR or a saved stack
    # return still pointing inside it. Reject all handler/cave references.
    if any(0x80001800 <= value < 0x80003000 for value in (*regs, sprs[8], sprs[9])):
        raise ValueError('CPU register may resume Gecko code')
    frames, sp = [], regs[1]
    for _ in range(256):
        if sp in (0, 0xFFFFFFFF):
            break
        if sp % 8 or not 0x80003000 <= sp <= 0x817FFFF8:
            raise ValueError('invalid stack chain')
        back, lr = mem.u32(sp), mem.u32(sp + 4)
        if 0x80001800 <= lr < 0x80003000:
            raise ValueError('stack return may resume Gecko code')
        frames.append(sp)
        if back and back <= sp:
            raise ValueError('nonascending stack chain')
        sp = back
    else:
        raise ValueError('unbounded stack chain')
    physical_start = address & 0x1FFFFFF
    physical_end = physical_start + length
    changed = bytearray(payload)
    invalidated = []
    for cache_index in range(2):
        base = offset + CACHE + cache_index * CACHE_SIZE
        valid = base + 0x8080
        tags = base + 0x8100
        modified = base + 0x9100
        for cache_set in range(128):
            for way in range(8):
                bit = 1 << way
                if not payload[valid + cache_set] & bit:
                    continue
                tag = struct.unpack_from('<I', payload, tags + (cache_set * 8 + way) * 4)[0]
                if tag & 31 or ((tag >> 5) & 127) != cache_set:
                    raise ValueError('cache tag schema mismatch')
                if tag & 0x30000000:
                    continue
                physical = tag & 0x1FFFFFF
                if physical < physical_end and physical + 32 > physical_start:
                    if payload[modified + cache_set] & bit:
                        raise ValueError('dirty cache overlaps replacement; never discard a write')
                    changed[valid + cache_set] &= ~bit
                    invalidated.append({'cache': cache_index, 'set': cache_set, 'way': way})
    return bytes(changed), {'cpu_offset': offset, 'pc': regs[32], 'npc': regs[33],
                            'lr': sprs[8], 'stack_frames': frames, 'invalidated': invalidated}
