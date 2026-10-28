"""Private synthetic setup: original UnitSetPos for Oscar at Ch6's Escape tile.

Does not call Escape, set completion, kill units, or change faction/ownership.
Only fires at Ch6/turn1/Yellow on Oscar force3 at his native starting tile.
Never included in production codes or packages. Generated INI is budget checked.
Runtime acceptance is separate; restored old states may discard this new hook.
"""
import argparse
import json
import struct
from pathlib import Path

from tools.owner_code import (_Asm, MFLR0, MTLR0, MFLR31, GET_UNIT_BY_PID, NOP, mr,
                              stwu,stw,lwz,lbz,lis,addi,li,cmpwi,c2_lines)
from tools.install_codes import ROOT,build_ini,parse_sections,validate_ini
from tools.netplay_setup import make_user
from tools.setup_pads import PORT1_KEYBOARD,keyboard_layout,_KEYS

HOOK, ORIGINAL = 0x800291D8, 0x9421FFD0
UNIT_SET_POS = 0x801A0E84
UNIT_GET_BY_POS = 0x800BD4C0
NAME = "DBG-CAMP-POS synthetic Ch6 Oscar Escape-position setup"


def words():
    a = _Asm()
    # Preserve input arguments plus CR, CTR, XER, LR and r29..31 around native calls.
    # The original input function has no floating-point arguments. ABI-preserved
    # r2/r13..r28 are not modified; our r29..31 are saved/restored explicitly.
    a(stwu(1,-0x80,1),stw(0,8,1),MFLR0,stw(0,0x44,1),
      0x7C000026,stw(0,0xC,1),0x7C0902A6,stw(0,0x10,1),
      0x7C0102A6,stw(0,0x14,1),stw(31,0x40,1),stw(30,0x48,1),stw(29,0x4C,1))
    for r in range(3,13):a(stw(r,0x18+4*(r-3),1))
    a(lis(12,0x8033))
    for offset,value in ((0x718,7),(0x719,3),(0x71A,0),(0x71B,1),(0x71F,1)):
        a(lbz(0,offset,12),cmpwi(0,value));a.br("bne","done")
    a.br("bl","past_pid")
    a(*struct.unpack(">4I",b"PID_OSCAR".ljust(16,b"\0")))
    a(*struct.unpack(">4I",b"PID_EMAKOU".ljust(16,b"\0")))
    a.label("past_pid");a(MFLR31)
    a(addi(3,31,0));a.call(GET_UNIT_BY_PID)
    a(cmpwi(3,0));a.br("beq","done")
    a(lwz(4,0x190,3),cmpwi(4,0));a.br("beq","done")
    a(lbz(0,8,4),cmpwi(0,3));a.br("bne","done")
    a(lwz(0,0x194,3),cmpwi(0,0));a.br("bne","done")
    a(lbz(0,0x1A8,3),cmpwi(0,0));a.br("beq","done")
    for offset,value in ((0x19E,14),(0x19F,9)):
        a(lbz(0,offset,3),cmpwi(0,value));a.br("bne","done")
    a(mr(30,3))
    # Emil guards the exit at (13,26). Move him aside alive before moving Oscar,
    # and reject a nonempty staging tile. This is synthetic setup, not a kill.
    a(li(3,13),li(4,25));a.call(UNIT_GET_BY_POS)
    a(cmpwi(3,0));a.br("bne","done")
    a(addi(3,31,16));a.call(GET_UNIT_BY_PID)
    a(cmpwi(3,0));a.br("beq","done")
    a(mr(29,3),lwz(4,0x190,3),cmpwi(4,0));a.br("beq","done")
    a(lbz(0,8,4),cmpwi(0,1));a.br("bne","done")
    for offset,value in ((0x19E,13),(0x19F,26)):
        a(lbz(0,offset,29),cmpwi(0,value));a.br("bne","done")
    a(lbz(3,0x198,29),li(4,13),li(5,25));a.call(UNIT_SET_POS)
    for offset,value in ((0x19E,13),(0x19F,25)):
        a(lbz(0,offset,29),cmpwi(0,value));a.br("bne","done")
    a(li(3,13),li(4,26));a.call(UNIT_GET_BY_POS)
    a(cmpwi(3,0));a.br("bne","done")
    a(lbz(3,0x198,30),li(4,13),li(5,26));a.call(UNIT_SET_POS)
    a.label("done")
    a(lwz(0,0xC,1),0x7C0FF120,lwz(0,0x10,1),0x7C0903A6,
      lwz(0,0x14,1),0x7C0103A6,lwz(0,0x44,1),MTLR0)
    for r in range(3,13):a(lwz(r,0x18+4*(r-3),1))
    a(lwz(31,0x40,1),lwz(30,0x48,1),lwz(29,0x4C,1),lwz(0,8,1),addi(1,1,0x80),ORIGINAL)
    w=a.words()
    return w+([NOP,0] if len(w)%2==0 else [0])


def ini():
    sections=parse_sections(build_ini(["COOP-P6","EXP-16"],verbose=False))
    sections["Gecko"] += ["$"+NAME,*c2_lines(HOOK,words())]
    sections["Gecko_Enabled"].append("$"+NAME)
    text="# Synthetic setup fixture only; never production/Netplay.\n"
    text += "\n".join("["+k+"]\n"+"\n".join(v) for k,v in sections.items())+"\n"
    return text,validate_ini(text)


def create(root: Path, card: Path):
    root=root.resolve()
    if (ROOT/"work").resolve() not in root.parents or root.exists():
        raise ValueError("requires a NEW destination inside this clone's work/")
    if not card.is_file() or card.suffix.lower()!=".gci":
        raise ValueError("source GCI card copy required")
    text,size=ini()
    root.mkdir(parents=True,exist_ok=False)
    make_user(root/"User",(ROOT/"Dolphin-x64/Games").resolve(),"Synthetic Escape fixture",
              PORT1_KEYBOARD,text,pad2=keyboard_layout(_KEYS))
    with (root/"User/GC/USA/Card A"/card.name).open("xb") as stream:
        stream.write(card.read_bytes())
    manifest={"classification":"synthetic_original_native_positioning",
              "status":"NOT TESTED","gecko_bytes":size,"debug_code":NAME,
              "guards":{"chapter":7,"turn":1,"phase":3,"pid":"PID_OSCAR","force":3,"xy":[14,9]},
              "setup":{"command":"UnitSetPos","oscar_xy":[13,26],"emil_xy":[13,25],"requires_vacant_staging_tile":True},
              "limitations":["manual route, combat, prior story history not exercised",
                             "Escape must still be selected in the original menu",
                             "do not use this configuration for natural progression or Netplay acceptance"]}
    (root/"fixture.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    return manifest


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,required=True);p.add_argument("--card",type=Path,required=True)
    a=p.parse_args();result=create(a.root,a.card)
    print(f"created {a.root}; {result['gecko_bytes']} Gecko bytes; NOT TESTED")
