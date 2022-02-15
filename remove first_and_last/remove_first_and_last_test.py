import unittest
from remove_first_and_last import remove_char

class RemoveFirstAndLastTest(unittest.TestCase):

    def test_remove_first_and_last(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')