class Solution:
    def inbound(self, i, j, board):
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            return True 
        return False
    
    def traverse(self, i, j, board, visited):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        if not self.inbound(i, j, board) or board[i][j] == "." or (i, j) in visited:
            return 
        
        visited.add((i, j))
        for dx, dy in directions:
            if self.inbound(dx + i, dy + j, board):
                self.traverse(dx + i, dy + j, board, visited)
                
        
    
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        count = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited and board[i][j] == "X":
                    self.traverse(i, j, board, visited)
                    count += 1
                    
        return count 
                    