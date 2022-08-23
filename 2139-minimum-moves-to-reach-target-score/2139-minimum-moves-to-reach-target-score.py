class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while maxDoubles and target > 1:
            if target % 2 == 0:
                target -= (target // 2)
                maxDoubles -= 1
            else:
                target -= 1
                
            moves += 1
            
        return target - 1 + moves