import unittest
from printer_error_script import printer_error


class DecimalToBinary(unittest.TestCase):



    def test_high_low(self):
        self.assertEqual(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"),"3/56")
        self.assertEqual(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"),"6/60")
        self.assertEqual(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"),"11/65")
