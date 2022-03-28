class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            minVal = float("inf")
            maxVal = float("-inf")
            
            for j in range(i, len(nums)):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                total += maxVal - minVal
                
        return total