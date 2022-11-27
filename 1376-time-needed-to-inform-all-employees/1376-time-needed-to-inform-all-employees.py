class Solution:
    def inform(self, employee, graph, informTime, visited):
        if employee in visited:
            return 0
        
        visited.add(employee)
        time = 0 
        for neighbour in graph[employee]:
            time = max(time, self.inform(neighbour, graph, informTime, visited) + informTime[employee])
                
        return time
            
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        visited = set()
        for employee, manager in enumerate(manager):
            graph[manager].append(employee)
        
        return self.inform(headID, graph, informTime, visited)