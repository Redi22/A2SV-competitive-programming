class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            heappush(self.maxHeap, -heappushpop(self.minHeap, -num))
        else:
            heappush(self.minHeap, -heappushpop(self.maxHeap, num))
            

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.maxHeap[0] - self.minHeap[0]) / 2
        else:
            return self.maxHeap[0]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()