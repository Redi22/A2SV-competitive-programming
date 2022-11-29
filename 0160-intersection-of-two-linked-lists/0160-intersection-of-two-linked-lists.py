# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head):
        count = 0
        slow = head
        while slow:
            slow = slow.next
            count += 1
            
        return count
            
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = self.getLength(headA)
        len_b = self.getLength(headB)
        dummy_a = headA
        dummy_b = headB
        
        if len_a > len_b:
            for i in range(len_a - len_b):
                dummy_a = dummy_a.next
        else:
            for i in range(len_b - len_a):
                dummy_b = dummy_b.next
                
  
        while dummy_a and dummy_b and dummy_a != dummy_b:
            dummy_a = dummy_a.next
            dummy_b = dummy_b.next
            
      
        return dummy_a
            
                
        
        