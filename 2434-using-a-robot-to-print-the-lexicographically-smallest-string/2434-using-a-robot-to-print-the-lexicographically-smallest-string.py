class Solution:
    def robotWithString(self, s: str) -> str:
        '''
         build the right freq
        
        loop on s
            append to t
            minus freq for char
            
            while check top of t if valid
                pop and add to p
                
            
            
                
        '''
        p = []
        t = []
        rights = [0] * 26
        
        for si in s:
            rights[ord(si) - ord('a')] += 1
            
        for si in s:
            t.append(si)
            rights[ord(si) - ord('a')] -= 1
            while t and sum(rights[:(ord(t[-1]) - ord('a'))]) == 0:
                p.append(t.pop())
                
        return "".join(p + t[::-1])
                
            