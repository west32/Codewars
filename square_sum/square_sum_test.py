from square_sum import square_sum
import unittest

class SquareTest(unittest.TestCase):

    def test_square_sum(self):
        self.assertEqual(square_sum([1, 2]), 5)
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)
        self.assertEqual(square_sum([]), 0)
        self.assertEqual(square_sum([-1, -2]), 5)
        self.assertEqual(square_sum([-1, 0, 1]), 2)