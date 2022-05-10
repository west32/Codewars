import unittest
from get_sum import get_sum


class GetSumTest(unittest.TestCase):

    def test_get_sum(self):
        self.assertEqual(get_sum(0, 1), 1)
        self.assertEqual(get_sum(0, -1), -1)


