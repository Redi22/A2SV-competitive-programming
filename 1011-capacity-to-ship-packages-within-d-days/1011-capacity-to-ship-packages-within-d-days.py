class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxx = sum(weights)
        minn = max(weights)
        best = maxx
        
        def possible(capacity):
            temp = days
            i = 0
            tempSum = 0
            for i in range(len(weights)):
                if tempSum + weights[i] <= capacity:
                    tempSum += weights[i]
                else:
                    tempSum = weights[i]
                    temp -= 1
                    
            return temp > 0
        
        while maxx > minn:
            mid = minn + (maxx - minn) // 2
            if possible(mid):
                best = mid
                maxx = mid 
            elif best != -1:
                minn = mid + 1
                
                
        return best
            
                    
                