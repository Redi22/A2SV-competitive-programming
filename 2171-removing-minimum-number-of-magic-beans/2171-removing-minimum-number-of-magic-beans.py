class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        running_cost = 0
        running_sum = sum(beans)
        beans.sort()
        min_cost = float("inf")
        n = len(beans)
        
        for i in range(len(beans)):
            running_sum -= beans[i]
            current_cost = (running_sum - ((n - i - 1) * beans[i]) + running_cost)
            min_cost = min(min_cost, current_cost)
            running_cost += beans[i]
            
        return min_cost