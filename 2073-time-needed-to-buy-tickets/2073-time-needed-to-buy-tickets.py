class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(ticket, i) for i, ticket in enumerate(tickets)])
        time = 0
        res = 0
        
        while queue:
            current, pos = queue.popleft()
            current -= 1
            time += 1
            if current > 0:
                queue.append((current, pos))
            elif pos == k:
                    res = time
            
        return res