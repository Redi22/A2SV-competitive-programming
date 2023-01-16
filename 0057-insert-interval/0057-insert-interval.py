
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        
        start, end = newInterval
        
        left = bisect_left(intervals, start, key=lambda x: x[1])
        if intervals[left - 1 if left > 0 else left][1] == start:
            left = left - 1 if left > 0 else 0
            
        right = bisect_left(intervals, end, key=lambda x: x[0])
        if intervals[right-1 if right == n else right][0] == end:
            right = right + 1 if right <= n - 1 else n - 1
            
        if left != right:
            start = min(start, intervals[left][0])
            end = max(end, intervals[0 if right == 0 else right - 1][1])
            
        return intervals[:left] + [[start, end]] + intervals[right:]