class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heap = [[0, sys.maxsize]]
        ans = [[0,0]]
        buildPoints = []
        
        for i, (x1, x2, y) in enumerate(buildings):
            buildPoints.append((x1, x2, -y))
            buildPoints.append((x2, 0, 0))
            
        buildPoints.sort(key=lambda x: (x[0],x[2],x[1]))
         
            
               
        for s,e,h in buildPoints:
            # Pop out the buildings which are already left behind.
            while heap and heap[0][1] <= s:
                heapq.heappop(heap)
            
            # If the current point is the start point of any building then push it to heap.
            if h != 0:
                heapq.heappush(heap, [h, e])
            
            # If by pushing the current point into heap, the maxHeight changed, then include the current point in answer
            if ans[-1][1] != -heap[0][0]:
                ans.append([s, -heap[0][0]])
            
        return ans[1:]
            
            
