#!/usr/bin/env python
# -*- coding: utf-8 -*-


def shell(array):
    length = len(array)
    steps = int(length/2)
    while steps > 0:
        for i in xrange(steps, length):
            key = array[i]
            index = i
            while array[index - steps] > key and index >= steps:
                array[index] = array[index - steps]
                index -= steps
            array[index] = key
        steps = int(steps/2)
    return array

if __name__ == "__main__":
    test_data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print shell(test_data)
