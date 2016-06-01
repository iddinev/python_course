#!/usr/bin/env python3

from bankaccount import BankAccount

account = BankAccount("Rado", 0, "$")
print(account)

print(account.deposit(1000))

print(account.balance())

print(str(account))

print(account.history())

print(account.withdraw(500))

print(account.balance())

print(account.history())

print(account.withdraw(1000))

print(account.balance())

print(int(account))

print(account.history())

