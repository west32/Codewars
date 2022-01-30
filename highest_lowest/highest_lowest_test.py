import unittest
from highest_lowest import high_and_low


class HelloworldTests(unittest.TestCase):

    def test_high_low(self):
        self.assertEqual(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9");
        self.assertEqual(high_and_low("1 2 3"), "3 1");



if __name__ == '__main__':
    unittest.main()