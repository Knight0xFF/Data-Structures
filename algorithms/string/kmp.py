#!/usr/bin/env python
# -*- coding: utf-8 -*-


def partial_table(string):
    ret = []
    for length in xrange(len(string)):
        substring = string[:length+1]
        prefix = [substring[:i] for i in xrange(len(substring)) if i]
        postfix = [substring[i:] for i in xrange(1, len(substring))]
        x = list(set(prefix) & set(postfix))
        if x:
            ret.append(len(x[0]))
        else:
            ret.append(0)
    return ret


def kmp(string, pattern):
    s_len = len(string)
    p_len = len(pattern)
    cur = 0
    table = partial_table(pattern)
    while cur < s_len - p_len:
        for i in xrange(p_len):
            if string[cur+i] != pattern[i]:
                cur += max(i - table[i-1], 1)
                break
        else:
            return True
    return False


print kmp("asdkwueabcdabdlkdf", "abcdabd")


