class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookup = {0: -1}
        summ = 0
        
        for i in range(len(nums)):
            summ += nums[i]
            
            if summ % k not in lookup:
                lookup[summ % k] = i
                
            elif i - lookup[summ % k] > 1:
                return True
            
        return False