class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0,1] , [0,-1] , [-1,0] , [1,0]]
        m = len(grid)
        n = len(grid[0])
        count = 0
        inbound = lambda r,c: 0<= r < m and 0<= c < n
        
        def dfsTraversal(row, col):
            visited.add((row, col))
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if inbound(new_row , new_col) and (new_row , new_col) not in visited and grid[new_row][new_col] == 1:
                    dfsTraversal(new_row,new_col)
                    
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        dfsTraversal(i,j)
                    
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    count += 1
        return count
                    
                    
                
            