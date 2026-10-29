"""Compact private positioning tables; no faction, story or action-state stores.

Records contain source-state unit/character pointers and xy guards. Not portable
to another roster or executable. New fixtures alone use this stack-save layout.
"""
import struct
from tools.owner_code import (_Asm, stwu, stw, lwz, lbz, lis, addi, li, cmpwi,
                              cmpw, mr, NOP, MFLR0, MTLR0, MFLR31)
from tools.fixture_position_code import UNIT_GET_BY_POS, UNIT_SET_POS, ORIGINAL


def words(chapter, phase, turn, records, *, queue=None, total_words=None):
    """records: unit, character (aligned), force, source_xy, destination_xy.

    queue optionally supplies a later Blue turn and its common original exit.
    Position ALL records during setup; later queue only Blue and move ONE unit.
    """
    if not 1<=len(records)<=159 or phase not in range(4) or not 1<=turn<=255 or not 1<=chapter<=31:
        raise ValueError('bounded nonempty position table and original single-byte guards required')
    if len({r['unit'] for r in records})!=len(records):raise ValueError('duplicate unit in setup table')
    if queue and not 1<=queue['turn']<=255:raise ValueError('unsupported queue turn')
    a=_Asm()
    a(stwu(1,-0xA0,1),stw(0,8,1),MFLR0,stw(0,0x8C,1),
      0x7C000026,stw(0,0xC,1),0x7C0902A6,stw(0,0x10,1),
      0x7C0102A6,stw(0,0x14,1),0xBC610018)  # stmw r3,+18(r1)
    a(lis(12,0x8033))
    for offset,value in ((0x718,chapter),(0x71A,0),(0x71C,1)):
        a(lbz(0,offset,12),cmpwi(0,value));a.br('bne','done')
    a(lbz(29,0x719,12),cmpwi(29,phase));a.br('bne','queue_guard' if queue else 'done')
    a(lbz(0,0x71B,12),cmpwi(0,turn));a.br('bne','done')
    if queue:
        a.br('beq','guards_done')
        a.label('queue_guard');a(cmpwi(29,0));a.br('bne','done')
        a(lbz(0,0x71B,12),cmpwi(0,queue['turn']));a.br('bne','done')
        a.label('guards_done')
    a.br('bl','data_end')
    data=b''
    for row in records:
        if row['character']&3 or row['force'] not in range(4):raise ValueError('unaligned character or unsupported force')
        data+=struct.pack('>II4B',row['unit'],row['character']|row['force'],
                          *row['source_xy'],*row['destination_xy'])
    a(*struct.unpack('>'+str(len(data)//4)+'I',data))
    a.label('data_end');a(MFLR31,li(28,len(records)))
    a.label('loop')
    a(lwz(30,0,31),lwz(0,0x188,30),lwz(4,4,31),0x5485003A,cmpw(0,5));a.br('bne','done') # clrrwi r5,r4,2
    a(lwz(6,0x190,30),lbz(0,8,6),0x70850003) # andi. r5,r4,3 (expected force)
    if queue:
        a(cmpwi(29,phase));a.br('beq','staging')
        a(cmpwi(5,0));a.br('bne','next')
        a(cmpwi(0,5));a.br('bne','active')
        a(lwz(0,0x1A0,30),0x70004000);a.br('beq','done');a.br('bne','next')
        a.label('active');a(cmpwi(0,0));a.br('bne','done')
        a(lwz(0,0x1A0,30),0x70000001);a.br('bne','done')
        for unitoff,recordoff in ((0x19E,10),(0x19F,11)):
            a(lbz(0,unitoff,30),lbz(4,recordoff,31),cmpw(0,4));a.br('bne','done')
        a(li(26,queue['exit'][0]),li(27,queue['exit'][1]));a.br('beq','move')
        a.label('staging')
    a(cmpw(0,5));a.br('bne','done')
    for unitoff,recordoff in ((0x19E,8),(0x19F,9)):
        a(lbz(0,unitoff,30),lbz(4,recordoff,31),cmpw(0,4));a.br('bne','next')
    a(lbz(26,10,31),lbz(27,11,31))
    if queue:a.label('move')
    a(lwz(0,0x194,30),cmpwi(0,0));a.br('bne','done')
    a(lbz(0,0x1A8,30),cmpwi(0,0));a.br('beq','done')
    a(mr(3,26),mr(4,27));a.call(UNIT_GET_BY_POS)
    a(cmpwi(3,0));a.br('bne','next')
    a(lbz(3,0x198,30),mr(4,26),mr(5,27));a.call(UNIT_SET_POS)
    if queue:
        a(cmpwi(29,0));a.br('beq','done')
    a.label('next');a(addi(31,31,12),addi(28,28,-1),cmpwi(28,0));a.br('bne','loop')
    a.label('done')
    a(lwz(0,0xC,1),0x7C0FF120,lwz(0,0x10,1),0x7C0903A6,
      lwz(0,0x14,1),0x7C0103A6,lwz(0,0x8C,1),MTLR0,
      0xB8610018,lwz(0,8,1),addi(1,1,0xA0)) # lmw r3,+18(r1)
    result=a.words()
    required=len(result)+2
    if total_words is None:total_words=required+(required%2)
    if required>total_words or total_words%2:raise ValueError(f'position setup requires {required} words; budget {total_words}')
    return result+[NOP]*(total_words-required)+[ORIGINAL,0]
