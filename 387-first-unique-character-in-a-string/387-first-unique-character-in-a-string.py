class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            
        for i in range(len(s)):
            if count[s[i]] == 1:
                break
                
        if i == len(s) - 1 and count[s[i]] != 1:
            return -1
        return i