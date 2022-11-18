class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def getValid(lefts, i):
            if i >= len(s):
                return lefts == 0
            
            if lefts < 0:
                return False
            
            if s[i] == "*":
                left = getValid(lefts + 1, i + 1)
                right = getValid(lefts - 1, i + 1)
                empty = getValid(lefts, i + 1)
                
                return left or right or empty
            
            elif s[i] == ")":
                lefts -= 1
                
            else:
                lefts += 1
                
            return getValid(lefts, i + 1)
        
        return getValid(0, 0)