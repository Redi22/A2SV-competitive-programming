class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = 0
        steps = 0
        for i in range(len(s)):
            zeros += s[i] == "0"
            
            if s[i] == "1" and zeros > 0:
                steps = max(zeros, steps + 1)
                
        return steps
                
                
            
                
                
                
                    
                