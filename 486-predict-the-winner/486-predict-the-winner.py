class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(prev, p1, p2, i, j):
            if i > j:
                return p1 >= p2
            
            if prev:
                return dp(not prev, p1, p2 + nums[j], i, j - 1) and dp(not prev, p1, p2 + nums[i], i + 1, j)
            else:
                return dp(not prev, p1 + nums[j], p2, i, j - 1) or dp(not prev, p1 + nums[i], p2, i + 1, j)
            
        return dp(False, 0, 0, 0, len(nums) - 1)