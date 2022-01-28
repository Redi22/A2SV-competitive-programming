class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        temp = head
        head = head.next
        temp.next = None
        
        while head:
            faster = head.next
            head.next = temp
            temp = head
            head = faster
            
        return temp