"""Private synthetic redirect at original chapter-script selection (CAMP-010).

Changes the chapter argument/field before the original descriptor and script
loader read it. No roster, recruitment, objective or completion changes. This
is an unaccepted fixture candidate until the loaded container and units match.
Never included in production definitions or packages.
"""
from tools.owner_code import _Asm,stwu,stw,lwz,lbz,stb,li,addi,cmpwi,NOP

HOOK,ORIGINAL = 0x8002D570,0x88630010


def words(source,target):
    if not 2 <= source <= 31 or not 3 <= target <= 31 or source == target:
        raise ValueError("invalid synthetic loader source/target")
    a=_Asm()
    # r3 is the original state-block pointer. Preserve r0, CR and r1; no calls,
    # LR/CTR/XER/FP or other GPR modifications. Execute displaced lbz last.
    a(stwu(1,-0x10,1),stw(0,8,1),0x7C000026,stw(0,12,1),
      lbz(0,0x10,3),cmpwi(0,source))
    a.br("bne","done")
    a(li(0,target),stb(0,0x10,3))
    a.label("done")
    a(lwz(0,12,1),0x7C0FF120,lwz(0,8,1),addi(1,1,0x10),ORIGINAL)
    result=a.words()
    return result+([NOP,0] if len(result)%2==0 else [0])
