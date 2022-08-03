class MyCalendar:

    def __init__(self):
        self.cal = []

    def book(self, start: int, end: int) -> bool:
        if not self.cal:
            self.cal.append([start,end])
            return True

        for i in range(len(self.cal)):
            if start <= self.cal[i][0] and self.cal[i][0] < end:
                return False
            if self.cal[i][0] < start and start < self.cal[i][1]:
                return False
            
                
        self.cal.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)