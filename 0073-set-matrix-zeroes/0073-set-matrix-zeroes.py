class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        
        def inBound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        def traverse(i, j, direction, matrix):
            dx, dy = direction
            
            if not inBound(i, j) or matrix[i][j] == 0:
                return 
            
            matrix[i][j] = float("inf")
            
            traverse(i + dx, j + dy, direction, matrix)
                
                
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    traverse(i + 1, j, (1, 0), matrix)
                    traverse(i - 1, j, (-1, 0), matrix)
                    traverse(i, j + 1, (0, 1), matrix)
                    traverse(i, j - 1, (0, -1), matrix)
                
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
                    
        