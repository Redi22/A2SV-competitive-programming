class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        word_dict = {}
        word_pattern = []
        count = 1
        ans = []
        
        for p in pattern: 
            
            if p in word_dict.keys():
                word_pattern.append(word_dict[p])
            else:
                word_pattern.append(count)
                word_dict[p] = count
                count += 1
        
        for word in words:
            word_dict = {}
            count = 1
            temp_pattern = []
            for p in word: 
                if p in word_dict.keys():
                    temp_pattern.append(word_dict[p])
                else:
                    temp_pattern.append(count)
                    word_dict[p] = count
                    count += 1
            if temp_pattern == word_pattern:
                ans.append(word)
                    
        return ans
        
