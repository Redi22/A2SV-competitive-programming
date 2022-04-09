from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        inbound = lambda r , c: 0 <= r < m and 0 <= c < n
        @lru_cache()
        def dfs(i,j):
            if not inbound(i, j):
                return float("inf")
            if (i, j) == (m - 1, n - 1):
                return grid[i][j]
            return min(dfs(i+1,j) , dfs(i, j+1)) + grid[i][j]
        
        step = dfs(0,0)
        return step
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         direction = [[0,-1] , [-1,0]]
#         visited = {}
#         n = len(grid[0])
#         m = len(grid)
#         inbound = lambda r , c: 0 <= r < m and 0 <= c < n
#         queue = deque([((m-1,n-1) , grid[m-1][n-1])])
#         newStep = 0
#         minStep = 20002
#         while queue:
#             level = []
#             poplen = len(queue)
#             for i in range(poplen):
#                 (currX , currY ), step = queue.popleft()
#                 visited[(currX,currY)] = step
#                 if(currX , currY) == (0,0):
#                     minStep = min(minStep , step)
#                 for dx, dy in direction:
#                     newX , newY = currX + dx , currY + dy
#                     if inbound(newX , newY):
#                         if (newX,newY) not in visited.keys():
#                             newStep = step + grid[newX][newY]
#                             level.append(((newX, newY) , newStep))
                        
#             queue += level
                    
#         return minStep
                    
                