class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        
    
        def traverse(i):
            if i not in graph or i in visited:
                return 
            
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    traverse(j)
            return 
        
        for i, (start, end, radius) in enumerate(bombs):
            for j, (s, e, r) in enumerate(bombs):
                if sqrt((start - s) ** 2 + (end - e) ** 2) <= radius:
                    graph[i].append(j)
            
        max_len = float("-inf")
        for i in range(len(bombs)):
            visited = set()
            length = traverse(i)
            max_len = max(max_len, len(visited))
            
        return max_len