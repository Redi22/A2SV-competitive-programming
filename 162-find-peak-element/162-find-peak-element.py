class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxx = max(nums)
        ans = -1
        for i in range(len(nums)):
            if nums[i] == maxx:
                ans = i
                break
        return ans