class SeatManager:

    def __init__(self, n: int):
        self.seats = []
        self.reserved = set()
        for i in range(1, n + 1):
            self.seats.append(i)
            
    def reserve(self) -> int:
        for i in range(len(self.seats)):
            if self.seats[i] not in self.reserved:
                seat = heapq.heappop(self.seats)
                self.reserved.add(seat)
                return seat
            
    
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        self.reserved.remove(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)