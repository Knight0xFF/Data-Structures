#!/usr/bin/env python
# -*- coding: utf-8 -*-

nodes = [6, 4, 2, 3, '#', '#', '#', '#', 5, 1, '#', '#', 7, '#', '#']
avlnodes = [6, 4, 2, '#', '#', '#', 5, 1, '#', '#', 7, '#', '#']

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.root = data
        self.left = left
        self.right = right


def pre_create(root):
    value = avlnodes.pop(0)
    if value == "#":
        root = None
    else:
        root = Node(value)
        root.left = pre_create(root.left)
        root.right = pre_create(root.right)
    return root


def pre_order(root):
    if root is None:
        return
    else:
        print root.root,
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    if root is None:
        return
    else:
        in_order(root.left)
        print root.root,
        in_order(root.right)


def post_order(root):
    if root is None:
        return
    else:
        post_order(root.left)
        post_order(root.right)
        print root.root,


def get_leaf_num(root):
    if root is None:
        return 0
    if root.right is None and root.left is None:
        return 1
    return get_leaf_num(root.right) + get_leaf_num(root.left)


def get_depth(root):
    if root is None:
        return 0
    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)
    return left_depth + 1 if left_depth > right_depth else right_depth + 1


def get_node_num_kth_level(root, k):
    if root is None or k < 1:
        return 0
    elif k == 1:
        return 1
    left_num = get_node_num_kth_level(root.left, k-1)
    right_num = get_node_num_kth_level(root.right, k-1)
    return left_num + right_num

def structure_cmp(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False


def is_avl(root):
    if root is None:
        return True
    distance = get_depth(root.left) - get_depth(root.right)
    if abs(distance) > 1:
        return False
    else:
        return is_avl(root.left) and is_avl(root.right)

if __name__ == "__main__":
    root = None
    root = pre_create(root)
    pre_order(root)
    print
    in_order(root)
    print
    post_order(root)
    print
    print "leaf num: ", get_leaf_num(root)
    print "depth: ", get_depth(root)
    print "3th node num: ", get_node_num_kth_level(root, 3)
    print "is avl: ", is_avl(root)

