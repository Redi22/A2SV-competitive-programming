class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()   
        
        def backtrack(i, path):
            result.append(path)
                
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                    
                backtrack(j + 1, path + [nums[j]])
                
            return
        
        backtrack(0, [])
        
        return result 