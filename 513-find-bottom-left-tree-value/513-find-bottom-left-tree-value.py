# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return []
        queue = collections.deque([root])
        popLen = 1
        level = []
        
        while queue:
            level = []
            temp = 0
            for i in range(popLen):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                    temp += 1
                if current.right:
                    queue.append(current.right)
                    temp += 1
            popLen = temp
        return level[0]