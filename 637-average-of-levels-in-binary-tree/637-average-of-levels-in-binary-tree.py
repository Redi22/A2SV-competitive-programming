# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        aveArray = []
        popLen = 1
        elementLen = 0
        queue = collections.deque([root])
        
        while queue:
            elementLen = popLen
            popLen = 0
            total = 0
            
            for i in range(elementLen):
                if queue:
                    current = queue.popleft()
                    total += current.val
                    if current.left:
                        queue.append(current.left)
                        popLen += 1
                    if current.right:
                        queue.append(current.right)
                        popLen += 1
            aveArray.append(total / elementLen)
            
        return aveArray
            
            
            