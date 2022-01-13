class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if(tokens[i] == "+" ):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 + num2)
            elif(tokens[i] == "*" ):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num1 * num2)
            elif(tokens[i] == "/" ):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2 / num1)
            elif(tokens[i] == "-" ):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2 - num1)
            else:
                stack.append(tokens[i])
        return int(stack[0])