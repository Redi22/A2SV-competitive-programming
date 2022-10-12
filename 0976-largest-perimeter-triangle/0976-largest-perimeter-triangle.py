class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        return ([0] + [a + b + c for a, b, c in zip(nums, nums[1:], nums[2:]) if c < a + b])[-1]