class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        result = []
        i = 0
        while n:
            if n & 1:
                powers.append(2 ** i)
            n = n >> 1
            i += 1
            
        for i in range(1, len(powers)):
            powers[i] *= powers[i - 1] 
            
            
        for start, end in queries:
            if start == 0:
                result.append((powers[end])  % (10 ** 9 + 7))
            else:
                result.append((powers[end] // powers[start - 1]) % (10 ** 9 + 7))
            
        return result
                