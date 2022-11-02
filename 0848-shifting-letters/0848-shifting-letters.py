class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix_sum = []
        result = []
        summ = 0
        
        for index in range(len(shifts) - 1, -1, -1):
            summ += shifts[index]
            prefix_sum.append(summ)
            
        prefix_sum = prefix_sum[::-1]
        for index in range(len(s)):
            result.append(chr((ord(s[index]) - 97 + prefix_sum[index]) % 26 + 97))
            
        return "".join(result)
    