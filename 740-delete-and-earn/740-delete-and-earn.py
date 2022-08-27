class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = defaultdict(lambda:0)
        count = Counter(nums)
        maxx = max(nums)
        
        maxPoints = [0] * (maxx + 2)
        for i in range(len(maxPoints)):
            maxPoints[i] = max(maxPoints[i-1] , maxPoints[i-2] + count[i] * i)
            
        return maxPoints[maxx]