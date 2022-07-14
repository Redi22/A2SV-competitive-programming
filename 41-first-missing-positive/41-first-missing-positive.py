class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        i = 0
        nums.sort()
        nums = list(dict.fromkeys(nums))
        
        while(i < len(nums)):
            if i != nums[i] -1:
                return i+1
            i += 1
        return i+1
        