"""Read-only bounded Rescue predicates, not a command-availability emulator.

CAMP-023 pins the original collector, relation query and capacity worker. There
is no call into Dolphin, and no unit or skill mutation.
"""
from tools.inspect_state import UNITS
from tools.talk_evidence import MAP,cell


def signed(byte):return byte-256 if byte&128 else byte


def capacity_stat(mem,unit):
    """Exact fields/first-equipped-item branches of original 8003A1E0..394."""
    character,job=mem.u32(unit+0x188),mem.u32(unit+0x18C)
    value=signed(mem.u8(character+0x1C))+mem.u8(job+0x3D)+signed(mem.u8(unit+0x1A9))
    bonuses=[]
    for base in (0x1CC,0x1EC):
        for index in range(4):
            item=unit+base+8*index;descriptor=mem.u32(item)
            if descriptor and mem.u8(item+5)&0x80:
                bonuses.append(signed(mem.u8(descriptor+0x28)));break
    return signed(min(value+signed(sum(bonuses)&255),99)&255)


def rescue(mem,carrier_slot,passenger_slot,carrier_xy,passenger_xy):
    a=UNITS+(carrier_slot-1)*0x280;b=UNITS+(passenger_slot-1)*0x280
    af=mem.u8(mem.u32(a+0x190)+8);bf=mem.u8(mem.u32(b+0x190)+8)
    relation=0 if af==bf else 1 if 1 in (af,bf) else 2
    ca,pa=capacity_stat(mem,a),capacity_stat(mem,b)
    terrain=mem.u8(MAP+0x100D+carrier_xy[0]+64*carrier_xy[1])
    dx,dy=passenger_xy[0]-carrier_xy[0],passenger_xy[1]-carrier_xy[1]
    direction={(0,-1):8,(1,0):2,(0,1):4,(-1,0):1}.get((dx,dy),0)
    predicates=dict(non_enemy_relation=relation!=1,capacity=ca-2>=pa,
                    target_ability3_absent=not bool(mem.u32(b+0x1BC)&8),
                    actor_no_carrier_or_passenger_role=not bool(mem.u32(a+0x1A0)&6),
                    target_no_carrier_or_passenger_role=not bool(mem.u32(b+0x1A0)&6),
                    actor_not_restricted_terrain=terrain!=0x16,
                    original_adjacent_edge=bool(direction and cell(mem,*carrier_xy)['edge_mask']&direction))
    return dict(static_predicates=predicates,all_bounded_predicates=all(predicates.values()),
                carrier_capacity_stat=ca,passenger_capacity_stat=pa,force_relation=relation,
                carrier_terrain_code=terrain,
                scope='Original bounded collector/capacity predicates only; actual menu context, complete engine eligibility and original Rescue remain runtime NOT TESTED.')
