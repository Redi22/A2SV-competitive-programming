class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n % 2 == 0:
            ans = self.myPow(x,n//2)
            return ans * ans
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        
        return self.myPow(x,n//2) * self.myPow(x,n-n//2)