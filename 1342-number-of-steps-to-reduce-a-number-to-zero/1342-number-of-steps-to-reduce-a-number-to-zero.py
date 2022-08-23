class Solution:
    def numberOfSteps(self, num: int) -> int:
        moves = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
                
            moves += 1
            
        return moves