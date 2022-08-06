class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        
        @lru_cache(None)
        def dp(summ):
            count = 0
            if summ == target:
                return 1
            elif summ > target:
                return 0
            
            for num in nums:
                count += dp(summ + num)
            return count
        
        # dp(0)
        return dp(0)
                