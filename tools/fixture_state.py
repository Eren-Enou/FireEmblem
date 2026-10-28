"""Append the private positioning C2 to a NEW copy of an accepted stable state.

Only the known Dolphin 2609a handler/layout and an exact stable code-list body
are accepted. The runtime-generated C2 branch-back words are checked separately.
This edits Gecko storage, not roster/story bytes. Original UnitSetPos runs later
under the setup hook guards. Never certifies an original movement route.
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path

from tools.install_codes import ROOT,build_ini,validate_ini
from tools.fixture_position_code import HOOK,words,ini
from tools.owner_code import c2_lines
from tools.netplay_package import enabled_codes
from tools.fe9.savestate import read_state,write_state
from tools.inspect_state import load_mem1
from tools.patch_state import apply_edits
from tools.verify_game import DEFAULT_IMAGE

HANDLER_SHA256="2b2ff0716aeb9b806cc61181e559041312957f25f04c435bd7da80a78917b33b"
HEADER=bytes.fromhex("00D0C0DE00D0C0DE")
TERMINATOR=bytes.fromhex("F000000000000000")


def validate_prefix(actual,base,text):
    """Match actual GCT bytes, allowing only correctly targeted C2 branch-backs."""
    offset=0
    for kind,name,lines in enabled_codes(text):
        if kind!="Gecko":continue
        expected=bytes.fromhex("".join(lines))
        observed=bytearray(actual[offset:offset+len(expected)])
        if len(observed)!=len(expected):raise ValueError("truncated active code list")
        index=0
        while index<len(expected):
            command,count=struct.unpack_from(">II",expected,index)
            if command>>24!=0xC2:
                raise ValueError("fixture append supports this stable C2-only list")
            end=index+8+count*8
            branch=int.from_bytes(observed[end-4:end],"big")
            displacement=(branch&0x3FFFFFC)-(0x4000000 if branch&0x2000000 else 0)
            target=base+offset+end-4+displacement
            if branch>>26!=18 or branch&3 or target!=(0x80000000|(command&0x1FFFFFF))+4:
                raise ValueError("active C2 branch-back does not match original hook")
            observed[end-4:end]=bytes(4)
            index=end
        if bytes(observed)!=expected:
            raise ValueError(f"active code list differs from stable definition: {name}")
        offset+=len(expected)
    if offset!=len(actual):raise ValueError("unexpected active code list length")


def create(source:Path,destination:Path):
    destination=destination.resolve();manifest=Path(str(destination)+".json")
    if (ROOT/"work").resolve() not in destination.parents:
        raise ValueError("fixture state must be inside this clone's work/")
    if destination.exists() or manifest.exists():
        raise ValueError("refusing to replace fixture state or manifest")
    handler=ROOT/"Dolphin-x64/Sys/codehandler.bin"
    if hashlib.sha256(handler.read_bytes()).hexdigest()!=HANDLER_SHA256:
        raise ValueError("unrecognized Dolphin code handler")
    info,mem=load_mem1(source,DEFAULT_IMAGE)
    if info.game_id!="GFEE01" or info.dolphin_version!="Dolphin 2609a":
        raise ValueError("unsupported state game/emulator")
    # Header occupies the handler's final eight bytes (Dolphin tag 2609a).
    header=0x80001800+handler.stat().st_size-8
    if mem.read(header,8)!=HEADER:
        raise ValueError("expected Gecko header missing")
    stable=build_ini(["COOP-P6","EXP-16"],verbose=False)
    size=validate_ini(stable);start=header+8;end=start+size
    validate_prefix(mem.read(start,size),start,stable)
    if mem.read(end,8)!=TERMINATOR:
        raise ValueError("expected stable code-list terminator missing")
    generated,combined=ini()
    addition=bytes.fromhex("".join(c2_lines(HOOK,words())))
    if combined!=size+len(addition) or end+len(addition)+8>0x80003000:
        raise ValueError("fixture code-list size/layout mismatch")
    if any(mem.read(end+8,len(addition))):
        raise ValueError("fixture append would replace nonzero handler tail data")
    _,payload=read_state(source)
    patched,edits=apply_edits(payload,mem.offset,[f"{end:X}={(addition+TERMINATOR).hex()}"])
    destination.parent.mkdir(parents=True,exist_ok=True)
    write_state(source,destination,patched)
    _,check=load_mem1(destination,DEFAULT_IMAGE)
    if check.read(end,len(addition)+8)!=addition+TERMINATOR:
        raise ValueError("fixture append verification failed")
    record={"classification":"synthetic_original_native_positioning","status":"NOT TESTED",
            "source":str(source.resolve()),"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
            "state_sha256":hashlib.sha256(destination.read_bytes()).hexdigest(),"gecko_bytes":combined,
            "handler_sha256":HANDLER_SHA256,"edit_address":f"{end:08X}","edit_bytes":len(addition)+8,
            "limitations":["only new Gecko storage appended; new hook not yet executed",
                            "original positioning is synthetic setup; Escape must run normally",
                            "launch with the separately generated DBG-CAMP-POS private INI"]}
    with manifest.open("x",encoding="utf-8") as stream:json.dump(record,stream,indent=2)
    return record


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("source",type=Path);p.add_argument("destination",type=Path)
    a=p.parse_args();record=create(a.source,a.destination)
    print(f"created {a.destination}; {record['gecko_bytes']} Gecko bytes; new hook NOT TESTED")
