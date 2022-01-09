class Solution:
def removeDuplicates(self, nums: List[int]) -> int:
    l , r = 0 ,1
    last_index = 0
    while(r < len(nums)):
        if(nums[l] == nums[r]):
            nums[r] = 200
            r += 1
        else:
            l = r
            r += 1
            last_index += 1
    nums.sort()
    nums = nums[:last_index+1]
    return last_index+1