class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        queue = deque([(0,0)])
        result = []
        direction = 0
        visited = set()
        
        isValid = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and (r, c) not in visited
        
        while queue:
            current = queue.popleft()
            
            result.append(matrix[current[0]][current[1]])
            
            visited.add(current)
            dx, dy = directions[direction]
            
            if not isValid(current[0] + dx, current[1] + dy):
                direction = (direction + 1) % 4
                dx, dy = directions[direction]
                
            if isValid(current[0] + dx, current[1] + dy):  
                queue.append((dx + current[0], dy + current[1]))
                
                
        return result