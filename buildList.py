class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

head = ListNode(1)
head.next = ListNode(2)
print head.next