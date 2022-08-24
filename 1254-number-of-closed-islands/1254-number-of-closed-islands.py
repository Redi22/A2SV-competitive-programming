class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n, island  = len(grid), len(grid[0]), 0
        DIR = [[1,0], [0,1], [-1,0], [0, -1]]
        
        inBound = lambda r, c: 0 <= r < m and 0 <= c < n

        
        def bfs(i, j):
            res = True
            currX, currY = i, j
            grid[currX][currY] = -1
            for dx, dy in DIR:
                nx = currX + dx
                ny = currY + dy

                if inBound(nx, ny) and grid[nx][ny] == 0:
                    res &= bfs(nx, ny)

            if currX==0 or currX==m-1 or currY==0 or currY==n-1:
                res = False
                
            return res
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if bfs(i, j):
                        island +=1
        
        return island