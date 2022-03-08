class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited = set()
        
        
        def dfsTraversal(row: int):
            visited.add(row)
            
            for j in range(n):
                if j not in visited and int(isConnected[row][j]) == 1:
                    dfsTraversal(j)
                
        for i in range(n):
            if i not in visited:
                dfsTraversal(i) 
                count += 1
        return count