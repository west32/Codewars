import unittest
from integer_to_string import number_to_string


class NumberToStringTest(unittest.TestCase):

    def test_high_low(self):
        self.assertEqual(number_to_string(67), '67')
        self.assertEqual(number_to_string(79585), '79585')
        self.assertEqual(number_to_string(79585), "79585")
        self.assertEqual(number_to_string(1+2), '3')
        self.assertEqual(number_to_string(1-2), '-1')


if __name__ == '__main__':
    unittest.main()