class Bitset:

    def __init__(self, size: int):
        self.zeros = set([i for i in range(size)])
        self.ones = set()
        self.flipped = False
        

    def fix(self, idx: int) -> None:
        if not self.flipped:
            if idx in self.zeros:
                self.zeros.remove(idx)
                
            self.ones.add(idx)
        else:
            if idx in self.ones:
                self.ones.remove(idx)
                
            self.zeros.add(idx)
            
        

    def unfix(self, idx: int) -> None:
        if not self.flipped:
            if idx in self.ones:
                self.ones.remove(idx)
                
            self.zeros.add(idx)
        else:
            if idx in self.zeros:
                self.zeros.remove(idx)
                
            self.ones.add(idx)
        

    def flip(self) -> None:
        self.flipped = not self.flipped
    
    def all(self) -> bool:
        if self.flipped:
            return len(self.ones) == 0
        
        return len(self.zeros) == 0
    

    def one(self) -> bool:
        if self.flipped:
            return len(self.zeros) != 0
        
        return len(self.ones) != 0

    def count(self) -> int:
        if self.flipped:
            return len(self.zeros)
        
        return len(self.ones)

    def toString(self) -> str:
        arr = ["0"] * (len(self.zeros) + len(self.ones))
        
        if self.flipped:
            for i in self.zeros:
                arr[i] = "1"
        else:
            for i in self.ones:
                arr[i] = "1"
                
        return "".join(arr)
                


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()