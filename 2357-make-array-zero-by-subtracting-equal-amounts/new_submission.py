class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([n for n in nums if n > 0]))
