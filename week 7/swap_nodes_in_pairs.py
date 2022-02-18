# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        temp = head
        prev = temp
        head = head.next
        curr = prev.next
        nex = prev.next.next
        
        while curr:
            if nex and nex.next:
                prev.next = nex.next
            else:
                prev.next = nex
            curr.next = prev
            prev = nex
            if nex:
                curr = nex.next
            if prev and prev.next:
                nex = prev.next.next
                
            else:
                break
        
        return head