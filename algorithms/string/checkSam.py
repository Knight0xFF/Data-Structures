#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Same:
    def checkSam(self, stringA, stringB):
        # write code here
        setA = sorted(stringA)
        setB = sorted(stringB)
        if setA == setB:
            return True
        return False

if __name__ == '__main__':
    s = Same()
    print s.checkSam("This is nowcoder","is This nowcoder")
