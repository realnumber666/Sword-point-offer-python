# -*- coding:utf-8 -*-
'''
1. head为空
2. k大于链表长度
3. k == 0, 倒数第0位，应该直接返回None
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if (head == None or k == 0):
            return None
        fast = head
        slow = head
        for i in range(k-1):
            if (fast.next == None):
                return None
            fast = fast.next
        
        while (fast.next != None):
            slow = slow.next
            fast = fast.next
            
        return slow