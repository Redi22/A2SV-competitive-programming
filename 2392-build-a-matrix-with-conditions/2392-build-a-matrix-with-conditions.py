class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        '''
        build two graphs for the rowConditions and the colConditions
        get the row order first
        iterate through the col graph and get the row order...put the number in that row and the col from previous computation
        
        '''
        
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        row_indegree = [0] * k
        col_indegree = [0] * k
        row_order = defaultdict(int)
        matrix = [[0] * k for _ in range(k)]
        
        for above, below in rowConditions:
            row_graph[above].append(below)
            row_indegree[below - 1] += 1
        
        
        for left, right in colConditions:
            col_graph[left].append(right)
            col_indegree[right - 1] += 1
            
            
        queue = deque([])
        
        
        for condition in range(1, k + 1):
            if row_indegree[condition - 1] == 0:
                queue.append(condition)
                
        needs_to_process = len(row_graph)
        row = 0
        while queue:
            current = queue.popleft()
            needs_to_process -= 1
            row_order[current] = row
            row += 1
            
            for neighbour in row_graph[current]:
                row_indegree[neighbour - 1] -= 1
                
                if row_indegree[neighbour - 1] == 0:
                    queue.append(neighbour)
        
        if needs_to_process > 0:
            return []
        
        for condition in range(1, k + 1):
            if col_indegree[condition - 1] == 0:
                queue.append(condition)
                
        needs_to_process = len(col_graph)
        col = 0
        
        while queue:
            current = queue.popleft()
            needs_to_process -= 1
            matrix[row_order[current]][col] = current
            col += 1
            
            for neighbour in col_graph[current]:
                col_indegree[neighbour - 1] -= 1
                
                if col_indegree[neighbour - 1] == 0:
                    queue.append(neighbour)
        
        if needs_to_process > 0:
            return []
        
        return matrix
        
        
                
        
        