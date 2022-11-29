# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        slow = head
        start = head
        
        for i in range(k - 1):
            fast = fast.next
            start = start.next
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        start.val, slow.val = slow.val, start.val
        
        return head