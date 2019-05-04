# -*- coding:utf-8 -*-
class Stack:
    def __init__(self):
        self.items = []
    def top(self):
        return self.items[-1]
    def pop(self):
        return self.items.pop()
    def push(self, item):
        self.items.append(item)
    def isEmpty(self):
        return self.items == []
    
class Solution:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack() # 辅助栈
    def push(self, node):
        # write code here
        # 如果stack1为空，直接append
        if (self.stack1.isEmpty()):
            self.stack1.push(node)
        # 如果stack1非空，把stack1的元素弹出，放进stack2
        # 新元素放入stack1，再把stack2元素弹出，放入stack1
        else:
            while (!self.stack1.isEmpty()):
                item = self.stack1.pop()
                self.stack2.push(item)
            self.stack1.push(node)
            while (!self.stack2.isEmpty()):
                item = self.stack2.pop()
                self.stack1.push(item)
    def pop(self):
        # return xx
        return self.stack1.pop()