class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [nums[0]]
        
        for i in range(1, len(nums)):
            # print(runningSum[-1], nums[i])
            runningSum.append(runningSum[-1] + nums[i])
        
        return runningSum