# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefSum = defaultdict(int)
        prefSum[0] = 1
        
        def dfs(root, summ):
            if not root:
                return 0
            
            res = prefSum[summ + root.val - targetSum]
            
            prefSum[summ + root.val] += 1
            
            res += dfs(root.right, summ + root.val) + dfs(root.left, summ + root.val)
            prefSum[summ + root.val] -= 1
            
            return res
            
        return dfs(root, 0)