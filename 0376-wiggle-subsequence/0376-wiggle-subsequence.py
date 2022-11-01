class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        positive = 1
        negative = 1
        
        for i in range(1, size):
            if nums[i] < nums[i - 1]:
                positive = negative + 1
                
            elif nums[i] > nums[i - 1]:
                negative = positive + 1
                
        
        return max(positive, negative)
                
            