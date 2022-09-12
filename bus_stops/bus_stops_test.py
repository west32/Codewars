import unittest
from bus_stops import number

class TestBusStops(unittest.TestCase):

    def test_number(self):
        self.assertEqual(number([[10,0],[3,5],[5,8]]),5)
        self.assertEqual(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
        self.assertEqual(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)