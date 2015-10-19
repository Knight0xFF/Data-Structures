#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, item, p=0):
        self.data = item
        self._next = p


class LinkList(object):
    def __init__(self):
        self.head = Node(0)

    def get_length(self):
        p = self.head
        length = 0
        while p:
            length += 1
            p = p._next
        return length

    def is_empty(self):
        return self.get_length() == 0

    def insert(self, index, item):
        p = self.head
        i = 1
        while p and i < index:
            p = p._next
            i += 1
        if p is None or i > index:
            return False
        node = Node(item, p)
        p._next = node
        return True

    def delete(self, index):
        ptr = self.head
        i = 1
        while i < index - 1 and ptr:
            ptr = ptr.__next
            i += 1
        if i > index or ptr is None:
            return False

    def search(self, item):
        ptr = self.head
        index = 0
        while ptr.data != item:
            ptr = ptr._next
            index += 1
            if ptr is None:
                return False
        return index

    def display(self):
        p = self.head
        index = 1
        while p._next:
            print p.data
            p = p._next


if __name__ == "__main__":
    link_list = LinkList()
    print link_list.get_length()
    print link_list.insert(1, 10)
    print link_list.insert(1, 4)
    link_list.display()
    print link_list.search(10)
