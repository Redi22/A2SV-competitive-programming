class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing , duplicated = -1, -1
        n = len(nums)
        count = Counter(nums)
        
        for number in range(1, n + 1):
            if number not in count:
                missing = number
            if count[number] > 1:
                duplicated = number
                
        return [duplicated, missing]