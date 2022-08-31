class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        ans = [i for i in range(len(quiet))]
        
        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
            
        queue = deque([])
        for g in graph:
            if indegree[g] == 0:
                queue.append(g)  
        
        while queue:
            curr = queue.popleft()
            for nei in graph[curr]:
                indegree[nei] -= 1
                if quiet[ans[nei]] > quiet[ans[curr]]:
                    ans[nei] = ans[curr]
                    
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return ans
                
                    