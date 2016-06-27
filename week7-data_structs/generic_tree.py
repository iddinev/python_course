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
        if len(self.children) == []:
            return True
        else:
            return False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        #  return "{}->|{}|".format(self.value, self.children)
        return str(self.value)

    def node_repr(self):
        print("{}->{}".format(self.value, self.children))


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
        nodes = Tree.stack(self._root)
        for node in nodes:
            if parent == node.value:
                parent_node = node
                parent_node.add_child(Node(value))

    def find(self, x):
        """
            Returns True or False if Node with value x is present in the tree
        """
        nodes = Tree.stack(self._root)
        return x in [node.value for node in nodes]

    def get_queue(self):
        nodes = Tree.queue(self._root)
        #  nodes = Tree.lsreduce(nodes)
        return nodes

    def get_stack(self):
        nodes = Tree.stack(self._root)
        return nodes

    @staticmethod
    def queue(root):
        """
            Depth-first algo.
        """
        if root.isleaf():
            return [root]
        else:
            return [root] + [Tree.queue(child) for child in root.children]

    @staticmethod
    def stack(root):
        """
            Breadth-first algo.
        """
        stack_list = []
        tmp_stack = [root]

        while tmp_stack != []:
            node = tmp_stack.pop(0)
            stack_list += [node]
            tmp_stack += [child for child in node.children]

        return stack_list

    @staticmethod
    def lsreduce(lst):
        if lst == []:
            return lst
        if isinstance(lst[0], list):
            return Tree.lsreduce(lst[0]) + Tree.lsreduce(lst[1:])
        return lst[:1] + Tree.lsreduce(lst[1:])

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
        bfs_list = []
        bfs_list.append((1, tuple(self._root.value)))

        stack_list = []
        tmp_stack = [self._root] + [None]
        level = 2
        node_list = []

        while tmp_stack != [None]:
            marker = []
            node = tmp_stack.pop(0)
            if node is None:
                node = tmp_stack.pop(0)
                marker = [None]
                bfs_list.append((level, tuple(node_list)))
                node_list = []
                level += 1
            stack_list += [node]
            node_list += [child for child in node.children]
            tmp_stack += node_list + marker

        return bfs_list


def queue(root):
    """
        Depth-first algo.
    """
    if root.isleaf():
        return [root]
    else:
        return [root] + [queue(child) for child in root.children]


def stack(root):
    stack_list = []
    tmp_stack = [root]

    while tmp_stack != []:
        node = tmp_stack.pop(0)
        stack_list += [node]
        tmp_stack += [child for child in node.children]

    return stack_list
