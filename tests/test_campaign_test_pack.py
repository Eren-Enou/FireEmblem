import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tests.test_ch10_talk import sample
from tools.campaign_test_pack import cases, prepare, review, verify_partner_wait, work_destination


def wait_pair():
    before, _ = sample()
    before['game']['units'][0]['flags'] |= 1
    before['game']['units'][1]['force'] = 3
    before['game']['units'][1]['flags'] = 0x80000
    before['evidence']['codes_fingerprint'] = 'c11089d39a0fe037'
    from tools.talk_evidence import CONVERSATION_KEY
    before['game']['talk_fixture']['flags'][CONVERSATION_KEY] = True
    after = copy.deepcopy(before)
    after['evidence']['state_sha256'] = 'after'
    after['game']['units'][1]['flags'] |= 1
    return before, after


class CampaignTestPackTests(unittest.TestCase):
    def test_wait_requires_human_port_and_original_ui_observations(self):
        a, b = wait_pair()
        self.assertEqual(verify_partner_wait(a, b, {})['status'], 'INCONCLUSIVE')
        self.assertEqual(verify_partner_wait(a, b, {'p1': True, 'p2': None})['status'], 'INCONCLUSIVE')
        self.assertEqual(verify_partner_wait(a, b, {'p1': True, 'p2': True})['status'], 'PASS')
        self.assertEqual(verify_partner_wait(a, b, {'p1': False, 'p2': True})['status'], 'FAIL')

    def test_wait_rejects_unit_loss_and_unrelated_changes(self):
        for change in ('missing', 'duplicate', 'force', 'hp', 'items', 'oscar', 'no_action', 'extra_flag', 'rescue'):
            a, b = wait_pair()
            target = b['game']['units'][1]
            if change == 'missing': b['game']['units'].pop()
            elif change == 'duplicate': b['game']['units'].append(copy.deepcopy(target))
            elif change == 'force': target['force'] = 0
            elif change == 'hp': target['hp'] -= 1
            elif change == 'items': target['inventory_slots_hex'] = '00' * 64
            elif change == 'oscar': b['game']['units'][0]['exp'] += 1
            elif change == 'no_action': target['flags'] &= ~1
            elif change == 'extra_flag': target['flags'] |= 0x4000
            elif change == 'rescue': target['rescue_link'] = 123
            with self.subTest(change=change):
                self.assertEqual(verify_partner_wait(a, b, {'observed': True})['status'], 'FAIL')

    def test_wait_rejects_wrong_script_stale_hooks_and_consumed_state_reuse(self):
        from tools.talk_evidence import CONVERSATION_KEY
        for change in ('script', 'hooks', 'same_state', 'code', 'turn', 'key', 'door'):
            a, b = wait_pair()
            if change == 'script': b['game']['event_scripts']['campaign_ids'] = [7]
            elif change == 'hooks': b['evidence']['intended_c2_verified'] = False
            elif change == 'same_state': b['evidence']['state_sha256'] = a['evidence']['state_sha256']
            elif change == 'code': b['evidence']['codes'].append('DBG-01')
            elif change == 'turn': b['game']['turn'] = 2
            elif change == 'key': b['game']['talk_fixture']['flags'][CONVERSATION_KEY] = False
            elif change == 'door': b['game']['talk_fixture']['cell_door']['state_byte'] |= 2
            with self.subTest(change=change):
                self.assertEqual(verify_partner_wait(a, b, {'observed': True})['status'], 'FAIL')

    def test_catalog_covers_every_ledger_stage_without_claiming_fixtures(self):
        ledger = json.loads(Path('campaign/verification.json').read_text(encoding='utf-8'))
        targeted = json.loads(Path('campaign/manual_cases.json').read_text())
        rows = cases(ledger, targeted)
        campaign = [r for r in rows if r['id'].startswith('campaign-')]
        self.assertEqual({r['chapter_key'] for r in campaign}, {r['key'] for r in ledger['chapters']})
        self.assertTrue(all(r['readiness'] == 'NEEDS_NATURAL_SAVE' for r in campaign))
        self.assertNotIn('next_prep', campaign[-1]['captures'])
        self.assertEqual(len(rows), len(targeted) + len(ledger['chapters']))

    def test_invalid_paths_and_duplicate_ids_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch('tools.campaign_test_pack.ROOT', root):
                with self.assertRaises(ValueError): work_destination(root / 'private-card')
                (root / 'work/existing').mkdir(parents=True)
                with self.assertRaises(ValueError): work_destination(root / 'work/existing')
        with self.assertRaises(ValueError):
            cases({'chapters': []}, [{'id': '../escape', 'captures': ['before']}])
        with self.assertRaises(ValueError):
            cases({'chapters': []}, [{'id': 'same', 'captures': ['before']}] * 2)

    def test_unrun_pack_review_is_not_tested_and_existing_pack_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            ledger = root / 'ledger.json'
            catalog = root / 'cases.json'
            ledger.write_text('{"chapters": []}')
            catalog.write_text(json.dumps([{'id': 'EXAMPLE', 'title': 'Example', 'priority': 1,
                'readiness': 'BLOCKED', 'classification': 'synthetic', 'captures': ['before', 'after'],
                'observations': ['original_ui'], 'steps': ['Wait for a fixture'], 'acceptance': 'review required'}]))
            with patch('tools.campaign_test_pack.ROOT', root):
                prepare(root / 'work/pack', ledger, catalog)
                result = review(root / 'work/pack/EXAMPLE')
                self.assertEqual(result['status'], 'NOT TESTED')
                self.assertEqual(result['missing_captures'], ['before', 'after'])
                with self.assertRaises(ValueError): prepare(root / 'work/pack', ledger, catalog)

    def test_generic_complete_bundle_never_automatically_passes_and_tampering_fails(self):
        from tools.campaign_test_pack import sha, write_json
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_json(root / 'case.json', {'id': 'GENERIC', 'captures': ['before', 'after'], 'observations': ['original_ui']})
            write_json(root / 'observations.json', {'observed': {'original_ui': True}})
            pair = wait_pair()
            for label, snap in zip(('before', 'after'), pair):
                dest = root / 'captures' / label
                dest.mkdir(parents=True)
                (dest / 'state.sav').write_bytes(label.encode())
                (dest / 'GFEE01.ini').write_text('exact config')
                snap['evidence']['state_sha256'] = sha(dest / 'state.sav')
                write_json(dest / 'snapshot.json', snap)
                write_json(dest / 'manifest.json', {'state_sha256': sha(dest / 'state.sav'), 'ini_sha256': sha(dest / 'GFEE01.ini')})
            self.assertEqual(review(root)['status'], 'INCONCLUSIVE')
            (root / 'captures/after/state.sav').write_bytes(b'changed evidence')
            result = review(root)
            self.assertEqual(result['status'], 'FAIL')
            self.assertIn('after: artifact hash mismatch', result['failures'])

    @unittest.skipUnless(Path('work/fixtures/ch10_partner_actions_v1/fixture.json').exists(), 'private fixture absent')
    def test_prepared_partner_seed_is_byte_identical_and_preserves_sources(self):
        from tools.campaign_test_pack import sha
        root = Path('work/fixtures/ch10_partner_actions_v1')
        record = json.loads((root / 'fixture.json').read_text())
        self.assertEqual(record['gecko_bytes'], 3240)
        self.assertEqual(record['fingerprint'], 'c11089d39a0fe037')
        self.assertEqual(sha(root / 'seed.s02.sav'), '558cfc791b073e8f1cd39f8d7cf3bc85aee95b14e95059c909ce334693ca9a74')
        for path, expected in record['source_hashes'].items():
            self.assertEqual(sha(Path(path)), expected)


if __name__ == '__main__':
    unittest.main()
