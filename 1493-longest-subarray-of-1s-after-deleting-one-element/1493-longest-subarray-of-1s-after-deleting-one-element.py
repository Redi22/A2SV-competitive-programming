class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j = 0
        res = 0
        zeros = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            while zeros > 1:
                if nums[j] == 0:
                    zeros -= 1
                j += 1
            res = max(res, i-j+1)
            
        if zeros == 0:
            return n-1
        else:
            return res-zeros