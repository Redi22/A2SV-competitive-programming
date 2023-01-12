class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [1] * n
        graph = defaultdict(list)
        
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
                
        
        def dfs(node, parent):
            total = 0
            count = defaultdict(int)
            
            for nei in graph[node]:
                if nei != parent:
                    curr = dfs(nei,node)
                    curr[labels[nei]] += 1
                    total += curr[labels[node]]
                    
                    for i in curr:
                        count[i] += curr[i]
            
            res[node] += total
            return count
                    
        
        dfs(0, -1)
        return res