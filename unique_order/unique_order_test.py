import unittest
from unique_order import unique_in_order

class UniqueInOrderTest(unittest.TestCase):

    def test_unique_in_order(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
