import unittest
from boolean_to_word import bool_to_word


class BooleanToWord(unittest.TestCase):

    def test_boolean_to_word(self):

        self.assertEqual(bool_to_word(True), "Yes")
        self.assertEqual(bool_to_word(False), "No")
