class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        
        @lru_cache(None)
        def dp(i, j):
            if i >= rows or j >= cols:
                return float("-inf")
            
            if i == rows - 1 and j == cols - 1:
                return min(dungeon[i][j], 0)
            
            return min(0, dungeon[i][j] + max(dp(i+1, j), dp(i, j+1)))
                    
        return abs(dp(0, 0)) + 1
                     
                
                