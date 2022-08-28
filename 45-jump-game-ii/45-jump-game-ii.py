class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        
        
        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(dp):
                    break
                dp[j] = min(dp[j], dp[i] + 1)
                
        return max(dp)