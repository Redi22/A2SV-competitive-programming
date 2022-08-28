class Solution:
    def trap(self, height: List[int]) -> int:
        minn = height[0]
        stack = []
        total = 0
        area = 0
        
        for i in range(len(height)):

            while stack and height[i] > height[stack[-1]]:
                popped = stack.pop()
                if not stack:
                    break;
                h = min(height[i], height[stack[-1]]) - height[popped]
                width = i - stack[-1] - 1
                area = h * width
                total += area

                
            stack.append(i)
        return total
            
            