class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {}
        for i, num in enumerate(nums):
            pos[num] = i
            
        for num, replacement in operations:
            pos[replacement] = pos[num]
            nums[pos[num]] = replacement
        return nums