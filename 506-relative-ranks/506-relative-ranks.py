class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [(-s, i) for i,s in enumerate(score)]
        ans = ["0"] * len(score)
        heapq.heapify(score)
        k = 1
        
        while score:
            cur = heapq.heappop(score)
            if k == 1:
                ans[cur[1]] = "Gold Medal"
            elif k == 2:
                ans[cur[1]] = "Silver Medal"
            elif k == 3:
                ans[cur[1]] = "Bronze Medal"
            else:
                ans[cur[1]] = str(k)
            k += 1
            
        return ans
        