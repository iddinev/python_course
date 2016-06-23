#!/usr/bin/env python3


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        if not isinstance(node, Node):
            raise ValueError('node should be Node')

        self.children.append(node)

    def isleaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def __str__(self):
        return self.value

    def __repr__(self):
        #  return "{}->|{}|".format(self.value, self.children)
        return self.__str__()

    def node_repr(self):
        return "{}->|{}|".format(self.value, self.children)


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
        nodes = stack(self._root)
        print(nodes)
        #  if parent in [node.value for node in nodes]:
            #  parent_node =

    def find(self, x):
        """
            Returns True or False if Node with value x is present in the tree
        """
        pass

    def give_node(self, x):
        pass

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
        pass

    def tree_repr(self):
        print(self._root.node_repr())

def stack(root):

    if root.isleaf():
        return [root]
    else:
        return [root] + [stack(child)[0] for child in root.children]
        #  print(statement)
        #  return statement
        #  return [root].extend([stack(child) for child in root.children])
        #  return stack_list.extend([stack(child) for child in root.children])
