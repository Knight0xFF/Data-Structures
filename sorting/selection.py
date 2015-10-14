#!/usr/bin/env python
# -*- coding: utf-8 -*-


def selection(array):
    length = len(array)
    for i in xrange(length):
        min_index = i
        for j in xrange(i+1, length):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


if __name__ == "__main__":
    test_data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print selection(test_data)
