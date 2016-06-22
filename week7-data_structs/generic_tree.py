#!/usr/bin/env python3


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self._isleaf = True

    def add_child(self, node):
        if not isinstance(node, Node):
            raise ValueError('node should be Node')

        self.children.append(node)
        self._isleaf = False

    def isleaf(self):
        return self._isleaf


class Tree:
    def __init__(self, *, root):
        """
            When we are creating a new tree, we must always have a root element.
            For example:
            tree = Tree(root=5)
        """
        self._root = Node(root)

    def add(self, *, value, parent):
        """
            When we are adding new element to our tree, we must specify the parent:
            tree = Tree(root=5)
            tree.add(4, parent=5)
            tree.add(3, parent=5)
            tree.add(2, parent=4)

            This will make the following tree:

                5
               / \
              4   3
             /
            2
        """

    def find(self, x):
        """
            Returns True or False if Node with value x is present in the tree
        """

    def give_node(self, x):


    def bfs_from_root(self):
        """
            Makes a Breadth-First-Search Algorithm from root
            Returns a list of tuples in the following format:
            [(tree_level, (node1_on_that_level, node2_on_that_level, ...)),
             (tree_level + 1, (node1_on_that_level, node2_on_that_level, ...))]

            If we take the tree from the add example, the result will look like that:

            [(1, (5, )),
             (2, (4, 3)),
             (3, (2, ))]

             We count our levels from 1.
        """
