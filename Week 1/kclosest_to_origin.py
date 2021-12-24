class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point:(sqrt((point[0] * point[0]) + (point[1] * point[1]))))
        return points[:k]
        