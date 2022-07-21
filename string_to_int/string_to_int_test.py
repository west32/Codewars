import unittest
from string_to_int import string_to_number

class StringToNumberTest(unittest.TestCase):

    def test_string_to_int(self):
        self.assertEqual(string_to_number("1234"), 1234)
        self.assertEqual(string_to_number("605"), 605)
        self.assertEqual(string_to_number("1405"), 1405)
        self.assertEqual(string_to_number("-7"), -7)