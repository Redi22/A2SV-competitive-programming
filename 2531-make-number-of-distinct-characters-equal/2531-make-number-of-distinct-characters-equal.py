class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        word1_set = [0 for i in range(26)]
        word2_set = [0 for i in range(26)]
        
        for i in range(len(word1)):
            word1_set[ord(word1[i]) - ord('a')] += 1
            
        for i in range(len(word2)):
            word2_set[ord(word2[i]) - ord('a')] += 1
            
        def check(set1, set2):
            return sum([s != 0 for s in set1]) == sum([c != 0 for c in set2])
        
        for i in range(26):
            for j in range(26):
                if word1_set[i] != 0 and word2_set[j] != 0:
                    word1_set[j] += 1
                    word2_set[j] -= 1
                    word1_set[i] -= 1
                    word2_set[i] += 1
                    
                    if check(word1_set, word2_set):
                        return True
                    
                    word1_set[j] -= 1
                    word2_set[j] += 1
                    word1_set[i] += 1
                    word2_set[i] -= 1
                    
        return False
    
    