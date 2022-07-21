class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l = 0
        r = len(tokens) - 1
        score = 0
        tokens.sort()
        temp = 0
        
        if len(tokens) == 1:
            if tokens[0] <= power:
                return 1
            else:
                return 0
        
        while l < r and (power >= tokens[l] or temp):
            while power >= tokens[l]:
                temp += 1
                power -= tokens[l]
                l += 1
                
            score = max(score, temp)
            
            if temp >= 1:
                power += tokens[r]
                r -= 1
                temp -= 1
            
            
        return score