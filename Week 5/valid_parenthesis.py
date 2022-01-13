class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = { ')':'('  ,   '}' :'{' , ']':'[' , '[' : '0' , '{':'0' , '(': '0'}
        stack.append(s[0])
        for i in range(1 ,len(s)):
            if(len(stack) > 0 and d[s[i]] == stack[len(stack) - 1]  ):
                stack.pop()
            else:
                stack.append(s[i])
        if(len(stack) == 0):
            return True
        return False