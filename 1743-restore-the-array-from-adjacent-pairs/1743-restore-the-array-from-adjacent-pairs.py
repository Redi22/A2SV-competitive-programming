class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        root = None
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        for r in graph:
            if len(graph[r]) == 1:
                root = r 
                break
                
        
        result = []
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            result.append(node)
            
            for nei in graph[node]:
                dfs(nei)
                
        dfs(root)
        return result
            