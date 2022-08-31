class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        ans = []
        outdegree = defaultdict(int)
        
        for i in range(len(graph)):
            for node in graph[i]:
                g[node].append(i)
            outdegree[i] = len(graph[i])
            
        
        queue = deque([])
        for i in range(len(graph)):
            if not graph[i]:
                queue.append(i)
                
        while queue:
            cur = queue.popleft()
            ans.append(cur)
            for n in g[cur]:
                outdegree[n] -= 1
                if outdegree[n] == 0:
                    queue.append(n)
                
        return sorted(ans)