"""Bounded PPC subset for setup-generator regressions; native calls are mocks."""
import struct
from tools.owner_code import GET_UNIT_BY_PID
from tools.fixture_position_code import UNIT_GET_BY_POS, UNIT_SET_POS, ORIGINAL


def run(code, spec, actors, occupied=False, chapter=None):
    base=0x10000000
    memory={base+i:b for i,b in enumerate(struct.pack('>'+str(len(code))+'I',*code))}
    def write(addr,value,width=4):
        for i,b in enumerate(value.to_bytes(width,'big')):memory[addr+i]=b
    def read(addr,width=4):return int.from_bytes(bytes(memory.get(addr+i,0) for i in range(width)),'big')
    for off,value in ((0x718,spec['chapter'] if chapter is None else chapter),(0x719,spec['phase']),
                      (0x71A,spec['turn']>>8),(0x71B,spec['turn']&255),(0x71C,1),(0x71C+spec['phase'],1)):
        write(0x80330000+off,value,1)
    units={}
    for index,(pid,unit) in enumerate(actors.items()):
        addr=0x81200000+index*0x280;force=0x81300000+index*16
        units[pid]=(addr,index+1)
        write(addr+0x188,unit.get('character',0x81400000+index*4))
        write(addr+0x190,force);write(force+8,unit.get('force',spec['force']),1)
        write(addr+0x194,unit.get('rescue',0));write(addr+0x198,index+1,1)
        write(addr+0x19E,unit['xy'][0],1);write(addr+0x19F,unit['xy'][1],1)
        write(addr+0x1A0,unit.get('flags',0));write(addr+0x1A8,unit.get('hp',20),1)
    regs=[0x12340000+r for r in range(32)];regs[1]=0x81000000
    initial=list(regs);spr={'lr':0x80200000,'ctr':0x80200100,'xer':0x1234,'cr':1}
    initial_spr=dict(spr);eq=True;pc=base;moves=[]
    for step in range(2000):
        w=read(pc);op=w>>26;rd=(w>>21)&31;ra=(w>>16)&31;rb=(w>>11)&31
        imm=w&65535;signed=imm-65536 if imm&32768 else imm;nxt=pc+4
        if w==ORIGINAL:
            return moves,regs==initial,spr==initial_spr,step
        if op in (14,15):regs[rd]=((regs[ra] if ra else 0)+(signed<<(16 if op==15 else 0)))&0xFFFFFFFF
        elif op in (32,34):regs[rd]=read(regs[ra]+signed,1 if op==34 else 4)
        elif op in (36,37):
            addr=(regs[ra]+signed)&0xFFFFFFFF;write(addr,regs[rd])
            if op==37:regs[ra]=addr
        elif op==24:regs[ra]=regs[rd]|imm
        elif op==21:
            shift=(w>>11)&31;mb=(w>>6)&31;me=(w>>1)&31
            rotated=((regs[rd]<<shift)|(regs[rd]>>(32-shift if shift else 32)))&0xFFFFFFFF
            mask=sum(1<<(31-bit) for bit in range(32) if (mb<=bit<=me if mb<=me else bit>=mb or bit<=me))
            regs[ra]=rotated&mask
        elif op in (46,47):
            addr=(regs[ra]+signed)&0xFFFFFFFF
            for r in range(rd,32):
                if op==46:regs[r]=read(addr+4*(r-rd))
                else:write(addr+4*(r-rd),regs[r])
        elif op==28:regs[ra]=regs[rd]&imm;eq=regs[ra]==0;spr['cr']=int(eq)
        elif op==11:eq=regs[ra]==(signed&0xFFFFFFFF);spr['cr']=int(eq)
        elif op==18:
            delta=w&0x3FFFFFC;delta-=0x4000000 if delta&0x2000000 else 0
            if w&1:spr['lr']=nxt
            nxt=pc+delta
        elif op==16:
            bo=(w>>21)&31;bi=(w>>16)&31
            if bo not in (4,12) or bi!=2:raise AssertionError('unsupported condition')
            if eq==(bo==12):
                delta=w&0xFFFC;delta-=65536 if delta&32768 else 0;nxt=pc+delta
        elif op==19 and w==0x4E800421:
            target=spr['ctr'];spr['lr']=nxt
            result=0
            if target==GET_UNIT_BY_PID:
                raw=bytearray();p=regs[3]
                while read(p,1):raw.append(read(p,1));p+=1
                result=units.get(raw.decode(),(0,0))[0]
            elif target==UNIT_GET_BY_POS:result=int(occupied)
            elif target==UNIT_SET_POS:moves.append((regs[3],regs[4],regs[5]))
            else:raise AssertionError('unexpected native call')
            for r in [0,*range(3,13)]:regs[r]=0xBAD00000+r
            regs[3]=result;eq=False;spr['cr']=0
        elif op==31:
            if w in (0x7C0802A6,0x7FE802A6):regs[rd]=spr['lr']
            elif w==0x7C0902A6:regs[0]=spr['ctr']
            elif w==0x7C0102A6:regs[0]=spr['xer']
            elif w==0x7C000026:regs[0]=spr['cr']
            elif w==0x7D8903A6:spr['ctr']=regs[12]
            elif w==0x7C0803A6:spr['lr']=regs[0]
            elif w==0x7C0903A6:spr['ctr']=regs[0]
            elif w==0x7C0103A6:spr['xer']=regs[0]
            elif w==0x7C0FF120:spr['cr']=regs[0];eq=bool(regs[0])
            elif (w>>1)&1023==444:regs[ra]=regs[rd]|regs[rb]
            elif w&0x7FF==0:eq=regs[ra]==regs[rb];spr['cr']=int(eq)
            else:raise AssertionError('unsupported instruction '+hex(w))
        else:raise AssertionError('unsupported opcode '+hex(w))
        pc=nxt
    raise AssertionError('setup instruction bound exceeded')
