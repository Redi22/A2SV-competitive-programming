# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorderTraversal(root) -> List[int]:
            if not root:
                return []
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
        check = inorderTraversal(root)
        isTrue = True
        for i in range(len(check)-1):
            if check[i] >= check[i+1]:
                isTrue = False
                break
        
        return isTrue
        
        