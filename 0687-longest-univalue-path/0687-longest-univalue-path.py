# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = 0
        def traverse(root, parent):
            nonlocal ans
            if not root:
                return 0
            
            left = traverse(root.left, root.val)
            right = traverse(root.right, root.val)
            ans = max(ans, left + right)
            if root.val == parent:
                return max(left, right) + 1
            return 0
            
            
        
        traverse(root,  root.val)
        return ans