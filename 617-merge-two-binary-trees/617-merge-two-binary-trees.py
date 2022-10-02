# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merger(root1, root2):
            if not root1 and not root2:
                return None
            
            r1 = root1.val if root1 else 0
            r2 = root2.val if root2 else 0
            
            root = TreeNode(r1 + r2)
            root.right = merger(root1.right if root1 else None, root2.right if root2 else None)
            root.left = merger(root1.left if root1 else None, root2.left if root2 else None)
            
            return root
        
        return merger(root1, root2)
            