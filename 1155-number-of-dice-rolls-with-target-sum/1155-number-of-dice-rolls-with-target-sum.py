class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        dp=[[0 for j in range(target+1)] for i in range(n)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 and j<=k and j!=0:
                    dp[i][j]=1
                elif i==0 and j>k:
                    dp[i][j]=0
                else:
                    if(j<=k):
                        a=0
                    else:
                        a=j-k
                    dp[i][j]=sum(dp[i-1][a:j])
        return dp[-1][-1]%MOD