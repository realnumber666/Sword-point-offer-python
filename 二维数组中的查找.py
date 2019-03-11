# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        '''
        从右上角开始，若target > a => col - 1
                     target < a => row + 1
        直到target = a ,return
        '''
        rows = len(array)
        if(rows == 0):
            return False
        cols = len(array[0])
        if(cols == 0):
            return False
        row = 0
        col = cols - 1
        a = array[row][col]
        while(row < rows and col >= 0):
            if(target == a):
                return True
            elif(target > a):
                col -= col
            else:
                row += row
        return False