"""Read-only native field-pair and private-profile persistence audit.

No GCI parser/writer, card edits or native save/reload acceptance. A serializer
field being present does not prove roster selection, save history or Netplay I/O.
"""
import argparse
import configparser
import hashlib
import json
from pathlib import Path
from tools.fe9.disc import DiscReader
from tools.fe9.ppc import Dol
from tools.verify_game import DEFAULT_IMAGE

FIELDS = {
    'level': {'unit_offset':0x19A, 'width':1, 'writer':(0x8003CB70,0x889E019A), 'loader':(0x8003C950,0x987E019A)},
    'exp': {'unit_offset':0x19B, 'width':1, 'writer':(0x8003CB7C,0x889E019B), 'loader':(0x8003C95C,0x987E019B)},
    'hp': {'unit_offset':0x1A8, 'width':1, 'writer':(0x8003CBD4,0x889E01A8), 'loader':(0x8003C9B4,0x987E01A8)},
    'flags': {'unit_offset':0x1A0, 'width':4, 'writer':(0x8003CBBC,0x38BE01A0), 'loader':(0x8003C994,0x38BE01A0)},
}
RAW_FLAGS = [(0x8003CBC0,0x38800004), (0x8003CBC4,0x4813D86D),
             (0x8003C998,0x38800004), (0x8003C99C,0x4813DE75)]


def validate_native(dol):
    pins = [pair for row in FIELDS.values() for pair in (row['writer'],row['loader'])] + RAW_FLAGS
    for address, word in pins:
        if dol.u32(address) != word: raise ValueError(f'native serialization signature differs at {address:08X}')
    return {'level':'STATICALLY VERIFIED', 'fields':FIELDS,
            'raw_flags_width':4, 'raw_flags_ownership_bits_present':True,
            'unknown':['complete UNIP wire schema/checksums','record selection by save mode','inventory item codec',
                       'story/global flag banks','chapter/save-slot/card identity','native read/write outcome']}


def audit_profile(path):
    raw = path.read_bytes()
    cfg = configparser.ConfigParser(interpolation=None, strict=True)
    cfg.read_string(raw.decode('utf-8-sig'))
    def boolean(key):
        value = cfg.get('NetPlay', key, fallback='').strip().lower()
        return {'true':True,'false':False}.get(value)
    settings = {k:boolean(k) for k in ('SyncSaves','SyncCodes','WriteSaveData')}
    write = settings['WriteSaveData']
    state = 'DISABLED_BY_PROFILE' if write is False else 'REQUESTED_NOT_RUNTIME_VERIFIED' if write is True else 'UNKNOWN'
    return {'path':str(path.resolve()),'sha256':hashlib.sha256(raw).hexdigest(),
            'settings':settings,'netplay_save_write_policy':state,
            'runtime_status':'UNTESTED by this audit',
            'scope':'Netplay configuration intent only; does not disable standalone native card I/O. Native save/host write-back/session restart must be demonstrated separately',
            'risks':['SyncSaves is not evidence of persistent write-back',
                     'temporary Netplay save data may not survive session end',
                     'a restored savestate is not a native card reload']}


def unit_view(snapshot, pid):
    units = [u for u in snapshot['game']['units'] if u['pid']==pid]
    if len(units)!=1: raise ValueError('serialization view requires exactly one selected PID')
    unit = units[0]
    result = {'pid':pid}
    for name, field in FIELDS.items():
        value = unit.get(name)
        if type(value) is not int or not 0 <= value < 1 << (8*field['width']):
            raise ValueError('missing or invalid serialized source field: ' + name)
        result[name] = value
    return result


def compare_views(before, after, pid):
    a, b = unit_view(before,pid), unit_view(after,pid)
    return {'status':'INCONCLUSIVE', 'pid':pid,
            'selected_field_changes':{k:[a[k],b[k]] for k in FIELDS if a[k]!=b[k]},
            'scope':'native-backed selected field comparison only; not evidence that native save/reload occurred',
            'excludes':['inventory','recruitment history','roster enumeration','save-slot/card identity','Netplay persistence']}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile',type=Path,help='read Config/Dolphin.ini; does not modify it')
    p.add_argument('--compare',type=Path,nargs=2,help='two decoded campaign snapshots')
    p.add_argument('--pid')
    args=p.parse_args()
    with DiscReader(DEFAULT_IMAGE) as disc: result={'native':validate_native(Dol(disc.read_dol()))}
    if args.profile: result['profile']=audit_profile(args.profile)
    if args.compare:
        if not args.pid: p.error('--compare requires --pid')
        result['comparison']=compare_views(*(json.loads(f.read_text(encoding='utf-8-sig')) for f in args.compare),args.pid)
    print(json.dumps(result,indent=2))
