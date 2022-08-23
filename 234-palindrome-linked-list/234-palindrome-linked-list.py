# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        stack = []
        
        if not slow.next:
            return True
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast:
            slow = slow.next
            
        for i in range(len(stack) - 1, -1, -1):
            
            if not slow or stack[i] != slow.val:
                return False
            slow = slow.next
            
        return True