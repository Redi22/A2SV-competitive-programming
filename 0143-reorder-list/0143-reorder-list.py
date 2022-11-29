# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = self.reverseList(slow.next)
        slow.next = None
        
        
        dummy_first, dummy_second = head, prev
        while dummy_second:
            nextt = dummy_first.next
            dummy_first.next = dummy_second
            dummy_first = dummy_second
            dummy_second = nextt
        