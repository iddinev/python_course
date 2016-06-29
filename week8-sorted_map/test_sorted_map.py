#!/usr/bin/env python3

from sorted_map import SortedMap


storage = SortedMap()

storage.add('b', 5)
storage.add('a', 4)

assert list(storage) == [('a', 4), ('b', 5)]

storage2 = SortedMap(comparator=lambda x, y: len(x) <= len(y))
storage2.add('aaa', 1)
storage2.add('aa', 2)
storage2.add('aaaa', 3)

assert list(storage2) == [('aa', 2), ('aaa', 1), ('aaaa', 3)]
