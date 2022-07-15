class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = piles[len(piles)//3:]
        i = 0
        ans = 0
        
        while i < len(piles):
            ans += piles[i]
            i += 2
         
        return ans