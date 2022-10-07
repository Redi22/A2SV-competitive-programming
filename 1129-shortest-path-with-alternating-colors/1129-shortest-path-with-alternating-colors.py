class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda: defaultdict(list))
        
        for start, end in redEdges:
            graph[True][start].append(end)
            
        for start, end in blueEdges:
            graph[False][start].append(end)
            
        queue = deque([(0, 0, False),(0, 0, True) ])
        res = [-1] * n
        visited = set()
        
        while queue:
            dist, node, color = queue.popleft()
            if res[node] == -1:
                res[node] = dist
            else:
                res[node] = min(res[node], dist)
            # print(not color, graph[not color][node])
            for nei in graph[not color][node]:
                # print(nei, node, color, dist)

                if (node, nei, not color) not in visited:
                    visited.add((node, nei,not color))
                    queue.append((dist + 1, nei, not color))
                    
        return res