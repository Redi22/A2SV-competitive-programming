class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
                
            stack.append(i)
            
        i = 0
        while stack and i < len(nums):
            while nums[i] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            i += 1
            
        return ans
            
            