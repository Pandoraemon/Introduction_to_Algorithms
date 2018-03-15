#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 习题2.2-2 选择排序


def get_minimum_index(seq):
    minimum_value = seq[0]
    minimum_index = 0
    for i in range(1, len(seq)):
        if seq[i] < minimum_value:
            minimum_value = seq[i]
            minimum_index = i
    return minimum_index


def select_sort(seq):
    for i in range(len(seq)-1):
        minimum_index = get_minimum_index(seq[i:]) + i  # 子数列的index， 需要加上之前已排序的i
        seq[i], seq[minimum_index] = seq[minimum_index], seq[i]
    return seq


if __name__ == '__main__':
    seq = [4, 2, 5, 1, 6, 3]
    select_sort(seq)
    print(seq)