class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def dp(i):
            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            single = dp(i + 1)
            double = 0
            
            if i < len(s) - 1 and int(s[i] + s[i + 1]) < 27:
                double = dp(i + 2) 
                
            return single + double 
        
        return dp(0)
    