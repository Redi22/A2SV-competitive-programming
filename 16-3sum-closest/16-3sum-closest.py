class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort()
        
        temp=sum(nums[:3])
        
        if temp>target:
            return temp
        
        temp=sum(nums[-3:])
        if temp<target:
            return temp
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currAns = nums[i] + nums[left] + nums[right]

                if currAns == target:
                    return currAns
                elif currAns < target:
                    left += 1
                else:
                    right -= 1
                
                if abs(currAns - target) < abs(ans - target):
                    ans = currAns
                
        return ans