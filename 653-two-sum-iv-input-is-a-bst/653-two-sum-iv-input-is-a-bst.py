# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        
        def traverse(root):
            if not root: 
                return False
            
            if k - root.val in visited:
                return True
            
            visited.add(root.val)
            leftSide = traverse(root.left) 
            rightSide = traverse(root.right)
            
            return leftSide or rightSide
        
        return traverse(root)
    
            
            