class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
        
        def traverse(node, parent):
            res = 0
            for nei in graph[node]:
                if nei != parent:
                    temp = traverse(nei, node)
                    if hasApple[nei] or temp != 0:
                        res += temp + 2

            return res 
        
        return traverse(0, -1)
        
                    
                    