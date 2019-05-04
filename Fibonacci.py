# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        def core(n):
            if (n == 0):
                return 0
            if (n == 1):
                return 1
            if (n == 2):
                return 1
            if (arr[n] != 0):
                return arr[n]
            
            arr[n] = core(n-1) + core(n-2)
            return arr[n]
        # write code here
        arr = [0]*(n+1)
        return core(n)
        
        

print Solution().Fibonacci(39)