class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        temp = head
        
        while(temp.next != None):
            length += 1
            temp = temp.next
        
        if length == 1:
            head = None
            return head
        
        if length == n:
            head = head.next
            return head
        
        target = length - n
        length = 1
        temp = head
        
        while(length < target):
            length += 1
            temp = temp.next
            
        temp.next = temp.next.next
        return head
