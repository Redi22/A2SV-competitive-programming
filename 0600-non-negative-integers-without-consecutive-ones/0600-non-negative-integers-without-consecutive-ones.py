class Solution:
    def findIntegers(self, n: int) -> int:
        sequence = [1, 2]
        
        for i in range(2, 30):
            sequence.append(sequence[-1] + sequence[-2])
            
        answer = 1
        last_bit = 0
        for i in range(30, -1, -1):
            if (1 << i) & n:
                answer += sequence[i]
                if last_bit: 
                    answer -= 1
                    break
                last_bit = 1
            else:
                last_bit = 0
                
        return answer 