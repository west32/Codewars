import unittest
from is_upper import is_uppercase

class IsUpperTest(unittest.TestCase):

    def test_is_upper(self):
        self.assertEqual(is_uppercase("c"), False)
        self.assertEqual(is_uppercase("C"), True)
        self.assertEqual(is_uppercase("hello I AM DONALD"), False)
        self.assertEqual(is_uppercase("HELLO I AM DONALD"), True)
        self.assertEqual(is_uppercase("$%&"), True)