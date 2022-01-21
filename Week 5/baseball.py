class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for i in range(len(ops)):
            print(ops[i])
            if ops[i] == "C":
                result.pop()
            elif ops[i] == "D":
                operand = result.pop()
                result.append(operand)
                result.append(2*operand)
            elif ops[i] == "+":
                operand1 = result.pop()
                operand2 = result.pop()
                result.append(operand2)
                result.append(operand1)
                result.append(operand1 + operand2)
            else:
                result.append(int(ops[i]))
            # print(result)
                
        return sum(result)