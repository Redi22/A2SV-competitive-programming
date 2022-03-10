class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        fresh = set()
        newlyRotten = set()
        directions = [[0,1] , [1,0] , [-1,0] , [0,-1]]
        m = len(grid)
        n = len(grid[0])
        step = 0
        
        inbound = lambda r ,c: 0 <= r < m and 0 <= c < n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                    
                elif grid[i][j] == 2:
                    rotten.add((i,j))
        while fresh:
            step += 1
            newlyRotten = set()
            for rot in rotten:
                for d in directions:
                    row = rot[0] + d[0]
                    col = rot[1] + d[1]
                    if inbound(row , col) and grid[row][col] == 1:
                        grid[row][col] = 2
                        newlyRotten.add((row,col))
            
            if len(newlyRotten) != 0:
                rotten = newlyRotten
                fresh = fresh.difference(newlyRotten)
            else:
                return -1
        return step
                