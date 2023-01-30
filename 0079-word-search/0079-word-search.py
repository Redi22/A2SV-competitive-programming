class Solution:
    def inBound(self, i, j, board):
        return 0 <= i < len(board) and 0 <= j < len(board[0])
    
    def traverse(self, i, j, board, target, target_index):
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        if target_index >= len(target):
            return True
        
        if not self.inBound(i, j, board) or board[i][j] != target[target_index]:
            return False
        
        temp = board[i][j]
        board[i][j] = "#" 
        res = False
        
        for dx, dy in directions:
            res |= self.traverse(dx + i, dy + j, board, target, target_index + 1)
            
        board[i][j] = temp
        return res
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_count = Counter(word)
        n = len(board)
        m = len(board[0])
        
        for i in range(n):
            for j in range(m):
                current = board[i][j]
                if current not in word_count:
                    continue
                word_count[current] -= 1
                if word_count[current] == 0:
                    del word_count[current]

        if not word_count:
            for i in range(n):
                for j in range(m):
                    if self.traverse(i, j, board, word, 0):
                        return True

        return False