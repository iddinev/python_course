#!/usr/bin/env python3


#  from iterators_and_generators import compress

#  print(list(compress(["Ivo", "Rado", "Ivan", "Panda"], [False, True, False])))

from iterators_and_generators import cycle


endless = cycle([1, 2, 3, 'a'])

for item in endless:
    print(item)
    nb = input('cycle: ')
