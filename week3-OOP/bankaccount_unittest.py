#!/usr/bin/env python3

from bankaccount import BankAccount
import unittest


class TestBankAccount(unittest.TestCase):

    def create_account_Test(self):
        testobj = BankAccount("Palqk", 0, "Shekel")
        self.assertEqual(("Palqk", 0, "Shekel"), (testobj._name, testobj.balance(), testobj._currency))


if __name__ == "__main__":
    unittest.main()
