class Solution:
    def traverse(self, position, arr, visited):
        if position in visited or position >= len(arr) or position < 0:
            return False
        
        if arr[position] == 0:
            return True
        
        visited.add(position)
        
        go_right = self.traverse(arr[position] + position, arr, visited)
        go_left = self.traverse(position - arr[position], arr, visited)
        
        return go_right or go_left
            
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        return self.traverse(start, arr, visited)