"""Pinned native lifecycle projections; no emulator or complete-engine claims.

The flag-fragment executor runs original instructions with only a force byte and
flag word in private Python memory. Unsupported instructions/accesses fail.
"""
import hashlib

FLAG_START = 0x80015740
FLAG_END = 0x800157A0
FLAG_SHA256 = 'a229f2f4909abd5ffcfb7686ad80ac4c6a215cc992fbe6b33d1e81739136e033'


def force_flags(flags, force):
    if type(force) is not int or not 0 <= force <= 7:
        raise ValueError('invalid tactical force')
    if not 0 <= flags <= 0xFFFFFFFF:
        raise ValueError('flags outside uint32')
    if force <= 4: return flags & ~0x18
    if force == 5: return (flags | 0x18) & ~8
    if force == 6: return flags | 8
    return flags


def mask(mb, me):
    bits = range(mb, me+1) if mb <= me else list(range(mb, 32)) + list(range(me+1))
    return sum(1 << (31-bit) for bit in bits)


def execute_flag_fragment(dol, force, flags, *, verify_identity=True):
    """Execute only original 0x80015740..A0; not the surrounding function."""
    force_flags(flags, force)  # input bounds, independent implementation below
    words = {pc: dol.u32(pc) for pc in range(FLAG_START, FLAG_END, 4)}
    blob = b''.join(words[pc].to_bytes(4, 'big') for pc in sorted(words))
    if verify_identity and hashlib.sha256(blob).hexdigest() != FLAG_SHA256:
        raise ValueError('native flag fragment identity differs')
    regs = [0]*32
    regs[30], regs[31] = 0x1000, 0x2000
    memory = {0x1008: force, 0x21A0: flags}
    cr, pc = [False, False, False], FLAG_START
    for _ in range(64):
        if pc == FLAG_END: return memory[0x21A0]
        if pc not in words: raise ValueError('branch outside native projection')
        w = words[pc]; op = w >> 26
        rd, ra = (w >> 21) & 31, (w >> 16) & 31
        imm = w & 65535; signed = imm-65536 if imm & 32768 else imm
        nxt = pc+4
        if op in (32, 34):
            address = regs[ra]+signed
            if address not in memory: raise ValueError('unmodeled native read')
            regs[rd] = memory[address]
        elif op == 36:
            address = regs[ra]+signed
            if address != 0x21A0: raise ValueError('unmodeled native write')
            memory[address] = regs[rd]
        elif op == 11:
            a = regs[ra]; a = a-0x100000000 if a & 0x80000000 else a
            cr = [a < signed, a > signed, a == signed]
        elif op == 16:
            bo, bi = (w >> 21) & 31, (w >> 16) & 31
            if bo not in (4, 12) or bi > 2 or w & 3:
                raise ValueError('unmodeled native conditional branch')
            if cr[bi] == (bo == 12):
                delta = w & 0xFFFC; delta -= 65536 if delta & 32768 else 0
                nxt = pc+delta
        elif op == 18:
            if w & 3: raise ValueError('unmodeled native branch flags')
            delta = w & 0x3FFFFFC; delta -= 0x4000000 if delta & 0x2000000 else 0
            nxt = pc+delta
        elif op == 21:
            shift, mb, me = (w >> 11) & 31, (w >> 6) & 31, (w >> 1) & 31
            value = regs[rd]
            regs[ra] = ((value << shift) | (value >> ((32-shift) % 32))) & mask(mb, me) & 0xFFFFFFFF
            if w & 1: raise ValueError('unmodeled native record bit')
        elif op == 24: regs[ra] = regs[rd] | imm
        else: raise ValueError(f'unsupported native projection opcode {op}')
        pc = nxt
    raise ValueError('native projection step bound')
