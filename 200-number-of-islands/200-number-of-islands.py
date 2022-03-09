class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1] , [1,0] , [0,-1] , [-1,0]]
        count = 0
        n = len(grid)
        m = len(grid[0])
        visited = set()
        
        inbounded = lambda r , c: 0 <= r < n and 0 <= c < m
        
        def dfsTraversal( row: int , col: int):
            visited.add((row , col))
            for d in directions:
                new_row , new_col = row + d[0] , col + d[1]
                
                if (new_row ,  new_col) not in visited and inbounded(new_row , new_col) and int(grid[new_row][new_col]) == 1:
                    dfsTraversal(new_row , new_col)
                
        for i in range(n):
            for j in range(m):
                if (i , j) not in visited and int(grid[i][j]) == 1:
                    dfsTraversal(i , j) 
                    count += 1
        return count