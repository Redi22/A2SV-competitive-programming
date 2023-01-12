class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        res = max(vals)
        graph = defaultdict(list)
        
        for s, d in edges:
            graph[s].append(vals[d])
            graph[d].append(vals[s])
            
        for node in graph:
            temp_k = 0
            graph[node] = sorted(graph[node], reverse = True)
            current = vals[node]
            
            for nei in graph[node]:
                if temp_k == k:
                    break
                    
                temp_k += 1
                current = max(nei + current, current)
                
            res = max(res, current)
        return res
    