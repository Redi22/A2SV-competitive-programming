from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.dict = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.dict[start] = self.dict.get(start,0)+1
        self.dict[end] = self.dict.get(end,0)-1
        ans = curr = 0
        for value in self.dict.values():
            curr+=value
            ans = max(ans, curr)
        return ans