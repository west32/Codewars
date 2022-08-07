import unittest
from transport_vac import rental_car_cost

class TestRentalCarCost(unittest.TestCase):

    def test_rental_car_cost(self):
        self.assertEqual(rental_car_cost(1),40)
        self.assertEqual(rental_car_cost(4),140)
        self.assertEqual(rental_car_cost(7),230)
        self.assertEqual(rental_car_cost(8),270)