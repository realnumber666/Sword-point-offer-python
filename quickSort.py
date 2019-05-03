# -*- coding: UTF-8 -*-
from partition import partition

def quickSort(arr, begin, end):
    '''
    partition(arr,0,len-1)
    把pivot_index右边和左边的再分别放进去
    直到数组长度<=1
    '''
    if (end - begin > 1):
        pivot_index = partition(arr, begin, end)
        # 因为partition是直接在原数组上操作，没有再进行拼接操作，所以一定要传begin, end的index
        quickSort(arr, 0, pivot_index - 1)
        quickSort(arr, pivot_index + 1, end)

    return arr

arr = [10, 23, 51, 18, 4, 31, 5, 13]
print quickSort(arr, 0, len(arr) - 1)