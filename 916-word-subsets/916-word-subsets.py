class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word_dict = [0] * 26
        ans = []
        
        def make_word_dict(word):
            temp_dict = [0] * 26
            
            for i in range(len(word)):
                temp_dict[ord(word[i]) - ord('a')] += 1
                
            return temp_dict
        
        for word2 in words2:
            for i,occ in enumerate(make_word_dict(word2)):
                word_dict[i] = max(word_dict[i], occ)
        
        
        for word in words1:
            possible = True
            
            temp = make_word_dict(word)
            for i in range(26):
                if temp[i] < word_dict[i]:
                    possible = False

            if possible:
                ans.append(word)
                
        return ans
                
        
        