class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        directions = [[0,1] , [0,-1] , [-1,0] , [1,0]]
        m = len(board)
        n = len(board[0])
        count = 0
        inbound = lambda r,c: 0<= r < m and 0<= c < n
        
        def dfsTraversal(row, col):
            visited.add((row, col))
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if inbound(new_row , new_col) and (new_row , new_col) not in visited and board[new_row][new_col] == "O":
                    dfsTraversal(new_row,new_col)
                    
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and board[i][j] == "O":
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        dfsTraversal(i,j)
                    
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"

                