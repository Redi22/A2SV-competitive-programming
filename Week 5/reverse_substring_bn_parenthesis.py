class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                temp = []
                ch = stack.pop()
                while ch != '(':
                    temp.append(ch)
                    ch = stack.pop()
                for j in range(len(temp)):
                    stack.append(temp[j])
        return "".join(stack)