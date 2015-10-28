#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, item, next=None, prior=None):
        self.data = item
        self._next = next
        self._prior = prior


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

    def insert(self, index, item):  # 在第index个元素前插入
        p = self.head
        i = 0
        while p and i < index - 1:
            p = p._next
            i += 1
        if p is None or i > index:
            return False
        node = Node(item, p._next, p)
        p._next = node
        return True

    def delete(self, index):
        ptr = self.head
        i = 1
        while ptr._next and i < index:
            ptr = ptr._next
            i += 1
        if i > index or ptr is None:
            return False
        q = ptr._next
        ptr._next = q._next
        return q.data

    def search(self, item):
        ptr = self.head
        index = 0
        while ptr.data != item:
            ptr = ptr._next
            index += 1
            if ptr is None:
                return False
        return index

    def search_prior(self, item):
        pass

    def display(self):
        p = self.head
        print "linklist:"
        while p._next:
            p = p._next
            print p.data

if __name__ == "__main__":
    link_list = LinkList()
    print link_list.insert(1, 10)
    print link_list.insert(1, 4)
    print link_list.insert(3, 5)
    link_list.display()
    print link_list.delete(1)
    link_list.display()
    print link_list.get_length()
