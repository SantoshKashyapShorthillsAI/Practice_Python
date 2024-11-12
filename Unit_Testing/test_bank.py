import unittest

from bank import bankaccount , InsufficientFunds

class test_bankaccount(unittest.TestCase):
    def setUp(self):
        self.bk=bankaccount(500)

    def test_deposit(self):
        self.bk.deposit(80)
        self.assertEqual(self.bk.balance,580)

    def test_withdrawal(self):
        self.bk.withdraw(80)
        self.assertEqual(self.bk.balance,420)

    def tearDown(self) -> None:
        self.bk=None