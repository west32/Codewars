import unittest
from transfer import Transfer


class TransferTest(unittest.TestCase):
    def test_len_bank_account_number(self):
        # przelew= Transfer()
        # self.assertEqual(Transfer.account_number_len_validation()( 12345678901234567890123456), True)
        self.assertEqual(Transfer.account_number_len_validation(self, None), False)
        self.assertEqual(Transfer.account_number_len_validation(self, 12312312312321312312321321321321312312321312), False)
        self.assertEqual(Transfer.account_number_len_validation(self, 12312452.435), False)
        self.assertEqual(Transfer.account_number_len_validation(self, 'dupadupadupadupadupadupa'), False)
        self.assertEqual(Transfer.account_number_len_validation(self,  123-12312-123),False)
        self.assertTrue(Transfer.account_number_len_validation(self,12345678901234567890123456))

# b= 3
# print(type(b))