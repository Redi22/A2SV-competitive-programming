# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxx = 0
        
        def traverse(root):
            nonlocal maxx
            
            if not root:
                return [0, float("-inf"), float("inf"), True]
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            if left[1] < root.val < right[2] and right[3] and left[3]:
                temp = left[0] + right[0] + root.val
                maxx = max(maxx, temp)
                return [temp, max(right[1], root.val), min(left[2], root.val), True]
            
            return [0, max(right[1], root.val), min(left[2], root.val), False]
        
        traverse(root)
        return maxx