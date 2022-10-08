class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        queue = [(0,k)]
        visited = {}
        
        for frm, to, weight in times:
            graph[frm].append((weight, to))
            
        while queue:
            dist, curr = heapq.heappop(queue)
            
            if curr not in visited:
                visited[curr] = dist
                
                for weight, node in graph[curr]: 
                    heapq.heappush(queue, (weight + dist, node))
                    
        return max(visited.values()) if len(visited) == n else -1
            
                
            
                
                
            
            
            
        