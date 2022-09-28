class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l = 0
        maxx = 0
        nums.sort()
        val = nums[0]
        
        for r in range(len(nums)):
            k -= (r - l) * (nums[r] - val)
            if l < r and k < 0:
                k += (nums[r] - nums[l])
                l += 1
                
            val = nums[r]
            maxx = max(maxx, (r - l + 1))

            
        return maxx