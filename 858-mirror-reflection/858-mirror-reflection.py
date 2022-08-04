class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m, n = 1, 1
        
        while p * m != q * n:
            n += 1
            m = q * n // p
            
        if n % 2 == 0:
            return 2
        
        if m % 2:
            return 1
        
        return 0