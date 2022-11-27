class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        queue = deque([0])
        capacity  = jug1Capacity + jug2Capacity
        directions  = [-jug1Capacity, jug1Capacity, jug2Capacity, -jug2Capacity]
        visited = set()
        
        if capacity < targetCapacity:
            return False
        
        while queue:
            current = queue.popleft()
            
            if current == targetCapacity:
                return True
            
            if current in visited or current < 0 or current > capacity:
                continue
                
            visited.add(current)
            
            for d in directions:
                queue.append(d + current)
                
        return False
    
            
            
            