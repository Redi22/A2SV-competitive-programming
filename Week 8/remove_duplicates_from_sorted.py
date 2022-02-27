# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        newList = ListNode()
        newHead = newList
        while head and head.next:
            if head.val != head.next.val:
                
                tempNode = ListNode(head.val)
                newList.next = tempNode
                
                head = head.next
                newList = newList.next
            else:
                temp = head.val
                while head and head.val == temp:
                    head = head.next
        if head:
            newList.next = head
        return newHead.next
     
                
                