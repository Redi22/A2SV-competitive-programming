class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        ans = [set() for i in range(n)]

        for out, inn in edges:
            graph[out].append(inn)
            indegree[inn] += 1
        
        queue = deque()
        for key in graph:
            if indegree[key] == 0:
                queue.append(key)
                
        while queue:
            curr = queue.popleft()
            for nei in graph[curr]:
                indegree[nei] -= 1
                ans[nei] = ans[nei] | ans[curr]
                ans[nei].add(curr)
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return [sorted(list(an)) for an in ans]
            
        
        