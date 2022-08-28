class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        for i in range(amount):
            dp.append(amount + 1)
                    
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                    
        return dp[amount] if dp[amount] != amount + 1 else -1             