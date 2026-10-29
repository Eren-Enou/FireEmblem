import json
import unittest
from pathlib import Path
from tools.campaign_graph import build, route, summary
from tools.fe9.disc import DiscReader
from tools.fe9.events import functions, instructions
from tools.verify_game import DEFAULT_IMAGE


@unittest.skipUnless(DEFAULT_IMAGE.exists(), 'pinned image absent')
class CampaignGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.disc = DiscReader(DEFAULT_IMAGE)
        cls.graph = build(cls.disc, json.loads(Path('campaign/verification.json').read_text(encoding='utf-8')))

    @classmethod
    def tearDownClass(cls): cls.disc.close()

    def test_real_containers_special_maps_and_separate_stage_contracts(self):
        self.assertEqual(summary(self.graph)['scripts'], 43)
        self.assertEqual(summary(self.graph)['chapter_stage_contracts'], 34)
        self.assertIn('Scripts/ending.cmb', self.graph['nodes'])
        for key in ('18.1','18.2','18.3','18.4','29','31'):
            self.assertIn('chapter:'+key, self.graph['nodes'])
        self.assertIn('Ch.27-2', self.graph['nodes']['chapter:29']['title'])

    def test_every_call_site_is_an_original_aligned_instruction(self):
        aligned = {}
        for node in self.graph['nodes'].values():
            if node['type'] != 'call_site': continue
            path = node['script']
            if path not in aligned:
                raw = self.disc.read_file(path)
                aligned[path] = {i['offset']:i['opcode'] for f in functions(raw) for i in instructions(raw, f)}
            self.assertEqual(aligned[path][node['offset']], 0x38)

    def test_cross_chapter_route_does_not_skip_unresolved_native_gate(self):
        a = route(self.graph, 'chapter:11', 'Scripts/C12.cmb')
        self.assertEqual(a['status'], 'NO ESTABLISHED PATH')
        self.assertTrue(a['unresolved_frontier'])
        b = route(self.graph, 'chapter:11', 'Scripts/C12.cmb', allow_unresolved=True)
        self.assertEqual(b['status'], 'INCONCLUSIVE')
        self.assertTrue(any(e['kind']=='unresolved_completion_dispatch' for e in b['path']))

    def test_stage_and_endgame_do_not_invent_complete_forward_routes(self):
        self.assertEqual(route(self.graph,'chapter:18.1','chapter:18.4',allow_unresolved=True)['status'], 'NO ESTABLISHED PATH')
        self.assertFalse(any(e['target']=='Scripts/C32.cmb' for e in self.graph['edges']))
        self.assertFalse(any(e['source']=='native_chapter_step:28' and e['kind']=='conditional_native_increment_target'
                             for e in self.graph['edges']))
        with self.assertRaisesRegex(ValueError, 'unknown'): route(self.graph, 'invented', 'chapter:11')

    def test_runtime_acceptance_does_not_promote_static_graph_connections(self):
        edges = [e for e in self.graph['edges'] if e['source']=='chapter:11']
        self.assertTrue(all(e['level'] in ('STATICALLY VERIFIED','UNRESOLVED') for e in edges))
