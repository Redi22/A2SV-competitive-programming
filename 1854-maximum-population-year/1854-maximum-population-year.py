class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        registration = []
        current = 0
        max_population = 0
        max_val = 0
        
        for birth, death in logs:
            registration.append((birth, 1))
            registration.append((death, -1))
            
        registration.sort()
        
        for year, val in registration:
            current += val
            if current > max_population:
                max_population = current
                max_val = year
        
        return max_val