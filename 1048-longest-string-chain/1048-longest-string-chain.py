class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        max_chain = 1
        
        for word in words:
            dp[word] = 1
            
        for word in sorted(words, key=len):
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    max_chain = max(max_chain, dp[word])
                      
        return max_chain

                