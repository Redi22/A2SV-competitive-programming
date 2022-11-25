class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        memo = {}
        
        def dp(start, end, cuts):
            
            if (start, end) in memo:
                return memo[(start, end)]

            if start >= end or not cuts:
                return 0
            
            res = float("inf")
            
            for i, cut in enumerate(cuts):
                res = min(res, dp(start, cut, cuts[:i]) + dp(cut, end, cuts[i + 1:]) + (end - start))
                
            memo[(start, end)] = res
            
            return memo[(start, end)]
                
        return dp(0, n, cuts)