"""Read-only local Talk fixture fields (CAMP-011); never invokes an event."""
from tools.inspect_state import STATE,UNITS
from tools.event_state import FLAG_TABLE, named_flags as flags

MAP=0x802CA518
DOOR_KEY="扉チャップケヴィン"
CONVERSATION_KEY="オスカーケビン"
MAP_OBJECT_ROOT=0x803672AC
MENU_CONTEXT=0x802EF4C8


def door(mem):
    """Original door-object query mask1000/exclusion10 at (19,14), read-only."""
    root=mem.u32(MAP_OBJECT_ROOT)
    if root&3 or not 0x80000000<=root<=0x817FFFE8:raise ValueError("invalid map-object root")
    count,table=mem.u16(root+6),mem.u32(root+0x14)
    if count>1024 or table&3 or not 0x80000000<=table<=0x81800000-count*0xB4:
        raise ValueError("invalid map-object table")
    for i in reversed(range(count)):
        obj=table+i*0xB4;descriptor=mem.u32(obj+0x10)
        if descriptor&3 or not 0x80000000<=descriptor<=0x817FFF40:
            raise ValueError("invalid map-object descriptor")
        mask=mem.u32(descriptor+0xBC)
        bounds=list(mem.read(obj+4,4))
        if mask&0x1000 and not mask&0x10 and bounds[0]<=19<=bounds[2] and bounds[1]<=14<=bounds[3]:
            state=mem.u8(obj+2)
            return {"index":i,"bounds":bounds,"descriptor_mask":mask,"state_byte":state,
                    "open_worker_marked":bool(state&2)}
    return None


def cell(mem,x,y):
    width,height=mem.u32(MAP),mem.u32(MAP+4)
    if not 0 < width <=64 or not 0 < height <=64 or not 0<=x<width or not 0<=y<height:
        raise ValueError("invalid map dimensions/cell")
    index=x+64*y
    return {"xy":[x,y],"occupant_id":mem.u8(MAP+0xD+index),
            "edge_mask":mem.u16(MAP+0x408E+2*index)}


def capture(mem):
    actor=mem.u32(MENU_CONTEXT)
    delta=actor-UNITS
    actor_slot=delta//0x280+1 if 0<=delta<159*0x280 and delta%0x280==0 else None
    return {"map_dimensions":[mem.u32(MAP),mem.u32(MAP+4)],
            "menu_context":{"mode12":mem.u8(MENU_CONTEXT+0x12),"flags16":mem.u8(MENU_CONTEXT+0x16),
                            "actor_slot":actor_slot},
            "cell_door":door(mem),
            "cells":[cell(mem,x,y) for x,y in ((19,14),(19,19),(20,19))],
            "flags":flags(mem),
            "scope":"local grid edges/occupancy and named flags; no event execution proof"}
