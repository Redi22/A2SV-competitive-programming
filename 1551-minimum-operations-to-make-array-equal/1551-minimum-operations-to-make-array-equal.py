class Solution:
    def minOperations(self, n: int) -> int:
        idx = n // 2
        target = n * idx
        summ = sum([(2 * i) + 1 for i in range(0, idx)])
            
        return target - summ
        