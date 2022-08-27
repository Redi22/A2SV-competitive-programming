class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = [len(str(num)) for num in nums]
        summ = 0
        for num in nums:
            if num % 2 == 0:
                summ += 1
            
        return summ