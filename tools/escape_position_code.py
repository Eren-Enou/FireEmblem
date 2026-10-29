"""Private original-UnitSetPos queue. No escape/faction/story/acted-bit writes."""
import struct
from tools.owner_code import (_Asm, MFLR0, MTLR0, MFLR31, GET_UNIT_BY_PID, NOP,
                              mr, stwu, stw, lwz, lbz, lis, addi, li, cmpwi)
from tools.fixture_position_code import ORIGINAL, UNIT_SET_POS, UNIT_GET_BY_POS


def words(chapter, phase, turn, force, actors, destination, total_words):
    a = _Asm()
    a(stwu(1,-0x80,1),stw(0,8,1),MFLR0,stw(0,0x44,1),
      0x7C000026,stw(0,0xC,1),0x7C0902A6,stw(0,0x10,1),
      0x7C0102A6,stw(0,0x14,1),stw(31,0x40,1),stw(30,0x48,1),stw(29,0x4C,1))
    for r in range(3,13): a(stw(r,0x18+4*(r-3),1))
    a(lis(12,0x8033))
    for off,value in ((0x718,chapter),(0x719,phase),(0x71A,turn>>8),(0x71B,turn&255),(0x71C+phase,1)):
        a(lbz(0,off,12),cmpwi(0,value)); a.br('bne','done')
    a.br('bl','data_end')
    data = b''.join(pid.encode().ljust(16,b'\0') + struct.pack('>II',*xy) for pid,xy in actors)
    a(*struct.unpack('>' + str(len(data)//4) + 'I',data))
    a.label('data_end'); a(MFLR31,li(29,len(actors)))
    a.label('next'); a(mr(3,31)); a.call(GET_UNIT_BY_PID)
    a(cmpwi(3,0)); a.br('beq','done')
    a(mr(30,3),lwz(4,0x190,30),cmpwi(4,0)); a.br('beq','done')
    a(lbz(0,8,4),cmpwi(0,5)); a.br('bne','on_map')
    # Skip only a genuinely escaped force5 unit, never a dead/away transfer.
    a(lwz(0,0x1A0,30),0x70004000); a.br('beq','done')
    a(addi(31,31,24),addi(29,29,-1),cmpwi(29,0)); a.br('bne','next'); a.br('beq','done')
    a.label('on_map'); a(cmpwi(0,force)); a.br('bne','done')
    a(lwz(0,0x1A0,30),0x70000001); a.br('bne','done')
    a(lwz(0,0x194,30),cmpwi(0,0)); a.br('bne','done')
    a(lbz(0,0x1A8,30),cmpwi(0,0)); a.br('beq','done')
    for unit_off,table_off in ((0x19E,16),(0x19F,20)):
        a(lbz(0,unit_off,30),lwz(4,table_off,31),0x7C002000); a.br('bne','done')  # cmpw r0,r4
    a(li(3,destination[0]),li(4,destination[1])); a.call(UNIT_GET_BY_POS)
    a(cmpwi(3,0)); a.br('bne','done')
    a(lbz(3,0x198,30),li(4,destination[0]),li(5,destination[1])); a.call(UNIT_SET_POS)
    a.label('done')
    a(lwz(0,0xC,1),0x7C0FF120,lwz(0,0x10,1),0x7C0903A6,
      lwz(0,0x14,1),0x7C0103A6,lwz(0,0x44,1),MTLR0)
    for r in range(3,13): a(lwz(r,0x18+4*(r-3),1))
    a(lwz(31,0x40,1),lwz(30,0x48,1),lwz(29,0x4C,1),lwz(0,8,1),addi(1,1,0x80))
    result = a.words()
    if len(result) + 2 > total_words:
        raise ValueError('setup exceeds replacement block budget')
    # Keep the last displaced instruction/branch-back at the same addresses.
    return result + [NOP] * (total_words-len(result)-2) + [ORIGINAL,0]
