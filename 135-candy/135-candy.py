class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        [1, 0 ,2]
        
        [1, 1, 1]
        [2, 1, 1]
        [2, 1, 2]
        
        
        """
        
        candiesGiven = [1] * len(ratings)
        for i in range(1 , len(ratings)):
            if ratings[i] > ratings[i-1]:
                candiesGiven[i] = candiesGiven[i-1] + 1
        for i in range(len(ratings) - 2 , -1 , -1 ):
            if ratings[i] > ratings[i+1]:
                candiesGiven[i] = max(candiesGiven[i] , candiesGiven[i+1] + 1)
        return sum(candiesGiven)
                