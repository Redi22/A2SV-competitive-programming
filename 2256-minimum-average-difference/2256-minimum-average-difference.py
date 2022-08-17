class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefSum = [0]
        ans = 0
        minn = float('inf')
        indx = 0
        
        for i in range(len(nums)):
            prefSum.append(prefSum[-1] + nums[i])
        
        for i in range(len(nums)):
            op1 = (prefSum[i+1] // (i + 1))
            op2 = 0
            if i != len(nums) - 1:
                op2 = ((prefSum[-1] - prefSum[i + 1]) // (len(nums) - i - 1))
            ans = abs( op1 - op2 )
            if ans < minn:
                indx = i
                minn = ans
                
        return indx
        
            
        