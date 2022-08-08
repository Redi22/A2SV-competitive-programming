class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        
        def backtrack(nums, path):
            if len(path) == n:
                result.append(path)
                return
            
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])
                
        backtrack(nums, [])
        return result