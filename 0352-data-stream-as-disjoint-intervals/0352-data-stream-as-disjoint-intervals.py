class SummaryRanges:

    def __init__(self):
        self.stack = []
        

    def addNum(self, value: int) -> None:
        self.stack.append(value)
        self.stack = list(set(self.stack))
        self.stack.sort()
        

    def getIntervals(self) -> List[List[int]]:
        res = []
        temp = [self.stack[0], self.stack[0]]
        for i in range(1, len(self.stack)):
            if self.stack[i] - 1 == temp[-1]: temp.append(self.stack[i])
            else:
                res.append([temp[0], temp[-1]])
                temp = [self.stack[i], self.stack[i]]
        res.append([temp[0], temp[-1]])
        return res
        