class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        [
        b : 3
        c : 4
        a : 2
        ]
        
        []
        []
        [a , b , c ]
        """
        
         

        
        
        lastIndex = {}
        result = []
        visited = set()
        for i in range(len(s)):
            lastIndex[s[i]] = i
            
            #bab
        
        for i in range(len(s)):
            
            if s[i] not in visited:
                while (result and result[-1] > s[i] and lastIndex[result[-1]] > i):
                    visited.remove(result.pop())

                result.append(s[i])
                visited.add(s[i])
                
                  
        return "".join(result)
                        
                