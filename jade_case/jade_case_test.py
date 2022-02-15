import unittest
from jade_case import to_jaden_case


class ToJadeCaseTest(unittest.TestCase):

    def test_jade_case(self):
        quote = "How can mirrors be real if our eyes aren't real"
        self.assertEqual(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")



if __name__ == '__main__':
    unittest.main()