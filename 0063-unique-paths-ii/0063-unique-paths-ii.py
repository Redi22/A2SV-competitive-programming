class Solution:
    def inbound(self, i, j, n, m):
        if 0 <= i < n and 0 <= j < m:
            return True
        return False
    
    def traverse(self, i, j, obstacleGrid, memo):
        if not self.inbound(i, j, len(obstacleGrid), len(obstacleGrid[0])) or obstacleGrid[i][j] == 1:
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if (i, j) == (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1):
            return 1
        
        memo[(i, j)] = self.traverse(i + 1, j, obstacleGrid, memo) + self.traverse(i, j + 1, obstacleGrid, memo)  
            
        return memo[(i, j)]
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        return self.traverse(0, 0, obstacleGrid, memo)