class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        half = pow(2, n-1)//2
        
        if n == 1:
            return 0
        
        elif k > half:
            return self.inverse(self.kthGrammar(n - 1 , k - half))
        
        else:
            return self.kthGrammar(n - 1 , k)
    
    def inverse(self, n: int):
        if n == 1:
            return 0
        
        else:
            return 1