#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def get_size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(142)
    print stack.get_size()
    print stack.peek()
    print stack.pop()
    print stack.is_empty()
