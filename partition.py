# -*- coding: UTF-8 -*-
def partition(arr, start, end):
    pivot = arr[start]
    # 初始化左右针
    l = start+1
    r = end
    # 在l<=r时循环
    while (l <= r):
        l_value = arr[l]
        r_value = arr[r]
        # 若l的值大于pivot，且r的值小于pivot，交换
        if (l_value > pivot and r_value < pivot):
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        # 若l的值小于pivot，l+1
        elif (l_value < pivot):
            l += 1
        # 若r的值大于pivot，r-1
        elif (r_value > pivot):
            r -= 1
    # 交换r和pivot，完成本轮排序
    arr[r], arr[start] = arr[start], arr[r]
    return arr


arr = [10, 23, 51, 18, 4, 31, 5, 13]
print partition(arr , 0, len(arr)-1)