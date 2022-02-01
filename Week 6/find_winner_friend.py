class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = []
        count = 1
        index = 0
        for i in range(1, n+1):
            nums.append(i)
        while len(nums) > 1:
            if count == k:
                count = 1
                nums.pop(index)
            else:
                count += 1
                index += 1
                index %= len(nums)
        return nums[0]