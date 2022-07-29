class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[r] == 0 and nums[l] != 0:
                l = r
                
            r += 1
        
            
                
                