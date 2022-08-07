class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        steps = 0
        while nums:
            cur = heapq.heappop(nums)
            if cur != 0:
                steps += 1
                for i in range(len(nums)):
                    nums[i] -= cur
        return steps