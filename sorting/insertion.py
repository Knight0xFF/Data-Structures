#!/usr/bin/env python
# -*- coding: utf-8 -*-


def insertion(array):
    length = len(array)
    for i in xrange(1, length):
        if array[i] < array[i-1]:  # 判断顺序，如果正确就不用再排
            key = array[i]
            index = i
            '''
            for j in xrange(index-1, -1, -1):
                if key < array[j]:
                    array[j+1] = array[j]
                    index = j
                else:
                    break
            '''
            while key < array[index-1] and index >= 1:
                array[index] = array[index-1]
                index -= 1
            array[index] = key
    return array


if __name__ == "__main__":
    test_data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print insertion(test_data)
