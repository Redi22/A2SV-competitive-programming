class Solution:
    
    def fib(self, n: int) -> int:
        memo = {0:0 , 1:1}
        def fi(n):
            nonlocal memo
            if n in memo.keys():
                return memo[n]
            memo[n] = fi(n-1) + fi(n-2)
            return memo[n]
        return fi(n)