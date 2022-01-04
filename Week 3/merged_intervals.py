class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
    
        merged_inervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        # print(intervals)
        for i in range(1, len(intervals)):
            
            
            if(intervals[i][0] <= end): 
                end = max(intervals[i][1], end)
            else:
                merged_inervals.append([start , end])
                print(i)
                start = intervals[i][0]
                end = intervals[i][1]
        merged_inervals.append([start, end])
            
        return merged_inervals
        