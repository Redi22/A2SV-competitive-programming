class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [float("-inf")] * n
        right_max[-1] = nums[-1]
        suffix_sum = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(suffix_sum, right_max[i + 1])
            
        max_sum = special_sum = nums[0]
        prefix_sum = 0
        current = 0
        
        for i in range(n):
            current = max(current, 0) + nums[i]
            max_sum = max(max_sum, current)
            prefix_sum += nums[i]
            if i < n - 1:
                special_sum = max(special_sum, prefix_sum + right_max[i + 1])
                
        return max(max_sum, special_sum)
            
        
            