class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []
        
        for i in range(len(capacity)):
            temp = capacity[i] - rocks[i]
            diff.append(temp)
        
        diff.sort()   
        
        for i in range(1, len(capacity)):
            diff[i] += diff[i - 1]
    
        return bisect.bisect_right(diff, additionalRocks) 
        