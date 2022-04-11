class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        
                # Are you here''''''


        nums.sort()

        result = nums[-1] - nums[0]
        maxx = nums[-1] - k
        minn = nums[0] + k

        for i in range(len(nums)-1):
            left = min(minn, nums[i+1]-k)
            right = max(maxx, nums[i]+k)

            result = min(result, right-left)

        return result