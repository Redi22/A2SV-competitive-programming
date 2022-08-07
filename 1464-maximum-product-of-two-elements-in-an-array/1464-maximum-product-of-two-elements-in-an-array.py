class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
            
        heapq.heapify(nums)
        maxx1 = heapq.heappop(nums)
        maxx2 = heapq.heappop(nums)
        return (maxx1 + 1) * (maxx2 + 1)