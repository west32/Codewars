import unittest
from tower import tower_builder

class TowerTest(unittest.TestCase):

    def test_tower_bulider(self):
        self.assertEqual(tower_builder(1), ['*', ])
        self.assertEqual(tower_builder(2), [' * ', '***'])
        self.assertEquals(tower_builder(3), ['  *  ', ' *** ', '*****'])