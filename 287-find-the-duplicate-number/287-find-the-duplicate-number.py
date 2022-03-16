class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        r = 1
        l = 0 
        while r < len(nums):
            if nums[r] == nums[l]:
                return nums[r]
            r += 1
            l += 1
        return -1
            