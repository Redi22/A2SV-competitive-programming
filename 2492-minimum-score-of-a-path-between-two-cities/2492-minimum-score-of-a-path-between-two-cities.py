class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for s, d, dist in roads:
            graph[s].append((d, dist))
            graph[d].append((s, dist))
            
        min_dist = float('inf')
        visited = set()
        
        def traverse(node):
            nonlocal min_dist
            
            for nei, dist in graph[node]:
                min_dist = min(min_dist, dist)
                if nei not in visited:
                    visited.add(nei)
                    traverse(nei)
                    
        traverse(1)    
        return min_dist
                    
        
                    
            