#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble(array):
    length = len(array)
    for i in xrange(1, length):
        for j in xrange(length-1, i-1, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
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


def binary_search(array, target):
    length = len(array)
    left_i = 0
    right_i = length-1
    while left_i <= right_i:
        middle_i = (left_i+right_i) / 2
        if target > array[middle_i]:
            left_i = middle_i + 1
        elif target < array[middle_i]:
            right_i = middle_i - 1
        if target == array[middle_i]:
            return middle_i
    else:
        return False


if __name__ == "__main__":
    test_data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print bubble(test_data)
