class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        def chooseStock(i , boughtBy):
            if i >= len(prices):
                return 0
            
            if (i, boughtBy) in memo:
                return memo[(i, boughtBy)]
            
            if boughtBy >= 0:
                memo[(i, boughtBy)] = max(chooseStock(i+1, boughtBy), (prices[i] - boughtBy) + chooseStock(i+2, -1))
                return memo[(i, boughtBy)]
        
            memo[(i, boughtBy)] = max(chooseStock(i+1, boughtBy), chooseStock(i+1, prices[i]))
            
            return memo[(i, boughtBy)]
        
        return max(chooseStock(0, prices[0]), chooseStock(0, -1))
    