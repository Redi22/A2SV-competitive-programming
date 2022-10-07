class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        def backtrack(path, node):
            if node == len(graph) - 1:
                result.append(path + [node])
                return
            
            for nei in graph[node]:
                backtrack(path + [node], nei)
            
        backtrack([], 0)
        return result 