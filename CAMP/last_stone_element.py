class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stones[i] for i in range(len(stones))]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            peek1 = - heapq.heappop(stones)
            peek2 = - heapq.heappop(stones)
            if peek1 != peek2:
                heapq.heappush(stones, - abs(peek1 - peek2))
            heapq.heapify(stones)
        print(stones)
        if len(stones) > 0:
            return -stones[0]
        return 0