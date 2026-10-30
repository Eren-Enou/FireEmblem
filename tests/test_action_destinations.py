import unittest
from tools.action_scenarios import destinations


class OrderedNativeDestinationTests(unittest.TestCase):
    def setUp(self):
        self.units=[dict(pid='guard',slot=9,xy=[13,25]),dict(pid='rhys',slot=14,xy=[14,8])]
        self.cells={(15,13):dict(occupant_id=0,edge_mask=15),
                    (13,25):dict(occupant_id=9,edge_mask=15)}

    def test_explicit_earlier_move_can_vacate_a_later_destination(self):
        self.assertEqual(len(destinations({'guard':(15,13),'rhys':(13,25)},self.units,
                                         lambda x,y:self.cells[x,y])),2)

    def test_later_move_and_unrelated_occupancy_cannot_be_assumed_away(self):
        with self.assertRaisesRegex(ValueError,'occupied'):
            destinations({'rhys':(13,25),'guard':(15,13)},self.units,lambda x,y:self.cells[x,y])
        self.cells[15,13]['occupant_id']=20
        with self.assertRaisesRegex(ValueError,'occupied'):
            destinations({'guard':(15,13),'rhys':(13,25)},self.units,lambda x,y:self.cells[x,y])

    def test_duplicates_missing_identity_and_invalid_edges_refused(self):
        for positions in ({'guard':(15,13),'rhys':(15,13)},{'unknown':(15,13)}):
            with self.assertRaises(ValueError):destinations(positions,self.units,lambda x,y:self.cells[x,y])
        self.cells[15,13]['edge_mask']=0
        with self.assertRaisesRegex(ValueError,'edge'):
            destinations({'guard':(15,13)},self.units,lambda x,y:self.cells[x,y])

    def test_source_record_cannot_vacate_a_different_grid_occupant(self):
        self.cells[13,25]['occupant_id']=20
        with self.assertRaisesRegex(ValueError,'occupied'):
            destinations({'guard':(15,13),'rhys':(13,25)},self.units,lambda x,y:self.cells[x,y])
