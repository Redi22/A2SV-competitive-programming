class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = False 
                if i != 0 and flowerbed[i-1] == 1:
                    left = True

                right = False
                if i != len(flowerbed) - 1 and flowerbed[i+1] == 1:
                    right = True
            
                if not left and not right:
                    flowerbed[i] = 1
                    n -= 1
                    
        return n <= 0
                
                    