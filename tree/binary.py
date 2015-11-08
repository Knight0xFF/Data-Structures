#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, data, left=None, right=None):
        self.root = data
        self.left = left
        self.right = right


def pre_create(root):
    value = raw_input('enter a node:')
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

if __name__ == "__main__":
    root = None
    root = pre_create(root)
    pre_order(root)
    print
    in_order(root)
    print
    post_order(root)
    print
    print get_leaf_num(root)
    print get_depth(root)

