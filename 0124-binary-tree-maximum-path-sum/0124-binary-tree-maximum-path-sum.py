# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = float("-inf")
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float("-inf")
            
            if not root.left and not root.right:
                self.ans = max(self.ans, root.val)
                return root.val
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, left + root.val, right + root.val, left + right + root.val, root.val)
            res = max(left + root.val, right + root.val, root.val)
            return res
            
        
        dfs(root)
        return self.ans