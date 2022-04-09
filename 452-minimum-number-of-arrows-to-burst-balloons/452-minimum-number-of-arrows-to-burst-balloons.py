class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        pos = [points[0][1]]
        for i in range(1,len(points)):
            if points[i][0] <= pos[-1] <= points[i][1]:
                continue
            else:
                if points[i][0] < pos[-1]:
                    continue
                else:
                    pos.append(points[i][1])
        return len(pos)