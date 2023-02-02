class Solution:
    def numberToWords(self, num: int) -> str:
        mapping = {1: "One",   11: "Eleven",    10: "Ten", 
              2: "Two",   12: "Twelve",    20: "Twenty", 
              3: "Three", 13: "Thirteen",  30: "Thirty", 
              4: "Four",  14: "Fourteen",  40: "Forty",
              5: "Five",  15: "Fifteen",   50: "Fifty", 
              6: "Six",   16: "Sixteen",   60: "Sixty", 
              7: "Seven", 17: "Seventeen", 70: "Seventy", 
              8: "Eight", 18: "Eighteen",  80: "Eighty",
              9: "Nine",  19: "Nineteen",  90: "Ninety"}
        
        def toWord(n):
            if not n:
                return []
            
            elif n < 20:
                return [mapping[n]]
            
            elif n < 100:
                return [mapping[n // 10*10]] + toWord(n % 10)
            
            return [mapping[n // 100], "Hundred"] + toWord(n % 100)
        
        ans = []
        huges = [[9, "Billion"], [6, "Million"], [3, "Thousand"], [0, ""]]
        
        for i, unit in huges: 
            n = num // 10**i
            num = num % 10**i
            ans += toWord(n)
            
            if n and unit:
                ans.append(unit)
                
        return " ".join(ans) or "Zero"