class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = set()
        
        def backtrack(i, words, word_len):
            if i > len(wordDict) or word_len > len(s):
                return 
            
            if word_len == len(s) and "".join(words) == s:
                result.add(" ".join(words))
                return
            
            for j in range(len(wordDict)):
                words.append(wordDict[j])
                backtrack(j, words, word_len + len(wordDict[j]))
                words.pop()
                
            
        backtrack(0, [], 0)
        return result
                