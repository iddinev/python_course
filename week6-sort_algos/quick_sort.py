#!/usr/bin/env python3


import time


def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result

    return timed


@timeit
def quick_sort(int_list, pivot_prc):

    if len(int_list) <= 1:
        return int_list

    pivot_index = int(len(int_list) * pivot_prc)
    pivot = int_list[pivot_index]
    print(pivot)

    smaller, larger, equal = [], [], []
    for i in range(0, len(int_list)):
        if int_list[i] == pivot:
            equal.append(int_list[i])
        elif int_list[i] < pivot:
            smaller.append(int_list[i])
        else:
            larger.append(int_list[i])

    print(smaller)
    print(equal)
    print(larger)

    return quick_sort(smaller, pivot_prc) + equal + quick_sort(larger, pivot_prc)
