class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited  = set()
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1] , [1,0] , [-1,0] , [0,-1]]
        inbound = lambda r , c: 0 <= r < m and 0 <= c < n
        count = 0
        maxCount = 0
        def dfsTraversal(row , col):
            nonlocal count 
            visited.add((row, col))
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if inbound(new_row, new_col) and (new_row , new_col) not in visited and grid[new_row][new_col] == 1:
                    count += 1
                    dfsTraversal(new_row , new_col)
            
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    dfsTraversal(i,j)
                    count += 1
                maxCount = max(count, maxCount)
                count = 0
        
        return maxCount