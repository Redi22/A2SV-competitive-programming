class Solution:
    def inbound(self, i, j, n, m):
        if 0 <= i < n and 0 <= j < m:
            return True
        return False
    
    def traverse(self, i, j, grid, open_cells):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        if not self.inbound(i, j, len(grid), len(grid[0])) or grid[i][j] == -1:
            return 0
        
        if grid[i][j] == 2:
            if open_cells == 0:
                return 1
            return 0
    
        temp = 0
        for dx, dy in directions:  
            grid[i][j] = -1
            temp += self.traverse(i + dx, j + dy, grid, open_cells - 1)
            grid[i][j] = 0
            
        return temp
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = (-1, -1)
        open_cells = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                    open_cells += 1
                elif grid[i][j] == 0:
                    open_cells += 1
                    
        return self.traverse(start[0], start[1], grid, open_cells)
    
        