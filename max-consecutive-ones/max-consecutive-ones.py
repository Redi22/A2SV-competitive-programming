class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                ones = 0
            else:
                ones += 1
            ans = max(ones, ans)
        return ans