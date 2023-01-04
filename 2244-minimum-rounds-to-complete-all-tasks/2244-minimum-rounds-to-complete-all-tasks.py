class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = list(Counter(tasks).values())
        rounds = 0
        
        for c in count:
            if c == 1:
                return -1
            
            if c % 3 == 0:
                rounds += (c // 3)
            else:
                rounds += (c // 3) + 1
                    
                
        return rounds