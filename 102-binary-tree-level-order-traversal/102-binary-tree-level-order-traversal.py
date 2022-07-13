# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        popLen = 1
        elementLen = 0
        queue = collections.deque([])
        
        if root:
            queue.append(root)
        
        while queue:
            elementLen = popLen
            popLen = 0
            temp = []
            
            for i in range(elementLen):
                
                if queue:
                    current = queue.popleft()
                    temp.append(current.val)
                    if current.left:
                        queue.append(current.left)
                        popLen += 1
                    if current.right:
                        queue.append(current.right)
                        popLen += 1
                        
            ans.append(temp)
            
        return ans