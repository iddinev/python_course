#!/usr/bin/env python3


class Node:

    def __init__(self, value, prev=None, next=None):

        if next is not None and\
                not isinstance(next, Node):
            raise TypeError('next should be instance of Node')

        if prev is not None and\
                not isinstance(prev, Node):
            raise TypeError('prev should be instance of Node')

        self.value = value
        self.prev = prev
        self.next = next

    def has_prev(self):
        return self.prev is not None

    def has_next(self):
        return self.next is not None

    def __str__(self):
        prev_val = self.prev.value if isinstance(self.prev, Node) else None
        next_val = self.next.value if isinstance(self.next, Node) else None
        return "{}<-{}->{}".format(prev_val, self.value, next_val)


class DoublyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._current_len = 0

    """ O(1) - Returns a Node object that represents the head """
    def get_head(self):
        #  print(self._head.__str__())
        return self._head.__str__()

    """ O(1) - Returns a Node object that represents the tail """
    def get_tail(self):
        return self._tail.__str__()

    """ O(1) - Returns the value of the first element """
    def get_first(self):
        return self._head.value if hasattr(self._head, 'value') else None

    """ O(1) - Returns the value of the last element """
    def get_last(self):
        #  return self._tail.value
        return self._tail.value if hasattr(self._tail, 'value') else None

    """ O(1) """
    def add_first(self, x):
        new_head = Node(x, next=self._head)
        self._head = new_head
        self._current_len += 1
        if self._current_len == 1:
            self._tail = self._head
        elif self._current_len == 2:
            self._tail = Node(self._tail.value, prev=self._head)

    """ O(1) """
    def add_last(self, x):
        new_tail = Node(x, prev=self._tail)
        self._tail = new_tail
        self._current_len += 1
        if self._current_len == 1:
            self._head = self._tail
        elif self._current_len == 2:
            self._head = Node(self._head.value, next=self._tail)

    """ O(1) """
    def remove_first(self):
        removed_head = self._head
        if self._current_len == 2:
            old_head = Node(self._tail.value)
            self._tail = old_head
        elif self._current_len == 1:
            old_head = None
            self._tail = None
        else:
            old_head = self._head.next
        self._head = old_head
        self._current_len -= 1
        return removed_head.value if hasattr(removed_head, 'value') else None

    """ O(1) """
    def remove_last(self):
        removed_tail = self._tail
        if self._current_len == 2:
            old_tail = Node(self._head.value)
            self._head = old_tail
        elif self._current_len == 1:
            old_tail = None
            self._head = None
        else:
            old_tail = self._tail.prev
        self._tail = old_tail
        self._current_len -= 1
        return removed_tail.value if hasattr(removed_tail, 'value') else None

    """ O(1) """
    def __len__(self): pass

    """ O(n) - Called when we do list(items) """
    def __iter__(self): pass
