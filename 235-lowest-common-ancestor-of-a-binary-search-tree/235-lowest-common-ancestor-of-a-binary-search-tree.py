# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recc(node):
            if node.val == p.val or node.val == q.val:
                return node
            
            if node.val < p.val and node.val < q.val:
                return recc(node.right)
                
            if node.val > p.val and node.val > q.val:
                return recc(node.left)
                
            return node
        
        return recc(root)