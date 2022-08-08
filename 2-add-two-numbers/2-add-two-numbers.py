# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        res = ans
        
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = 0
            if temp > 9:
                carry = temp // 10
                temp = temp % 10
                
            l1 = l1.next
            l2 = l2.next
            ans.next = ListNode(temp)
            ans = ans.next
            
        while l1:
            temp = l1.val + carry
            carry = 0
            if temp > 9:
                carry = temp // 10
                temp = temp % 10
            ans.next = ListNode(temp)
            ans = ans.next
            l1 = l1.next
        while l2:
            temp = l2.val + carry
            carry = 0
            if temp > 9:
                carry = temp // 10
                temp = temp % 10
            ans.next = ListNode(temp)
            ans = ans.next
            l2 = l2.next
            
        if carry:
            ans.next = ListNode(carry)
        
        return res.next
            
        
        