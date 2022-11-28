class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        word_len = set([len(word) for word in wordDict])
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for l in range(1, len(s) + 1):
            for length in word_len:
                if s[l - 1 : l + length - 1] in word_set and l+length-1 <= len(s):
                    dp[l+length-1] |= dp[l - 1]
                    
        return dp[len(s)]