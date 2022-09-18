import unittest
from vovels import disemvowel

class TestDisemvovel(unittest.TestCase):

    def test_disemvovel(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")