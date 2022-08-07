import unittest
from divisors import divisors

class TestDivisors(unittest.TestCase):

    def test_divisorst(self):
        self.assertEqual(divisors(1), 1)
        self.assertEqual(divisors(4), 3)
        self.assertEqual(divisors(5), 2)
        self.assertEqual(divisors(12), 6)
        self.assertEqual(divisors(30), 8)
        self.assertEqual(divisors(4096), 13)