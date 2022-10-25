class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        for s in word1:
            w1 += s
            
        w2 = ""
        for s in word2:
            w2 += s
        
        return w1 == w2