# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return 
        stack = [root]
        ans = []
        
        while stack:
            neww = []
                    
            for cur in stack:
                if cur.left: neww.append(cur.left)
                if cur.right: neww.append(cur.right)
                    
            ans.append(stack[-1].val)
            stack = neww
        return ans
    