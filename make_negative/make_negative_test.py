from make_negative import make_negative
import unittest

class MakeNegativeTest(unittest.TestCase):

    def test_make_negative(self):
        self.assertEqual(make_negative(42),-42)
        self.assertEqual(make_negative(-9), -9)
        self.assertEqual(make_negative(0), 0)