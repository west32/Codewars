import unittest
from square_digit import square_digits

class SquareDigitTest(unittest.TestCase):

    def test_square_test(self):
        self.assertEqual(square_digits(9119), 811181)
        self.assertEqual(square_digits(0), 0)
