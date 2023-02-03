class Solution(object):

    def __init__(self, w):
        self.pre_sum = [w[0]]
        for i in range(1, len(w)):
            self.pre_sum.append(self.pre_sum[-1] + w[i])
        

    def pickIndex(self):
        x = random.randint(1, self.pre_sum[-1])
        index = bisect_left(self.pre_sum, x)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()