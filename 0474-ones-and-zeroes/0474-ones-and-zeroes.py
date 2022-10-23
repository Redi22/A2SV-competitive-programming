class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        @lru_cache(None)
        def dp(i, m, n):
            if m < 0 or n < 0:
                return float("-inf")
            
            if i >= len(strs):
                return 0
            
            take = dp(i + 1, m - strs[i].count("0"), n - strs[i].count("1")) + 1
            dont_take = dp(i + 1, m, n)
            
            return max(take, dont_take)
        
        return dp(0, m, n)
            
            
                