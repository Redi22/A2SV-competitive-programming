class Solution:
    def traverse(self, current, graph, path, all_paths, target):
        if current == target:
            all_paths.append(path[:])
            
        if len(graph[current]) == 0:
            return 
        
        for neighbour in graph[current]:
            path.append(neighbour)
            self.traverse(neighbour, graph, path, all_paths, target)
            path.pop()
            
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []
        path = [0]
        target = len(graph) - 1
        
        self.traverse(0, graph, path, all_paths, target)
        return all_paths