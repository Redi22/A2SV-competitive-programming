class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = []
        for i in range(len(ops)):
            if ops[i] == "C":
                result.pop()
            elif ops[i] == "D":
                result.append(2*result[-1])
            elif ops[i] == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(ops[i]))
                
        return sum(result)