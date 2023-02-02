class Solution:
    def numberOfWays(self, s: str) -> int:
        reverse_ones = [0]
        
        for si in s[::-1]:
            reverse_ones.append(reverse_ones[-1] + (si == "1"))
            
        reverse_ones = reverse_ones[::-1][:-1]
        count = 0
        ones = 0
        
        for i in range(len(s)):
            
            if s[i] == "0":
                count += (reverse_ones[i] * ones)
            else:
                count += (abs(len(s) - reverse_ones[i] - i) * abs(i - ones))
                
            ones += (s[i] == "1") 
                
        return count
            