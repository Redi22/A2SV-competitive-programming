class Solution:
    def findComplement(self, num: int) -> int:
        l = len(bin(num)) - 2
        return num ^ (2 ** l) - 1
        