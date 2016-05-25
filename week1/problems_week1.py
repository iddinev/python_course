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


def gas_stations(distance, tank_size, stations):

    distance_stations = [stations[i] - stations[i-1] for i in range(1, len(stations))]
    distance_stations.insert(0, stations[0])
    distance_stations.append(distance - stations[len(stations)-1])

    remaining_tank = tank_size
    stations_list = []
    stations.append(distance)

    for i in range(0, len(stations) - 1):
        if (remaining_tank - distance_stations[i]) < distance_stations[i+1]:
            stations_list.append(stations[i])
            remaining_tank = tank_size
        else:
            remaining_tank -= distance_stations[i]

    return stations_list


def num_to_alpha(keypad, num):
    keypad_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                   '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if str(keypad) == '7' or str(keypad) == '9':
        num = num % 4
    else:
        num = num % 3
    return keypad_dict[str(keypad)][num-1]


def numbers_to_message(pressed_sequence):
    grouped_list = group(pressed_sequence)
    result_str = ''
    iterator = iter(range(0, len(grouped_list)))

    for i in iterator:

        if grouped_list[i][0] == 1:
            result_str += num_to_alpha(grouped_list[i+1][0], len(grouped_list[i+1])).upper()
            next(iterator)
        elif grouped_list[i][0] == -1:
            pass
        elif grouped_list[i][0] == 0:
            result_str += ' '
        else:
            result_str += num_to_alpha(grouped_list[i][0], len(grouped_list[i]))

    return result_str
