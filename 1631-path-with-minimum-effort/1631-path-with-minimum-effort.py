class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        DIR = [[0,1], [0,-1], [-1,0], [1,0]]
        heap = [(0,(n-1, m-1))]
        ans = 0
        
        inBound = lambda r,c: 0 <= r < n and 0 <= c < m
        visited = set()
        
        while heap:
            step, curr = heappop(heap)
            
            ans = max(ans, step)
            if curr == (0, 0):
                return ans
            
            currX, currY = curr
            visited.add(curr)
            
            for dx, dy in DIR:
                nx = currX + dx
                ny = currY + dy
                
                if (nx, ny) not in visited and inBound(nx, ny):
                    newStep = abs(heights[currX][currY] - heights[nx][ny])
                    heappush(heap, (newStep, (nx,ny)))
                    
        return ans