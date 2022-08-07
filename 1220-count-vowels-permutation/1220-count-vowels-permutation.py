class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dpOld = [1,1,1,1,1]
        if n == 1:
            return sum(dpOld)
        
        for i in range(1,n):
            dpNew = [0,0,0,0,0]
            dpNew[0] = dpOld[1] + dpOld[2] + dpOld[4]
            dpNew[1] = dpOld[0] + dpOld[2]
            dpNew[2] = dpOld[1] + dpOld[3] 
            dpNew[3] = dpOld[2] 
            dpNew[4] = dpOld[2] + dpOld[3]
            
            dpOld = dpNew
            
        return(sum(dpNew) % (1000000007))