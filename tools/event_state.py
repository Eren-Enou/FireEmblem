"""Read the pinned current named-event table, never infer absent flags/stages.

CAMP-011 anchors the 96 names and parallel bitset to original native get.
No global flag-bank or Chapter17 part discriminator is claimed decoded.
"""
from tools.inspect_state import STATE

FLAG_TABLE = STATE + 0xB4


def named_flags(mem):
    result = {}
    for i in range(96):
        pointer = mem.u32(FLAG_TABLE + 4 * i)
        if not pointer:
            continue
        if not 0x80000000 <= pointer < 0x81800000:
            raise ValueError('event flag name pointer outside MEM1')
        raw = mem.read(pointer, min(256, 0x81800000 - pointer))
        if b'\0' not in raw:
            raise ValueError('unterminated event flag name')
        name = raw.split(b'\0', 1)[0].decode('shift_jis')
        value = bool(mem.u8(FLAG_TABLE + 0x300 + i // 8) & (1 << (i % 8)))
        if name in result and result[name] != value:
            raise ValueError('ambiguous duplicate event flag name')
        result[name] = value
    return result


def inspect(mem):
    try:
        return {'complete_table_read': True, 'values': named_flags(mem),
                'scope': 'current 96-slot named table only; absent keys and other/global flag banks are UNKNOWN'}
    except ValueError as exc:
        return {'complete_table_read': False, 'values': None, 'error': str(exc),
                'scope': 'UNKNOWN; malformed or unavailable named table, never assumed all-clear'}
