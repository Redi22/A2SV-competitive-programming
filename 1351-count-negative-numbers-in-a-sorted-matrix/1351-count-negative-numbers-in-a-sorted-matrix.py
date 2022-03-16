class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        r = m - 1
        c = 0
        count = 0
        firstNeg = n
        for i in range(m):
            r = n-1
            l = 0
            while l <= r:
                mid = l + (r - l) // 2
                if grid[i][mid] < 0:
                    firstNeg = mid
                    r = mid - 1
                else:
                    l = mid + 1
            count += n - firstNeg
            
        return count
            