class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set()
        l = r = 0
        while l < len(nums):
            if nums[l] not in numSet:
                numSet.add(nums[l])
                nums[l] , nums[r] = nums[r] , nums[l]
                r += 1
            else:
                l += 1
            
        return r