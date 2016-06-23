#!/usr/bin/env python3

from generic_tree import Tree, Node

tree = Tree(root='/')
tree._root.add_child(Node('a'))
tree._root.add_child(Node('b'))
tree._root.add_child(Node('c'))
print('real children of root')
print(tree._root.children)
print("")
print('computed children of root')
tree.add(value=1, parent=1)
print("")
print('Tree repr func')
tree.tree_repr()
