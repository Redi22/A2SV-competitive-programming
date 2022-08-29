class StockSpanner:

    def __init__(self):
        self.curr = 0
        self.stack = []
        self.indecies = []

    def next(self, price: int) -> int:       
        i = self.curr
        diff = 0
        
        while self.stack and price >= self.stack[-1]:
            currentPrice, i = self.stack.pop(), self.indecies.pop()
            diff = self.curr - i
            
        
        self.indecies.append(i)
        self.stack.append(price)
        self.curr += 1
        
        return diff + 1
    
    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)