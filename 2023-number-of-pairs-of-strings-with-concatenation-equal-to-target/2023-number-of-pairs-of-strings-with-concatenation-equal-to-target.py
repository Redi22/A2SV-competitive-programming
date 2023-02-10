class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        valid_pair = 0
        for i, num in enumerate(nums):
            for j, another in enumerate(nums):
                if (num + another) == target and i != j:
                    valid_pair += 1
                    
                
        return valid_pair