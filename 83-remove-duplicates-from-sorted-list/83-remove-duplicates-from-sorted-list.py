# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        slow = head
        fast = head.next
        
        while fast:
            while fast and fast.val == slow.val:
                fast = fast.next
                slow.next = fast
            slow = slow.next
            
            if fast and fast.next:
                fast = fast.next
        
        return head
        
        
        
        