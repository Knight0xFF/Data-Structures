#!/usr/bin/env python
# -*- coding: utf-8 -*-


class fibs(object):
    def __init__(self, target):
        self.target = target
        self.n = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.target:
            temp = self.b
            self.a, self.b = self.b, self.a +self.b
            self.n += 1
            return temp

        raise StopIteration

if __name__ == "__main__":
    for i in fibs(5):
        print i