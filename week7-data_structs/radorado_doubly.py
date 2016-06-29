#!/usr/bin/env python3


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value

        if next is not None and\
                not isinstance(next, Node):
            raise TypeError('next should be instance of Node')

        if prev is not None and\
                not isinstance(prev, Node):
            raise TypeError('prev should be instance of Node')

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
        self.__head = None
        self.__tail = None
        self.__count = 0

    def __handle_head_and_tail_if_empty(self):
        if self.__count == 0:
            self.__head = None
            self.__tail = None

    """ O(1) - Returns a Node object that represents the head """
    def get_head(self): return self.__head

    """ O(1) - Returns a Node object that represents the head """
    def get_tail(self): return self.__tail

    """ O(1) - Returns the value of the first element """
    def get_first(self):
        if self.__head is not None:
            return self.__head.value

    """ O(1) - Returns the value of the last element """
    def get_last(self):
        if self.__tail is not None:
            return self.__tail.value

    """ O(1) """
    def add_first(self, x):
        node = Node(x)

        if self.__count == 0:
            self.__head = node
            self.__tail = self.__head
        else:
            temp = self.__head
            self.__head = node

            self.__head.next = temp
            temp.prev = self.__head

        self.__count += 1

    """ O(1) """
    def add_last(self, x):
        if self.__count == 0:
            return self.add_first(x)

        node = Node(x)
        temp = self.__tail

        self.__tail = node

        self.__tail.prev = temp
        temp.next = self.__tail

        self.__count += 1

    """ O(1) """
    def remove_first(self):
        if self.__count == 0:
            return

        value = self.__head.value
        self.__head = self.__head.next

        if self.__head is not None:
            self.__head.prev = None

        self.__count -= 1
        self.__handle_head_and_tail_if_empty()

        return value

    """ O(1) """
    def remove_last(self):
        if self.__count == 0:
            return

        value = self.__tail.value
        self.__tail = self.__tail.prev

        if self.__tail is not None:
            self.__tail.next = None

        self.__count -= 1
        self.__handle_head_and_tail_if_empty()

        return value

    """ O(1) """
    def __len__(self):
        return self.__count

    """ O(n) - Called when we do list(items) """
    def __iter__(self):
        result = []
        node = self.__head

        while node is not None:
            result.append(node.value)
            node = node.next

        return iter(result)
