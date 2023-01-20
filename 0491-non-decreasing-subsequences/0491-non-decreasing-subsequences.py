class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        valids = set()
        
        def bk(path, valids, i):
            if i == len(nums):
                if len(path) >= 2: valids.add(tuple(path))
                return 
            
            
            if not path or path[-1] <= nums[i]:
                path.append(nums[i])
                bk(path, valids, i+1)
                path.pop()  
                
            bk(path, valids, i+1)
        bk([], valids, 0)
        return valids