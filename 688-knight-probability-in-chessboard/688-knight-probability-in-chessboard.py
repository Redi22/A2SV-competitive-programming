class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        DIR = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
        insideCount = 0
        
        @lru_cache(None)
        def dfs(step, i, j):
            insideCount = 0

            if not 0 <= i < n or not 0 <= j < n:
                return 0

            if step == k:
                    insideCount += 1

            if step < k:
                for dx, dy in DIR:
                    insideCount += dfs(step + 1, i + dx, j + dy) / 8
                return insideCount

            return insideCount
                
        insideCount = dfs(0, row, column)
        return (insideCount)

        

        