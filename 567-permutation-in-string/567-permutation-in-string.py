class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLen = len(s1)
        windowDic = Counter(s1)
        
        for i in range(len(s2)):
            count = Counter(s2[i: i + windowLen])
            if count == windowDic:
                return True
            
        return False