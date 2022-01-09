class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mismatch = []
        for i in range(1 , len(nums)+1):
            nums.append(i)
        nums = Counter(nums)
        for num , freq in nums.items():
            if(freq != 2):
                mismatch.append(num)
        return mismatch 