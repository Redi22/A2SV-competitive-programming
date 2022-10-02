# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            
            withRoot = left[1] + right[1] + root.val
            withoutRoot = max(left) + max(right)
                
            return [withRoot, withoutRoot]
        
        return max(dfs(root))