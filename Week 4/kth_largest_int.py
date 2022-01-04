class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = lambda x: int(x), reverse = True)
        return nums[k-1]