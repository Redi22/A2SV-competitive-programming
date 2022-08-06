"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        stack = [root]
        prev = root
        
        while stack:
            neww = []

            for i in range(len(stack)-1):
                stack[i].next = stack[i + 1]
                
            for cur in stack:
                if cur.left: neww.append(cur.left)
                if cur.right: neww.append(cur.right)
                    
            stack = neww
        return root
    