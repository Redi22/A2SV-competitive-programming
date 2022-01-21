class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        finalStr = []
        for letter in s:
            if(letter == '#' and finalStr):
                finalStr.pop()
            elif( letter != '#'):
                finalStr.append(letter)
        s = "".join(finalStr)
        finalStr = []
        for letter in t:
            if(letter == '#' and finalStr):
                finalStr.pop()
            elif( letter != '#'):
                finalStr.append(letter)
        t = "".join(finalStr)
        return(s == t)
            
                    