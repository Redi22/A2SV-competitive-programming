class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        currX = 0
        currY = len(matrix[0]) - 1
        
        while currX < len(matrix) and currY > -1:
            
            if target < matrix[currX][currY]:
                currY -= 1
            elif target > matrix[currX][currY]:
                currX += 1
            else:
                return True
                
        return False