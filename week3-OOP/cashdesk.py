#!/usr/bin/env python3


class Bill:

    def __init__(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        elif amount <= 0:
            raise ValueError
        else:
            self._amount = amount

    def total(self):
        return self.__int__()

    @property
    def nominals(self):
        return list([self.total()])

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


class BatchBill:

    def __init__(self, bills):
        if not isinstance(bills, list):
            raise TypeError
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    @property
    def nominals(self):
        return [int(x) for x in self._bills]

    def total(self):
        return sum([x.total() for x in self._bills])

    def __getitem__(self, index):
        return self._bills[index]

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, 'list_of_Bill()')


class CashDesk:

    def __init__(self):
        self._pool = []

    def take_money(self, money):
        if isinstance(money, (Bill, BatchBill)):
            self._pool.append(money)

    def total(self):
        return sum([x.total() for x in self._pool])

    def inspect(self):

        inspect_string = "We have a total of {0}$ in the desk\n".format(self.total())
        inspect_string += "We have the following count of bills, sorted in ascending order:"

        bill_nominals = []
        for i in range(0, len(self._pool)):
            bill_nominals.extend(self._pool[i].nominals)

        unique_nominals = list(set(bill_nominals))
        unique_nominals.sort()

        bill_count = []
        bill_count.extend([bill_nominals.count(nominal) for nominal in unique_nominals])

        for i in range(0, len(bill_count)):
            inspect_string +=\
            "\n{}$ bills - {}".format(unique_nominals[i], bill_count[i])

        return inspect_string
