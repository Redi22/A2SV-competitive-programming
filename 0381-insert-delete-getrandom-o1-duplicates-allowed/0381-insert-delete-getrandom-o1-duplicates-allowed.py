class RandomizedCollection:

    def __init__(self):
        self.random_dict = defaultdict(set)
        self.keys = []
        

    def insert(self, val: int) -> bool:
        self.random_dict[val].add(len(self.keys))
        self.keys.append(val)
        return len(self.random_dict[val]) == 1
    
    def remove(self, val: int) -> bool:
        if not self.random_dict[val]:
            return False
        
        remove, last = self.random_dict[val].pop(), self.keys[-1]
        self.keys[remove] = last
        self.random_dict[last].add(remove)
        self.random_dict[last].discard(len(self.keys) - 1)

        self.keys.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.keys)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()