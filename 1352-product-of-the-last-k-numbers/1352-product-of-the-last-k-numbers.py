class ProductOfNumbers:

    def __init__(self):
        self.queue = []
        self.prefProduct = [1]

    def add(self, num: int) -> None:
        self.queue.append(num)
        if num == 0:
            self.prefProduct = []
        else:
            if self.prefProduct:
                self.prefProduct.append(self.prefProduct[-1] * num)
            else:
                self.prefProduct = [num]
        
    def getProduct(self, k: int) -> int:
        if k < len(self.prefProduct):
            return self.prefProduct[-1] // self.prefProduct[-k-1]
        
        elif k == len(self.prefProduct):
            return self.prefProduct[-1]
        return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)