# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 or not list2:
            if not list1:
                return list2
            else:
                return list1
        
        
        if list1.val <= list2.val:
            answer = list1
            p1 = answer.next
            p2 = list2
            
        else:
            answer = list2
            p1 = answer.next
            p2 = list1
        
        head = answer
        
        while p1 or p2:
            if not p1:
                head.next = p2
                p2 = p2.next
                head = head.next
            elif not p2:
                head.next = p1
                p1 = p1.next
                head = head.next
                
            elif p2.val <= p1.val:
                head.next = p2
                head = head.next
                p2 = p2.next
                
            else:
                head.next = p1
                head = head.next
                p1 = p1.next
                
        return answer