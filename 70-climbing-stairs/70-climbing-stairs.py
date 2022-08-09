class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        old = 1
        new = 2
        for i in range(2, n):
            new, old = new + old, new
        return new