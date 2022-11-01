class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        def check(row,col):
            ### If a ball get out of the box, return col
            if row==m:
                return col
				
			### note that since grid contains 1 and -1 representing to right and to left, 
			### we can just add the grid[row][col] to current collumn to get the new column
            new_col = col+grid[row][col]
			
            ### if the new column is already out of the box 
            ### or the neighbor cell doesn't equal to grid[row][col] 
            ### the ball will get stuck and we just return -1
            if new_col==n or new_col==-1 or grid[row][new_col]!=grid[row][col]:
                return -1
            else:
                return check(row+1,new_col)
        res = []
        for i in range(n):
            res.append(check(0,i))
        return res