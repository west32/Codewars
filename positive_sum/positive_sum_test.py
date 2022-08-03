import unittest
from positive_sum import  positive_sum

class PositiveSumTest(unittest.TestCase):

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1,2,3,4,5]),15)
        self.assertEqual(positive_sum([1,-2,3,4,5]),13)
        self.assertEqual(positive_sum([-1,2,3,4,-5]),9)