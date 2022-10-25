class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0] * len(s)
        i = 0
        j = 1
        while j < len(s):
            if s[i] == s[j]:
                LPS[j] = i + 1
                i += 1
                j += 1
            elif i > 0:
                i = LPS[i - 1]
            else:
                j += 1
                
        return s[:LPS[-1]]
                