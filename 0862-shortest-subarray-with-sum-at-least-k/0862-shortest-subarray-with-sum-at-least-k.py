class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pref = [0]
        for num in nums:
            pref.append(pref[-1] + num)
        
        queue = deque([])
        maxx = float("inf")
        for r in range(len(pref)):
            while queue and pref[queue[-1]] >= pref[r]:
                queue.pop()
                
            
            while queue and pref[r] - pref[queue[0]] >= k:
                l = queue.popleft()
                maxx = min(maxx, r - l)
                
            queue.append(r)
        return maxx if maxx != float("inf") else -1