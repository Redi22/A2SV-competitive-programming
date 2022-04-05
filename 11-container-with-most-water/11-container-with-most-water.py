class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxR = r 
        maxL = l
        maxArea = 0
        while (l < r):
            tempArea = abs((l - r) * min(height[l] , height[r]))
            maxArea = max(tempArea , maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
            
        return maxArea