# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        graph = defaultdict(list)
        
        def dfs(node, parent):
            if parent: graph[node].append(parent)
            if node.left:
                graph[node].append(node.left)
                dfs(node.left, node)
            if node.right:
                graph[node].append(node.right)
                dfs(node.right, node)
        
        dfs(root, None)        
        queue = deque([(target, 0)])
        visited = set()
        
        while queue:
            cur, dis = queue.popleft()
            if cur not in visited:
                visited.add(cur)
                if dis > k:
                    continue
                
                if dis == k:
                    res.append(cur.val)
            
                for n in graph[cur]:
                    queue.append((n, 1+dis))
        
        
        
        return res