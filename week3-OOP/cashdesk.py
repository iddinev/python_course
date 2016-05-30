#!/usr/bin/env python3


class Bill:

    def __init__(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        elif amount <= 0:
            raise ValueError
        else:
            self._amount = amount

    def __int__(self):
        return self._amount

    def __str__(self):
        return "A {}$ bill".format(self._amount)

    def __eq__(self, other):
        return self._amount == other

    def __hash__(self):
        return self._amount

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self._amount)


class BillBatch:

    def __init__(self, bills):
        if not isinstance(bills, list):
            raise TypeError
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    def total(self):
        return sum([int(x) for x in self._bills])

    def __getitem__(self, index):
        return self._bills[index].__str__()

    def __repr__(self)


class CashDesk:
    pass
