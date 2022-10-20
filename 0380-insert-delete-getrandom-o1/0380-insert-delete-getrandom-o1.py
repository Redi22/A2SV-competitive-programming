class RandomizedSet:

    def __init__(self):
        self.random_set = set()

    def insert(self, val: int) -> bool:
        
        if val in self.random_set:
            return False
        
        self.random_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.random_set:
            return False
        
        self.random_set.remove(val)
        return True
    

    def getRandom(self) -> int:
        return random.choice(list(self.random_set))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()