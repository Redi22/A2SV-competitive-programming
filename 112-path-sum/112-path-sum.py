# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root and not root.right and not root.left:
            if root.val ==targetSum:
                return True
            return False
        if not root:
            return False
        return self.hasPathSum(root.right , targetSum - root.val) or self.hasPathSum(root.left , targetSum-root.val)