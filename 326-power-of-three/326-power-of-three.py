class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if not n or n<0:
            return False
        
        return (math.log10(n)/ math.log10(3)) % 1 == 0