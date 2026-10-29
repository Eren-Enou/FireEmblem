"""Execute pinned original campaign scenes against a strict, explicit model.

VM branches and startup helpers are original bytecode. Native operations are
modeled, not PowerPC execution. No activation, timing, save, cleanup or runtime
compatibility is inferred. Unknown natives fail instead of returning success.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

from tools.fe9.disc import DiscReader
from tools.fe9.events import functions
from tools.fe9.event_vm import execute
from tools.verify_game import DEFAULT_IMAGE

SCRIPT_SHA256 = {
    'Scripts/C11.cmb': '153812f03aa5540589777cd8dbffc8bfd7c5494025e0ba3e905454834b94730d',
    'Scripts/startup.cmb': '2ff9182ab485b50792deb78947ab557dcb3f4be66e24b3912da0cb230e033d01',
    'Scripts/C07.cmb': 'c4bb776bfc12cbcacb7bad6cebd906d1e9d88b609cd535a9d51410b20a8feacc',
    'Scripts/C21.cmb': 'd27bd04ba9fd98dbab8a355cb7ec9adab303364f34c67224b4983ca2abb7a5eb',
}
PRISONERS = ('PID_KEVIN', 'PID_CHAP', 'PID_NEPENEE')
ESCAPE_KEYS = dict(zip(PRISONERS, ('ケヴィン離脱', 'チャップ離脱', 'ネフェニー離脱')))
DOOR_KEYS = dict(zip(PRISONERS, ('扉チャップケヴィン', '扉チャップケヴィン', '扉ネフェニー')))
PRESENTATION = {'BGMQuietOn', 'BGMQuietOff', 'TalkEvent', 'DefaultEscapeTalk',
                'UnitFocusOff', 'UnitFadeOut', 'UnitMoveDir', 'UnitMoveWait', 'UnitFadeOff',
                'ENVSilentOn', 'Fade', 'WaitM', 'BGMFadeOut'}


def load_scripts(image=DEFAULT_IMAGE):
    with DiscReader(image) as disc:
        result = {name: disc.read_file(name) for name in SCRIPT_SHA256}
    for name, raw in result.items():
        if hashlib.sha256(raw).hexdigest() != SCRIPT_SHA256[name]:
            raise ValueError('unsupported script identity: ' + name)
    return result


class World:
    """Test-provided native facts/effects; never represents the whole engine.

    UnitGet selector4 = rescued passenger (CAMP-001). Lookup supplies stable
    identity tokens. GetStatus/GetForce supply caller-provided fields. Transfer
    changes force only in this model; preservation is an assumption, not proof
    that the native worker preserves every bit. Escape is recorded, not executed.
    """
    def __init__(self, scripts, units=None, *, actor='PID_OSCAR', passenger=0,
                 flags=(), maniac=False):
        self.scripts = scripts
        self.units = copy.deepcopy(units if units is not None else {
            'PID_IKE': {'force': 0, 'flags': 0x400},
            'PID_OSCAR': {'force': 3, 'flags': 0x60000400},
            **{pid: {'force': 2, 'flags': 0x80000} for pid in PRISONERS}})
        self.actor, self.passenger, self.maniac = actor, passenger, maniac
        self.flags, self.bm, self.calls, self.escaped, self.doors = set(flags), {4: 0}, [], [], set()
        self.helpers = {f.name: f.index for f in functions(scripts['Scripts/startup.cmb'])}
        self.helper_depth = 0

    def native(self, name, args):
        self.calls.append({'command': name, 'args': copy.deepcopy(args)})
        if name in ('UnitTransferToForceByPID', 'UnitCheckExistsByPID2'):
            if self.helper_depth >= 8:
                raise ValueError('named helper depth exceeded')
            self.helper_depth += 1
            try:
                return execute(self.scripts['Scripts/startup.cmb'], self.helpers[name],
                               self.native, arguments=args)['return']
            finally:
                self.helper_depth -= 1
        if name == 'MindGetMe': return self.actor
        if name == 'UnitGetByPID': return args[0] if args[0] in self.units else 0
        if name == 'UnitGetStatus': return self.units[args[0]]['flags']
        if name == 'UnitGetForce': return self.units[args[0]]['force']
        if name == 'UnitGet':
            if args != [self.actor, 4]: raise ValueError('unmodeled UnitGet selector/actor')
            return self.passenger
        if name == 'BMGetValue': return self.bm.get(args[0], 0)
        if name == 'BMSetValue': self.bm[args[0]] = args[1]; return 0
        if name == 'get': return int(args[0] in self.flags)
        if name == 'set': self.flags.add(args[0]); return 0
        if name == 'Maniac': return int(self.maniac)
        if name == 'UnitTransferToForce':
            self.units[args[0]]['force'] = args[1]
            return 0
        if name == 'UnitEscape': self.escaped.append(args); return 0
        if name == 'EventGetX': return 19
        if name == 'EventGetY': return 14
        if name == 'DoorOpen': self.doors.add(tuple(args)); return 0
        if name in PRESENTATION: return 0
        raise ValueError('unmodeled native: ' + name)

    def run(self, script, scene, *, stop_before=()):
        return execute(self.scripts[script], scene, self.native, stop_before=stop_before)

    def talk(self, actor, target, script='Scripts/C11.cmb'):
        if actor not in self.units or target not in self.units:
            return False
        matches = conversation_scene(self.scripts[script], actor, target, self.flags)
        if len(matches) != 1:
            return False
        self.run(script, matches[0])
        return True


class JillWorld(World):
    """C21 scene26 relationship inputs; no support/story history is synthesized."""
    PRESENTATION = {'BgmChangeEvt_MapToEvt2', 'CopyMapCamera', 'WaitF', 'InstantFocus',
                    'InstantSetMapCamera', 'SetMapCamera', 'FadeWait', 'FocusHardWait',
                    'UnitFocusByPID', 'PastMapCamera', 'ENVSilentOff', 'BgmContEvt_EvtToMap1'}

    def __init__(self, scripts, *, force=3, mist=0, lethe=0):
        super().__init__(scripts)
        self.units.update({'PID_JILL': {'force': force, 'flags': 0x60000400},
                           'PID_SIHARAMU': {'force': 1, 'flags': 0}})
        self.relationships = {'PID_MIST': mist, 'PID_LETHE': lethe}
        self.attack_sequences = []

    def native(self, name, args):
        if name == 'PersonGetYellLevel':
            if args[0] != 'PID_JILL' or args[1] not in self.relationships:
                raise ValueError('unmodeled relationship query')
            self.calls.append({'command': name, 'args': args.copy()})
            return self.relationships[args[1]]
        if name == 'UnitSetCpAttackSeq':
            self.calls.append({'command': name, 'args': args.copy()})
            self.attack_sequences.append(args.copy())
            return 0
        if name in self.PRESENTATION:
            self.calls.append({'command': name, 'args': args.copy()})
            return 0
        return super().native(name, args)


def conversation_scene(raw, actor, target, consumed=()):
    """Identity/reversal/key portion of CAMP-004 matcher; no menu/edge proof."""
    matches = []
    for f in functions(raw):
        event = f.trigger(raw).get('conversation_event')
        if not event or event['key'] in consumed:
            continue
        if (actor, target) == (event['actor'], event['target']) or (
                event['reversible'] and (target, actor) == (event['actor'], event['target'])):
            matches.append(f.index)
    return matches


def report(scripts):
    rows = []
    for pid in PRISONERS:
        for maniac in (False, True):
            for door in (False, True):
                for escaped in (False, True):
                    flags = ([DOOR_KEYS[pid]] if door else []) + ([ESCAPE_KEYS[pid]] if escaped else [])
                    world = World(scripts, flags=flags, maniac=maniac)
                    result = world.run('Scripts/C11.cmb', 57, stop_before={'AllUnitEscape'})
                    if result.get('halted_before', {}).get('command') != 'AllUnitEscape':
                        raise ValueError('original cleanup boundary not reached')
                    rows.append({'pid': pid, 'maniac': maniac, 'door': door, 'escaped': escaped,
                                 'transferred_blue': world.units[pid]['force'] == 0,
                                 'transfer_calls': [c for c in world.calls if c['command'] == 'UnitTransferToForce']})
    jill = []
    for force in (0, 3):
        for reverse in (False, True):
            for mist in range(4):
                for lethe in range(4):
                    world = JillWorld(scripts, force=force, mist=mist, lethe=lethe)
                    actor, target = ('PID_SIHARAMU', 'PID_JILL') if reverse else ('PID_JILL', 'PID_SIHARAMU')
                    if not world.talk(actor, target, 'Scripts/C21.cmb'):
                        raise ValueError('original Jill scene selection failed')
                    jill.append({'force_before': force, 'reverse': reverse, 'mist_query': mist,
                                 'lethe_query': lethe, 'force_after': world.units['PID_JILL']['force'],
                                 'attack_sequence_calls': world.attack_sequences})
    return {'classification': 'MODEL VERIFIED only', 'script_sha256': SCRIPT_SHA256, 'cleanup_cases': rows,
            'jill_cases': jill,
            'scope': 'original C11 cleanup prefix/startup helpers before AllUnitEscape and C21 Jill event branches; modeled native/relationship inputs',
            'excludes': ['scene activation', 'native transfer implementation', 'AllUnitEscape', 'permanent recruitment',
                         'chapter completion', 'save/load', 'Netplay']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('work/ch10_event_model.json'))
    args = parser.parse_args()
    result = report(load_scripts())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, ensure_ascii=True)
    print(f"{len(result['cleanup_cases'])} cleanup-prefix / {len(result['jill_cases'])} Jill cases; MODEL ONLY; wrote {args.out}")
