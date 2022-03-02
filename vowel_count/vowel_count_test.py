import unittest

from vowel_count import get_count


class VowelCount(unittest.TestCase):

    def test_vowel_count(self):
        self.assertEqual(get_count("aeiou"), 5)
        self.assertEqual(get_count(""), 0)
        self.assertEqual(get_count("y"), 0)
        self.assertEqual(get_count("bcdfghjklmnpqrstvwxz y"), 0)
        self.assertEqual(get_count("abracadabra"), 5)