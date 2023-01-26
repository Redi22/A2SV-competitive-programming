class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        visited = [float("inf")] * n
        
        for frm, to, price in flights:
            graph[frm].append((price, to))
            
        queue = [(0, 0, src)]
        while queue:
            price, step, curr = heapq.heappop(queue)
            
            if visited[curr] <= step:  
                continue
                
            if curr == dst:
                return price
            
            if step > k:
                continue
            
            visited[curr] = step
            
            for p, node in graph[curr]:
                heapq.heappush(queue, (p + price, step + 1, node))
                    
        return -1
    
    