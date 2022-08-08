class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        keyboard = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def backtrack(idx, path):
            if idx >= len(digits):
                if path: result.append("".join(path))
                return
            for char in keyboard[digits[idx]]:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()
                
        backtrack(0, [])
        return result
            