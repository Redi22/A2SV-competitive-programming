# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        current = head
        count = 0
        
        for i in range(left - 1):
            current = current.next
            
        last = current
        
        while current and count <= (right - left):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1
            
        return prev 
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        prev = ListNode(0)
        ans = prev
        
        while dummy:
            start = dummy
            right = 0
            full = True
            
            for i in range(k):
                if not dummy:
                    full = False
                    break
                dummy = dummy.next
                right += 1
                
            if full:
                prev.next = self.reverseBetween(start, 1, right)
                for i in range(k):
                    prev = prev.next
                    
            else:
                prev.next = start
                start = start.next
                
                    
        return ans.next
            