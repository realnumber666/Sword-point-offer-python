# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while (n):
            n = (n-1) & n
            print bin(n)
            count += 1
        return count

print bin((-3-1)&(-3))