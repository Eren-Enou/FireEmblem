"""Bounded original C18 prefixes and native Complete18 request contract.

No map loading, stage activation, native sequence cleanup or runtime completion
is simulated. Stage3 completion stops before SetGrid/cutscene state changes.
"""
import argparse
import hashlib
import json
from pathlib import Path
from tools.campaign_event_model import LifecycleWorld, load_scripts
from tools.fe9.disc import DiscReader
from tools.verify_game import DEFAULT_IMAGE

SCRIPT = 'Scripts/C18.cmb'
SHA256 = 'e942b11ab26ef9c6aec26fcb25d6a7110a6560629d3f531cd728a0d86f2c40f9'
COMPLETIONS = {1: 82, 2: 85, 3: 88}
OPENINGS = {2: 83, 3: 86, 4: 89}


def load(image=DEFAULT_IMAGE):
    scripts = load_scripts(image)
    with DiscReader(image) as disc: raw = disc.read_file(SCRIPT)
    if hashlib.sha256(raw).hexdigest() != SHA256: raise ValueError('C18 identity differs')
    scripts[SCRIPT] = raw
    return scripts


def complete18_request(stage):
    if stage not in (1, 2, 3): raise ValueError('only original stage1..3 Complete18 requests modeled')
    return stage + 4  # original 0x800B6E34/3C/44 -> state+0x54 at0x800B6E54


class StageWorld(LifecycleWorld):
    PRESENTATION = {'ENVSilentOn', 'Fade', 'WaitM', 'FadeWait', 'BGMFadeOut',
                    'UnitFocusOff', 'InstantFocus', 'InstantSetMapCamera', 'ENVNoisyOn',
                    'TalkEvent', 'WaitF', 'CopyMapCamera', 'BuildInstHide', 'BGMPlay'}

    def __init__(self, scripts, units=None, *, turn=9, previous_turns=7, **kwargs):
        super().__init__(scripts, units, **kwargs)
        self.turn = turn
        self.bm[3] = previous_turns
        self.flags.update({'クリア条件１', 'クリア条件２', 'クリア条件３'})

    def native(self, name, args):
        if name == 'BMGetTurn': return self.turn
        if name == 'BMSetTurn': self.turn = args[0]; return 0
        if name == 'clr': self.flags.discard(args[0]); return 0
        if name == 'GetBattleType': return 0  # explicit test input, not original runtime fact
        if name == 'ForceGetCount':
            return sum(u['force'] == args[0] and u.get('pid', k) is not None for k, u in self.units.items())
        if name == 'ForceGetFirst':
            return next((k for k, u in self.units.items() if u['force'] == args[0] and u.get('pid', k) is not None), 0)
        if name == 'UnitCheckExistsByPID':
            from tools.fe9.event_vm import execute
            return execute(self.scripts['Scripts/startup.cmb'], self.helpers[name], self.native, arguments=args)['return']
        if name in self.PRESENTATION: return 0
        return super().native(name, args)

    def completion_prefix(self, stage):
        if stage not in COMPLETIONS: raise ValueError('no modeled internal transition for stage4')
        boundary = 'SetGrid' if stage == 3 else 'Complete18'
        result = self.run(SCRIPT, COMPLETIONS[stage], stop_before={boundary})
        if result.get('halted_before', {}).get('command') != boundary:
            raise ValueError('required original completion boundary not reached')
        if stage != 3 and result['halted_before']['args'] != [stage]:
            raise ValueError('wrong original Complete18 argument')
        return result

    def opening_prefix(self, stage):
        if stage not in OPENINGS: raise ValueError('only original next-part openings2..4 modeled')
        result = self.run(SCRIPT, OPENINGS[stage], stop_before={'MapLoad'})
        if result.get('halted_before', {}).get('args') != ['bmap18']:
            raise ValueError('original map-load boundary differs')
        return result


def report(scripts):
    rows = []
    for stage in (1, 2, 3):
        world = StageWorld(scripts)
        completion = world.completion_prefix(stage)
        rows.append({'completed_part_input': stage, 'completion_halt': completion['halted_before'],
                     'bm3_after_prefix': world.bm[3], 'completion_executed_to_request': stage != 3,
                     'native_request_code_if_invoked': complete18_request(stage),
                     'native_request_invoked': False})
        opening = world.opening_prefix(stage+1)
        rows[-1].update(next_part_opening_input=stage+1, turn_after_opening_prefix=world.turn,
                        opening_halt=opening['halted_before'])
    return {'classification': 'bounded MODEL VERIFIED only', 'script_sha256': SHA256, 'transitions': rows,
            'unknown': ['Complete18 transitive native effects', 'MapLoad/reinforcements', 'phase initialization',
                        'stage3 remaining cutscene', 'stage4 clear', 'native roster/save/Netplay preservation']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = report(load())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x', encoding='utf-8') as stream: json.dump(result, stream, indent=2)
    print(f'3 original transition-prefix contracts; MODEL ONLY; wrote {args.out}')
