class Solution:
    def concatenatedBinary(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append(bin(i+1)[2:])
        
        return int("".join(arr), 2) % (7 + 10 ** 9 )