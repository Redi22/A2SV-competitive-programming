class Solution:
    def calculate(self, s):
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
    
        i, num, stack, sign = 0, 0, [], "+"
        
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in "+-*/":
                update(sign, num)
                num, sign = 0, s[i]
            elif s[i] == "(":                                        # For BC I and BC III
                num, j = self.calculate(s[i + 1:])
                i = i + j
            elif s[i] == ")":                                        # For BC I and BC III
                update(sign, num)
                return sum(stack), i + 1
            i += 1
        update(sign, num)
        return sum(stack)