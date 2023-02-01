class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        def inBound(i,  row):
            if row:
                return 0 <= i < len(mat)
            return 0 <= i < len(mat[0])
        
        
        def prefixSumBuild(mat):
            pref = [[0 for i in range(len(mat[0]) + 1)] for j in range(len(mat) + 1)] 
            
            
            for i in range(1, len(mat) + 1):
                for j in range(1, len(mat[0]) + 1):
                    if i > 0 and j > 0:
                        pref[i][j] = mat[i-1][j-1] + pref[i][j-1] + pref[i-1][j] - pref[i-1][j-1]
                    elif i == 0 and j > 0:
                        pref[i][j] = mat[i-1][j-1] + pref[i][j-1]
                    elif j == 0 and i > 0:
                        pref[i][j] = mat[i-1][j-1] + pref[i-1][j]
                    else:
                        pref[i][j] = mat[i-1][j-1]
                    
            return pref
        
        pref_sum = prefixSumBuild(mat)
        res = [[0 for i in range(len(mat[0]))] for j in range(len(mat))] 
        
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                base_i = min(len(mat) - 1, i + k) + 1
                base_j = min(len(mat[0]) - 1 , j + k) + 1
                up_i = max(0, i - k)  + 1
                left_j = max(0, j - k ) + 1
                
                res[i][j] = pref_sum[base_i][base_j] - pref_sum[up_i - 1][base_j] - pref_sum[base_i][left_j - 1] + pref_sum[up_i - 1][left_j - 1]
               
        return res
                    
                