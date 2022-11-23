class Solution:
    def minimumDeleteSum(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        @cache
        def dp(i, j):
            if i >= m:
                value_left = 0
                for k in range(j, len(text2)):
                    value_left += ord(text2[k])
                return value_left
            
            if j >= n:
                value_left = 0
                for k in range(i, len(text1)):
                    value_left += ord(text1[k])
                return value_left
            
            if text1[i] == text2[j]:
                return dp(i + 1, j + 1)
            else:
                return min(dp(i, j + 1) + ord(text2[j]), dp(i + 1, j) + ord(text1[i]))

        
        return dp(0, 0)
       
            
    
    
        