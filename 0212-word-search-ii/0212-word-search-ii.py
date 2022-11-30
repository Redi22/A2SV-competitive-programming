class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        result = []
        inBound = lambda r,c: 0 <= r < len(board) and 0 <= c < len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def traverse(i, j, root):
            if "#" in root:
                result.append(root['#'])
                del root['#'] 
                
            if not inBound(i, j) or board[i][j] not in root:
                return 
            
            temp = board[i][j]
            board[i][j] = "."
            
            for dx, dy in directions:
                traverse(dx + i, dy + j, root[temp])
                
            if not root[temp]:
                del root[temp]
                
            board[i][j] = temp
            
        for word in words:
            current = root
            for letter in word:
                if letter not in current:
                    current[letter] = {}
                    
                current = current[letter]
                
            current["#"] = word
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                traverse(i, j, root)
                
        return result