#!/usr/bin/env python3

from random import randint
from quick_sort import *
from count_sort import *

random_nums = []
random_nums.extend([randint(-50, 50) for x in range(0, 11)])
print(random_nums, '\n')

print(countsrt(random_nums))

