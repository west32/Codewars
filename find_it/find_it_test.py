import unittest
from find_it import find_it

class FindItTest(unittest.TestCase):

    def test_find_it(self):
        self.assertEqual(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        self.assertEqual(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
        self.assertEqual(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)
        self(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)