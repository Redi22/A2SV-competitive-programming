class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Solution
        # 1. Sort costs ascending
        # 2. Decreases coins until < 0
        # 3. Return number of bars
        
        # 1. Sort costs ascending
        costs.sort()
        
        # 2. Decrease coins until < 0 
        for i,cost in enumerate(costs):
            coins -= cost
            if coins < 0:
                # Return number of bars
                return i 

        # Handle edge case
        # more coins than the sum of costs
        return i + 1