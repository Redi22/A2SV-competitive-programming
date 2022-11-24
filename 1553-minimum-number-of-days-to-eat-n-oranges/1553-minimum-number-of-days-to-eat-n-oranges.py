class Solution:
    def minDays(self, n: int) -> int:
        
        @cache
        def dp(n):
            if n < 3:
                return n
           
            eat_2 = (n % 2) + dp(n // 2) 
            eat_3 = (n % 3) + dp(n // 3) 

            return 1 + min(eat_2, eat_3) 
        
        return dp(n)