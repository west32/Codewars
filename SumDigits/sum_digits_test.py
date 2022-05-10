import unittest
from sum_digits import sum_digits

class SumDigitsTest(unittest.TestCase):

    def test_sum_digits(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(99), 18)
        self.assertEqual(sum_digits(-32), 5)