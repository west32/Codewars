import unittest
from set_alarm import set_alarm

class SetAlarmTest(unittest.TestCase):

    def test_set_alarm(self):
        self.assertEqual(set_alarm(True, True), False, "Fails when input is True, True")
        self.assertEqual(set_alarm(False, True), False, "Fails when input is False, True")
        self.assertEqual(set_alarm(False, False), False, "Fails when input is False, False")
        self.assertEqual(set_alarm(True, False), True, "Fails when input is True, False")