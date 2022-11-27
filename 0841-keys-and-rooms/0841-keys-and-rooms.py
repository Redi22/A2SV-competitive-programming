class Solution:
    def traverse(self, room, rooms, visited):
        if room in visited:
            return 
        
        visited.add(room)
        
        for r in rooms[room]:
            self.traverse(r, rooms, visited)
            
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.traverse(0, rooms, visited)
        return len(visited) == len(rooms) 