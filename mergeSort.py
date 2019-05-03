# -*- coding: UTF-8 -*-
def mergeSortedToOne(a, b):
    i, j = 0, 0
    res = []
    # 都指着两个数列的头，比较大小，小的放在res里，指针挪一位，再进行比较
    while (i <= len(a)-1 and j <= len(b)-1):
        a_item = a[i]
        b_item = b[j]
        if (a_item < b_item):
            res.append(a_item)
            i += 1
        elif (a_item > b_item):
            res.append(b_item)
            j += 1
    if (i <= len(a)-1):
        res += a[i:]
    if (j <= len(b)-1):
        res += b[j:]

    return res

def mergeSort(arr):
    '''
    对半拆分arr，直到拆到单个
    从下往上将两个有序的arr拼接为一个有序的arr
    '''
    if (len(arr) <= 1):
        return arr

    left = mergeSort(arr[0:len(arr)//2])
    right = mergeSort(arr[len(arr)//2:])

    res = mergeSortedToOne(left, right)

    return res

arr = [10, 23, 51, 18, 4, 31, 5, 13]
print mergeSort(arr)
    