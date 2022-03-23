class Solution:
    def countOdds(self, low: int, high: int) -> int:
        val = (high - low)//2 + (high%2 or low%2)
        return val