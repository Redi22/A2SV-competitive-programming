class FreqStack:

    def __init__(self):
        self.freqStack = defaultdict(int)
        self.orderStack = defaultdict(list)
        self.maxFreq = 0
        

    def push(self, val: int) -> None:
        self.freqStack[val] += 1
        self.orderStack[self.freqStack[val]].append(val)
        self.maxFreq = max(self.maxFreq , self.freqStack[val])
        

    def pop(self) -> int:
        val = self.orderStack[self.maxFreq].pop()
        if not self.orderStack[self.maxFreq]:
            self.maxFreq -= 1
        self.freqStack[val] -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()