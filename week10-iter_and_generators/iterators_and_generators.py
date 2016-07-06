#!/usr/bin/env python3


def chain(iterable_one, iterable_two):
    """
    >>> list(chain(range(0, 4), range(4, 8)))
    [0, 1, 2, 3, 4, 5, 6, 7]
    """
    yield from iterable_one
    yield from iterable_two


def compress(iterable, mask):
    """
    >>> list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
    ["Panda"]
    """
    iterator = iter(iterable)
    mask_iterator = iter(mask)
    while True:
        result = next(iterator)
        if next(mask_iterator):
            yield result


def cycle(iterable):
    """
    >>> endless = cycle(range(0,10))
    for item in endless:
            print(item)
    """
    # Create an endles generator - endles concatenation of the iterable.
    generator = (x for y in iter(lambda: 0, 1) for x in iterable)
    # Yield from the endles repetition generator.
    yield from generator
