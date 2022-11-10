class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = 0
        n = len(digits)
        result = []
        for i, digit in enumerate(digits):
            answer += (digit * (10 ** (n - i - 1)))
            
        if digits[-1] == 9:
            digits.append(0)
            
        answer += 1
        while answer > 0:
            result.append(answer % 10)
            answer //= 10
        
        return result[::-1]
        