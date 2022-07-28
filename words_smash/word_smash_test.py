import unittest
from word_smash import smash

class TestSmash(unittest.TestCase):

    def test_smash(self):
        self.assertEqual(smash(["hello", "world"]), "hello world")
        self.assertEqual(smash(["hello", "amazing", "world"]), "hello amazing world")
        self.assertEqual(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")
