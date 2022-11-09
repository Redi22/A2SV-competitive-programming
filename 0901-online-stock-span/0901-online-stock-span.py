class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        popped = 1
        while self.stack and self.stack[-1][0] <= price:
            popped += self.stack.pop()[1]
            
        self.stack.append((price, popped))
        
        return popped


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)