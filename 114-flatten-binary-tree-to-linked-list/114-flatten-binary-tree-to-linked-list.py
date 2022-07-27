# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = []
        if root.right: stack.append(root.right)
        if root.left: stack.append(root.left)
        
        curr = root
        while stack:
            nxt = stack.pop()
            curr.left = None
            curr.right = nxt
            
            if nxt.right: stack.append(nxt.right)
            if nxt.left: stack.append(nxt.left)
            
            curr = nxt