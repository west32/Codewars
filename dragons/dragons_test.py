import unittest
from dragons import hero

class TestHero(unittest.TestCase):

    def test_hero(self):
        self.assertEqual(hero(10, 5), True)
        self.assertEqual(hero(7, 4), False)
        self.assertEqual(hero(4, 5), False)
        self.assertEqual(hero(100, 40), True)
        self.assertEqual(hero(1500, 751), False)
        self.assertEqual(hero(0, 1), False)