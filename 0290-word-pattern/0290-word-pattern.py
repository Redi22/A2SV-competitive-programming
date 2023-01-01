class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        p1, h1 = "", dict()
        p2, h2 = "", dict()

        for i in range(len(pattern)):
            if pattern[i] in h1:
                p1 += h1[pattern[i]]
            else:
                h1[pattern[i]] = str(i)
                p1 += str(i)

            if words[i] in h2:
                p2 += h2[words[i]]
            else:
                h2[words[i]] = str(i)
                p2 += str(i)
            if p1 != p2:
                ## Clearing the memory
                h1 = dict()
                p1 = ""
                h2 = dict()
                p2 = ""
                return False
        return True