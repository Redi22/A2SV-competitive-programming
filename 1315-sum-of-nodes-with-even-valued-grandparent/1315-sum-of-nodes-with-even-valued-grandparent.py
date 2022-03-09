# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, totalSum=0):
        self.totalSum = totalSum
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sumEvenGran( root: TreeNode , parent: TreeNode , grand: TreeNode):
            if not root:
                return 0

            if grand and grand.val % 2 == 0:
                self.totalSum += root.val
                
            sumEvenGran(root.left , root , parent)
            sumEvenGran(root.right , root , parent) 

        
        sumEvenGran(root , None , None)
        return self.totalSum
    