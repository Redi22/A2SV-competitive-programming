class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        build indegree lookup based on the lesser elements directed to the greater ones
        from the ones with 0 indegree start sorting and counting the max
        update the global maxx accordingly 
        
        '''
        
        
        inDegree = defaultdict(int)
        n = len(matrix)
        m = len(matrix[0])
        DIR = [[0,1], [1,0], [-1,0], [0,-1]]
        queue = deque([])
        maxx = float("-inf")
        inBound = lambda r, c: 0 <= r < n and 0 <= c < m
        
        for i in range(n):
            for j in range(m):
                for dx, dy in DIR:
                    if inBound(i + dx, j + dy) and matrix[i + dx][j + dy] < matrix[i][j]:
                        inDegree[(i,j)] += 1
        
        for i in range(n):
            for j in range(m):
                if inDegree[(i, j)] == 0: queue.append((1, i, j))
        
        while queue:
            step, i, j = queue.popleft()
            maxx = max(step, maxx)
            
            for dx, dy in DIR:
                if inBound(i + dx, j + dy) and matrix[i + dx][j + dy] > matrix[i][j]:
                    inDegree[(i + dx, j + dy)] -= 1
                    
                    if inDegree[(i + dx, j + dy)] == 0:
                        queue.append((step + 1, i + dx, j + dy))
                    
        return maxx