# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return 
        
        slow = head
        fast = head.next
        
        if fast:
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if slow.next: slow.next = slow.next.next
            
        return head