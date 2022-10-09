class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k + 1):
            temp = prices[:]
            for frm, to, price in flights: 
                
                if temp[frm] != float("inf"):
                    temp[to] = min(temp[to], price + prices[frm])
                    
            prices = temp
            
        return prices[dst] if prices[dst] != float("inf") else -1