class Solution:
    
    def isValid(self, x, y, n, grid):
        if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
            return True
        return False
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        start (0, 0) and use bfs for traversal
        
        '''
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1: 
            return -1
        
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
        queue = deque([(1,0,0)])
        visited = set([(0,0)])
        

        while queue:
            step, current_x, current_y = queue.popleft()
            
            if (current_x, current_y) == (n - 1, n - 1):
                return step
            
            for direction_x, direction_y in directions:
                new_direction_x = direction_x + current_x
                new_direction_y = direction_y + current_y
                
                if self.isValid(new_direction_x, new_direction_y, n, grid) and \
                (new_direction_x, new_direction_y) not in visited:
                    visited.add((new_direction_x, new_direction_y))
                    queue.append((step + 1, new_direction_x, new_direction_y))
                    
        return -1
                    