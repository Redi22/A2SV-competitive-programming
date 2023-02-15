class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            temp = columnNumber % 26
            columnNumber //= 26
            res.append(chr(temp + 65))
            
        return "".join(res[::-1])
    
    