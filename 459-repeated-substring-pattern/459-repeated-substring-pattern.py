class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for i in range(n):
            if n % (i + 1) == 0:
                if s[:i + 1] * (n // (i + 1)) == s and i != n - 1:
                    return True
                    
        return False