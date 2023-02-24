class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        lookup = defaultdict(set)
        res = [0] * k
        
        for user, time in logs:
            lookup[user].add(time)
            
        for user, time_set in lookup.items():
            res[len(time_set) - 1] += 1
            
        return res