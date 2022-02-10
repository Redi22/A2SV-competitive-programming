# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        halfStack = []
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            halfStack.append(slow.val)
            slow = slow.next
            
        if fast:
            slow = slow.next
        while slow:
            if not slow.val == halfStack.pop():
                return False
            else:
                slow = slow.next
        return True
        
            