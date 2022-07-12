class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        bSum = [0]
        total = 0
        result = []
    
        for i in range(len(nums)-1, 0, -1):
            total += nums[i]
            bSum.append(total)
            
        total = 0
        for i in range(len(nums)): 
            if(total == bSum.pop()):
                return i
            total += nums[i]
           
        return -1