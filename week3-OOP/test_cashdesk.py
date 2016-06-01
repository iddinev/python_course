#!/usr/bin/env python3

from cashdesk import Bill, BatchBill, CashDesk

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)
print(batch.nominals)
print(batch.total())

desk = CashDesk()

desk.take_money(Bill(5))
desk.take_money(batch)
desk.take_money(Bill(5))
desk.take_money(batch)

print(desk.inspect())
