# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(node, summ):
            if not node:
                return 0
            right = traverse(node.right, summ)
            
            node.val = max(right + node.val, summ + node.val)
            
            left = traverse(node.left, node.val)
            return max(left, node.val)
        
        traverse(root, 0)
        return root