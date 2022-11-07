class Solution:
    def maximum69Number (self, num: int) -> int:
        shift = -1
        original = num
        best = -1
        
        while num > 0:
            shift += 1
            if num % 10 == 6:
                best = shift
            num //= 10
            
        return original + (3 * (10 ** best)) if best != -1 else original
            