class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        
        for i, num in enumerate(nums):
            cur += num
            
            while d and cur - d[0][1] >= k:
                res = min(res, i + 1 - d.popleft()[0])
                
            while d and cur <= d[-1][1]:
                d.pop()
                
            d.append([i + 1, cur])
            
        return res if res < float('inf') else -1
                
            
                
            