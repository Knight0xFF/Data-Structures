#!/usr/bin/env python
# -*- coding: utf-8 -*-


def quick(array):
    return qsort(array, 0, len(array)-1)


def qsort(array, left, right):
    if left > right:
        return array
    key = array[left]
    l_index = left
    r_index = right
    while l_index < r_index:
        while array[r_index] >= key and l_index < r_index:
            r_index -= 1
        while array[l_index] <= key and l_index < r_index:
            l_index += 1
        array[l_index], array[r_index] = array[r_index], array[l_index]
    array[left], array[l_index] = array[l_index], key  # 左右往中移动最后重合，这个位置为key所应该在的位置
    qsort(array, left, l_index-1)
    qsort(array, l_index+1, right)
    return array

if __name__ == "__main__":
    test_data = [26, 44, 38, 5, 47, 15, 36, 3, 27, 2, 46, 4, 19, 50, 48]
    print quick(test_data)

