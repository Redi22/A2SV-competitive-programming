class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0,0,1,2,4,6,9]
        
        if n < 7:
            return dp[n]
    
        
        for i in range(7, n + 1):
            dp.append( 3 * dp[i - 3])
            
        return dp[-1]