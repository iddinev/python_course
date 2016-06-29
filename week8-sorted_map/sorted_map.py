#!/usr/bin/env python3

from collections import deque

class SortedMap:
    """
    This is a key-value container that keeps a sorted represnetation
    Sorting is done using the comparator function passed to __init__
    If no comparator is passed, natural order of keys is used:
    k1 <> k2
    """
    def __init__(self, comparator=None):
        if comparator is None:
            comparator = lambda x, y: x <= y

        self.comparator = comparator
        self.container = dict()
        self.delist =

    def add(self, key, value):
        """
        Adds a new key-value pair
        If the key is already existing - override it
        """
        self.container[key] = value

    def get(self, key, default=None):
        """
        Should return the corresponding value to key
        Returns default otherwise
        """
        return self.container.get(key, default)

    def __contains__(self, key):
        """
        Usage: key in map
        """

    def __iter__(self):
        result = []

        """
        Code here that populates result with values
        """

        return iter(result)
