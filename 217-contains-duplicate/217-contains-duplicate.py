class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        ans = False
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                ans = True
                break
        
        return ans