import unittest
from Account import *


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         pass
#
#
# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    account = Account("1234", "Muiliyu Sodiq", "0000")

    print(account.get_account())
    account.update_pin("0000", "1212")
    print(account.get_account())

    account.deposit(5_500)
    print(f'Balance after deposit is: {account.check_balance("1212")}')

    account.withdraw(2_500, "1212")
    print(f'Balance after deposit is: {account.check_balance("1212")}')

