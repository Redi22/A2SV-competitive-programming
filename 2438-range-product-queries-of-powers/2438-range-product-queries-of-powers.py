class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        result = []
        mod = 10**9 + 7
        i = 0
        while n:
            if n & 1:
                powers.append(2 ** i)
            n = n >> 1
            i += 1
        
        @cache
        def dp(start, end):
            if start > end:
                return 1
            if start == end:
                return powers[start]
            return (dp(start+1, end-1) * powers[start] * powers[end]) % mod
        
        for start, end in queries:
            result.append(dp(start, end))
            
        return result
                