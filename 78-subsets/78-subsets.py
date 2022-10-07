class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        
        def backtrack(i, path):
            result.append(path)
                
            for j in range(i, len(nums)):
                backtrack(j + 1, path + [nums[j]])
                
            return
        
        backtrack(0, [])
        
        return result