from opposittes import lovefunc
import unittest

class TestOpossites(unittest.TestCase):

    def test_lovefunc(self):
        self.assertEqual(lovefunc(1, 4), True)
        self.assertEqual(lovefunc(2, 2), False)
        self.assertEqual(lovefunc(0, 1), True)
        self.assertEqual(lovefunc(0, 0), False)