# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def builder(arr):
            if not arr:
                return None 
            maxx =  max(arr)
            maxIdx = arr.index(maxx)
            
            root = TreeNode(maxx)
            root.right =  builder(arr[maxIdx+1:])
            root.left =  builder(arr[:maxIdx])
            
            return root
        
        return builder(nums)