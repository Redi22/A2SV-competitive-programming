class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        prev = nums[-1]
        while k >1:
            prev = heapq.heappop(nums)
            k -= 1
            
        return -nums[0]