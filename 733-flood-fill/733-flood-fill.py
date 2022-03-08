class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        n = len(image)
        m = len(image[0])
        visited = set()
        DIR = [[0,1] , [-1,0] , [1, 0] , [0,-1]]
        
        inbound = lambda r ,c: 0 <= r < n and 0 <= c < m
        
        def dfsTraversal( row: int , col: int):
            image[row][col] = newColor
            visited.add((row , col))
            for d in DIR:
                new_row , new_col = row + d[0] , col + d[1]
                if (new_row , new_col) in visited or not inbound(new_row , new_col) or image[new_row][new_col] != startColor:
                    continue
                dfsTraversal(new_row , new_col)
        dfsTraversal(sr , sc)  
        return image
        
            