class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #check for ideal place
        ideal = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                ideal = i
                break
        
        if ideal == -1:
            nums.sort()
            return nums
        
        #search a grater element that is the smallest from the others
        minn = float("inf")
        min_index = -1
        for i in range(ideal + 1, len(nums)):
            if nums[ideal] < nums[i] < minn:
                minn = nums[i]
                min_index = i
                
            
        #swap the ideal with the found element
        nums[ideal] , nums[min_index] = nums[min_index], nums[ideal]
        
        # bubble sort the ones to the left of the ideal pos
        for i in range(ideal + 1, len(nums)):
            for j in range(ideal + 1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    
        
        
        
        