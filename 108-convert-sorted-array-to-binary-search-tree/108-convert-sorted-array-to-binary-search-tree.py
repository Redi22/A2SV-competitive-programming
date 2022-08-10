# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBst(arr):
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = makeBst(arr[:mid])
            root.right = makeBst(arr[mid + 1:])
            return root
        
        return makeBst(nums)
            
            