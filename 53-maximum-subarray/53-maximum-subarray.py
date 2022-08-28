class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(dp)):
            dp[i] = max((dp[i - 1] + dp[i]), dp[i])
            
        return max(dp)