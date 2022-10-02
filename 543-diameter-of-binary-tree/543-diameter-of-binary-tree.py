# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth = 0
        
        def dfs(root):
            nonlocal depth
            
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            
            depth = max(depth, left + right + 2)
            
            return 1 + max(left, right)
        
        dfs(root)
        return depth
            