class DataStream:

    def __init__(self, value: int, k: int):
        self.nums = []
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.nums.append(num)
        else:
            self.nums = []
            
        return len(self.nums) >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)