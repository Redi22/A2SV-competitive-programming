class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0] , nums[1])
        
        def robSeq(nums, n):
            dp = [0] * n
            if n == 1:
                return nums[0]
            if n == 2:
                return max(nums[0] , nums[1])
            dp[0] = nums[0]
            dp[1] = nums[1]
            for i in range(2 , n):
                dp[i] = nums[i] + max(dp[:i-1])
            return max(dp[-1] , dp[-2])
        
        
        return max(robSeq(nums[:n-1], n-1), robSeq(nums[1:n+1], n-1))