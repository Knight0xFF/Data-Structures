#!/usr/bin/env python
# -*- coding: utf-8 -*-


def allrange(array, to, length):
    for i in xrange(length-1):
        array[i], array[i+1] = array[i+1], array[i]
        print array
    if array == to:
        return
    allrange(array, to, length)


def aal(array):
    allrange(array, array, len(array))
#
# def swap(array):
#     array[0], array[-1] = array[-1], array[0]
#     print array
#
# arr = [1, 3, 4]
# swap(arr)
# print arr

a, b = 1, 3

aal([1,2,3, 4])
