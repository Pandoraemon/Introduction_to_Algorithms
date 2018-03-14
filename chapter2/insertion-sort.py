#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# 插入排序


def insertion_sort(seq):
    for i in range(1, len(seq)):
        item = seq[i]
        for j in range(i)[::-1]:
            if item < seq[j]:
                seq[j+1] = seq[j]
                seq[j] = item
            else:
                break
    return seq


if __name__ == '__main__':
    seq = [5, 2, 4, 6, 1, 3]
    insertion_sort(seq)
    print(seq)
