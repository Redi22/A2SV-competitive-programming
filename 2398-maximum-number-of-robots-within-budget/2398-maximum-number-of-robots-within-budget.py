class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCost: List[int], budget: int) -> int:
        n = len(chargeTimes)
        max_size = 0
        heap = []
        running_sum = 0
        l = 0

        for r in range(n):
            #expand
            running_sum += runningCost[r]
            
            if not heap or -heap[0][0] > chargeTimes[r]:
                heapq.heappush(heap, (-chargeTimes[r], r))
                
            elif heap[0][0] < chargeTimes[r]:
                heap = [(-chargeTimes[r], r)]


            #until valid contract
            while l <= r and (-heap[0][0] + (r - l + 1) * running_sum) > budget:
                running_sum -= runningCost[l]
                if (-chargeTimes[l], l) == heap[0]:
                    heapq.heappop(heap)

                l += 1

            #update maximum    
            max_size = max(max_size, r - l + 1)

        return max_size

