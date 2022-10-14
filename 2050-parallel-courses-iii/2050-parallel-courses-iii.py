class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dp = time[:]
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        queue = deque([])
        
        for frm, to in relations:
            graph[frm].append(to)
            inDegree[to] += 1
            
        for i in range(1, n + 1):
            if inDegree[i] == 0: 
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            for nei in graph[curr]:
                inDegree[nei] -= 1
                dp[nei - 1] = max(dp[nei - 1], dp[curr - 1] + time[nei - 1])
                
                if inDegree[nei] == 0:
                    queue.append(nei)
                    
        return max(dp)