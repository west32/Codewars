import unittest
from stray_number import stray

class StrayTest(unittest.TestCase):

    def test_stray(self):
        self.assertEqual(stray([1, 1, 1, 1, 1, 1, 2]), 2)
        self.assertEqual(stray([2, 3, 2, 2, 2]), 3)
        self.assertEqual(stray([3, 2, 2, 2, 2]), 3)