class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        candidates = defaultdict(int)
        uniques = defaultdict(int)
        
        l = 0
        for r in range(len(s)):
            uniques[s[r]] += 1
            
            while len(uniques) > maxLetters or (r - l + 1) > minSize:
                uniques[s[l]] -= 1
                if uniques[s[l]] <= 0:
                    del uniques[s[l]]
                l += 1
            
            if (r - l + 1) == minSize:
                candidates[s[l:r + 1]] += 1
        
        if candidates:
            return max(candidates.values())
                
        return 0