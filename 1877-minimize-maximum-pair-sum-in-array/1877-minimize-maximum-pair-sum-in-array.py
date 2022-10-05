class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        maxx = 0
        while l < r:
            maxx = max(maxx, nums[l] + nums[r])
            l += 1
            r -= 1
        return maxx