class Solution:
    def smallestNumber(self, s: str) -> str:
        res, stack = [], []
        
        for i,c in enumerate(s + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)
            