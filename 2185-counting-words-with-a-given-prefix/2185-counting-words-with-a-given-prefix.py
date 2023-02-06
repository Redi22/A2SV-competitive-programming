class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0
        
        for word in words:
            count += (word[:n] == pref)
            
        return count