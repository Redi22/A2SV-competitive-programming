class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        res = 0
        
        for si in s:
            b += (si == 'b')
            if si == 'a':
                res = min(b, res + 1)
                
        return res
                
                
              