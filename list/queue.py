#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Queue(object):
    def __init__(self):
        self.items = []

    def get_size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


if __name__ == "__main__":
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    print q.items
    q.enqueue(3)
    q.dequeue()
    print q.items