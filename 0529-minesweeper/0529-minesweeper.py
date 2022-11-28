class Solution:
    def inBound(self, r, c, board):
        return 0 <= r < len(board) and 0 <= c < len(board[0])

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        queue = deque([click])
        directions = [(0, -1), (0, 1), (-1, -1), (1, 1), (1, 0), (-1, 0), (-1, 1), (1, -1)]
   
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        
        while queue:
            current_x, current_y = queue.pop()

            if not self.inBound(current_x, current_y, board) or board[current_x][current_y] != "E":
                continue

            board[current_x][current_y] = "B"
            count = 0
            for dx, dy in directions:
                new_x = dx + current_x
                new_y = dy + current_y

                if self.inBound(new_x, new_y, board):
                    count += board[new_x][new_y] == "M"
                    
            board[current_x][current_y] = str(count) 
            
            if count == 0:
                board[current_x][current_y] = "B" 
                for dx, dy in directions:
                    new_x = dx + current_x
                    new_y = dy + current_y
                    queue.append((new_x, new_y))
            
            


        return board

    
        