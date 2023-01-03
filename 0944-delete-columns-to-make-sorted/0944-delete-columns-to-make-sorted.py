class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        cols = [[] for _ in range(m)] 
        
        for i in range(n):
            for j in range(m):
                cols[j].append(strs[i][j])
                
        return sum([cols[i] != sorted(cols[i]) for i in range(m)])
    
                
        