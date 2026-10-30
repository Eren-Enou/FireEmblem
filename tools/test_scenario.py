"""Scenario plans and attributed runtime evidence; never emulator execution or input."""
from __future__ import annotations

import argparse
import configparser
import hashlib
import json
import re
from pathlib import Path

from tools.install_codes import ROOT, validate_ini
from tools.verify_game import DEFAULT_IMAGE
from tools.netplay_package import fingerprint
from tools.campaign_snapshot import capture
from tools.campaign_test_pack import (CATALOG, collect, review, sha, work_destination,
                                     write_json, verify_partner_wait)

PACKAGE = ROOT / 'work/scenarios/human_v1'
SOURCES = {
    'CH10-PARTNER-WAIT': ROOT / 'work/fixtures/ch10_partner_actions_v1',
    'CH10-NATIVE-RESUME': ROOT / 'work/fixtures/ch10_native_resume_v1',
}
ESCAPES = ('CH10-PRISONER-ESCAPE', 'CH6-IKE-COMPLETE')
DIRECTORIES = {'CH10-PRISONER-ESCAPE': 'CH10-PRISONER-ESCAPE-v2'}
from tools.next_scenarios import NAMES as TRANSITIONS
from tools.action_scenarios import NAMES as ACTIONS
NEXT=(*TRANSITIONS,*ACTIONS)


def known():
    return (*SOURCES,*ESCAPES,*NEXT)


def scenario_dir(name, root=PACKAGE):
    return private(root / DIRECTORIES.get(name, name), ROOT / 'work')


BLOCKED = {
    'CH10-PRISONER-CLEANUP': 'Superseded by the separate CH10-CHAPTER-COMPLETE candidate. Original ending/permanent recruitment is still runtime unverified.',
    'CH17-STAGE-TRANSITIONS': 'Needs original stage-specific map and near-clear state, roster, difficulty and stage/story history for all four stages. Shared C18 script alone cannot establish the stage.',
    'CH9-PARTNER-CLEANUP': 'Accepted native transformation/Wait and new combat candidate do not supply original near-clear history. No chapter-completion/recruitment outcome is synthesized.',
}


def private(path, root):
    original = path.absolute()
    path, root = path.resolve(), root.resolve()
    if root not in path.parents:
        raise ValueError('path escapes private scenario: ' + str(path))
    # Reject junctions/symlinks even if they currently resolve inside the root.
    for part in [original, *original.parents]:
        if part == root:
            break
        if part.is_symlink() or (hasattr(part, 'is_junction') and part.is_junction()):
            raise ValueError('linked scenario path refused: ' + str(part))
    return path


def configuration(profile):
    """Only the known GCI-folder layout; reject external card/path overrides."""
    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read(profile / 'Config/Dolphin.ini')
    if cfg.get('Core', 'EnableCheats', fallback='').lower() != 'true':
        raise ValueError('EnableCheats must be True')
    if any(cfg.get('Core', key, fallback='') != '6' for key in ('SIDevice0', 'SIDevice1')):
        raise ValueError('two GameCube controller ports required')
    # Dolphin writes many ordinary settings on exit. Storage and expansion-device
    # overrides require separate review, including empty/default-looking values.
    for key in cfg['Core']:
        if any(token in key for token in ('memcard', 'gci', 'exidevice', 'override', 'path')):
            value = cfg['Core'][key].strip()
            if value and not (key == 'overrideregionsettings' and value.lower() == 'false'):
                raise ValueError('unreviewed Core/card override: ' + key)
    for key, expected in (('SlotA','8'),('SlotB','255'),('SerialPort1','255'),('SerialPort2','255')):
        if cfg.get('Core',key,fallback=expected) != expected:
            raise ValueError('private GCI-folder / empty peripheral layout required: ' + key)
    forbidden = {'paths', 'gci', 'memorycards'}
    if forbidden & {s.lower() for s in cfg.sections()}:
        raise ValueError('external storage/path configuration refused')
    return cfg


def bindings(profile):
    from tools.setup_pads import PORT1_KEYBOARD, PORT2_KEYBOARD
    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read(profile / 'Config/GCPadNew.ini')
    for section, expected in (('GCPad1',PORT1_KEYBOARD),('GCPad2',PORT2_KEYBOARD)):
        for key, value in expected.items():
            if key.endswith('/Calibration'): continue
            if cfg.get(section,key,fallback='').upper() != value.upper():
                raise ValueError('expected supplied keyboard binding: '+section+'/'+key)


def prepare(root=PACKAGE):
    """NEW independent profile/card per test; source profiles remain read-only."""
    from tools.netplay_setup import make_user
    from tools.setup_pads import PORT1_KEYBOARD, PORT2_KEYBOARD
    root = work_destination(root)
    rows = {r['id']: r for r in json.loads(CATALOG.read_text(encoding='utf-8'))}
    # Complete source checks before creating any destination.
    for name, source in SOURCES.items():
        config = source / 'User/GameSettings/GFEE01.ini'
        snap = capture(source / 'seed.s02.sav', DEFAULT_IMAGE, config, 'offline-preparation')
        verdict = verify_partner_wait(snap, snap, {})
        other = [f for f in verdict['failures'] if f not in (
            'distinct state hashes required', 'Kieran must acquire only acted bit')]
        if other or not list((source / 'User/GC/USA/Card A').glob('*.gci')):
            raise ValueError(name + ': source preconditions rejected: ' + '; '.join(other))
    root.mkdir(parents=True)
    for name, source in SOURCES.items():
        dest = root / name
        dest.mkdir()
        files = [source / 'seed.s02.sav', source / 'User/GameSettings/GFEE01.ini',
                 source / 'User/Config/GCPadNew.ini',
                 *sorted((source / 'User/GC/USA/Card A').glob('*.gci'))]
        hashes = {str(p): sha(p) for p in files}
        text = files[1].read_text()
        make_user(dest / 'User', DEFAULT_IMAGE.parent.resolve(), 'PRIVATE ' + name,
                  PORT1_KEYBOARD, text, pad2=PORT2_KEYBOARD)
        for src in files:
            target = dest / ('seed.s02.sav' if src.name == 'seed.s02.sav' else src.relative_to(source))
            if src.suffix.lower() == '.gci' or src.name == 'seed.s02.sav':
                with target.open('xb') as stream:
                    stream.write(src.read_bytes())
            elif src.name == 'GCPadNew.ini':
                target.write_bytes(src.read_bytes())
        (dest / 'card-before').mkdir()
        for card in (dest / 'User/GC/USA/Card A').glob('*.gci'):
            with (dest / 'card-before' / card.name).open('xb') as stream:
                stream.write(card.read_bytes())
        write_json(dest / 'case.json', rows[name])
        write_json(dest / 'observations.json', {'observed': {k: None for k in rows[name]['observations']},
                                             'notes': '', 'source_history': 'synthetic post-Talk; inherited card identity unverified'})
        pinned = {str(p.relative_to(dest)): sha(p) for p in [dest / 'seed.s02.sav',
            dest / 'User/GameSettings/GFEE01.ini', dest / 'User/Config/GCPadNew.ini',
            *sorted((dest / 'card-before').glob('*.gci'))]}
        initial_cards = {p.name: sha(p) for p in (dest / 'User/GC/USA/Card A').glob('*.gci')}
        write_json(dest / 'scenario.json', {'id': name, 'readiness': 'PREPARED_RUNTIME_UNVERIFIED',
            'source_hashes': hashes, 'pinned': pinned, 'initial_cards': initial_cards,
            'fingerprint': fingerprint(text), 'gecko_bytes': validate_ini(text),
            'card_identity': 'UNVERIFIED; refusal is fixture INCONCLUSIVE'})
        if any(sha(Path(p)) != digest for p, digest in hashes.items()):
            raise ValueError('source changed during preparation; candidate rejected')
    return {'prepared': list(SOURCES), 'root': str(root), 'status': 'NOT TESTED'}


def check(name, fresh=False, root=PACKAGE):
    if name in BLOCKED:
        raise ValueError('BLOCKED: ' + BLOCKED[name])
    if name not in known():
        raise ValueError('unknown scenario; use -List')
    if fresh and name not in ('CH10-NATIVE-RESUME', 'CH6-IKE-COMPLETE',*TRANSITIONS):
        raise ValueError('fresh boot only belongs to the native resume scenario')
    from tools.fe9.disc import DiscReader
    from tools.verify_game import EXPECTED_ID, EXPECTED_REVISION, EXPECTED_DOL_SHA1
    with DiscReader(DEFAULT_IMAGE) as disc:
        header, dol = disc.header(), disc.read_dol()
    if (header['game_id'],header['revision']) != (EXPECTED_ID,EXPECTED_REVISION) or hashlib.sha1(dol).hexdigest()!=EXPECTED_DOL_SHA1:
        raise ValueError('original GFEE01 rev0 executable identity mismatch')
    dest = scenario_dir(name, root)
    manifest = json.loads(private(dest / 'scenario.json', dest).read_text(encoding='utf-8'))
    if manifest['id'] != name:
        raise ValueError('scenario identity mismatch')
    fresh = fresh or manifest.get('launch_type')=='native'
    for relative, digest in manifest['pinned'].items():
        path = private(dest / relative, dest)
        if fresh and relative.replace('\\','/') == 'User/Config/GCPadNew.ini':
            continue  # Dolphin may expand defaults; required mappings checked below.
        if sha(path) != digest:
            raise ValueError('immutable prerequisite changed: ' + relative)
    profile = private(dest / 'User', dest)
    configuration(profile)
    bindings(profile)
    for path in profile.rglob('*'):
        private(path, dest)
    cards = list((profile / 'GC/USA/Card A').glob('*.gci'))
    if not cards or len(cards) != len(manifest['initial_cards']):
        raise ValueError('private card files missing')
    if fresh:
        def identity(path):
            data = path.read_bytes()
            if len(data) < 64 or data[:6] != b'GFEE01':
                raise ValueError('unexpected private GCI game/header')
            return data[:6],data[8:40]
        # Dolphin may rename a GCI on flush. Compare its original directory-entry
        # identity against the immutable backup; never rewrite that identity.
        expected = sorted(identity(dest/'card-before'/name) for name in manifest['initial_cards'])
        if sorted(identity(p) for p in cards) != expected:
            raise ValueError('private GCI directory-entry identities changed')
    elif any(p.name not in manifest['initial_cards'] for p in cards):
        raise ValueError('private card set unexpected')
    changed = {p.name for p in cards if sha(p) != manifest['initial_cards'].get(p.name)}
    if changed and not fresh:
        raise ValueError('private card changed; use native -FreshBoot after Suspend, or prepare a NEW trial; never restore seed over changed card history')
    config = profile / 'GameSettings/GFEE01.ini'
    text = config.read_text()
    size = validate_ini(text)
    if size != manifest['gecko_bytes'] or fingerprint(text) != manifest['fingerprint']:
        raise ValueError('configuration fingerprint/budget mismatch')
    if name in NEXT:
        from tools.next_scenarios import runtime_candidate
        runtime_candidate(fingerprint(text))
    if name in NEXT:
        from tools.fixture_state import HANDLER_SHA256
        if sha(ROOT/'Dolphin-x64/Sys/codehandler.bin')!=HANDLER_SHA256:
            raise ValueError('handler identity changed')
        if sha(ROOT/'Dolphin-x64/Dolphin.exe')!=manifest['executable_sha256']:
            raise ValueError('Dolphin executable identity changed')
        for path,digest in manifest['source_hashes'].items():
            if sha(Path(path))!=digest: raise ValueError('accepted source changed: '+path)
        inspection=dest/('source.sav' if manifest['launch_type']=='native' else 'seed.s02.sav')
        inspection_ini=dest/'source.ini' if manifest['launch_type']=='native' else config
        snap=capture(inspection,DEFAULT_IMAGE,inspection_ini,'offline-check')
        failures=[] if snap['game']==manifest['source_game'] and snap['evidence']['intended_c2_verified'] else ['source roster/scripts or installed codes differ']
    else:
        snap = capture(dest / 'seed.s02.sav', DEFAULT_IMAGE, config, 'offline-check')
    if name in ESCAPES:
        from tools.escape_scenarios import geometry, SPECS
        from tools.inspect_state import load_mem1
        _, mem = load_mem1(dest / 'seed.s02.sav', DEFAULT_IMAGE)
        geometry(mem, SPECS[name])
        failures = []
        if snap['game'] != manifest['source_game'] or not snap['evidence']['intended_c2_verified']:
            failures.append('seed roster/scripts or installed replacement differ')
    elif name not in NEXT:
        verdict = verify_partner_wait(snap, snap, {})
        failures = [f for f in verdict['failures'] if f not in (
            'distinct state hashes required', 'Kieran must acquire only acted bit')]
    if failures:
        raise ValueError('starting state rejected: ' + '; '.join(failures))
    exe = ROOT / 'Dolphin-x64/Dolphin.exe'
    if not exe.is_file() or not DEFAULT_IMAGE.is_file():
        raise ValueError('local Dolphin executable or original image missing')
    args = ['--user', str(profile), '--exec', str(DEFAULT_IMAGE.resolve())]
    if not fresh:
        args += ['--save_state', str(dest / 'seed.s02.sav')]
    row = json.loads((dest / 'case.json').read_text(encoding='utf-8'))
    steps = (row['steps'] if name in NEXT and not (fresh and name=='CH10-CHAPTER-COMPLETE') else
             ['Fresh boot: original Load from this SAME private card; NEVER load a savestate. Save reloaded.sav before acting.'] if fresh and name=='CH10-CHAPTER-COMPLETE' else
             ['Fresh boot: use original native Resume/Load; NEVER load a savestate. Capture after before acting.',
              'If Suspend was refused, record exact refusal; this is INCONCLUSIVE inherited card identity.'] if fresh else [
                  'This launcher restores a separate synthetic scenario derived from accepted event evidence. Do not use Restart Chapter.',
                  *(row['steps'] if name in ESCAPES else row['steps'][1:-1]),
                  'Capture labels: '+', '.join(row['captures'])+'. Use this launcher with -Capture, -Passed/-Failed and -Review; see docs/SCENARIO_TESTS.md.'])
    return {'title': row['title'], 'readiness': manifest['readiness'], 'gecko_bytes': size,
            'fingerprint': manifest['fingerprint'], 'steps': steps,
            'evidence_directory': str(dest), 'executable': str(exe), 'arguments': args,
            'card_identity': manifest['card_identity'], 'changed_card_files': sorted(changed)}


def listing(root=PACKAGE):
    """Keep accepted runtime evidence separate from current launch safety."""
    result=[]
    for name in known():
        try:dest=scenario_dir(name,root)
        except ValueError as exc:
            result.append(dict(scenario=name,readiness='INVALID',runtime='INCONCLUSIVE',reason=str(exc)));continue
        if not (dest/'scenario.json').is_file():
            result.append(dict(scenario=name,readiness='MISSING_PREREQUISITES',runtime='NOT TESTED'))
            continue
        try:verdict=review(dest)
        except (ValueError,OSError,KeyError,configparser.Error) as exc:
            result.append(dict(scenario=name,readiness='INVALID',runtime='INCONCLUSIVE',reason='Evidence unreadable: '+str(exc)));continue
        row=dict(scenario=name,runtime=verdict['status'])
        try:
            plan=check(name,root=root)
            row.update(readiness=verified_readiness(dest) if verdict['status']=='PASS' else 'OFFLINE_VALIDATED_CANDIDATE',
                       offline_validation='PASS',gecko_bytes=plan['gecko_bytes'])
        except (ValueError,OSError,KeyError,configparser.Error) as exc:
            row.update(readiness=verified_readiness(dest) if verdict['status']=='PASS' else 'INVALID',
                       offline_validation='REFUSED',reason=str(exc))
        if verdict['status']=='FAIL': row['readiness']='FAILED_VALIDATION'
        result.append(row)
    return result+[dict(scenario=name,readiness='BLOCKED',runtime='NOT TESTED',reason=reason) for name,reason in BLOCKED.items()]


def collect_all(dest):
    """One owner command, no overwrites. Existing bundles must match raw input."""
    case=json.loads((dest/'case.json').read_text(encoding='utf-8'))
    configuration(dest/'User')
    for path in (dest/'User').rglob('*'):private(path,dest)
    collected=[];retained=[];missing=[]
    # Check all collisions before writing any new evidence.
    for label in case['captures']:
        raw=private(dest/(label+'.sav'),dest)
        saved=dest/'captures'/label
        if saved.exists():
            manifest=json.loads((saved/'manifest.json').read_text(encoding='utf-8'))
            if raw.exists() and sha(raw)!=manifest['state_sha256']:
                raise ValueError('raw state differs from immutable capture: '+label+'; prepare a NEW trial')
    for label in case['captures']:
        raw=dest/(label+'.sav')
        if (dest/'captures'/label).exists(): retained.append(label)
        elif raw.is_file():
            collect(dest,label,raw,dest/'User/GameSettings/GFEE01.ini',profile=dest/'User');collected.append(label)
        else:missing.append(label)
    return dict(collected=collected,retained=retained,missing_raw_states=missing,review=review(dest))


def verified_readiness(dest):
    path = dest / 'observations.json'
    record = json.loads(path.read_text(encoding='utf-8')) if path.is_file() else {}
    operators = {v['operator'] for v in record.get('attribution', {}).values()}
    return 'RUNTIME_VERIFIED' if 'agent' in operators else 'HUMAN_VERIFIED'


def observe(dest, passed, failed, notes, operator='human'):
    if operator not in ('human', 'agent'):
        raise ValueError('operator must be human or agent')
    case = json.loads((dest / 'case.json').read_text(encoding='utf-8'))
    allowed = set(case['observations'])
    if (set(passed) | set(failed)) - allowed or set(passed) & set(failed):
        raise ValueError('use declared observation names; cannot mark one both passed and failed')
    path = dest / 'observations.json'
    record = json.loads(path.read_text(encoding='utf-8'))
    attribution = record.setdefault('attribution', {})
    # Older declarations came from the owner. Preserve their attribution when
    # an agent adds a different check or a note to the same trial.
    for key, value in record['observed'].items():
        if value is not None:
            attribution.setdefault(key, dict(operator='human', method='manual'))
    author = dict(operator=operator, method='computer_use' if operator == 'agent' else 'manual')
    for key in passed:
        record['observed'][key] = True
        attribution[key] = dict(author)
    for key in failed:
        record['observed'][key] = False
        attribution[key] = dict(author)
    record.setdefault('declarations', []).append(dict(**author, passed=list(passed), failed=list(failed), notes=notes))
    if notes:
        record['notes'] += ('\n' if record['notes'] else '') + notes
    # Preserve each declaration as an exclusive immutable revision.
    history = dest / 'observation-history'
    history.mkdir(exist_ok=True)
    write_json(history / (str(len(list(history.glob('*.json'))) + 1).zfill(4) + '.json'), record)
    path.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial', default='human_v1', help='named independent work/scenarios/ trial')
    sub = parser.add_subparsers(dest='mode', required=True)
    sub.add_parser('list')
    p = sub.add_parser('prepare'); p.add_argument('--root', type=Path)
    p = sub.add_parser('check'); p.add_argument('name'); p.add_argument('--fresh-boot', action='store_true')
    p = sub.add_parser('capture'); p.add_argument('name'); p.add_argument('label'); p.add_argument('state', type=Path)
    p = sub.add_parser('review'); p.add_argument('name')
    p = sub.add_parser('collect'); p.add_argument('name')
    p.add_argument('--passed',action='append',default=[]);p.add_argument('--failed',action='append',default=[]);p.add_argument('--notes',default='')
    p.add_argument('--operator', choices=('human','agent'), default='human')
    p = sub.add_parser('observe'); p.add_argument('name'); p.add_argument('--passed', action='append', default=[])
    p.add_argument('--failed', action='append', default=[]); p.add_argument('--notes', default='')
    p.add_argument('--operator', choices=('human','agent'), default='human')
    args = parser.parse_args()
    try:
        if not re.fullmatch(r'[A-Za-z0-9_-]+',args.trial):
            raise ValueError('trial must be a plain directory name')
        package = ROOT / 'work/scenarios' / args.trial
        if args.mode == 'list':
            result = listing(package)
        elif args.mode == 'prepare':
            destination = args.root or package
            result = prepare(destination)
            from tools.escape_scenarios import prepare as prepare_escape
            for name in ESCAPES:
                prepare_escape(name, destination / DIRECTORIES.get(name,name))
            result['prepared'] += list(ESCAPES)
        elif args.mode == 'check': result = check(args.name, args.fresh_boot, root=package)
        else:
            if args.name not in known():
                raise ValueError('unknown or blocked scenario')
            dest = scenario_dir(args.name,root=package)
            if args.mode == 'capture':
                configuration(dest / 'User')
                for path in (dest / 'User').rglob('*'): private(path, dest)
                result = collect(dest, args.label, args.state, dest / 'User/GameSettings/GFEE01.ini', profile=dest / 'User')
            elif args.mode == 'observe': result = observe(dest, args.passed, args.failed, args.notes, args.operator)
            elif args.mode == 'collect':
                if args.passed or args.failed or args.notes: observe(dest,args.passed,args.failed,args.notes,args.operator)
                result=collect_all(dest)
            else: result = review(dest)
    except (ValueError, OSError, KeyError, configparser.Error) as exc:
        print(json.dumps({'status': 'REFUSED', 'reason': str(exc)}))
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return int(isinstance(result, dict) and (result.get('status') == 'FAIL' or result.get('review',{}).get('status')=='FAIL'))


if __name__ == '__main__':
    raise SystemExit(main())
