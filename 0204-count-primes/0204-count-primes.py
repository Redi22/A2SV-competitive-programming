class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [True] * n
        
        if n > 0: is_prime[0] = False
        if n> 1: is_prime[1] = False
        
        for i in range(2, int(sqrt(n)) + 1):
            for j in range(i * i, n, i):
                if is_prime[i]:
                    is_prime[j] = False
            
        return sum([num for num in is_prime if num])