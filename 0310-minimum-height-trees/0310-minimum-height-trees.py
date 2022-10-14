class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        can only be 2 
        highest dependency should be candidate
        get leaf nodes and keep removing 
        get the last 2 candidates and return 
        
        '''
        graph = defaultdict(list)
        queue = []
        candidates = n
        degree = defaultdict(int)
        seen = set()
        
        if n < 3: return [i for i in range(n)]
        
        for frm, to in edges:
            graph[frm].append(to)
            graph[to].append(frm)
            degree[frm] += 1
            degree[to] += 1

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
                seen.add(i)

        while queue and candidates > 2:
            newLevel =  []
            for curr in queue:
                seen.add(curr)
                candidates -= 1
                for nei in graph[curr]:
                    degree[nei] -= 1
                    
                    if degree[nei] == 1:
                        newLevel.append(nei)
            queue = newLevel
            
            

        return [i for i in range(n) if i not in seen]
                    
        
            
            