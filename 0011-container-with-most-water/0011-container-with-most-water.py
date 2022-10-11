class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        problem: maxiumum water contain. -> max area
                 rectangular area
                 
        inputs: heights = [1,8,6,2,5,4,8,3,7]
        
        what to find: two points start and end that makeup our rectangle
        ||
        |      |
        1,8,6,2,5,4,8,3
            |       |
          1             8
        ans = 0
        global ans = (8 - 0) * min(1, 7) => 8
        8 - 1 * 7
        ans = max(ans, temp) = max(49, 8) => 49
         
        o(n) -> 10^8
        o(n ^ 2) -> o(nlogn) ->  10^4
        o(logn) -> 10^9
        
        '''
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            temp = (r - l) * min(height[l], height[r])
            ans = max(ans, temp)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return ans
                
        
        