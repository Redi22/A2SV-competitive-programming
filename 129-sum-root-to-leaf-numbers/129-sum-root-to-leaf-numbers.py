# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = []
        def dfs(summ, node):
            if not node:
                return 0
            summ = summ * 10 + node.val
            
            if not node.left and not node.right:
                return summ
            
            return dfs(summ, node.left) + dfs(summ, node.right)
            
           
    
        return dfs(0, root)
        