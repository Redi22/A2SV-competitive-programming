class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diags = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diags[i-j].append(mat[i][j])
                
        for key,diag in diags.items():
            diag.sort()
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = diags[i-j][0]
                diags[i-j] = diags[i-j][1:]
                
        return mat