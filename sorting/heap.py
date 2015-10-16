#!/usr/bin/env python
# -*- coding: utf-8 -*-


def heap_adjust(array, start, end):  # start为需要调整的堆的位置
    root = start
    while True:
        child = root * 2 + 1  # 获取子节点
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child+1]:  # 获得较大的子节点
            child += 1
        if array[root] < array[child]:  # 较大的节点为父节点
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break


def heap_sort(array):
    length = len(array)
    start = int(length/2 - 1)
    for i in xrange(start, -1, -1):
        heap_adjust(array, i, length-1)
    for i in xrange(length-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_adjust(array, 0, i-1)
    return array


if __name__ == "__main__":
    test_data = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    print heap_sort(test_data)
