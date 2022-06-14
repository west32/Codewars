from paperwork import paperwork
import unittest

class PaperworkTest(unittest.TestCase):

    def test_paperwork(self):
        self.assertEqual(paperwork(5, 5), 25, "Failed at Paperwork(5,5)")
        self.assertEqual(paperwork(-5, 5), 0, "Failed at Paperwork(-5,5)")
        self.assertEqual(paperwork(5, -5), 0, "Failed at Paperwork(5,-5)")
        self.assertEqual(paperwork(-5, -5), 0, "Failed at Paperwork(-5,-5)")
        self.assertEqual(paperwork(5, 0), 0, "Failed at Paperwork(5,0)")