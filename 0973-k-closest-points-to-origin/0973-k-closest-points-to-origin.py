class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        kClosest = []
        
        #for each point calculate distance and push to heap 
        for xCordinate, yCordinate in points:
            distance = xCordinate ** 2 + yCordinate ** 2
            heapq.heappush(heap, [distance, [xCordinate, yCordinate]])
        
        
        #add the closest points to our answer until we reach k 
        for i in range(k):
            closeElement = heapq.heappop(heap)
            kClosest.append(closeElement[1])
            
        return kClosest
            