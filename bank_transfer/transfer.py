

class Transfer():
    def __init__(self,account_number):
        self.account_number=account_number

    def account_number_len_validation(self, account_number):
        propper_form=('12345678901234567890123456')
        return len(propper_form)==len(str(account_number))


#
# # print(przelew)