class Solution:
    def bitwiseComplement(self, n: int) -> int:
        l = len(bin(n)) - 2
        return n ^ (2 ** l) - 1