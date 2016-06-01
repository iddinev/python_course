#!/usr/bin/env python3

class BankAccount:

    def __init__(self, name, balance, currency):
        if not isinstance(name, str) or not isinstance(currency, str):
            raise TypeError
        elif balance < 0:
            raise ValueError
        else:
            self._name = name
            self._balance = balance
            self._currency = currency
            self._history = ['Account was created']

    def balance(self):
        self._history.append('Balance check -> {}$'.format(self._balance))
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self._balance += amount
            self._history.append('Deposited {}$'.format(amount))

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError
        elif self._balance - amount < 0:
            self._history.append('Withdraw for {}$ failed.'.format(amount))
            return False
        else:
            self._balance -= amount
            self._history.append('{}$ was withdrawed'.format(amount))
            return True

    def transfer_to(self, account, amount):
        pass

    def history(self):
        return self._history

    def __int__(self):
        self._history.append('__int__ check -> {}$'.format(self._balance))
        return self._balance

    def __str__(self):
        return "Bank account for {0} with balance of {1}{2}".format(self._name,
                                                                    self._balance,
                                                                    self._currency)
