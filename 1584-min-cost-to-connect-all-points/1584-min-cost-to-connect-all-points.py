class Solution:
    def find(self, u, parent):
        
        if parent[u] == (-1, -1):
            return u
        
        parent[u] = self.find(parent[u], parent)
        return parent[u]
    

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        n = len(points)
        parent = defaultdict(lambda: (-1, -1))
        cost = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append((distance, tuple(points[i]), tuple(points[j])))
                
        distances.sort()
        
        for distance, point_x, point_y in distances:
            px = self.find(point_x, parent)
            py = self.find(point_y, parent)
            
            if distance and px != py:
                parent[px] = py 
                cost += distance
            
        return cost
        