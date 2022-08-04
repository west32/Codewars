import unittest
from testing_lines import number

class TestingLines(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(number([]), [])
        self.assertEqual(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])