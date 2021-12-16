class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        point_with_dis = [[point[0] , point[1], sqrt((point[0] * point[0]) + (point[1] * point[1]))] for  point in points]
        point_with_dis.sort(key=lambda points:points[2])
        point_with_dis = [[point_with_dis[i][0] , point_with_dis[i][1]] for i in range(k) ]
        
        return point_with_dis
        