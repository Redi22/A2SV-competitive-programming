class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [[1] * size for _ in range(2)]
        
        for i in range(1, size):
            if nums[i] == nums[i - 1]:
                dp[0][i] = dp[0][i - 1]
                dp[1][i] = dp[1][i - 1]
                
            elif nums[i] < nums[i - 1]:
                dp[1][i] = dp[0][i - 1] + 1
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = dp[1][i - 1] + 1
                dp[1][i] = dp[1][i - 1]
                
        
        return max(dp[0][size - 1], dp[1][size - 1])
                
            