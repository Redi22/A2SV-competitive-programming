class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ si.lower() for si in s if si.isalnum()]
        return all(s[i] == s[~i] for i in range(len(s) // 2))