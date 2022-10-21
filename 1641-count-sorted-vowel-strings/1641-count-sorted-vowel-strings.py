class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5  for i in range(n)]
        
        #initialize our base cases
        dp[0] = [1,1,1,1,1]
        for j in range(n):
            dp[j][0] = 1
        
        for i in range(1, n):
            for j in range(1, 5):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return sum(dp[-1])