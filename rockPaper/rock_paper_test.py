import unittest
from rock_paper import rps

class TestRockPaper(unittest.TestCase):

    def test_rps(self):
        self.assertEqual(rps('rock', 'scissors'), "Player 1 won!")
        self.assertEqual(rps('scissors', 'rock'), "Player 2 won!")
        self.assertEqual(rps('rock', 'rock'), 'Draw!')
