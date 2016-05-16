#!/usr/bin/env python3



def sum_of_digits(n):
    n = abs(int(n))
    sum = 0
    for digit in list(str(n)):
        sum += int(digit)
    return sum


def to_digits(n):
    n = abs(int(n))
    return list(str(n))


def to_number(digits):
    str_digits = [str(ch) for ch in digits]
    return ''.join(str_digits)


def fact_digits(n):
    n = abs(int(n))
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


def count_words(arr):
    word_count = {}
    unique_words = set(arr)
    for word in unique_words:
        word_count[word] = arr.count(word)
    return word_count


def iterations_of_nan_expand(expanded):

