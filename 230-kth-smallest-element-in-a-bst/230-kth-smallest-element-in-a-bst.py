# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root: Optional[TreeNode],) -> List[int]:
            if not root:
                return []
    
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) 
        
        Lst = inorderTraversal(root)
        
        return Lst[k - 1]