import unittest
from summation import summation

class SummationTest(unittest.TestCase):

    def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)
        self.assertEqual(summation(22), 253)
        self.assertEqual(summation(100), 5050)
        self.assertEqual(summation(213), 22791)
