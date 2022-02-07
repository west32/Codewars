import unittest
from printer_error import printer_error


class DecimalToBinary(unittest.TestCase):



    def test_high_low(self):
        self.assertEqual(add_binary(1,1),"10")
        self.assertEqual(add_binary(0,1),"1");
        self.assertEqual(add_binary(1,0),"1")
        self.assertEqual(add_binary(2,2),"100")
        self.assertEqual(add_binary(51,12),"111111")


if __name__ == '__main__':
    unittest.main()