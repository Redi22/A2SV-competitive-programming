# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1 2 4 _ _ _
        1 3 4 5 --  6 7 8 
        
        
        '''
        
        ans = ListNode()
        res = ans
        
        while list1 and list2:
            if list1.val <= list2.val:
                ans.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ans.next = ListNode(list2.val)
                list2 = list2.next
            ans = ans.next
            
        if list1:
            ans.next = list1
            
        if list2: 
            ans.next = list2
            
        return res.next