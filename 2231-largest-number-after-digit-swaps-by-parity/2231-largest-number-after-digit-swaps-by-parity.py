class Solution:
    def largestInteger(self, num: int) -> int:
        oddPq = []
        evenPq = []
        ans = [0] * len(str(num))
        
        for i,n in enumerate(str(num)):
            if int(n) % 2 == 0:
                evenPq.append(-int(n))
            else:
                oddPq.append(-int(n))
        heapq.heapify(evenPq)
        heapq.heapify(oddPq)
        
        for i,n in enumerate(str(num)):
            if int(n) % 2 == 0:
                ans[i] = str(-1 * heapq.heappop(evenPq))
            else:
                ans[i] = str(-1 * heapq.heappop(oddPq))
                
        return "".join(ans)
                