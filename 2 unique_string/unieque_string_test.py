import unittest
from unique_string import find_uniq

class TestUniqueString(unittest.TestCase):

    def test_find_uniq(self):
        self.assertEqual(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
        self.assertEqual(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo')
        self.assertEqual(find_uniq([ '    ', 'a', '  ' ]), 'a')