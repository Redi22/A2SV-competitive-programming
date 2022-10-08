class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        negDiag = set()
        posDiag = set()
        board = [["."] * n for i in range(n)]
        
        def bk(i):
            if i == n:
                possible = ["".join(row) for row in board]
                res.append(possible)
                return 
            
            for j in range(n):
                if j in cols or (i - j) in negDiag  or (j + i) in posDiag:
                    continue
                    
                cols.add(j)
                negDiag.add(i - j)
                posDiag.add(i + j)
                board[i][j] = "Q"

                bk(i + 1)

                cols.remove(j)
                negDiag.remove(i - j)
                posDiag.remove(i + j)
                board[i][j] = "."

            
        bk(0)
        return res