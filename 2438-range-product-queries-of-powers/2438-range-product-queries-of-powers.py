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
            
        
        for start, end in queries:
            product = 1
            for i in range(start, end + 1):
                product *= powers[i]
                
            result.append(product % (10 ** 9 + 7))
            
        return result
                