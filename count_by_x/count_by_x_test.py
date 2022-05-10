import unittest
from count_by_x import count_by


class CountByX(unittest.TestCase):

    def test_count_by(self):
        self.assertEqual(count_by(1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(count_by(2, 5), [2, 4, 6, 8, 10])
        self.assertEqual(count_by(3, 5), [3, 6, 9, 12, 15])
        self.assertEqual(count_by(50, 5), [50, 100, 150, 200, 250])
        self.assertEqual(count_by(100, 5), [100, 200, 300, 400, 500])