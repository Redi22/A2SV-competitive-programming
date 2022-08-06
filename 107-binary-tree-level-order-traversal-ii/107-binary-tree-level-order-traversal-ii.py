# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        stack = [root]
        ans = []
        
        while stack:
            ans.append([])
            neww = []
            
            for cur in stack:
                ans[-1].append(cur.val)
                
                if cur.left: neww.append(cur.left)
                if cur.right: neww.append(cur.right)
                    
            stack = neww
            
        return ans[::-1]