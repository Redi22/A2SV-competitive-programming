class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = list(s)
        sArr.sort()
        tArr = list(t)
        tArr.sort()
        
        return sArr == tArr