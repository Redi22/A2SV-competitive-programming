# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return True if self.dfs(root) != float(-inf) else False
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if abs(left - right) <= 1:
            return 1 + max(self.dfs(root.right), self.dfs(root.left))
        return float(-inf)
        
                
            
        