class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for i in range(len(nums)):
            pos = bisect.bisect_left(LIS, nums[i])
            
            if pos == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[pos] = nums[i]
                
        return len(LIS)