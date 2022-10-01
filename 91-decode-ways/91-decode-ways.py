class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s) + [1]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if 1 <= int(s[i:j + 1]) <= 26:
                    dp[i] += dp[j + 1]
                else:
                    break
        return dp[0]