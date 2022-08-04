class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = defaultdict(int)
        nums.sort()
        maxx = nums[0] + 1
        steps = 0
        
        for i in range(len(nums)):
            if nums[i] in count:
                steps += abs(nums[i] - maxx)
                count[maxx] = 1 
                maxx += 1 
            else:
                count[nums[i]] = 1
                maxx = nums[i] + 1
                
        return steps