class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [ [0]*n for i in range(m)]
        ans = 0
        
        for g in guards:
            grid[g[0]][g[1]] = 1
      
        for w in walls:
            grid[w[0]][w[1]] = -1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for backward in range(i-1, -1, -1):
                        if grid[backward][j] == -1 or grid[backward][j] == 1:
                            break
                        grid[backward][j] = 2
                    for forward in range(i+1, m):
                        if grid[forward][j] == -1 or grid[forward][j] == 1:
                            break
                        grid[forward][j] = 2
                        
                    for upward in range(j-1, -1, -1):
                        if grid[i][upward] == -1 or grid[i][upward] == 1:
                            break
                        grid[i][upward] = 2
                    for downward in range(j+1, n):
                        if grid[i][downward] == -1 or grid[i][downward] == 1:
                            break
                        grid[i][downward] = 2
                        
        for i in range(m):
            ans += grid[i].count(0)
            
        return ans