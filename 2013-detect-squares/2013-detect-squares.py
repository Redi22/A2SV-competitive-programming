class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        squares = 0
        
        for x, y in self.points:
            if abs(point[0] - x) == abs(point[1] - y) and point[1] != y:
                if (point[0], y) in self.points and (x, point[1]) in self.points:
                    squares += self.points[(x, point[1])] * self.points[(x, y)] * self.points[(point[0], y)]
                    
        return squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)