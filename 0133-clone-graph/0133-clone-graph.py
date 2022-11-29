"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue = deque([node])
        visited = {node.val: Node(node.val)}
        
        while queue:
            current = queue.popleft()
            clone_current = visited[current.val]
            
            for nei in current.neighbors:
                if nei.val not in visited:
                    visited[nei.val] = Node(nei.val)
                    queue.append(nei)
                    
                clone_current.neighbors.append(visited[nei.val])
        
        return visited[node.val]
                
                