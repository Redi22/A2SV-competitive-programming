class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums) - 1
        
        for i in range(len(nums) - 1 , -1, -1 ):
            if i + nums[i] >= idx:
                idx = i
            
        return idx == 0