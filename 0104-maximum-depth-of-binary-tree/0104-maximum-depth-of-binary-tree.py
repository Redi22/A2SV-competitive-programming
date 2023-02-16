# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        queue = [root]
        while queue:
            newLevel = []
            for node in queue:
                if node.right: newLevel.append(node.right)
                if node.left: newLevel.append(node.left)
                    
            queue = newLevel
            ans += 1
            
        return ans