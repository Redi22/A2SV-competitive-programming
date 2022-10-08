class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        directly connected components 
        '''
        
        graph = defaultdict(list)
        res = [-1] * len(queries)
        
        for i, (num, div) in enumerate(equations):
            graph[num].append((div, values[i]))
            graph[div].append((num, 1 / values[i]))
            
        for i, (num, div) in enumerate(queries):
                
            queue = deque([(num,1)])
            ans = 1
            visited = set()
            
            while queue:
                curr = queue.popleft()
                visited.add(curr[0])
                if curr[0] == div:
                    if num in graph.keys():
                        res[i] = curr[1]
                    
                    break

                for child in graph[curr[0]]:
                    if child[0] not in visited:
                        queue.append((child[0], child[1] * curr[1]))
            
        
        return res
                    
            