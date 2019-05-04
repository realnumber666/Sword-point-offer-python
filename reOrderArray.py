# -*- coding:utf-8 -*-
'''
1. 数字原本顺序会被打乱的方法，前后针
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        l = 0
        r = len(array)-1
        while (l <= r):
            l_value = array[l]
            r_value = array[r]
            if (l_value%2 == 0 and r_value%2 == 1):
                array[l], array[r] = array[r], array[l]
            elif (l_value%2 == 1):
                l += 1
            elif (r_value%2 == 0):
                r -= 1
                
        return array

'''
2. 不占用多余空间的inplace算法，类似冒泡算法
时间复杂度O(n^2)
'''

'''
3. 空间换时间，直接新建数组
时间复杂度O(n)
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in range(len(array)):
            if (array[i]%2 == 0):
                even.append(array[i])
            else:
                odd.append(array[i])
        return odd+even