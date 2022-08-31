class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        words = [word for word in words if word]
        words = words[::-1]
        return " ".join(words)