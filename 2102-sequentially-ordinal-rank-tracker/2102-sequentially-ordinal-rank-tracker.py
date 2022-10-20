class Rank:
    def __init__(self, value=None, name=None):
        self.value = value
        self.name = name
        
    def __lt__(self, rank):
        if rank.value > self.value:
            return True
        
        if rank.value == self.value:
            return self.name > rank.name
        

class SORTracker:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.min_size = 1

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.min_heap, Rank(score, name))        
        
        if len(self.min_heap) > self.min_size:
            candidate = heapq.heappop(self.min_heap)
            
            heapq.heappush(self.max_heap, (-candidate.value, candidate.name))

        
    def get(self) -> str:
        answer = self.min_heap[0].name
        self.min_size += 1
        
        if len(self.min_heap) < self.min_size and  self.max_heap:
            candidate = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, Rank(-candidate[0], candidate[1]))
            
        return answer


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()