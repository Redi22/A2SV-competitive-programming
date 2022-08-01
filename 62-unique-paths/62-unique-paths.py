class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 1
        arr = [1] * n
        
        if n == 1 or m == 1:
            return 1
        
        for i in range(1,m):
            for j in range(1, n):
                arr[j] = arr[j-1] + arr[j] 
                
        return arr[-1]
                