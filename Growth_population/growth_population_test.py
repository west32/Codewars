import unittest
from growth_population import nb_year

class PupulationTest(unittest.TestCase):

    def test_nb_year(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)