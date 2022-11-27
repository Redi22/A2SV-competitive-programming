class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        max_slice = 0
        dp = [0] * len(nums)
        
        for i in range(2, len(nums)):
            if nums[i - 1] - nums[i - 2] == nums[i] - nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                
            max_slice += dp[i]
        return max_slice