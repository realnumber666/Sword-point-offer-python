temp = listNode.val
        if(listNode.next == None):
            return listNode
        pointer1 = listNode.next
        if(pointer1.next == None):
            pointer1.next = ListNode(temp)
            return pointer1
        pointer2 = pointer1.next
        while(pointer1.next != None):
            pointer1.next = ListNode(temp)
            temp = pointer1.val
            pointer1 = pointer2
            pointer2 = pointer2.next
        return pointer1