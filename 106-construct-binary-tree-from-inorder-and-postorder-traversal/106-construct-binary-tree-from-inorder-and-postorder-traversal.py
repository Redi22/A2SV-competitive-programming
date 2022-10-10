# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inOrderDict = {inorder[i]: i for i in range(len(inorder))}
        i = len(postorder) - 1
        def dfs(s, e):
            nonlocal i
            if s > e or i < 0:
                return None
            
           
            inorderIdx = inOrderDict[postorder[i]]

            root = TreeNode(inorder[inorderIdx])
            i -= 1
            root.right = dfs(inorderIdx + 1, e)
            root.left  = dfs(s, inorderIdx - 1)
            

            
            return root
        
        return dfs(0, len(inorder) - 1)