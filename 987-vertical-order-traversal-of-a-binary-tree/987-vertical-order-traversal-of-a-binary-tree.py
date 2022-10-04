# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [(root, 0)]
        ans = defaultdict(list)
        
        while queue:
            newLevel = []
            res = defaultdict(list)
            
            for child, col in queue:
                res[col].append(child.val)
                if child.right:
                    newLevel.append((child.right, col + 1))
                    
                if child.left:
                    newLevel.append((child.left, col - 1))
                    
            for key in res:
                ans[key] += sorted(res[key])
                
            queue = newLevel
            
        return [ans[key] for key in sorted(ans.keys())]
                