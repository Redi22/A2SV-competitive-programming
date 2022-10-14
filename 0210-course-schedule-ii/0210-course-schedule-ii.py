class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        build the graph 
        start from any node
        do dfs and cycle detection 
        a list for coloring, a stack to collect the sequence, 
        '''
        def detectAndDfs(node):
            nonlocal graph, colors, stack
            if colors[node] == 1:
                return True
            
            if colors[node] == 2:
                return False
            
            colors[node] = 1
            for nei in graph[node]:
                isCycle = detectAndDfs(nei)
                if isCycle: return isCycle
            
            colors[node] = 2
            stack.append(node)
                    
            return False
                
        
        graph = defaultdict(list)
        stack = []
        colors = [0] * numCourses
        
        for frm, to in prerequisites:
            graph[to].append(frm)
            
        for node in range(numCourses):
            if detectAndDfs(node): return []
            
        
        return stack[::-1]