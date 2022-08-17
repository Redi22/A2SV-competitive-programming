class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        valid = {
            2:[(-1,0),(1,0)],
            1:[(0,1),(0,-1)],
            5:[(-1,0),(0,-1)],
            3:[(1,0),(0,-1)],
            6:[(0,1),(-1,0)],
            4:[(0,1),(1,0)]
        }
        
        m = len(grid)
        n = len(grid[0])
        in_bound = lambda r,c: 0<= r < m and 0<= c < n
        visited = set()
        queue = deque([(0,0)])
        
        while queue:
            currX, currY = queue.popleft()
            if (currX, currY) == (len(grid) - 1, len(grid[0]) - 1):
                return True
            visited.add((currX, currY))
            for x,y in valid[grid[currX][currY]]:
                nx = x + currX
                ny = y + currY
                
                if in_bound(nx,ny) and (nx, ny) not in visited:
                    if (-x,-y) in valid[grid[nx][ny]]:
                        queue.append((nx, ny))
                    
        return False