#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Binary(object):
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = Binary(new_node)
        else:
            t = Binary(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = Binary(new_node)
        else:
            t = Binary(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_value(self):
        return self.key

if __name__ == "__main__":
    b = Binary("test")
    print b.left_child, b.right_child
    b.insert_left("1left")
    print b.left_child, b.right_child
    b.insert_left("1right")
    print b.left_child.left_child, b.right_child

