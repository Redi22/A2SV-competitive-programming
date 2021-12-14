class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] == target):
                indices.append(i)
        
        return indices
                