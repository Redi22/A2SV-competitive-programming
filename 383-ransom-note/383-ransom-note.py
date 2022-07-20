class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranCounter = Counter(ransomNote)
        magCounter = Counter(magazine)
        ans = True
        
        for i,chCount in ranCounter.items():
            if magCounter[i] < chCount:
                ans =  False
                break
        
        return ans
    