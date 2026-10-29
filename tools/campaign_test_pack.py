"""Generate manual campaign cases and collect evidence; never drives Dolphin.

Only the narrow post-Talk Kieran Wait case has an automated gameplay verdict.
Other cases collect evidence for review, never promote the campaign ledger.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

from tools.install_codes import ROOT, validate_ini
from tools.campaign_snapshot import capture, differences
from tools.netplay_package import fingerprint
from tools.verify_game import DEFAULT_IMAGE

CATALOG = ROOT / 'campaign/manual_cases.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, data):
    with path.open('x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write('\n')


def work_destination(path):
    path = path.resolve()
    if (ROOT / 'work').resolve() not in path.parents:
        raise ValueError('destination must be a NEW directory inside this clone work/')
    if path.exists():
        raise ValueError('refusing to overwrite existing test directory')
    return path


def cases(ledger, targeted):
    rows = list(targeted)
    for chapter in ledger['chapters']:
        key = chapter['key']
        final = key == ledger['chapters'][-1]['key']
        labels = ['prep', 'before_clear', 'after_clear', 'reloaded']
        if not final:
            labels.insert(3, 'next_prep')
        rows.append({
            'id': 'campaign-' + re.sub(r'[^A-Za-z0-9_-]', '_', key), 'title': chapter['title'] + ' full clear and persistence',
            'chapter_key': key, 'priority': 3, 'readiness': 'NEEDS_NATURAL_SAVE',
            'classification': 'naturally_progressed_required', 'captures': labels,
            'observations': ['natural_history', 'original_objective', 'expected_roster', 'fresh_card_reload', 'no_unexpected_behavior'],
            'steps': [
                'Use a separately copied, naturally progressed card with stable COOP-P6 + EXP-16 only; fresh boot. Record difficulty and prior story/recruitment choices.',
                'Capture prep (or the first controllable map if no preparations). Record every deployed/benched permanent PID, forced deployment, cap, ownership and inventory.',
                'Play the original objective. Exercise Blue and Yellow actions, native NPC/partner phases and original turn reinforcements. Capture any unexpected event separately.',
                'Capture before_clear immediately before the final original objective action; then after_clear at the first stable post-clear screen. Record the action, deaths, escape order, recruits and scripted departures.',
                ('For Endgame, observe original ending/credits and capture the first available stable completion state; record whether the game offers any native save. Do not invent a postgame roster screen.' if final else
                 'Let original story cleanup finish. Save only to an unused disposable card slot; reach next preparations and capture next_prep. Compare against expected story departures and recruits, not exact whole-roster equality.'),
                'Close Dolphin. Fresh boot the SAME disposable profile/card without loading a state. Load the new native save and capture reloaded at the equivalent screen. If no native save is offered, record this checkpoint as unavailable; do not substitute savestate restore.',
            ], 'acceptance': 'Human review of original objective/cleanup plus persistent living roster, expected story transfers, ownership, progression and items. Synthetic clears cannot certify natural campaign continuity.'
        })
    ids = [r['id'] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate test IDs')
    for row in rows:
        if not re.fullmatch(r'[A-Za-z0-9_-]+', row['id']) or not row['captures']:
            raise ValueError('invalid case ID or missing capture labels')
        if len(row['captures']) != len(set(row['captures'])) or any(
                not re.fullmatch(r'[A-Za-z0-9_-]+', label) for label in row['captures']):
            raise ValueError('invalid or duplicate capture labels')
    return rows


def prepare(root, ledger_path=ROOT / 'campaign/verification.json', catalog_path=CATALOG):
    root = work_destination(root)
    rows = cases(json.loads(ledger_path.read_text(encoding='utf-8')),
                 json.loads(catalog_path.read_text(encoding='utf-8')))
    root.mkdir(parents=True)
    index = ['# Manual campaign test pack', '',
             'Start with CH10-PARTNER-WAIT. Later cases require suitable saves; this pack does not generate missing story history.',
             'No emulator launch/input occurs. See docs/CAMPAIGN_MANUAL_TESTS.md for exact commands and capture handling.', '',
             '| Case | Priority | Availability |', '|---|---|---|']
    for row in rows:
        dest = root / row['id']
        dest.mkdir()
        write_json(dest / 'case.json', row)
        write_json(dest / 'observations.json', {
            'observed': {k: None for k in row['observations']},
            'notes': '', 'difficulty': '', 'source_history': '',
            'runtime_commit': '', 'machine': '', 'expected_story_changes': []})
        content = ['# ' + row['title'], '', 'Availability: ' + row['readiness'], '',
                   'Classification: ' + row['classification'], '',
                   'Save captures with these exact labels: ' + ', '.join(row['captures']), '']
        content += [f'{i}. {step}' for i, step in enumerate(row['steps'], 1)]
        content += ['', 'Acceptance: ' + row['acceptance'], '',
                    'Fill observations.json only after performing the actions. Leave unobserved values null. Record failures as false.',
                    'A state comparison cannot prove which controller pressed a button, that the original UI ran, or that natural history exists.']
        (dest / 'README.md').write_text('\n'.join(content) + '\n', encoding='utf-8')
        index.append(f"| [{row['id']}]({row['id']}/README.md) | {row['priority']} | {row['readiness']} |")
    (root / 'README.md').write_text('\n'.join(index) + '\n', encoding='utf-8')
    return {'cases': len(rows), 'root': str(root), 'status': 'NOT TESTED'}


def prepare_partner(root, source):
    """Copy a validated post-Talk state/card; add no codes and edit no RAM."""
    from tools.ch10_talk_fixture import verify as verify_talk
    from tools.netplay_setup import make_user
    from tools.setup_pads import PORT1_KEYBOARD, PORT2_KEYBOARD
    root = work_destination(root)
    source = source.resolve()
    config = source / 'User/GameSettings/GFEE01.ini'
    text = config.read_text()
    size = validate_ini(text)
    # Consume byte-identical accepted before/after event evidence; never infer Talk
    # observation here. The copied seed only supplies post-event setup conditions.
    before = capture(source / 'before.s02.sav', DEFAULT_IMAGE, config, 'source-analysis')
    after = capture(source / 'after.s02.sav', DEFAULT_IMAGE, config, 'source-analysis')
    result = verify_talk(before, after, observed=False)
    if result['failures']:
        raise ValueError('source Talk state effects rejected: ' + '; '.join(result['failures']))
    cards = sorted((source / 'User/GC/USA/Card A').glob('*.gci'))
    if not cards:
        raise ValueError('source private GCI missing')
    files = [source / 'after.s02.sav', config, *cards]
    bindings = source / 'User/Config/GCPadNew.ini'
    if bindings.exists():
        files.append(bindings)
    original = {str(p): sha(p) for p in files}
    root.mkdir(parents=True)
    make_user(root / 'User', DEFAULT_IMAGE.parent, 'EXPERIMENTAL Ch10 partner action',
              PORT1_KEYBOARD, text, pad2=PORT2_KEYBOARD)
    if bindings.exists():
        (root / 'User/Config/GCPadNew.ini').write_bytes(bindings.read_bytes())
    for card in cards:
        with (root / 'User/GC/USA/Card A' / card.name).open('xb') as stream:
            stream.write(card.read_bytes())
    with (root / 'seed.s02.sav').open('xb') as stream:
        stream.write((source / 'after.s02.sav').read_bytes())
    if any(sha(Path(path)) != value for path, value in original.items()):
        raise ValueError('source changed during copy; do not launch this candidate')
    record = {'classification': 'synthetic_ch10_post_talk', 'status': 'NOT TESTED',
              'gecko_bytes': size, 'fingerprint': fingerprint(text),
              'source_hashes': original, 'seed_sha256': sha(root / 'seed.s02.sav'),
              'limits': 'No new positioning, flag, faction or gameplay edit. Original fixture hook remains installed and its consumed-key guard should skip setup. Native save may refuse inherited card identity; that is fixture INCONCLUSIVE, not proof of a campaign failure.'}
    write_json(root / 'fixture.json', record)
    workspace = str(ROOT).replace("'", "''")
    (root / 'Launch.ps1').write_text(
        "$ErrorActionPreference = 'Stop'\n$workspace = '" + workspace + "'\n"
        "$exe = Join-Path $workspace 'Dolphin-x64/Dolphin.exe'\n"
        "$image = Join-Path $workspace 'Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso'\n"
        "& $exe --user (Join-Path $PSScriptRoot 'User') --exec $image --save_state (Join-Path $PSScriptRoot 'seed.s02.sav')\n",
        encoding='utf-8')
    (root / 'Boot-Native.ps1').write_text(
        "$ErrorActionPreference = 'Stop'\n$workspace = '" + workspace + "'\n"
        "$exe = Join-Path $workspace 'Dolphin-x64/Dolphin.exe'\n"
        "$image = Join-Path $workspace 'Dolphin-x64/Games/Fire Emblem - Path of Radiance (USA).ciso'\n"
        "& $exe --user (Join-Path $PSScriptRoot 'User') --exec $image\n",
        encoding='utf-8')
    return record


def collect(case_dir, label, state, ini, image=DEFAULT_IMAGE, *, profile=None):
    case_dir = case_dir.resolve()
    if (ROOT / 'work').resolve() not in case_dir.parents:
        raise ValueError('case directory must be inside this clone work/')
    case = json.loads((case_dir / 'case.json').read_text(encoding='utf-8'))
    if label not in case['captures']:
        raise ValueError('capture label not declared in case')
    text = ini.read_text()
    size = validate_ini(text)
    dest = case_dir / 'captures' / label
    if dest.exists():
        raise ValueError('refusing to replace captured evidence')
    original_state, original_ini = sha(state), sha(ini)
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    snapshot = capture(state, image, ini, commit)
    if snapshot['evidence']['state_sha256'] != original_state:
        raise ValueError('source state changed while being decoded')
    dest.mkdir(parents=True)
    # Raw state and exact intended INI preserved; only new files are written.
    for original, name in ((state, 'state.sav'), (ini, 'GFEE01.ini')):
        with (dest / name).open('xb') as stream:
            stream.write(original.read_bytes())
    if sha(dest / 'state.sav') != original_state or sha(dest / 'GFEE01.ini') != original_ini or sha(ini) != original_ini:
        raise ValueError('source changed during capture; evidence rejected')
    write_json(dest / 'snapshot.json', snapshot)
    profile_files = {}
    if profile is not None:
        profile = profile.resolve()
        if case_dir not in profile.parents:
            raise ValueError('capture profile must belong to the private case')
        sources = [profile / 'Config/Dolphin.ini', profile / 'Config/GCPadNew.ini',
                   *sorted(p for p in (profile / 'GC').rglob('*') if p.is_file())]
        for path in sources:
            if profile not in path.resolve().parents:
                raise ValueError('profile evidence points outside private storage')
            relative = Path('profile') / path.relative_to(profile)
            target = dest / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            digest = sha(path)
            with target.open('xb') as stream: stream.write(path.read_bytes())
            if sha(target) != digest or sha(path) != digest:
                raise ValueError('profile/card changed during evidence capture')
            profile_files[str(relative)] = digest
    write_json(dest / 'manifest.json', {'source_state': str(state.resolve()), 'state_sha256': original_state,
                                      'ini_sha256': original_ini, 'gecko_bytes': size,
                                      'snapshot_sha256': sha(dest / 'snapshot.json'),
                                      'profile_files': profile_files,
                                      'analysis_commit': commit, 'runtime_commit': 'declare separately in observations.json'})
    return {'written': str(dest), 'live_c2_verified': snapshot['evidence']['intended_c2_verified'],
            'gecko_bytes': size, 'status': 'INCONCLUSIVE', 'scope': 'evidence capture only; no gameplay acceptance'}


def verify_partner_wait(before, after, observed):
    failures = []
    expected = {'COOP-P6', 'EXP-16', 'FIXTURE-LOADER', 'DBG-CAMP-TALK'}
    for label, snap in (('before', before), ('after', after)):
        game, evidence = snap['game'], snap['evidence']
        if not evidence.get('intended_c2_verified'):
            failures.append(label + ': live hooks unverified')
        if {n.split()[0] for n in evidence.get('codes', [])} != expected:
            failures.append(label + ': unexpected codes')
        if evidence.get('codes_fingerprint') != 'c11089d39a0fe037':
            failures.append(label + ': expected prepared post-Talk fingerprint')
        scripts = game.get('event_scripts', {})
        if (game['chapter'], game['phase'], game['turn']) != (11, 3, 1) or game['control'][3] != 1:
            failures.append(label + ': expected turn1 Chapter10 human Yellow')
        if not scripts.get('complete_chain') or scripts.get('campaign_ids') != [11] or not scripts.get('chapter_matches'):
            failures.append(label + ': original loaded C11 unverified')
    for key in ('codes_fingerprint', 'dolphin'):
        if before['evidence'].get(key) != after['evidence'].get(key):
            failures.append('configuration mismatch: ' + key)
    hashes = [s['evidence'].get('state_sha256') for s in (before, after)]
    if not all(hashes) or hashes[0] == hashes[1]:
        failures.append('distinct state hashes required')
    left, right = before['game']['units'], after['game']['units']
    targets = [u for u in left if u['pid'] == 'PID_KEVIN']
    if len(targets) != 1 or len([u for u in right if u['pid'] == 'PID_KEVIN']) != 1:
        failures.append('exactly one Kieran required in both captures')
    else:
        a = targets[0]
        b = next(u for u in right if u['pid'] == 'PID_KEVIN')
        if a['force'] != 3 or a['hp'] <= 0 or a['death_record'] or a['flags'] & 1:
            failures.append('before Kieran must be living unacted Yellow')
        if a['slot'] != 19 or a['xy'] != [20, 19] or a['rescue_link']:
            failures.append('before Kieran differs from prepared inside-cell fixture')
        if b['flags'] != a['flags'] | 1:
            failures.append('Kieran must acquire only acted bit')
        normalized = json.loads(json.dumps(right))
        next(u for u in normalized if u['pid'] == 'PID_KEVIN')['flags'] = a['flags']
        if left != normalized:
            failures.append('Wait changed additional roster fields')
    from tools.talk_evidence import CONVERSATION_KEY
    for snap in (before, after):
        if snap['game'].get('talk_fixture', {}).get('flags', {}).get(CONVERSATION_KEY) is not True:
            failures.append('original Talk key must remain set')
    for key in ('flags', 'cell_door'):
        if before['game'].get('talk_fixture', {}).get(key) != after['game'].get('talk_fixture', {}).get(key):
            failures.append('door/chapter/conversation state changed')
    if before['game'].get('event_flags') != after['game'].get('event_flags'):
        failures.append('registered event flags changed during Wait')
    declined = [key for key, value in observed.items() if value is False]
    failures += ['human reported failed check: ' + key for key in declined]
    return {'status': 'FAIL' if failures else 'PASS' if observed and all(v is True for v in observed.values()) else 'INCONCLUSIVE',
            'failures': failures, 'scope': 'original P2 Kieran Wait/P1 lockout local effect after synthetic Talk only',
            'excludes': ['permanent recruitment', 'escape', 'chapter clear/transition', 'native save/reload', 'Netplay']}


def review(case_dir):
    case = json.loads((case_dir / 'case.json').read_text(encoding='utf-8'))
    observations = json.loads((case_dir / 'observations.json').read_text(encoding='utf-8'))
    snapshots, missing, failures, unverified = {}, [], [], []
    for label in case['captures']:
        dest = case_dir / 'captures' / label
        if not (dest / 'snapshot.json').exists():
            missing.append(label)
            continue
        manifest = json.loads((dest / 'manifest.json').read_text(encoding='utf-8'))
        for relative, digest in manifest.get('profile_files', {}).items():
            path = (dest / relative).resolve()
            if dest.resolve() not in path.parents or sha(path) != digest:
                failures.append(label + ': profile/card artifact mismatch')
        if not manifest.get('snapshot_sha256'):
            unverified.append(label)
        elif sha(dest / 'snapshot.json') != manifest['snapshot_sha256']:
            failures.append(label + ': decoded snapshot hash mismatch')
        if sha(dest / 'state.sav') != manifest['state_sha256'] or sha(dest / 'GFEE01.ini') != manifest['ini_sha256']:
            failures.append(label + ': artifact hash mismatch')
        snapshots[label] = json.loads((dest / 'snapshot.json').read_text(encoding='utf-8'))
        if snapshots[label]['evidence'].get('state_sha256') != manifest['state_sha256']:
            failures.append(label + ': snapshot state hash mismatch')
        if not snapshots[label]['evidence'].get('intended_c2_verified'):
            failures.append(label + ': live C2 bodies unverified')
    observed = {k: observations.get('observed', {}).get(k) for k in case['observations']}
    refused_card = case['id'] == 'CH10-NATIVE-RESUME' and observed.get('native_suspend_accepted') is False
    failures += ['human reported failed check: ' + k for k, value in observed.items() if value is False and not (refused_card and k == 'native_suspend_accepted')]
    if refused_card and not failures:
        return {'status': 'INCONCLUSIVE', 'reason': 'Original Suspend refused; inherited card identity is unverified. Preserve exact refusal screenshot; do not spoof identity.', 'missing_captures': missing}
    if failures or missing:
        return {'status': 'FAIL' if failures else 'NOT TESTED' if not snapshots else 'INCONCLUSIVE',
                'failures': failures, 'missing_captures': missing}
    if unverified:
        return {'status': 'INCONCLUSIVE', 'failures': [], 'unverified_snapshot_digests': unverified,
                'scope': 'legacy evidence readable but decoded analysis integrity unverified; recollect into a NEW case directory, never edit the old bundle'}
    if case['id'] == 'CH10-PARTNER-WAIT':
        return verify_partner_wait(snapshots['before'], snapshots['after'], observed)
    if case['id'] == 'CH10-PRISONER-ESCAPE':
        from tools.scenario_verdicts import prisoner_escape
        return prisoner_escape(snapshots['before'], snapshots['after'], observed)
    if case['id'] in ('CH10-NATIVE-RESUME','CH6-IKE-COMPLETE'):
        from tools.scenario_verdicts import native_resume, ch6_completion
        verified_write=False
        # The pre-test baseline is immutable, unlike a card copied after play.
        # Existing capture/profile hashes were checked above. Never infer native
        # reload from a changed card without the separate human observations.
        if (case_dir / 'scenario.json').is_file():
            setup=json.loads((case_dir / 'scenario.json').read_text(encoding='utf-8'))
            baseline=setup.get('initial_cards',{})
            original_ok=bool(baseline) and all(
                sha(case_dir/'card-before'/name)==digest and
                setup.get('pinned',{}).get(str(Path('card-before')/name))==digest
                for name,digest in baseline.items())
            final_label='reloaded' if case['id']=='CH6-IKE-COMPLETE' else 'after'
            manifest=json.loads((case_dir/'captures'/final_label/'manifest.json').read_text(encoding='utf-8'))
            cards={Path(path.replace('\\','/')).name:digest for path,digest in manifest.get('profile_files',{}).items()
                   if path.replace('\\','/').startswith('profile/GC/USA/Card A/') and path.lower().endswith('.gci')}
            verified_write=original_ok and set(cards)==set(baseline) and any(cards[name]!=baseline[name] for name in baseline)
        return ch6_completion(snapshots,observed,verified_write) if case['id']=='CH6-IKE-COMPLETE' else native_resume(snapshots['before'],snapshots['after'],observed,verified_write)
    labels = case['captures']
    return {'status': 'INCONCLUSIVE', 'failures': [],
            'scope': 'complete evidence bundle awaiting event-specific human/engineering review; no campaign acceptance',
            'missing_observations': [k for k, v in observed.items() if v is not True],
            'capture_changes': {a + ' -> ' + b: differences(snapshots[a], snapshots[b]) for a, b in zip(labels, labels[1:])}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='mode', required=True)
    p = sub.add_parser('prepare'); p.add_argument('--root', type=Path, required=True)
    p = sub.add_parser('partner-profile'); p.add_argument('--root', type=Path, required=True)
    p.add_argument('--source', type=Path, default=ROOT / 'work/fixtures/ch10_oscar_kieran_v1')
    p = sub.add_parser('capture'); p.add_argument('case', type=Path); p.add_argument('label')
    p.add_argument('state', type=Path); p.add_argument('--ini', type=Path, required=True)
    p = sub.add_parser('review'); p.add_argument('case', type=Path)
    args = parser.parse_args()
    try:
        if args.mode == 'prepare': result = prepare(args.root)
        elif args.mode == 'partner-profile': result = prepare_partner(args.root, args.source)
        elif args.mode == 'capture': result = collect(args.case, args.label, args.state, args.ini)
        else: result = review(args.case)
    except (ValueError, OSError, KeyError) as exc:
        print('REFUSED: ' + str(exc))
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return int(result.get('status') == 'FAIL')


if __name__ == '__main__':
    raise SystemExit(main())
