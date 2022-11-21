class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        queue = deque([(entrance, 0)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(maze)
        m = len(maze[0])
        exit_rows = [0, n - 1]
        exit_cols = [0, m - 1] 
        
        while queue:
            current, step = queue.popleft()
            
            if (current[0], current[1]) in visited:
                continue
                
            visited.add((current[0], current[1]))
            
            if (current[0] in exit_rows or current[1] in exit_cols) and current != entrance:
                return step
            
            for dx, dy in directions:
                new_x = dx + current[0]
                new_y = dy + current[1]
                
                if 0 <= new_x < n and 0 <= new_y < m and maze[new_x][new_y] == "." and (new_x, new_y) not in visited:
                    queue.append(((new_x, new_y), step + 1))
                    
        return -1
                    
            
                    
                