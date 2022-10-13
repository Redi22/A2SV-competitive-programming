# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        
        def inorder(root, idx):
            nonlocal ans
            if not root:
                return 0
            
            
            less = inorder(root.left, idx) + 1
            
            if idx + less  == k:
                ans = root.val
                
            more = inorder(root.right, less + idx )
            
            return less + more 
        
        inorder(root, 0)
        return ans