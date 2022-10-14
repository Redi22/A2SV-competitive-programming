# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = [[""], [""]]
        
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def traverse(node, path):
            if not node:
                return False
            
            if node.val == startValue:
                self.ans[0] = path[:]
            elif node.val == destValue:
                self.ans[1] = path[:]
                
            path.append("L")
            left =  traverse(node.left, path)
            path.pop()
            path.append("R")
            right = traverse(node.right, path)
            path.pop()
                
            return 
        
        traverse(root, [""])
        sToRoot = self.ans[0]
        rtoDst = self.ans[1]
        l = 0
        minn = min(len(sToRoot), len(rtoDst))
        while l < minn and sToRoot[l] == rtoDst[l]:
            l += 1
        
        sToRoot = ["U"] * (len(sToRoot) - l) 
        rtoDst = rtoDst[l:]
        
        return "".join(sToRoot + rtoDst)
        
        
    
        