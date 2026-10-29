"""Repack ONLY private setup C2s in a new state, retaining the stable prefix.

Restores removed hook instructions from the verified original DOL. Installs the
new C2 branch and return immediately, so restored states do not execute stale
hooks before the next handler pass. CPU/cache checks are mandatory (CAMP-022).
"""
import struct
from tools.install_codes import ROOT, build_ini, validate_ini
from tools.netplay_package import enabled_codes
from tools.fixture_state import HEADER, TERMINATOR, HANDLER_SHA256, validate_prefix
from tools.fixture_cpu import guard_and_invalidate
from tools.campaign_test_pack import sha, work_destination
from tools.inspect_state import load_mem1
from tools.fe9.savestate import read_state, write_state
from tools.fe9.disc import DiscReader
from tools.fe9.ppc import Dol, direct_branch_target
from tools.patch_state import apply_edits
from tools.verify_game import DEFAULT_IMAGE, EXPECTED_DOL_SHA1
import hashlib


def branch(source, target):
    delta = target-source
    if delta % 4 or not -0x2000000 <= delta < 0x2000000:
        raise ValueError('unaligned or out-of-range hook branch')
    return (0x48000000 | (delta & 0x3FFFFFC)).to_bytes(4, 'big')


def blocks(text):
    result = []
    for kind, name, lines in enabled_codes(text):
        if kind != 'Gecko': raise ValueError('C2-only layout required')
        raw = bytes.fromhex(''.join(lines))
        offset = 0
        while offset < len(raw):
            command, count = struct.unpack_from('>II', raw, offset)
            end = offset+8+count*8
            if command >> 24 != 0xC2 or not count or end > len(raw):
                raise ValueError('invalid C2 block')
            result.append((0x80000000 | (command & 0x1FFFFFF), raw[offset:end], name))
            offset = end
    if len({hook for hook, _, _ in result}) != len(result):
        raise ValueError('duplicate hook')
    return result


def replace(source, old_text, new_text, destination):
    destination = work_destination(destination)
    handler = ROOT/'Dolphin-x64/Sys/codehandler.bin'
    if sha(handler) != HANDLER_SHA256: raise ValueError('handler mismatch')
    stable = build_ini(['COOP-P6','EXP-16'], verbose=False)
    baseline, old, new = blocks(stable), blocks(old_text), blocks(new_text)
    if old[:len(baseline)] != baseline or new[:len(baseline)] != baseline:
        raise ValueError('stable gameplay prefix must remain byte-identical')
    if len(new) != len(baseline)+1 or len(old) < len(baseline):
        raise ValueError('exactly one new private setup required')
    if any(not name.startswith('DBG-CAMP-') and not name.startswith('FIXTURE-LOADER')
           for _, _, name in old[len(baseline):]):
        raise ValueError('unrecognized old private setup')
    if not new[-1][2].startswith('DBG-CAMP-'): raise ValueError('private setup name required')
    old_size, new_size = validate_ini(old_text), validate_ini(new_text)
    info, mem = load_mem1(source, DEFAULT_IMAGE)
    start = 0x80001800+handler.stat().st_size
    if mem.read(start-8,8) != HEADER or mem.read(start+old_size,8) != TERMINATOR:
        raise ValueError('active handler layout mismatch')
    validate_prefix(mem.read(start,old_size),start,old_text)
    offset=0
    for hook, raw, _ in old:
        word=mem.u32(hook)
        if word & 3 or direct_branch_target(hook,word) != start+offset+8:
            raise ValueError('source installed hook differs from active C2')
        offset+=len(raw)
    with DiscReader(DEFAULT_IMAGE) as disc: dol_raw=disc.read_dol()
    if hashlib.sha1(dol_raw).hexdigest()!=EXPECTED_DOL_SHA1: raise ValueError('DOL identity mismatch')
    dol=Dol(dol_raw)
    stable_size=sum(len(raw) for _,raw,_ in baseline)
    hook, addition, _=new[-1]
    if hook not in {h for h,_,_ in old} and mem.u32(hook)!=dol.u32(hook):
        raise ValueError('new private hook already patched by unknown code')
    address=start+stable_size
    addition=addition[:-4]+branch(address+len(addition)-4,hook+4)
    span=max(old_size,new_size)+8-stable_size
    packed=addition+TERMINATOR
    if len(packed)>span or start+stable_size+span>0x80003000:
        raise ValueError('private layout exceeds handler storage')
    if new_size>old_size and any(mem.read(start+old_size+8,new_size-old_size)):
        raise ValueError('extension would overwrite nonzero handler tail')
    edits={address:packed+bytes(span-len(packed))}
    for old_hook, _, _ in old[len(baseline):]: edits[old_hook]=dol.u32(old_hook).to_bytes(4,'big')
    # The displaced original instruction must be the penultimate setup word.
    if addition[-8:-4]!=dol.u32(hook).to_bytes(4,'big'):
        raise ValueError('new setup displaced instruction mismatch')
    edits[hook]=branch(hook,address+8)
    state_info,payload=read_state(source)
    guarded=payload; guards=[]
    for addr,data in sorted(edits.items()):
        guarded,report=guard_and_invalidate(guarded,state_info,mem,addr,len(data))
        guards.append(report)
    patched,_=apply_edits(guarded,mem.offset,[f'{a:X}={data.hex()}' for a,data in sorted(edits.items())])
    # No roster, event flag or CPU register stores. Only explicit spans and the
    # clean-cache valid bits accepted by guard_and_invalidate may differ.
    write_state(source,destination,patched)
    _,out=load_mem1(destination,DEFAULT_IMAGE)
    validate_prefix(out.read(start,new_size),start,new_text)
    for addr,data in edits.items():
        if out.read(addr,len(data))!=data: raise ValueError('relayout verification failed')
    if out.read(start,stable_size)!=mem.read(start,stable_size): raise ValueError('stable code bytes changed')
    return dict(source_sha256=sha(source),state_sha256=sha(destination),gecko_bytes=new_size,
                removed_private_hooks=[f'{a:08X}' for a,_,_ in old[len(baseline):]],
                edit_spans=[dict(address=f'{a:08X}',bytes=len(d)) for a,d in sorted(edits.items())],cpu_safety=guards)
