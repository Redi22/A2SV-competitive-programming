class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        maxLength = 1
        
        def dfs(node):
            nonlocal maxLength
            possiblePath = [0, 0]
            
            for child in graph[node]:
                curr = dfs(child)

                if s[node] != s[child]:
                    heapq.heappush(possiblePath, curr)
                
                if len(possiblePath) > 2:
                    heapq.heappop(possiblePath)
                 
            maxLength = max(maxLength, 1 + sum(possiblePath))
            return 1 + max(possiblePath)
        
        for i, node in enumerate(parent):
            graph[node].append(i)
                
        dfs(0)
        return maxLength