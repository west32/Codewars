import unittest
from find_unique import find_uniq


class TestFindUnique(unittest.TestCase):

    def test_find_unique(self):
        self.assertEqual(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        self.assertEqual(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        self.assertEqual(find_uniq([ 3, 10, 3, 3, 3 ]), 10)