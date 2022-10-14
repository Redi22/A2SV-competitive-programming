class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        canReach from course1 to course2 
        
        '''
        res = []
        graph = defaultdict(list)
        ans = [set() for _ in range(numCourses)]
        inDegree = defaultdict(int)
        queue = deque()

        for frm, to in prerequisites:
            graph[frm].append(to)
            inDegree[to] += 1
        
        for key in range(numCourses):
            if inDegree[key] == 0: 
                queue.append(key)
                
        while queue:
            curr = queue.popleft()
            for nei in graph[curr]:
                ans[nei] |= ans[curr]
                ans[nei].add(curr)
                
                inDegree[nei] -= 1
                
                if inDegree[nei] == 0:
                    queue.append(nei)
                    
        
        for frm, to in queries:
            res.append(frm in ans[to])
                
        return res