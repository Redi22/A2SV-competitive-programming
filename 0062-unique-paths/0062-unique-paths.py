class Solution:
    def inbound(self, i, j, m, n):
        if 0 <= i < m and 0 <= j < n:
            return True
        return False
    
    @lru_cache(None)
    def traverse(self, i, j, m, n):
        if not self.inbound(i, j, m, n):
            return 0
        
        if (i, j) == (m - 1, n - 1):
            return 1
        
        return self.traverse(i + 1, j, m, n) + self.traverse(i, j + 1, m, n)
            
        
    def uniquePaths(self, m: int, n: int) -> int:
        return self.traverse(0, 0, m, n)
        