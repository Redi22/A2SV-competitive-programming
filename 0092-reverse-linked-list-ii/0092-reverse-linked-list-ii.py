# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        current = head
        before_last = None
        count = 0
        
        for i in range(left - 1):
            before_last = current
            current = current.next
            
        last = current
        
        while current and count <= (right - left):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1
            
        last.next = current
        if before_last:
            before_last.next = prev
        
        return head if before_last else prev
        