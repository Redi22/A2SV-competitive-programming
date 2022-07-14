class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = {}
        ans = []
        
        for i in range(len(edges)):
            inDegree[edges[i][1]] = 0
        
        for i in range(n):
            if i not in inDegree:
                ans.append(i)
                
        return ans