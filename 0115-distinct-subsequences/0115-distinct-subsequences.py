class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if i >= len(t):
                return 1
            
            if j >= len(s):
                return 0
            
            if s[j] == t[i]:
                current =  dp(i, j + 1) + dp(i + 1, j + 1)
                return current 
            
            return dp(i, j + 1)
        
    
        return dp(0, 0)
            
            
        