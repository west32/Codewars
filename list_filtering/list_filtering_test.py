import unittest
from list_filtering import filter_list


class FirstTestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(filter_list([1, 2, 'a', 'b']), [1, 2])
        self.assertEqual(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15])
        self.assertEqual(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123])

if __name__ == '__main__':
    unittest.main()