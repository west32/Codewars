import unittest
from is_valid_walk import is_valid_walk

class ValidWalkTest(unittest.TestCase):

    def test_is_valid(self):
        self.assertEqual(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True)
        self.assertEqual(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False)
        self.assertEqual(is_valid_walk(['w']), False)
        self.assertEqual(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), False)