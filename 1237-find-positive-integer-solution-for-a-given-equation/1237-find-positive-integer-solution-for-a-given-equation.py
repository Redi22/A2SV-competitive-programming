"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        pairs = []
        
        for i in range(1, 1001):
            left = 1 
            right = 1000

            while left <= right:
                mid = (left + right) // 2
                if customfunction.f(i, mid) > z:
                    right = mid - 1
                elif customfunction.f(i, mid) < z:
                    left = mid + 1
                else:
                    pairs.append([i, mid])
                    break
        
        return pairs