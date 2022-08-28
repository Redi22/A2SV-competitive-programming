class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        l = 0
        ans = float('inf')
        i = 0
        
        while l < len(nums):
            summ += nums[l] 
                
            while summ >= target:
                ans = min(ans, l - i + 1)
                summ -= nums[i]
                i += 1
            
            l += 1
            
        return ans if ans != float('inf') else 0