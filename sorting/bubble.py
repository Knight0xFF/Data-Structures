#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble(array):
    length = len(array)
    for i in xrange(length):
        for j in xrange(1, length-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array


def bubble_s(array):
    length = len(array)
    key = length
    for i in xrange(length):
        swapped = True
        for j in xrange(1, key):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                key = j  # 记录最后交换的位置，后面的有序
                swapped = False  # 如果没有发生交换，则后面有序，结束排序
        if swapped:
            break
    return array


if __name__ == "__main__":
    test_data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print bubble(test_data)
    print bubble_s(test_data)
