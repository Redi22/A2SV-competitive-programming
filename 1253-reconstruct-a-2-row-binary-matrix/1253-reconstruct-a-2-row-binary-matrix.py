class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        
        mat = [[0] * len(colsum) , [0] * len(colsum)]
        up = upper
        low = lower
        for i in range(len(colsum)):
            if colsum[i] == 2:
                mat[0][i] = 1
                mat[1][i] = 1
                upper -= 1
                lower -= 1
                
        for i in range(len(colsum)):
            if colsum[i] == 1:
                if upper:
                    upper -= 1
                    mat[0][i] = 1
                elif lower:
                    mat[1][i] = 1
                    lower -= 1
       
        if sum(mat[0]) == up  and sum(mat[1]) == low:            
            return mat
        return []
                
            