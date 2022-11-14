class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        memo = {}
        
        @lru_cache(None)
        def getLDS(i, last):
            
            if i >= len(nums):
                return 0
            
            take = 0
            if nums[i] % last == 0:
                take = getLDS(i + 1,  nums[i]) + 1
                
            not_take = getLDS(i + 1, last)
            
            return max(take, not_take)
            
        last = 1
        for i in range(len(nums)):
            take = 0
            if nums[i] % last == 0:
                take = getLDS(i + 1,  nums[i]) + 1
            not_take = getLDS(i + 1, last)
            
            if take > not_take:
                result.append(nums[i])
                last = nums[i]
                
        return result