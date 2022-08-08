import unittest
from same_arrays import comp


class TestComp(unittest.TestCase):

    def test_comp(self):
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
        self.assertEqual(comp(a1, a2), True)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
        self.assertEqual(comp(a1, a2), False)
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
        self.assertEqual(comp(a1, a2), False)
