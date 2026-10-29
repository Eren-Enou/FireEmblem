"""Synthetic Chapter10 Oscar positioning only; original Talk must run manually.

Kieran, door, faction, ownership, recruitment and conversation flags are untouched.
Guarded to this accepted turn1 fixture and the original empty inside-cell tile.
Native get checks the original conversation key; UnitSetPos moves only Oscar.
See RESEARCH CAMP-011 for geometry, eligibility, addresses and pinned evidence.
"""
import struct
from tools.owner_code import (_Asm,MFLR0,MTLR0,MFLR31,GET_UNIT_BY_PID,NOP,mr,
                              stwu,stw,lwz,lbz,lis,addi,li,cmpwi,c2_lines)
from tools.fixture_position_code import HOOK,ORIGINAL,UNIT_SET_POS,UNIT_GET_BY_POS
from tools.install_codes import parse_sections,validate_ini

NAME="DBG-CAMP-TALK synthetic Ch10 Oscar inside Kieran cell"
KEY="オスカーケビン"
GET_FLAG=0x800BB04C
OSCAR_FROM=(2,19)
OSCAR_TO=(19,19)
KIERAN_XY=(20,19)


def words():
    a=_Asm()
    a(stwu(1,-0x80,1),stw(0,8,1),MFLR0,stw(0,0x44,1),
      0x7C000026,stw(0,0xC,1),0x7C0902A6,stw(0,0x10,1),
      0x7C0102A6,stw(0,0x14,1),stw(31,0x40,1),stw(30,0x48,1),stw(29,0x4C,1))
    for r in range(3,13):a(stw(r,0x18+4*(r-3),1))
    a(lis(12,0x8033))
    for offset,value in ((0x718,11),(0x719,3),(0x71A,0),(0x71B,1),(0x71F,1)):
        a(lbz(0,offset,12),cmpwi(0,value));a.br("bne","done")
    a.br("bl","data_end")
    data=b"PID_OSCAR".ljust(16,b"\0")+b"PID_KEVIN".ljust(16,b"\0")+KEY.encode("shift_jis").ljust(16,b"\0")
    a(*struct.unpack(">12I",data));a.label("data_end");a(MFLR31)
    a(addi(3,31,32));a.call(GET_FLAG)
    a(cmpwi(3,0));a.br("bne","done")
    a(addi(3,31,0));a.call(GET_UNIT_BY_PID)
    a(cmpwi(3,0));a.br("beq","done")
    a(mr(30,3))
    a(lwz(0,0x1A0,30),0x70000001);a.br("bne","done")  # original acted bit
    for register,pid_offset,force,xy in ((30,0,3,OSCAR_FROM),(29,16,2,KIERAN_XY)):
        if register==29:
            a(addi(3,31,pid_offset));a.call(GET_UNIT_BY_PID)
            a(cmpwi(3,0));a.br("beq","done")
            a(mr(29,3))
        a(lwz(4,0x190,register),cmpwi(4,0));a.br("beq","done")
        a(lbz(0,8,4),cmpwi(0,force));a.br("bne","done")
        a(lwz(0,0x194,register),cmpwi(0,0));a.br("bne","done")
        a(lbz(0,0x1A8,register),cmpwi(0,0));a.br("beq","done")
        for offset,value in zip((0x19E,0x19F),xy):
            a(lbz(0,offset,register),cmpwi(0,value));a.br("bne","done")
    # No phase/action/flag writes: original scene and ownership remain authoritative.
    a(li(3,OSCAR_TO[0]),li(4,OSCAR_TO[1]));a.call(UNIT_GET_BY_POS)
    a(cmpwi(3,0));a.br("bne","done")
    a(lbz(3,0x198,30),li(4,OSCAR_TO[0]),li(5,OSCAR_TO[1]));a.call(UNIT_SET_POS)
    a.label("done")
    a(lwz(0,0xC,1),0x7C0FF120,lwz(0,0x10,1),0x7C0903A6,
      lwz(0,0x14,1),0x7C0103A6,lwz(0,0x44,1),MTLR0)
    for r in range(3,13):a(lwz(r,0x18+4*(r-3),1))
    a(lwz(31,0x40,1),lwz(30,0x48,1),lwz(29,0x4C,1),lwz(0,8,1),addi(1,1,0x80),ORIGINAL)
    result=a.words()
    return result+([NOP,0] if len(result)%2==0 else [0])


def ini(base):
    sections=parse_sections(base)
    sections["Gecko"].extend(["$"+NAME,*c2_lines(HOOK,words())])
    sections["Gecko_Enabled"].append("$"+NAME)
    text="# EXPERIMENTAL synthetic inside-cell Talk fixture; never production/Netplay.\n"
    text+="\n".join("["+key+"]\n"+"\n".join(value) for key,value in sections.items())+"\n"
    return text,validate_ini(text)
