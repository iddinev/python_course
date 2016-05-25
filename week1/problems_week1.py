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
    isNaN_list = expanded.split(' a ')
    if isNaN_list.pop() != 'NaN':
        return False
    elif (set(isNaN_list) | set(["Not"])) != set(["Not"]):
        return False
    else:
        return len(isNaN_list)


def group(items):
    result = []
    result.append([items[0]])
    last_items_index = len(items) - 1
    last_result_index = len(result) - 1
    subsequence = 1
    for i in range(0, last_items_index):
        current_element = items[i]
        if items[i+1] == current_element:
            subsequence += 1
        else:
            result[last_result_index].extend([current_element for j in range(1, subsequence)])
            result.append([items[i+1]])
            last_result_index = len(result) - 1
            subsequence = 1
    return result


def max_consecutive(items):
    group_list = group(items)
    group_list.sort(key=len, reverse=True)
    return len(group_list[0])
