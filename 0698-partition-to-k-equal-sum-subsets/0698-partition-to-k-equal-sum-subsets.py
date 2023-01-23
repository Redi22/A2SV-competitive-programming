class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsets = [0] * k
        nums.sort(reverse = True)
        total = sum(nums)
        target = total // k
        memo = {}
        
        if total % k != 0:
            return False
        
        
        def bk(i):
            if i == len(nums):
                return True
            
            current = tuple(subsets)
            
            if current in memo:
                return memo[current]
            
            for j in range(k):
                if subsets[j] + nums[i] <= target:
                    subsets[j] += nums[i]
                    if bk(i + 1):
                        return True
                    subsets[j] -= nums[i]
                    
            memo[current] = False
            return False
            
        return bk(0)
            
            