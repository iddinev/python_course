#!/usr/bin/env python3



def sum_of_digits(n):
    n = abs(int(n))
    sum = 0
    # if isinstance(n, int) is False:
    # return "input is not int"
    for digit in list(str(n)):
        sum += int(digit)
    return sum


def to_digits(n):
    n = abs(int(n))
    # if isinstance(n, int) is False:
    # return "input is not int"
    return list(str(n))


def to_number(digits):
    string = ''
    # if isinstance(digits, list) is False:
    # return "input is not list"
    for char in digits:
        string += str(char)
    return string


def fact_digits(n):
    n = abs(int(n))
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


def count_words(arr):

