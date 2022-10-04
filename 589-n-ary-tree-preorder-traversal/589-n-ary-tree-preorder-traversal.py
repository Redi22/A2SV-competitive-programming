"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def traverse(root):
            if not root:
                return []
            res = []
            for child in root.children:
                res += traverse(child)
                
            return [root.val] + res
        
        return traverse(root)
        