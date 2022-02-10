import unittest
from reversed_string import solution


class ReversedStrig(unittest.TestCase):

    def test_high_low(self):
        self.assertEqual(solution('world'), 'dlrow')
        self.assertEqual(solution('hello'), 'olleh')
        self.assertEqual(solution(''), '')
        self.assertEqual(solution('h'), 'h')




if __name__ == '__main__':
    unittest.main()