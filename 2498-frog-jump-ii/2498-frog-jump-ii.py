class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return abs(stones[0] - stones[1])
        
        max_jumps = 0
        for i in range(2, len(stones)):
            max_jumps = max(max_jumps, abs(stones[i] - stones[i - 2]))
            
        return max_jumps