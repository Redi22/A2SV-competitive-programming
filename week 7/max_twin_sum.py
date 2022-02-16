if not head:
            return head
        
        maxSum = 0
        
        start = ListNode(head.val,None)
        original = start
        
        reverse = head
        head = head.next
        reverse.next = None
        
        while head:
            start.next = ListNode(head.val,None)
            start = start.next
            
            faster = head.next
            head.next = reverse
            reverse = head
            head = faster
        
        while reverse and original:
            tempSum = reverse.val + original.val
            maxSum = max(tempSum , maxSum)
            
            reverse = reverse.next
            original = original.next
        
        return maxSum