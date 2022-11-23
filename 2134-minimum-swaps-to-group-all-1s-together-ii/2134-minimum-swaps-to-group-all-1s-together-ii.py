class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum([num == 1 for num in nums])
        nums += nums
        swaps = ones
        l = 0
        zeros = sum(num == 0 for num in nums[:ones])
        
        for r in range(ones, len(nums)):
            zeros -= nums[l] == 0
            zeros += nums[r] == 0
            l += 1
            swaps = min(swaps, zeros)
            
        return swaps
             
            