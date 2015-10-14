#!/usr/bin/env python
# -*- coding: utf-8 -*-


def separate(array):
    if len(array) <= 1:  # 递归判断条件
        return array
    num = int(len(array) / 2)
    left = separate(array[:num])
    right = separate(array[num:])
    return merge(left, right)


def merge(left, right):
    l_index, r_index = 0, 0
    result = []
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    result += left[l_index:]  # 添加剩余元素
    result += right[r_index:]
    return result

if __name__ == "__main__":
    test_data = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print separate(test_data)
