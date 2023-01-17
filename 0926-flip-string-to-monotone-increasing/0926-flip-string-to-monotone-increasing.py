class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        counts = [] 
        zeros = 0
        ones = 0
        all_zeros = s.count("0")
        res = all_zeros
        
        for i in range(len(s)):
            ones += (s[i] == "1")
            counts.append(ones)
        
        
        for i in range(len(counts)):
            zeros += (s[i] == "0")
            res = min(res, counts[i] + (all_zeros - zeros), )
                          
        return res
                          