# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        queue = deque([(p,q)])
    
        while queue:
            p, q = queue.popleft()
            
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            
        return True
                    
            
            