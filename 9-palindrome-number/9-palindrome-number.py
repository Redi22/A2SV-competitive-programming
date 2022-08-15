class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return all(x[i] == x[~i] for i in range(len(x) // 2))