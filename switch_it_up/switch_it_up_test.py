import unittest
from switch_it_up import switch_it_up

class SwitchTest(unittest.TestCase):

    def test_switch(self):
        self.assertEqual(switch_it_up(0), "Zero")
        self.assertEqual(switch_it_up(9), "Nine")