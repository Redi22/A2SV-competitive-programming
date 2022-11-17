class Solution:
    def countSplitSize(self, size, nums):
        count = 0
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            if current > size:
                count += 1
                current = nums[i]
                
        return count + 1
            
            
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        best = r
        
        while l <= r:
            mid = (l + r) // 2
            size = self.countSplitSize(mid, nums)
            if size <= k:
                best = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return best