class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        
        @cache
        def dp(i, k):
            if k <= 0 or i >= len(events):
                return 0
            
            skip = dp(i + 1, k)
            
            pos = bisect.bisect_left(events, [events[i][1] + 1, 0, 0])
            pick = dp(pos, k - 1) + events[i][2]
            
            return max(pick, skip)
        
        return dp(0, k)
                
            