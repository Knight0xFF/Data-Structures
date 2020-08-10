#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ReverseEqual:
    def checkReverseEqual(self, s1, s2):
        # write code here
        common_point = self.get_common(s1, s2)
        print common_point
        for i in common_point:
            new_s1 = s1[i:] + s1[0:i]
            if s2 == new_s1:
                return True
            else:
                continue
        return False

    def get_common(self, s1, s2):
        res = []
        first_c2 = s2[0]
        for i in xrange(len(s1)):
            if s1[i] == first_c2:
                res.append(i)
        return res

    def checkReverseEqual_s(self, s1, s2):
        new_s1 = s1 + s1
        if s2 in new_s1:
            return True
        return False

if __name__ == '__main__':
    s = ReverseEqual()
    print s.checkReverseEqual_s("waterbottle","erbottlewat")
