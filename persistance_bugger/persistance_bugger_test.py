import unittest
from persistance_bugger import persistence

class BuggerTest(unittest.TestCase):

    def test_persistance(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)