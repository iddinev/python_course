#!/usr/bin/env python3


import time


def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te-ts))
        return result

    return timed


def find_range(int_list):
    if int_list != []:
        int_list.sort()
        min_num = int_list[0]
        max_num = int_list[-1]
        return min_num, max_num


def count_sort(int_list, min_num, max_num):
    counts = [0 for x in range(0, max_num - min_num + 1)]

    for i in range(0, len(int_list)):
        num = int_list[i]
        counts[num-min_num] += 1

    result = []
    for i in range(0, len(counts)):
        num = counts[i]
        result.extend([i + min_num for x in range(0, num)])

    #  print(result)
    return result

count_sort = timeit(count_sort)


def countsrt(int_list):
    lower, upper = find_range(int_list)
    return count_sort(int_list, lower, upper)
