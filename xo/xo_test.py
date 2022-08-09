import unittest
from xo import xo

class XoTest(unittest.TestCase):

    def test_xo(self):
        self.assertEqual(xo('xo'), True)
        self.assertEqual(xo('xo0'), True)
        self.assertEqual(xo('xxxoo'), False)
