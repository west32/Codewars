import unittest
from encode_string import duplicate_encode

class DuplicateEncode(unittest.TestCase):

    def test_duplicate_encode(self):
        self.assertEqual(duplicate_encode("din"),"(((")
        self.assertEqual(duplicate_encode("recede"),"()()()")
        self.assertEqual(duplicate_encode("Success"),")())())","should ignore case")
        self.assertEqual(duplicate_encode("(( @"),"))((")