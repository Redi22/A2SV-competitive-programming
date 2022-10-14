class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        '''
        build the relationship
        start from the less fortunate
        remove edges and take the min of quiteness from the coming nodes as an ans for the curr
        
        
        '''
        
        graph = defaultdict(list)
        ans = [i for i in range(len(quiet))]
        inDegree = defaultdict(int)
        queue = deque([])
        
        for rich, poor in richer:
            graph[rich].append(poor)
            inDegree[poor] += 1
        
        for i in range(len(quiet)):
            if inDegree[i] == 0:
                queue.append(i)
                
        while queue:
            curr = queue.popleft()
            for nei in graph[curr]:
                inDegree[nei] -= 1
                
                if quiet[ans[nei]] > quiet[ans[curr]]:
                    ans[nei] = ans[curr]
                    
                if inDegree[nei] == 0:
                    queue.append(nei)

        return ans